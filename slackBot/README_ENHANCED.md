# Enhanced ICHydro Slack Bot

## New Features

### 1. Multi-Content Type Publishing
The bot now supports publishing different types of content through a dropdown menu:

- **📰 News/Social Media Posts** - LinkedIn posts and social media content
- **📄 Research Papers** - Academic publications with full metadata
- **📺 Press/Media Coverage** - Press articles and media mentions  
- **🏛️ Policy Support** - Policy-related content and government engagement

### 2. Slash Commands

#### `/publish-news`
Opens a modal with content type selection:
1. Choose content type (News, Paper, Press, or Policy)
2. Fill in the appropriate form
3. Preview is shown in Slack after submission

#### `/remove-news`
Opens a modal to remove news entries:
1. Shows list of existing news items (numbered)
2. Select item to remove
3. Confirms deletion

### 3. Auto-Numbering
All news entries are now automatically numbered with an `id` field for easy reference and removal.

### 4. Enhanced Form Fields

#### News/Press/Policy Form:
- **LinkedIn/Article URL** - Supports both LinkedIn posts and generic URLs
- **Short Title** (optional) - Auto-truncated to 10 words for news feed display
- **Date** (optional) - YYYY-MM-DD format, defaults to today
- **Author** (optional) - Defaults to your Slack name

#### Paper Form:
- **DOI or Paper URL** - Direct link to the publication
- **Paper Title** - Full title of the research paper
- **Authors** - Comma-separated list of authors
- **Journal/Publication** - Where the paper was published
- **Year** - Publication year
- **Abstract/Description** (optional) - Brief summary

### 5. Slack Preview
After publishing, you receive a formatted preview in Slack showing:
- Title
- Date and author
- Description
- Image (if available)

## Setup Instructions

### Required Environment Variables
```bash
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
GITHUB_TOKEN=your-github-pat
```

### Required Slack Scopes
- `commands` - For slash commands
- `chat:write` - For sending messages
- `users:read` - For getting user names

### Slack App Configuration

1. **Slash Commands** - Add these commands:
   - `/publish-news` - Request URL: `https://your-domain/slack/commands/publish-news`
   - `/remove-news` - Request URL: `https://your-domain/slack/commands/remove-news`

2. **Interactivity** - Enable and set Request URL: `https://your-domain/slack/interactivity`

3. **OAuth & Permissions** - Add the required scopes above

### Installation

```bash
cd slackBot
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install flask slack-sdk pygithub requests beautifulsoup4 pyyaml
```

### Running the Bot

Development:
```bash
source venv/bin/activate
python bot.py
```

Production (with ngrok for testing):
```bash
ngrok http 3000
# Update Slack app URLs with ngrok URL
```

Production (with Gunicorn):
```bash
gunicorn -w 4 -b 0.0.0.0:3000 bot:app
```

## News.yml Format

The enhanced bot creates news entries with this structure:

```yaml
- id: 1
  short_title: "Congratulations Clara!"
  title: "Full title from LinkedIn or article"
  date: 2025-12-13
  description: "Brief description..."
  link: "https://..."
  author: "Author Name"
  image: "https://..."  # Optional

- id: 2
  # ... next entry
```

## Content Type Prefixes

When publishing papers, press, or policy content, the title is automatically prefixed:
- Papers: `📄` emoji + formatted citation
- Press: `📺 Press:` prefix
- Policy: `🏛️ Policy:` prefix

## Error Handling

The bot provides clear error messages for:
- Invalid URLs
- Scraping failures
- GitHub API errors
- Missing required fields

## Supported URL Types

- LinkedIn posts (linkedin.com/posts/...)
- Generic articles (extracts OpenGraph meta tags)
- DOI links (for papers)
- Any URL with meta tags

## Future Enhancements

- [ ] Bulk import of papers from bibliography file
- [ ] Scheduled posts
- [ ] Draft/preview mode before publishing
- [ ] Rich text editing
- [ ] Attachment support
- [ ] Analytics on news engagement
