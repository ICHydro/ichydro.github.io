# Quick Start Checklist

Use this checklist to set up your Slack to Jekyll bot quickly.

## ☐ Part 1: Slack App Setup (15 minutes)

### Create App
- [ ] Go to https://api.slack.com/apps
- [ ] Click "Create New App" → "From scratch"
- [ ] Name: "News Publisher"
- [ ] Select your workspace

### Configure Permissions
- [ ] Go to "OAuth & Permissions"
- [ ] Add scopes: `chat:write`, `commands`, `users:read`
- [ ] Click "Install to Workspace"
- [ ] Copy Bot User OAuth Token (xoxb-...) → save for later

### Enable Interactivity
- [ ] Go to "Interactivity & Shortcuts"
- [ ] Toggle ON
- [ ] Request URL: `https://YOUR-URL/slack/interactivity` (set later)

### Create Slash Command
- [ ] Go to "Slash Commands"
- [ ] Click "Create New Command"
- [ ] Command: `/publish-news`
- [ ] Request URL: `https://YOUR-URL/slack/commands/publish-news` (set later)
- [ ] Save

### Get Signing Secret
- [ ] Go to "Basic Information"
- [ ] Copy Signing Secret → save for later

## ☐ Part 2: GitHub Token (5 minutes)

- [ ] Go to https://github.com/settings/tokens
- [ ] Generate new token (classic)
- [ ] Name: "Slack Jekyll Bot"
- [ ] Select scope: `repo` (full control)
- [ ] Generate token
- [ ] Copy token (ghp_...) → save for later

## ☐ Part 3: Local Setup (10 minutes)

- [ ] Download/clone the bot code
- [ ] Create virtual environment: `python3 -m venv venv`
- [ ] Activate: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Copy `.env.example` to `.env`
- [ ] Add your tokens to `.env`:
  ```
  SLACK_BOT_TOKEN=xoxb-...
  SLACK_SIGNING_SECRET=...
  GITHUB_TOKEN=ghp_...
  ```

## ☐ Part 4: Test Locally (10 minutes)

- [ ] Run bot: `python bot.py`
- [ ] Open new terminal
- [ ] Install ngrok: https://ngrok.com/download
- [ ] Run ngrok: `ngrok http 3000`
- [ ] Copy ngrok URL (https://abc123.ngrok.io)
- [ ] Update Slack app URLs:
  - [ ] Interactivity Request URL: `https://abc123.ngrok.io/slack/interactivity`
  - [ ] Slash Command Request URL: `https://abc123.ngrok.io/slack/commands/publish-news`

## ☐ Part 5: Test the Bot (5 minutes)

- [ ] Open Slack
- [ ] Type `/publish-news` in any channel
- [ ] Modal should appear
- [ ] Fill in test post
- [ ] Click "Publish"
- [ ] Check your GitHub repo for the new post

## ☐ Part 6: Jekyll Setup (15 minutes)

- [ ] Copy `jekyll-templates/post.html` to `_layouts/post.html` in your repo
- [ ] Copy `jekyll-templates/news.html` to `news.html` in your repo root
- [ ] Create `assets/img/posts/` directory if it doesn't exist
- [ ] Commit and push changes
- [ ] Wait for GitHub Pages to rebuild (1-2 minutes)
- [ ] Visit `https://yourusername.github.io/news` to see the feed

## ☐ Part 7: Deploy to Production (20 minutes)

Choose one deployment option:

### Option A: Heroku
- [ ] Install Heroku CLI
- [ ] Run: `heroku create your-bot-name`
- [ ] Set config vars:
  ```bash
  heroku config:set SLACK_BOT_TOKEN=xoxb-...
  heroku config:set SLACK_SIGNING_SECRET=...
  heroku config:set GITHUB_TOKEN=ghp_...
  ```
- [ ] Deploy: `git push heroku main`
- [ ] Update Slack URLs with Heroku URL

### Option B: Railway
- [ ] Sign up at https://railway.app
- [ ] New Project → Deploy from GitHub
- [ ] Add environment variables in dashboard
- [ ] Copy Railway URL
- [ ] Update Slack URLs with Railway URL

### Option C: Render
- [ ] Sign up at https://render.com
- [ ] New Web Service → Connect GitHub
- [ ] Add environment variables
- [ ] Copy Render URL
- [ ] Update Slack URLs with Render URL

## ☐ Final Steps

- [ ] Test production deployment with `/publish-news`
- [ ] Add more team members to Slack workspace
- [ ] Customize tag list in `bot.py` as needed
- [ ] Add news link to your website navigation

---

## Troubleshooting

**Bot doesn't respond:**
- Check server is running
- Verify URLs in Slack app match your deployment
- Check server logs

**Modal doesn't open:**
- Verify signing secret is correct
- Check Interactivity is enabled

**Posts don't appear:**
- Check GitHub repo `_posts/` directory
- Wait 1-2 minutes for GitHub Pages rebuild
- Check GitHub Actions for build errors

---

## You're Done! 🎉

Test it out:
1. Type `/publish-news` in Slack
2. Fill in the form
3. Wait 1-2 minutes
4. Check your website at `/news`

Need help? Check the full README.md for detailed troubleshooting.
