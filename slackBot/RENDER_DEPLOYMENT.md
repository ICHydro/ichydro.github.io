# Deploying Slack Bot to Render.com

## Prerequisites

Before deploying, you'll need:
1. ✅ Slack Bot Token (starts with `xoxb-`)
2. ✅ Slack Signing Secret
3. ✅ GitHub Personal Access Token (starts with `ghp_`)

If you don't have these yet, see the main README.md for setup instructions.

---

## Step 1: Push Code to GitHub

Make sure your `slackBot` folder is committed and pushed to your GitHub repository:

```bash
cd /Users/tslr/Projects/work/ichydro.github.io
git add slackBot/
git commit -m "Add Slack bot for LinkedIn news integration"
git push fork people-page-update
```

---

## Step 2: Create Render Account

1. Go to [https://render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with your **GitHub account** (recommended)
4. Authorize Render to access your GitHub repositories

---

## Step 3: Create New Web Service

1. From your Render dashboard, click **"New +"** → **"Web Service"**

2. **Connect Your Repository**:
   - Find and select: `trowan92/ichydro.github.io`
   - Click **"Connect"**

3. **Configure the Service**:
   - **Name**: `ichydro-slack-bot` (or your choice)
   - **Region**: Choose closest to you (e.g., Oregon, Frankfurt)
   - **Branch**: `people-page-update`
   - **Root Directory**: `slackBot`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn bot:app`
   - **Plan**: Select **"Free"**

4. Click **"Advanced"** to add environment variables

---

## Step 4: Add Environment Variables

Click **"Add Environment Variable"** for each of these:

### Variable 1: SLACK_BOT_TOKEN
- **Key**: `SLACK_BOT_TOKEN`
- **Value**: Your Slack bot token (starts with `xoxb-...`)
  - Get this from: [Slack API](https://api.slack.com/apps) → Your App → OAuth & Permissions

### Variable 2: SLACK_SIGNING_SECRET
- **Key**: `SLACK_SIGNING_SECRET`
- **Value**: Your Slack signing secret
  - Get this from: [Slack API](https://api.slack.com/apps) → Your App → Basic Information → App Credentials

### Variable 3: GITHUB_TOKEN
- **Key**: `GITHUB_TOKEN`
- **Value**: Your GitHub personal access token (starts with `ghp_...`)
  - Create at: [GitHub Settings](https://github.com/settings/tokens) → Generate new token (classic)
  - Required scope: `repo` (full control)

### Variable 4: GITHUB_REPO (Already set in render.yaml)
- **Key**: `GITHUB_REPO`
- **Value**: `trowan92/ichydro.github.io`

---

## Step 5: Deploy

1. Click **"Create Web Service"**
2. Render will now:
   - Clone your repository
   - Install dependencies
   - Start your bot
   - Assign a public URL

3. **Wait for deployment** (usually 2-3 minutes)
   - You'll see logs streaming in real-time
   - Look for: `"Your service is live 🎉"`

4. **Copy your service URL**
   - It will look like: `https://ichydro-slack-bot.onrender.com`
   - You'll need this for Slack configuration

---

## Step 6: Configure Slack App URLs

Now that your bot is live, update your Slack app configuration:

### A. Update Interactivity URL

1. Go to [Slack API Apps](https://api.slack.com/apps)
2. Select your app
3. Go to **"Interactivity & Shortcuts"**
4. Set **Request URL** to: `https://YOUR-RENDER-URL.onrender.com/slack/interactivity`
   - Example: `https://ichydro-slack-bot.onrender.com/slack/interactivity`
5. Click **"Save Changes"**

### B. Update Slash Command URL

1. In your Slack app, go to **"Slash Commands"**
2. Click on your `/publish-news` command
3. Update **Request URL** to: `https://YOUR-RENDER-URL.onrender.com/slack/commands/publish-news`
   - Example: `https://ichydro-slack-bot.onrender.com/slack/commands/publish-news`
4. Click **"Save"**

---

## Step 7: Test Your Bot

1. Open your Slack workspace
2. In any channel, type: `/publish-news`
3. A modal should appear asking for a LinkedIn URL
4. Paste a LinkedIn post URL and submit
5. The bot should:
   - Scrape the LinkedIn post
   - Update `_data/news.yml` in your GitHub repo
   - Send you a success message

---

## Monitoring Your Deployment

### View Logs
1. Go to your Render dashboard
2. Click on your `ichydro-slack-bot` service
3. Click **"Logs"** tab to see real-time activity

### Check Service Status
- Your service URL should show: "OK" or a simple status message
- Visit: `https://your-service.onrender.com/` in a browser

---

## Troubleshooting

### Bot not responding in Slack?
- ✅ Check Render logs for errors
- ✅ Verify environment variables are set correctly
- ✅ Ensure Slack URLs are updated with your Render URL
- ✅ Check that your service is "Live" (not sleeping)

### "Invalid request" error?
- ✅ Check that `SLACK_SIGNING_SECRET` is correct
- ✅ Verify the request URLs in Slack match your Render URL exactly

### GitHub errors?
- ✅ Verify `GITHUB_TOKEN` has `repo` scope
- ✅ Check that the branch `people-page-update` exists
- ✅ Ensure `_data/news.yml` path is correct

### LinkedIn scraping fails?
- ✅ Make sure the LinkedIn URL is publicly accessible
- ✅ Some posts may require authentication (won't work)
- ✅ Check if LinkedIn is blocking requests (rate limiting)

---

## Updating Your Bot

When you make changes to the bot code:

1. Commit and push changes to GitHub:
   ```bash
   git add slackBot/
   git commit -m "Update bot functionality"
   git push fork people-page-update
   ```

2. Render will **auto-deploy** (if you enabled auto-deploy)
   - Or manually click **"Manual Deploy"** → **"Deploy latest commit"**

---

## Free Tier Limits

Render's free tier includes:
- ✅ 750 hours/month (more than enough for 24/7 operation)
- ✅ Automatic SSL/HTTPS
- ✅ Auto-deploy from GitHub
- ✅ Custom domains (if needed)
- ⚠️ Service may spin down after 15 min of inactivity (takes ~30s to wake up)

For your usage (1-2 posts/week), this is perfect!

---

## Need Help?

- **Render Documentation**: [https://render.com/docs](https://render.com/docs)
- **Slack API Documentation**: [https://api.slack.com/docs](https://api.slack.com/docs)
- **Check Render Status**: [https://status.render.com](https://status.render.com)

---

## Success! 🎉

Once everything is working:
1. Type `/publish-news` in Slack
2. Paste a LinkedIn post URL
3. Your news feed automatically updates!

The workflow is now:
```
LinkedIn Post → Slack Command → Render Bot → GitHub → Website Update
```
