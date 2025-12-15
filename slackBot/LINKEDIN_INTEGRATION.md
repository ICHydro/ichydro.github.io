# LinkedIn Integration for News Feed

## Overview

The Slack bot has been updated to automatically fetch content from LinkedIn posts and add them to the ICHydro website news feed.

## How It Works

1. **User posts a LinkedIn URL** in Slack using `/publish-news`
2. **Bot scrapes the LinkedIn post** to extract:
   - Post title (from OpenGraph meta tags)
   - Post description/content
   - Featured image (if available)
   - Original LinkedIn URL
3. **Bot updates `_data/news.yml`** with the new entry
4. **GitHub Pages rebuilds** the site automatically
5. **News appears** in the scrollable feed on the home page

## Usage

### In Slack:

```
/publish-news
```

This opens a modal where you can:
- **LinkedIn Post URL**: (Required) The full URL to the LinkedIn post
- **Post Title**: (Optional) Override the auto-extracted title
- **Tags**: (Optional) Add categorization tags
- **Author**: (Optional) Override with custom author name

### Example LinkedIn URLs:

- `https://www.linkedin.com/posts/username_activityid`
- `https://www.linkedin.com/feed/update/urn:li:activity:1234567890`

## Technical Details

### Scraping Method

The bot uses BeautifulSoup4 to parse LinkedIn's OpenGraph meta tags:
- `og:title` for the post title
- `og:description` for the content
- `og:image` for featured images

### Data Storage

News entries are stored in `_data/news.yml` with this structure:

```yaml
- title: "Post Title"
  date: 2025-12-12
  description: "Brief description from LinkedIn (max 200 chars)..."
  link: "https://www.linkedin.com/posts/..."
  author: "Author Name"
```

### News Feed Display

The home page displays news in a scrollable container:
- Maximum height: 500px
- Auto-scrollbar with custom ICHydro styling
- Links open in new tabs
- Sorted by date (newest first)

## Installation

### Additional Requirements

```bash
pip install beautifulsoup4==4.12.2 lxml==4.9.3
```

### Configuration

The bot commits to the `people-page-update` branch. Update this in `bot.py` if needed:

```python
file_content = repo.get_contents(news_file_path, ref="people-page-update")
```

## Limitations

- LinkedIn may block scraping attempts if rate limits are exceeded
- Some LinkedIn posts may have restricted access requiring authentication
- Content extraction relies on OpenGraph meta tags which may not be present on all posts
- Images are referenced by URL, not downloaded to the repo

## Troubleshooting

**Error: "Failed to scrape LinkedIn post"**
- Check if the URL is accessible without login
- Verify the URL is a valid LinkedIn post
- LinkedIn may be blocking the user agent

**News not appearing on site**
- Check if the GitHub Action completed successfully
- Verify the news.yml file was updated in the repository
- Ensure Jekyll rebuild was triggered

## Future Enhancements

- Add LinkedIn authentication for private posts
- Download and host images locally
- Support for LinkedIn article URLs
- Automatic tagging based on post content
- Thumbnail previews in news feed
