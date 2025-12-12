# Slack to Jekyll News Publisher Bot

This bot allows you to publish news posts to your Jekyll GitHub Pages site directly from Slack using a `/publish-news` command.

## Features

- 📝 Create Jekyll posts with title, content, and images
- 🏷️ Tag posts with predefined badges
- 📸 Automatic image download and commit to GitHub
- 👤 Author attribution (uses Slack name by default)
- 🎨 Clean modal interface in Slack

---

## Prerequisites

1. **Python 3.8+** installed
2. **GitHub account** with repository access
3. **Slack workspace** where you have permissions to install apps

---

## Part 1: Create Slack App

### Step 1: Create the Slack App

1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Click **"Create New App"**
3. Choose **"From scratch"**
4. Name your app: `News Publisher`
5. Select your workspace
6. Click **"Create App"**

### Step 2: Configure OAuth & Permissions

1. In the left sidebar, click **"OAuth & Permissions"**
2. Scroll down to **"Scopes"** → **"Bot Token Scopes"**
3. Add these scopes:
   - `chat:write` - Send messages as the bot
   - `commands` - Add slash commands
   - `users:read` - Read user information
   
4. Scroll to top and click **"Install to Workspace"**
5. Click **"Allow"**
6. **Copy the "Bot User OAuth Token"** (starts with `xoxb-`) - you'll need this later

### Step 3: Enable Interactivity

1. In the left sidebar, click **"Interactivity & Shortcuts"**
2. Toggle **"Interactivity"** to **ON**
3. Set **Request URL** to: `https://YOUR-SERVER-URL/slack/interactivity`
   - (We'll set this up later - you can use ngrok for local testing)
4. Click **"Save Changes"**

### Step 4: Create Slash Command

1. In the left sidebar, click **"Slash Commands"**
2. Click **"Create New Command"**
3. Fill in:
   - **Command**: `/publish-news`
   - **Request URL**: `https://YOUR-SERVER-URL/slack/commands/publish-news`
   - **Short Description**: `Publish a news post to the website`
   - **Usage Hint**: `[Opens a form to create a post]`
4. Click **"Save"**

### Step 5: Get Your Signing Secret

1. In the left sidebar, click **"Basic Information"**
2. Scroll to **"App Credentials"**
3. **Copy the "Signing Secret"** - you'll need this later

---

## Part 2: Create GitHub Personal Access Token

### Step 1: Generate Token

1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name: `Slack Jekyll Bot`
4. Set expiration (recommend: 90 days or No expiration if secure)
5. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - This includes: `repo:status`, `repo_deployment`, `public_repo`, `repo:invite`
6. Click **"Generate token"**
7. **Copy the token** (starts with `ghp_`) - you won't see it again!

---

## Part 3: Set Up the Bot Server

### Step 1: Install Dependencies

```bash
# Clone or download the bot code
cd slack-jekyll-bot

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your tokens
nano .env  # or use any text editor
```

Add your tokens to `.env`:

```env
SLACK_BOT_TOKEN=xoxb-your-actual-bot-token
SLACK_SIGNING_SECRET=your-actual-signing-secret
GITHUB_TOKEN=ghp_your-actual-github-token
```

### Step 3: Test Locally with ngrok

For local testing, use ngrok to create a public URL:

```bash
# Install ngrok: https://ngrok.com/download

# Start your bot
python bot.py

# In another terminal, start ngrok
ngrok http 3000
```

Copy the ngrok URL (e.g., `https://abc123.ngrok.io`) and:
1. Update your Slack app's **Interactivity Request URL** to `https://abc123.ngrok.io/slack/interactivity`
2. Update your **Slash Command Request URL** to `https://abc123.ngrok.io/slack/commands/publish-news`

---

## Part 4: Deploy to Production

For production, deploy to a cloud service. Here are popular options:

### Option A: Deploy to Heroku

```bash
# Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create app
heroku create your-slack-bot-name

# Set environment variables
heroku config:set SLACK_BOT_TOKEN=xoxb-...
heroku config:set SLACK_SIGNING_SECRET=...
heroku config:set GITHUB_TOKEN=ghp_...

# Create Procfile
echo "web: gunicorn bot:app" > Procfile

# Deploy
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a your-slack-bot-name
git push heroku main

# Your URL will be: https://your-slack-bot-name.herokuapp.com
```

### Option B: Deploy to Railway

1. Go to [https://railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Connect your GitHub account and select the bot repository
4. Add environment variables in Railway dashboard
5. Railway will auto-deploy and give you a URL

### Option C: Deploy to Render

1. Go to [https://render.com](https://render.com)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn bot:app`
5. Add environment variables
6. Click **"Create Web Service"**

### Update Slack App URLs

After deployment, update your Slack app with the production URLs:
1. Go to [https://api.slack.com/apps](https://api.slack.com/apps)
2. Select your app
3. Update **Interactivity Request URL**: `https://your-domain.com/slack/interactivity`
4. Update **Slash Command Request URL**: `https://your-domain.com/slack/commands/publish-news`

---

## Part 5: Set Up Jekyll News Page

### Step 1: Create News Layout

Create `_layouts/post.html` in your Jekyll site:

```html
---
layout: default
---

<article class="post">
  <header class="post-header">
    <h1 class="post-title">{{ page.title }}</h1>
    
    <div class="post-meta">
      <time datetime="{{ page.date | date_to_xmlschema }}">
        {{ page.date | date: "%B %d, %Y" }}
      </time>
      {% if page.author %}
        <span class="post-author">by {{ page.author }}</span>
      {% endif %}
    </div>
    
    {% if page.tags %}
    <div class="post-tags">
      {% for tag in page.tags %}
        <span class="tag-badge">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </header>
  
  {% if page.image %}
  <div class="post-image">
    <img src="{{ page.image }}" alt="{{ page.title }}">
  </div>
  {% endif %}
  
  <div class="post-content">
    {{ content }}
  </div>
</article>
```

### Step 2: Create News Feed Page

Create `news.html` in your Jekyll site root:

```html
---
layout: default
title: News
---

<div class="news-feed">
  <h1>Latest News</h1>
  
  <div class="posts">
    {% for post in site.posts %}
      <article class="post-preview">
        <h2>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h2>
        
        <div class="post-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">
            {{ post.date | date: "%B %d, %Y" }}
          </time>
          {% if post.author %}
            <span class="post-author">by {{ post.author }}</span>
          {% endif %}
        </div>
        
        {% if post.tags %}
        <div class="post-tags">
          {% for tag in post.tags %}
            <span class="tag-badge">{{ tag }}</span>
          {% endfor %}
        </div>
        {% endif %}
        
        {% if post.image %}
        <div class="post-thumbnail">
          <img src="{{ post.image }}" alt="{{ post.title }}">
        </div>
        {% endif %}
        
        <div class="post-excerpt">
          {{ post.excerpt }}
        </div>
        
        <a href="{{ post.url | relative_url }}" class="read-more">Read more →</a>
      </article>
    {% endfor %}
  </div>
</div>
```

### Step 3: Add CSS Styling

Add this to your CSS file (e.g., `assets/css/style.css`):

```css
/* Tag badges */
.post-tags {
  margin: 1rem 0;
}

.tag-badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  margin: 0.25rem 0.25rem 0.25rem 0;
  background-color: #0366d6;
  color: white;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 500;
}

/* Post styling */
.post-header {
  margin-bottom: 2rem;
}

.post-title {
  margin-bottom: 0.5rem;
}

.post-meta {
  color: #586069;
  font-size: 0.875rem;
  margin-bottom: 1rem;
}

.post-author {
  margin-left: 0.5rem;
}

.post-image img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 2rem;
}

/* News feed */
.news-feed {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.post-preview {
  margin-bottom: 3rem;
  padding-bottom: 3rem;
  border-bottom: 1px solid #e1e4e8;
}

.post-preview h2 {
  margin-bottom: 0.5rem;
}

.post-preview h2 a {
  color: #24292e;
  text-decoration: none;
}

.post-preview h2 a:hover {
  color: #0366d6;
}

.post-thumbnail img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 1rem 0;
}

.post-excerpt {
  margin: 1rem 0;
  color: #586069;
}

.read-more {
  color: #0366d6;
  text-decoration: none;
  font-weight: 500;
}

.read-more:hover {
  text-decoration: underline;
}
```

---

## Usage

### Publishing a Post

1. In any Slack channel, type `/publish-news`
2. A modal will appear with fields for:
   - **Title** - The post title
   - **Content** - Post content (supports Markdown)
   - **Image URL** - Optional image (will be downloaded and committed)
   - **Tags** - Select from predefined tags
   - **Author** - Optional (defaults to your Slack name)
3. Click **"Publish"**
4. The bot will commit the post to GitHub
5. GitHub Pages will automatically rebuild (takes 1-2 minutes)
6. You'll receive a confirmation message in Slack

### Adding More Tags

Edit `bot.py` and add tags to the `PREDEFINED_TAGS` list:

```python
PREDEFINED_TAGS = [
    "water-quality",
    "smartwater",
    # Add your new tags here
    "new-tag-name",
]
```

Restart the bot after adding tags.

---

## Troubleshooting

### Bot doesn't respond to `/publish-news`

- Check that your server is running and accessible
- Verify Slack app URLs are correct
- Check server logs for errors

### Modal doesn't open

- Verify `SLACK_SIGNING_SECRET` is correct
- Check that Interactivity is enabled in Slack app

### Posts don't appear on site

- Check GitHub Actions to see if build succeeded
- Verify posts are in `_posts/` directory
- Check that Jekyll `_config.yml` includes posts

### Images don't upload

- Verify `GITHUB_TOKEN` has repo permissions
- Check that `assets/img/posts/` directory exists
- Verify image URL is publicly accessible

### Bot authentication errors

- Regenerate tokens if they've expired
- Verify all environment variables are set correctly
- Check that bot is installed in your workspace

---

## Security Notes

- ⚠️ Never commit your `.env` file to Git
- 🔐 Store tokens as environment variables in production
- 🔄 Rotate tokens periodically
- 🚫 Use `.gitignore` to exclude sensitive files

Add to `.gitignore`:
```
.env
venv/
__pycache__/
*.pyc
```

---

## Support

For issues or questions:
- Check the troubleshooting section above
- Review Slack API docs: https://api.slack.com
- Review GitHub API docs: https://docs.github.com/en/rest
- Check Jekyll docs: https://jekyllrb.com/docs/

---

## License

MIT License - feel free to modify and use as needed!
