# Slack Bot Enhancement Summary

## ✅ Completed Changes

### 1. **Multi-Content Type Support**
Added dropdown selection for 4 content types:
- 📰 **News/Social Media** - LinkedIn posts and social updates
- 📄 **Research Papers** - Full academic publication with DOI, authors, journal, year, abstract
- 📺 **Press/Media** - Media coverage and press articles  
- 🏛️ **Policy Support** - Policy-related announcements

### 2. **New Slash Commands**

#### `/publish-news`
- Opens content type selector
- Redirects to appropriate form based on selection
- Supports LinkedIn scraping AND generic URL scraping
- Auto-extracts title, description, and images from OpenGraph meta tags
- Shows preview in Slack after publishing

#### `/remove-news` (NEW)
- Lists all existing news items with numbers
- Select item to remove from list
- Confirms deletion with item details

### 3. **Auto-Numbering System**
- Every news entry now gets an `id` field (1, 2, 3, etc.)
- Makes it easy to reference and remove specific entries
- Counter increments automatically

### 4. **Enhanced News Form**
Updated fields:
- **Short Title** - Optional 10-word max title for feed display (auto-truncated)
- **Date** - Optional YYYY-MM-DD field (defaults to today)
- **Author** - Optional (defaults to Slack username)
- **URL** - Now supports both LinkedIn AND generic articles

### 5. **Paper Submission Form**
New comprehensive form for research papers:
- DOI or URL
- Full title
- Authors (comma-separated)
- Journal/Publication name
- Year
- Abstract/Description (optional)

Creates news entry with:
- Title: "📄 New Paper: [short title]"
- Description: "New paper published in [Journal] ([Year]): [Title]. [Abstract preview]"
- Link: DOI or article URL
- Auto-dated to today

### 6. **Enhanced Scraping**
Two scraping functions:
- **scrape_linkedin_post()** - Extracts from LinkedIn posts
- **scrape_generic_url()** - NEW! Extracts from any URL using OpenGraph and standard meta tags

Both extract:
- Title (og:title or <title>)
- Description (og:description or meta description)
- Image (og:image)

### 7. **Content Type Prefixes**
Auto-adds prefixes for different content types:
- Papers: `📄` emoji + formatted citation
- Press: `📺 Press:` in short_title
- Policy: `🏛️ Policy:` in short_title  
- News: No prefix

### 8. **Slack Preview**
After publishing any content, user receives formatted Slack message with:
- Success confirmation
- Content details (title, date, author)
- Image preview (if available)
- Description preview (first 200 chars)

### 9. **YAML Integration**
- Installed PyYAML package
- Parse existing news.yml to count entries
- Proper YAML formatting for all fields
- Maintains existing structure

## 📁 File Changes

### `/Users/tslr/Projects/work/ichydro.github.io/slackBot/bot.py`
- **Added**: `yaml` import
- **Added**: `load_dotenv()` for .env file support
- **Added**: `/remove-news` command endpoint
- **Modified**: `/publish-news` now opens content type selector
- **Added**: `open_content_type_modal()` - Shows 4 content types
- **Added**: `open_remove_news_modal()` - Lists news items for removal
- **Added**: `get_news_modal_view()` - Reusable news form
- **Added**: `get_paper_modal_view()` - Paper submission form
- **Added**: `handle_content_type_selection()` - Routes to correct form
- **Added**: `handle_news_submission()` - Processes news/press/policy
- **Added**: `handle_paper_submission()` - Processes paper entries
- **Added**: `handle_remove_news_submission()` - Removes news items
- **Added**: `scrape_generic_url()` - Scrapes non-LinkedIn URLs
- **Added**: `create_news_entry_enhanced()` - With ID and short_title support
- **Added**: `remove_news_entry()` - Deletes entry by index

### `/Users/tslr/Projects/work/ichydro.github.io/slackBot/README_ENHANCED.md` (NEW)
Complete documentation:
- Feature descriptions
- Setup instructions
- Command usage
- Environment variables
- YAML format examples

## 🎯 Next Steps

### 1. **Configure Slack App**
Add the new slash command:
```
Command: /remove-news
Request URL: https://your-ngrok-url/slack/commands/remove-news
Description: Remove a news feed item
```

### 2. **Test the Bot**
```bash
cd /Users/tslr/Projects/work/ichydro.github.io/slackBot
source venv/bin/activate
python bot.py
```

### 3. **Test with Ngrok**
```bash
# In another terminal
ngrok http 3000

# Update Slack app URLs:
# - /publish-news: https://your-ngrok-url/slack/commands/publish-news
# - /remove-news: https://your-ngrok-url/slack/commands/remove-news
# - Interactivity: https://your-ngrok-url/slack/interactivity
```

### 4. **Test Scenarios**

**Publishing News:**
1. Run `/publish-news` in Slack
2. Select "📰 News/Social Media Post"
3. Paste LinkedIn URL
4. Add optional short title
5. Submit
6. Check preview in Slack
7. Verify entry appears in `_data/news.yml` with ID

**Publishing Paper:**
1. Run `/publish-news` in Slack
2. Select "📄 Research Paper"
3. Fill in DOI, title, authors, journal, year
4. Submit
5. Check news feed has "New Paper!" entry

**Removing News:**
1. Run `/remove-news` in Slack
2. See numbered list of articles
3. Select one to remove
4. Confirm deletion
5. Verify entry removed from `_data/news.yml`

### 5. **Production Deployment**
When ready for production:
- Deploy to Render.com or Heroku
- Update Slack app URLs to production domain
- Set environment variables on hosting platform
- Use Gunicorn: `gunicorn -w 4 -b 0.0.0.0:3000 bot:app`

## 📊 Data Format

**News.yml entries now include:**
```yaml
- id: 1
  short_title: "Optional 10-word title"
  title: "Full title from LinkedIn/article"
  date: 2025-12-13
  description: "Description (200 char max)"
  link: "https://..."
  author: "Author Name"
  image: "https://..."  # Optional
```

**Paper entries format:**
```yaml
- id: 2
  short_title: "New Paper: Effects of instream wood..."
  title: "📄 Howard BC, Baker I, et al. (2025). Full title. Journal Name."
  date: 2025-12-13
  description: "New paper published in Journal Name (2025): Full title. Abstract preview..."
  link: "https://doi.org/10.xxxx/xxxxx"
  author: "ICHydro Team"
```

## 🔧 Dependencies Installed
- ✅ PyYAML 6.0.3
- ✅ python-dotenv (already installed)

All other dependencies (Flask, slack-sdk, PyGithub, requests, beautifulsoup4) were already installed.

## 🚀 Ready to Test!

The bot is fully enhanced and ready for testing. Start it with:
```bash
cd /Users/tslr/Projects/work/ichydro.github.io/slackBot
source venv/bin/activate
python bot.py
```

Then test in Slack with `/publish-news` and `/remove-news` commands!
