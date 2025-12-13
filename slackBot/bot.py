import os
import json
import base64
import re
import yaml
from datetime import datetime
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from github import Github
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration - set these as environment variables
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = "trowan92/ichydro.github.io"

# Initialize clients
slack_client = WebClient(token=SLACK_BOT_TOKEN)
signature_verifier = SignatureVerifier(SLACK_SIGNING_SECRET)
github_client = Github(GITHUB_TOKEN)

# Predefined tags - add more as needed
PREDEFINED_TAGS = [
    "water-quality",
    "smartwater",
    "sensor-deployment",
    "research",
    "lorawan",
    "thingsboard",
    "buoy",
    "river-chess",
    "data-analysis",
    "fieldwork",
    "collaboration",
    "equipment",
    "maintenance",
    "news",
    "announcement"
]

@app.route("/slack/commands/publish-news", methods=["POST"])
def publish_news_command():
    """Handle the /publish-news slash command"""
    
    # Verify the request is from Slack
    if not verify_slack_request(request):
        return jsonify({"error": "Invalid request"}), 403
    
    # Get trigger_id to open modal
    trigger_id = request.form.get("trigger_id")
    
    # Open content type selection modal
    open_content_type_modal(trigger_id)
    
    # Acknowledge the command immediately
    return "", 200

@app.route("/slack/commands/remove-news", methods=["POST"])
def remove_news_command():
    """Handle the /remove-news slash command"""
    
    # Verify the request is from Slack
    if not verify_slack_request(request):
        return jsonify({"error": "Invalid request"}), 403
    
    # Get trigger_id to open modal
    trigger_id = request.form.get("trigger_id")
    
    # Open removal modal with list of news items
    open_remove_news_modal(trigger_id)
    
    # Acknowledge the command immediately
    return "", 200

@app.route("/slack/interactivity", methods=["POST"])
def handle_interactivity():
    """Handle modal submissions and button clicks"""
    
    # Verify the request is from Slack
    if not verify_slack_request(request):
        return jsonify({"error": "Invalid request"}), 403
    
    payload = json.loads(request.form.get("payload"))
    
    if payload["type"] == "view_submission":
        callback_id = payload["view"]["callback_id"]
        
        if callback_id == "content_type_modal":
            return handle_content_type_selection(payload)
        elif callback_id == "publish_news_modal":
            return handle_news_submission(payload)
        elif callback_id == "publish_paper_modal":
            return handle_paper_submission(payload)
        elif callback_id == "remove_news_modal":
            return handle_remove_news_submission(payload)
        else:
            return handle_modal_submission(payload)  # legacy
    
    return "", 200

def verify_slack_request(request):
    """Verify that the request came from Slack"""
    return signature_verifier.is_valid_request(request.get_data(), request.headers)

def open_content_type_modal(trigger_id):
    """Open modal to select content type"""
    modal = {
        "type": "modal",
        "callback_id": "content_type_modal",
        "title": {"type": "plain_text", "text": "Publish Content"},
        "submit": {"type": "plain_text", "text": "Next"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "input",
                "block_id": "content_type_block",
                "label": {"type": "plain_text", "text": "What would you like to publish?"},
                "element": {
                    "type": "static_select",
                    "action_id": "content_type_select",
                    "placeholder": {"type": "plain_text", "text": "Select content type"},
                    "options": [
                        {"text": {"type": "plain_text", "text": "📰 News/Social Media Post"}, "value": "news"},
                        {"text": {"type": "plain_text", "text": "📄 Research Paper"}, "value": "paper"},
                        {"text": {"type": "plain_text", "text": "📺 Press/Media"}, "value": "press"},
                        {"text": {"type": "plain_text", "text": "🏛️ Policy Support"}, "value": "policy"}
                    ]
                }
            }
        ]
    }
    slack_client.views_open(trigger_id=trigger_id, view=modal)

def open_remove_news_modal(trigger_id):
    """Open modal to remove news entries"""
    # Get current news entries
    try:
        repo = github_client.get_repo(GITHUB_REPO)
        file_content = repo.get_contents("_data/news.yml", ref="people-page-update")
        current_content = base64.b64decode(file_content.content).decode('utf-8')
        
        # Parse news entries to create options
        import yaml
        news_items = yaml.safe_load(current_content) or []
        
        if not news_items:
            # No items to remove
            modal = {
                "type": "modal",
                "callback_id": "no_news_modal",
                "title": {"type": "plain_text", "text": "Remove News"},
                "close": {"type": "plain_text", "text": "Close"},
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": "No news items found to remove."}
                    }
                ]
            }
        else:
            # Create options from news items
            options = []
            for idx, item in enumerate(news_items[:25]):  # Slack limit of 100 options, show first 25
                title = item.get('short_title') or item.get('title', 'Untitled')
                date = item.get('date', 'No date')
                options.append({
                    "text": {"type": "plain_text", "text": f"#{idx+1}: {title[:50]} ({date})"}, 
                    "value": str(idx)
                })
            
            modal = {
                "type": "modal",
                "callback_id": "remove_news_modal",
                "title": {"type": "plain_text", "text": "Remove News Item"},
                "submit": {"type": "plain_text", "text": "Remove"},
                "close": {"type": "plain_text", "text": "Cancel"},
                "blocks": [
                    {
                        "type": "input",
                        "block_id": "news_item_block",
                        "label": {"type": "plain_text", "text": "Select news item to remove"},
                        "element": {
                            "type": "static_select",
                            "action_id": "news_item_select",
                            "placeholder": {"type": "plain_text", "text": "Choose an item"},
                            "options": options
                        }
                    }
                ]
            }
        
        slack_client.views_open(trigger_id=trigger_id, view=modal)
    except Exception as e:
        # Error modal
        modal = {
            "type": "modal",
            "callback_id": "error_modal",
            "title": {"type": "plain_text", "text": "Error"},
            "close": {"type": "plain_text", "text": "Close"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"Error loading news items: {str(e)}"}
                }
            ]
        }
        slack_client.views_open(trigger_id=trigger_id, view=modal)

def open_news_modal(trigger_id):
    """Open modal for news/social media post"""
    modal = {
        "type": "modal",
        "callback_id": "publish_news_modal",
        "title": {"type": "plain_text", "text": "Publish News"},
        "submit": {"type": "plain_text", "text": "Publish"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "input",
                "block_id": "linkedin_url_block",
                "label": {"type": "plain_text", "text": "LinkedIn Post URL"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "linkedin_url_input",
                    "placeholder": {"type": "plain_text", "text": "https://www.linkedin.com/posts/..."}
                }
            },
            {
                "type": "input",
                "block_id": "short_title_block",
                "label": {"type": "plain_text", "text": "Short Title (10 words max, optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "short_title_input",
                    "placeholder": {"type": "plain_text", "text": "Brief title for news feed"}
                },
                "optional": True
            },
            {
                "type": "input",
                "block_id": "date_block",
                "label": {"type": "plain_text", "text": "Date (YYYY-MM-DD, optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "date_input",
                    "placeholder": {"type": "plain_text", "text": "Leave blank for today"}
                },
                "optional": True
            },
            {
                "type": "input",
                "block_id": "author_block",
                "label": {"type": "plain_text", "text": "Author Name (optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "author_input",
                    "placeholder": {"type": "plain_text", "text": "Leave blank to use your Slack name"}
                },
                "optional": True
            }
        ]
    }
    slack_client.views_open(trigger_id=trigger_id, view=modal)

def open_paper_modal(trigger_id):
    """Open modal for research paper submission"""
    modal = {
        "type": "modal",
        "callback_id": "publish_paper_modal",
        "title": {"type": "plain_text", "text": "Publish Paper"},
        "submit": {"type": "plain_text", "text": "Publish"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "input",
                "block_id": "paper_doi_block",
                "label": {"type": "plain_text", "text": "DOI or Paper URL"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_doi_input",
                    "placeholder": {"type": "plain_text", "text": "10.xxxx/xxxxx or https://..."}
                }
            },
            {
                "type": "input",
                "block_id": "paper_title_block",
                "label": {"type": "plain_text", "text": "Paper Title"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_title_input",
                    "multiline": True
                }
            },
            {
                "type": "input",
                "block_id": "paper_authors_block",
                "label": {"type": "plain_text", "text": "Authors (comma-separated)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_authors_input",
                    "placeholder": {"type": "plain_text", "text": "Smith J., Doe A., et al."}
                }
            },
            {
                "type": "input",
                "block_id": "paper_journal_block",
                "label": {"type": "plain_text", "text": "Journal/Publication"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_journal_input"
                }
            },
            {
                "type": "input",
                "block_id": "paper_year_block",
                "label": {"type": "plain_text", "text": "Year"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_year_input",
                    "placeholder": {"type": "plain_text", "text": "2025"}
                }
            },
            {
                "type": "input",
                "block_id": "paper_abstract_block",
                "label": {"type": "plain_text", "text": "Abstract/Description (optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_abstract_input",
                    "multiline": True,
                    "placeholder": {"type": "plain_text", "text": "Brief description or abstract"}
                },
                "optional": True
            }
        ]
    }
    slack_client.views_open(trigger_id=trigger_id, view=modal)

def handle_content_type_selection(payload):
    """Handle content type selection and open appropriate modal"""
    values = payload["view"]["state"]["values"]
    content_type = values["content_type_block"]["content_type_select"]["selected_option"]["value"]
    
    # Get user for opening next modal
    trigger_id = payload["trigger_id"] if "trigger_id" in payload else None
    
    # We need to return a response that updates the view
    if content_type == "news":
        return {
            "response_action": "update",
            "view": get_news_modal_view()
        }
    elif content_type == "paper":
        return {
            "response_action": "update",
            "view": get_paper_modal_view()
        }
    elif content_type == "press":
        # For now, press uses same form as news but with different title prefix
        return {
            "response_action": "update",
            "view": get_news_modal_view("Press Coverage")
        }
    elif content_type == "policy":
        # Policy uses same form as news but with different title prefix
        return {
            "response_action": "update",
            "view": get_news_modal_view("Policy Support")
        }
    
    return "", 200

def get_news_modal_view(content_type="News"):
    """Get the modal view for news/press/policy"""
    return {
        "type": "modal",
        "callback_id": "publish_news_modal",
        "title": {"type": "plain_text", "text": f"Publish {content_type}"},
        "submit": {"type": "plain_text", "text": "Publish"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "input",
                "block_id": "linkedin_url_block",
                "label": {"type": "plain_text", "text": "LinkedIn Post URL or Article Link"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "linkedin_url_input",
                    "placeholder": {"type": "plain_text", "text": "https://www.linkedin.com/posts/... or article URL"}
                }
            },
            {
                "type": "input",
                "block_id": "short_title_block",
                "label": {"type": "plain_text", "text": "Short Title (10 words max, optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "short_title_input",
                    "placeholder": {"type": "plain_text", "text": "Brief title for news feed"}
                },
                "optional": True
            },
            {
                "type": "input",
                "block_id": "date_block",
                "label": {"type": "plain_text", "text": "Date (YYYY-MM-DD, optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "date_input",
                    "placeholder": {"type": "plain_text", "text": "Leave blank for today"}
                },
                "optional": True
            },
            {
                "type": "input",
                "block_id": "author_block",
                "label": {"type": "plain_text", "text": "Author Name (optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "author_input",
                    "placeholder": {"type": "plain_text", "text": "Leave blank to use your Slack name"}
                },
                "optional": True
            }
        ],
        "private_metadata": json.dumps({"content_type": content_type})
    }

def get_paper_modal_view():
    """Get the modal view for paper submission"""
    return {
        "type": "modal",
        "callback_id": "publish_paper_modal",
        "title": {"type": "plain_text", "text": "Publish Paper"},
        "submit": {"type": "plain_text", "text": "Publish"},
        "close": {"type": "plain_text", "text": "Cancel"},
        "blocks": [
            {
                "type": "input",
                "block_id": "paper_doi_block",
                "label": {"type": "plain_text", "text": "DOI or Paper URL"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_doi_input",
                    "placeholder": {"type": "plain_text", "text": "10.xxxx/xxxxx or https://..."}
                }
            },
            {
                "type": "input",
                "block_id": "paper_title_block",
                "label": {"type": "plain_text", "text": "Paper Title"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_title_input",
                    "multiline": True
                }
            },
            {
                "type": "input",
                "block_id": "paper_authors_block",
                "label": {"type": "plain_text", "text": "Authors (comma-separated)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_authors_input",
                    "placeholder": {"type": "plain_text", "text": "Smith J., Doe A., et al."}
                }
            },
            {
                "type": "input",
                "block_id": "paper_journal_block",
                "label": {"type": "plain_text", "text": "Journal/Publication"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_journal_input"
                }
            },
            {
                "type": "input",
                "block_id": "paper_year_block",
                "label": {"type": "plain_text", "text": "Year"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_year_input",
                    "placeholder": {"type": "plain_text", "text": "2025"}
                }
            },
            {
                "type": "input",
                "block_id": "paper_abstract_block",
                "label": {"type": "plain_text", "text": "Abstract/Description (optional)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "paper_abstract_input",
                    "multiline": True,
                    "placeholder": {"type": "plain_text", "text": "Brief description or abstract"}
                },
                "optional": True
            }
        ]
    }

def handle_news_submission(payload):
    """Handle news/press/policy submission"""
    user_id = payload["user"]["id"]
    values = payload["view"]["state"]["values"]
    
    # Get content type from metadata
    metadata = json.loads(payload["view"].get("private_metadata", "{}"))
    content_type = metadata.get("content_type", "News")
    
    # Extract URL
    url = values["linkedin_url_block"]["linkedin_url_input"]["value"].strip()
    
    if not url:
        slack_client.chat_postMessage(
            channel=user_id,
            text="❌ Please provide a URL"
        )
        return "", 200
    
    # Scrape content
    try:
        if 'linkedin.com' in url.lower():
            linkedin_data = scrape_linkedin_post(url)
        else:
            # Generic URL scraping
            linkedin_data = scrape_generic_url(url)
    except Exception as e:
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error scraping URL: {str(e)}"
        )
        return "", 200
    
    # Extract form values
    short_title_value = values.get("short_title_block", {}).get("short_title_input", {}).get("value")
    short_title = short_title_value.strip() if short_title_value else ""
    
    # Auto-truncate to 10 words
    if short_title:
        words = short_title.split()
        if len(words) > 10:
            short_title = " ".join(words[:10])
    
    date_value = values.get("date_block", {}).get("date_input", {}).get("value")
    date_str = date_value.strip() if date_value else datetime.now().strftime("%Y-%m-%d")
    
    author_value = values.get("author_block", {}).get("author_input", {}).get("value")
    author = author_value.strip() if author_value else ""
    if not author:
        user_info = slack_client.users_info(user=user_id)
        author = user_info["user"]["real_name"]
    
    # Create title with prefix based on content type
    if content_type == "Press Coverage":
        title_prefix = "📺 Press: "
    elif content_type == "Policy Support":
        title_prefix = "🏛️ Policy: "
    else:
        title_prefix = ""
    
    full_title = linkedin_data['title']
    if short_title:
        display_title = short_title
    else:
        display_title = full_title
    
    try:
        # Create news entry
        create_news_entry_enhanced(
            short_title=short_title or None,
            title=full_title,
            date=date_str,
            description=linkedin_data['content'],
            link=url,
            author=author,
            image_url=linkedin_data.get('image_url')
        )
        
        # Send success message with preview
        preview_blocks = [
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"✅ *{content_type} published successfully!*"}
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"*Title:* {display_title}\n*Date:* {date_str}\n*Author:* {author}"}
            }
        ]
        
        if linkedin_data.get('image_url'):
            preview_blocks.append({
                "type": "image",
                "image_url": linkedin_data['image_url'],
                "alt_text": "Post image"
            })
        
        preview_blocks.append({
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"*Description:* {linkedin_data['content'][:200]}..."}
        })
        
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"✅ {content_type} published!",
            blocks=preview_blocks
        )
        
    except Exception as e:
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error publishing: {str(e)}"
        )
    
    return "", 200

def handle_paper_submission(payload):
    """Handle paper submission"""
    user_id = payload["user"]["id"]
    values = payload["view"]["state"]["values"]
    
    # Extract paper details
    doi_url = values["paper_doi_block"]["paper_doi_input"]["value"].strip()
    title = values["paper_title_block"]["paper_title_input"]["value"].strip()
    authors = values["paper_authors_block"]["paper_authors_input"]["value"].strip()
    journal = values["paper_journal_block"]["paper_journal_input"]["value"].strip()
    year = values["paper_year_block"]["paper_year_input"]["value"].strip()
    abstract_value = values.get("paper_abstract_block", {}).get("paper_abstract_input", {}).get("value")
    abstract = abstract_value.strip() if abstract_value else ""
    
    # Create description
    description = f"New paper published in {journal} ({year}): {title}"
    if abstract:
        description += f"\n\n{abstract[:200]}..."
    
    # Create news entry
    try:
        create_news_entry_enhanced(
            short_title=f"New Paper: {title[:50]}...",
            title=f"📄 {authors} ({year}). {title}. {journal}.",
            date=datetime.now().strftime("%Y-%m-%d"),
            description=description,
            link=doi_url if doi_url.startswith('http') else f"https://doi.org/{doi_url}",
            author="ICHydro Team",
            image_url=None
        )
        
        # Send success with preview
        slack_client.chat_postMessage(
            channel=user_id,
            text="✅ Paper published to news feed!",
            blocks=[
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": "✅ *Paper published successfully!*"}
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {"type": "mrkdwn", "text": f"*Title:* {title}\n*Authors:* {authors}\n*Journal:* {journal} ({year})\n*DOI/URL:* {doi_url}"}
                }
            ]
        )
        
    except Exception as e:
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error publishing paper: {str(e)}"
        )
    
    return "", 200

def handle_remove_news_submission(payload):
    """Handle news item removal"""
    user_id = payload["user"]["id"]
    values = payload["view"]["state"]["values"]
    
    # Get selected item index
    item_index = int(values["news_item_block"]["news_item_select"]["selected_option"]["value"])
    
    try:
        remove_news_entry(item_index)
        
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"✅ News item #{item_index + 1} removed successfully!"
        )
    except Exception as e:
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error removing news item: {str(e)}"
        )
    
    return "", 200

def scrape_generic_url(url):
    """Scrape content from a generic URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to extract title
        title = ""
        og_title = soup.find('meta', property='og:title')
        if og_title:
            title = og_title.get('content', '')
        if not title:
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.get_text(strip=True)
        
        # Try to extract description
        content = ""
        og_description = soup.find('meta', property='og:description')
        if og_description:
            content = og_description.get('content', '')
        if not content:
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                content = meta_desc.get('content', '')
        
        # Try to extract image
        image_url = ""
        og_image = soup.find('meta', property='og:image')
        if og_image:
            image_url = og_image.get('content', '')
        
        return {
            'title': title or 'Article',
            'content': content or 'Read the full article',
            'image_url': image_url,
            'link': url
        }
        
    except Exception as e:
        raise Exception(f"Failed to scrape URL: {str(e)}")

def scrape_linkedin_post(url):
    """Scrape content from a LinkedIn post URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to extract title from meta tags
        title = ""
        og_title = soup.find('meta', property='og:title')
        if og_title:
            title = og_title.get('content', '')
        
        # Try to extract description/content
        content = ""
        og_description = soup.find('meta', property='og:description')
        if og_description:
            content = og_description.get('content', '')
        
        # Try to extract image
        image_url = ""
        og_image = soup.find('meta', property='og:image')
        if og_image:
            image_url = og_image.get('content', '')
        
        # If content is still empty, try to find it in the page body
        if not content:
            # Look for LinkedIn post content selectors (these may change)
            post_content = soup.find('div', class_='feed-shared-update-v2__description-wrapper')
            if post_content:
                content = post_content.get_text(strip=True)
        
        return {
            'title': title or 'LinkedIn Post',
            'content': content or 'View the full post on LinkedIn',
            'image_url': image_url,
            'link': url
        }
        
    except Exception as e:
        raise Exception(f"Failed to scrape LinkedIn post: {str(e)}")

def handle_modal_submission(payload):
    """Process the modal submission and create GitHub post"""
    
    user_id = payload["user"]["id"]
    values = payload["view"]["state"]["values"]
    
    # Extract LinkedIn URL
    linkedin_url = values["linkedin_url_block"]["linkedin_url_input"]["value"].strip()
    
    # Validate LinkedIn URL
    if not linkedin_url or 'linkedin.com' not in linkedin_url.lower():
        slack_client.chat_postMessage(
            channel=user_id,
            text="❌ Please provide a valid LinkedIn post URL"
        )
        return "", 200
    
    # Scrape LinkedIn content
    try:
        linkedin_data = scrape_linkedin_post(linkedin_url)
    except Exception as e:
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error scraping LinkedIn post: {str(e)}"
        )
        return "", 200
    
    # Extract form values - use LinkedIn data as fallback
    title_value = values["title_block"]["title_input"].get("value")
    title = (title_value.strip() if title_value else "") or linkedin_data['title']
    content = linkedin_data['content']
    image_url = linkedin_data['image_url']
    link = linkedin_data['link']
    
    # Get selected tags
    tags = []
    if values.get("tags_block") and values["tags_block"]["tags_input"].get("selected_options"):
        tags = [option["value"] for option in values["tags_block"]["tags_input"]["selected_options"]]
    
    # Get author name or use Slack username
    author_value = values.get("author_block", {}).get("author_input", {}).get("value")
    author = author_value.strip() if author_value else ""
    if not author:
        user_info = slack_client.users_info(user=user_id)
        author = user_info["user"]["real_name"]
    
    try:
        # Create the news entry with image
        create_news_entry(title, content, link, author, image_url)
        
        # Send success message
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"✅ News published successfully! It will appear on the site shortly.\n\nTitle: {title}\nLinkedIn: {link}\nImage: {'✓' if image_url else '✗'}"
        )
        
    except Exception as e:
        # Send error message
        slack_client.chat_postMessage(
            channel=user_id,
            text=f"❌ Error publishing post: {str(e)}"
        )
    
    return "", 200

def create_news_entry(title, description, link, author, image_url=None):
    """Add a new entry to the news.yml file"""
    
    repo = github_client.get_repo(GITHUB_REPO)
    news_file_path = "_data/news.yml"
    
    # Get current news.yml content
    try:
        file_content = repo.get_contents(news_file_path, ref="people-page-update")
        current_content = base64.b64decode(file_content.content).decode('utf-8')
        sha = file_content.sha
    except:
        # If file doesn't exist, start with empty content
        current_content = ""
        sha = None
    
    # Create new news entry
    date = datetime.now()
    new_entry = f"""
- title: "{title}"
  date: {date.strftime("%Y-%m-%d")}
  description: "{description[:200]}{'...' if len(description) > 200 else ''}"
  link: "{link}"
  author: "{author}"
"""
    
    # Add image if available
    if image_url:
        new_entry += f'  image: "{image_url}"\n'
    
    # Prepend new entry to existing content
    updated_content = new_entry.strip() + "\n" + current_content
    
    # Update the file
    try:
        if sha:
            repo.update_file(
                path=news_file_path,
                message=f"Add news: {title}",
                content=updated_content,
                sha=sha,
                branch="people-page-update"
            )
        else:
            repo.create_file(
                path=news_file_path,
                message=f"Create news file and add: {title}",
                content=updated_content,
                branch="people-page-update"
            )
    except Exception as e:
        raise Exception(f"Failed to update news file: {str(e)}")
    
    return news_file_path

def create_news_entry_enhanced(short_title, title, date, description, link, author, image_url=None):
    """Add a new entry to the news.yml file with auto-numbering"""
    
    repo = github_client.get_repo(GITHUB_REPO)
    news_file_path = "_data/news.yml"
    
    # Get current news.yml content
    try:
        file_content = repo.get_contents(news_file_path, ref="people-page-update")
        current_content = base64.b64decode(file_content.content).decode('utf-8')
        sha = file_content.sha
    except:
        # If file doesn't exist, start with empty content
        current_content = ""
        sha = None
    
    # Parse existing entries to get count
    import yaml
    try:
        existing_entries = yaml.safe_load(current_content) or []
        entry_count = len(existing_entries)
    except:
        entry_count = 0
    
    # Create new news entry with number
    new_entry = f"""
- id: {entry_count + 1}"""
    
    if short_title:
        new_entry += f'\n  short_title: "{short_title}"'
    
    new_entry += f'''
  title: "{title}"
  date: {date}
  description: "{description[:200]}{'...' if len(description) > 200 else ''}"
  link: "{link}"
  author: "{author}"'''
    
    # Add image if available
    if image_url:
        new_entry += f'\n  image: "{image_url}"'
    
    new_entry += "\n"
    
    # Prepend new entry to existing content
    updated_content = new_entry.strip() + "\n" + current_content
    
    # Update the file
    try:
        if sha:
            repo.update_file(
                path=news_file_path,
                message=f"Add news #{entry_count + 1}: {short_title or title[:50]}",
                content=updated_content,
                sha=sha,
                branch="people-page-update"
            )
        else:
            repo.create_file(
                path=news_file_path,
                message=f"Create news file and add: {short_title or title[:50]}",
                content=updated_content,
                branch="people-page-update"
            )
    except Exception as e:
        raise Exception(f"Failed to update news file: {str(e)}")
    
    return news_file_path

def remove_news_entry(item_index):
    """Remove a news entry by index"""
    
    repo = github_client.get_repo(GITHUB_REPO)
    news_file_path = "_data/news.yml"
    
    # Get current news.yml content
    try:
        file_content = repo.get_contents(news_file_path, ref="people-page-update")
        current_content = base64.b64decode(file_content.content).decode('utf-8')
        sha = file_content.sha
    except Exception as e:
        raise Exception(f"Failed to read news file: {str(e)}")
    
    # Parse YAML
    import yaml
    try:
        news_items = yaml.safe_load(current_content) or []
    except Exception as e:
        raise Exception(f"Failed to parse news YAML: {str(e)}")
    
    if item_index < 0 or item_index >= len(news_items):
        raise Exception(f"Invalid item index: {item_index}")
    
    # Get item title for commit message
    removed_item = news_items[item_index]
    removed_title = removed_item.get('short_title') or removed_item.get('title', 'Unknown')
    
    # Remove the item
    del news_items[item_index]
    
    # Convert back to YAML
    updated_content = yaml.dump(news_items, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    # Update the file
    try:
        repo.update_file(
            path=news_file_path,
            message=f"Remove news item: {removed_title[:50]}",
            content=updated_content,
            sha=sha,
            branch="people-page-update"
        )
    except Exception as e:
        raise Exception(f"Failed to update news file: {str(e)}")
    
    return removed_title

def create_jekyll_post(title, content, image_url, tags, author):
    """Create a new Jekyll post in the GitHub repository (legacy function)"""
    
    repo = github_client.get_repo(GITHUB_REPO)
    
    # Generate filename
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d")
    slug = title.lower().replace(" ", "-").replace("/", "-")
    # Remove special characters
    slug = ''.join(c for c in slug if c.isalnum() or c == '-')
    filename = f"_posts/{date_str}-{slug}.md"
    
    # Handle image if provided
    image_path = ""
    if image_url:
        image_path = download_and_commit_image(repo, image_url, slug, date_str)
    
    # Create front matter
    front_matter = {
        "layout": "post",
        "title": title,
        "date": date.strftime("%Y-%m-%d %H:%M:%S %z"),
        "author": author,
        "tags": tags
    }
    
    if image_path:
        front_matter["image"] = f"/{image_path}"
    
    # Build the post content
    post_content = "---\n"
    for key, value in front_matter.items():
        if isinstance(value, list):
            post_content += f"{key}:\n"
            for item in value:
                post_content += f"  - {item}\n"
        else:
            post_content += f"{key}: {value}\n"
    post_content += "---\n\n"
    post_content += content
    
    # Commit the post
    try:
        repo.create_file(
            path=filename,
            message=f"New post: {title}",
            content=post_content,
            branch="main"
        )
    except Exception as e:
        # If main doesn't exist, try master
        repo.create_file(
            path=filename,
            message=f"New post: {title}",
            content=post_content,
            branch="master"
        )
    
    return filename

def download_and_commit_image(repo, image_url, slug, date_str):
    """Download image from URL and commit to GitHub"""
    
    try:
        # Download image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Determine file extension
        content_type = response.headers.get('content-type', '')
        if 'jpeg' in content_type or 'jpg' in content_type:
            ext = 'jpg'
        elif 'png' in content_type:
            ext = 'png'
        elif 'gif' in content_type:
            ext = 'gif'
        elif 'webp' in content_type:
            ext = 'webp'
        else:
            ext = 'jpg'  # default
        
        # Create image path
        image_filename = f"{date_str}-{slug}.{ext}"
        image_path = f"assets/img/posts/{image_filename}"
        
        # Commit image to repo
        try:
            repo.create_file(
                path=image_path,
                message=f"Add image for post: {slug}",
                content=response.content,
                branch="main"
            )
        except Exception as e:
            # Try master if main doesn't exist
            repo.create_file(
                path=image_path,
                message=f"Add image for post: {slug}",
                content=response.content,
                branch="master"
            )
        
        return image_path
        
    except Exception as e:
        print(f"Error downloading/committing image: {e}")
        return ""

if __name__ == "__main__":
    # For development - use a production server like gunicorn for deployment
    app.run(host="0.0.0.0", port=3000, debug=True)
