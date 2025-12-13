import os
import json
import base64
import re
from datetime import datetime
from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from github import Github
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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
    
    # Open modal for post input
    open_modal(trigger_id)
    
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
        return handle_modal_submission(payload)
    
    return "", 200

def verify_slack_request(request):
    """Verify that the request came from Slack"""
    return signature_verifier.is_valid_request(request.get_data(), request.headers)

def open_modal(trigger_id):
    """Open a modal dialog for creating a news post"""
    
    # Build tag options
    tag_options = [{"text": {"type": "plain_text", "text": tag}, "value": tag} 
                   for tag in PREDEFINED_TAGS]
    
    modal = {
        "type": "modal",
        "callback_id": "publish_news_modal",
        "title": {"type": "plain_text", "text": "Publish News Post"},
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
                "block_id": "title_block",
                "label": {"type": "plain_text", "text": "Post Title (optional - will be extracted from LinkedIn)"},
                "element": {
                    "type": "plain_text_input",
                    "action_id": "title_input",
                    "placeholder": {"type": "plain_text", "text": "Leave blank to auto-extract"}
                },
                "optional": True
            },
            {
                "type": "input",
                "block_id": "tags_block",
                "label": {"type": "plain_text", "text": "Tags"},
                "element": {
                    "type": "multi_static_select",
                    "action_id": "tags_input",
                    "placeholder": {"type": "plain_text", "text": "Select tags"},
                    "options": tag_options
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
