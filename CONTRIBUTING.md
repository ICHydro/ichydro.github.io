
# 🤝 How to contribute to the ICHydro website

## 🔀 Pull requests

To contribute a change to the repository, open a pull requests. If not a member, this can be done by forking the repository. To make your changes locally:

```bash
# Create a new branch
git checkout -b your-feature-name

# Make changes and test locally
bundle exec jekyll serve

# Commit changes
git add .
git commit -m "Descriptive commit message"

# Push to remote
git push origin your-feature-name
```

Then, create PR on GitHub, request review from team members and merge after approval.

## 🔒 Security & Best Practices

### Never Commit These Files:
- `slackBot/.env` - Contains API tokens
- `slackBot/venv/` - Python virtual environment
- `Gemfile.lock` - Ruby dependency lock
- `.DS_Store` - macOS metadata
- Personal credentials or tokens

These are already in `.gitignore`.

### For Slack Bot Deployment:
Store secrets in environment variables:
```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
GITHUB_TOKEN=ghp_...
```

## 🐛 Troubleshooting

### Site not updating after commit
- Check GitHub Actions tab for build status
- Wait 5 minutes - builds take time
- Clear browser cache (Cmd+Shift+R / Ctrl+Shift+R)
- Verify commit in repository history

### YAML syntax errors
- Use spaces, not tabs for indentation
- Wrap strings with special characters in quotes
- Verify date format: YYYY-MM-DD
- Ensure colons have space after them
- Check that each item starts with a dash (`-`)

### Images not displaying
- Verify image URL is accessible
- Check file path for local images
- Ensure image is committed to repository
- Confirm format is supported (JPG, PNG, GIF)

### Jekyll build fails locally
```bash
# Update dependencies
bundle update

# Clear cache
bundle exec jekyll clean

# Rebuild
bundle exec jekyll serve
```
