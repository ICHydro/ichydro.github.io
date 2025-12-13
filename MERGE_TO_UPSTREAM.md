# Merging Fork Back to Upstream Repository

This guide explains how to merge your `people-page-update` branch from your fork (`trowan92/ichydro.github.io`) back into the main ICHydro repository (`ICHydro/ichydro.github.io`).

## 📋 Pre-Merge Checklist

### ✅ Changes Made in This Branch

1. **Researcher Profiles & Publications**
   - Added Uganda to Ben Howard's locations
   - Added Dr Uswah Khairuddin as visiting researcher
   - Updated Dan Bartley profile with complete bio
   - Updated Estefania Quenta bio
   - Fixed Anthony Ross bio grammar
   - Added India location to HYDROFLUX project
   - Added Ben Howard 2025 instream wood paper
   - Removed duplicate "Chiefs and floods" publication

2. **Homepage Enhancements**
   - Interactive globe with 11 country highlights
   - Country tooltips showing projects and people
   - News feed with LinkedIn integration
   - Research theme badges (reduced sizing)
   - Image slideshow

3. **Slack Bot Enhancements**
   - Multi-content type selector (News, Papers, Press, Policy)
   - `/publish-news` - Publish various content types
   - `/remove-news` - Remove news entries
   - Auto-numbering for news entries
   - Paper submission form with DOI, authors, journal, year
   - Generic URL scraping (not just LinkedIn)
   - Short titles with 10-word auto-truncation
   - Slack preview messages

### 🧹 Repository Cleanup

**Files to Clean Up Locally (already in .gitignore):**
- `Gemfile.backup` - Old Gemfile backup
- `Gemfile.lock` - Ruby dependency lock (regenerated)
- `IC HYDRO Website Update.csv` - Working spreadsheet
- `.DS_Store` files - macOS metadata
- `vendor/bundle/` - Ruby gems (installed locally)
- `slackBot/venv/` - Python virtual environment
- `slackBot/.env` - Environment variables (KEEP LOCAL ONLY)
- `slackBot/test_linkedin_scraper.py` - Test script
- `_bibliography/missing_entries.txt` - Working notes
- `_bibliography/scopus_WB_1.12.25` - Working file

**Files Committed and Ready:**
- `_data/researchers.yml` - ✅ Updated profiles
- `_data/projects.yml` - ✅ Added locations
- `_bibliography/references.bib` - ✅ Fixed publications
- `_layouts/home.html` - ✅ Globe and tooltips
- `index.md` - ✅ Cleaned up
- `slackBot/bot.py` - ✅ Enhanced bot
- `slackBot/README_ENHANCED.md` - ✅ Documentation
- `SLACK_BOT_ENHANCEMENT_SUMMARY.md` - ✅ Summary
- `.gitignore` - ✅ Updated

## 🔄 Method 1: Pull Request (Recommended)

This is the standard GitHub workflow and provides review opportunity.

### Step 1: Ensure Everything is Committed
```bash
cd /Users/tslr/Projects/work/ichydro.github.io
git status
# If there are uncommitted changes to home.html:
git add _layouts/home.html
git commit -m "Final home.html updates"
git push fork people-page-update
```

### Step 2: Create Pull Request on GitHub

1. Go to your fork: https://github.com/trowan92/ichydro.github.io
2. Click "Compare & pull request" button
3. **Base repository:** `ICHydro/ichydro.github.io`
4. **Base branch:** `main` (or `master`)
5. **Head repository:** `trowan92/ichydro.github.io`
6. **Compare branch:** `people-page-update`

### Step 3: Fill Out PR Details

**Title:**
```
Enhanced Researcher Profiles, Interactive Globe, and Slack Bot Features
```

**Description:**
```markdown
## Summary
This PR includes major enhancements to the ICHydro website including updated researcher profiles, an interactive globe with tooltips, and a comprehensive Slack bot for content publishing.

## Changes

### 👥 Researcher Profiles & Publications
- Added Uganda to Ben Howard's research locations
- Added Dr Uswah Khairuddin (Visiting Researcher from UTM)
- Enhanced Dan Bartley profile with complete academic background
- Updated Estefania Quenta bio with latest research focus
- Added India location to HYDROFLUX project
- **Publications:** Added missing 2025 paper, removed duplicate entry

### 🌍 Homepage Interactive Globe
- Added D3.js globe with 11 highlighted countries (Peru, Ecuador, Colombia, Venezuela, Chile, Bolivia, Ethiopia, India, Nepal, UK, USA)
- Interactive tooltips showing:
  - Projects active in each country (with logos)
  - Researchers working in each location (with photos)
- Location-to-country mapping system supporting multi-country regions (e.g., "Andes")

### 📰 News Feed Integration
- LinkedIn post integration with auto-scraping
- Scrollable feed with image thumbnails
- Short title display (10 words max)
- Date and author metadata

### 🤖 Slack Bot Enhancements
- **Multi-content publishing:** News, Papers, Press, Policy
- **Commands:** `/publish-news` and `/remove-news`
- **Auto-numbering:** All news entries get sequential IDs
- **Paper form:** DOI, authors, journal, year, abstract
- **URL scraping:** LinkedIn + generic URLs via OpenGraph
- **Previews:** Formatted Slack messages with content preview

### 📚 Documentation
- `slackBot/README_ENHANCED.md` - Complete bot documentation
- `SLACK_BOT_ENHANCEMENT_SUMMARY.md` - Implementation summary
- Updated `.gitignore` for better repository hygiene

## Testing
- ✅ Jekyll builds successfully
- ✅ Globe tooltips working for all countries
- ✅ Slack bot tested locally with ngrok
- ✅ News feed displays correctly
- ✅ All researcher profiles render properly

## Dependencies
- PyYAML added for Slack bot YAML parsing
- D3.js v7 (already included via CDN)
- No breaking changes to existing dependencies

## Deployment Notes
- Slack bot requires environment variables (SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET, GITHUB_TOKEN)
- See `slackBot/README_ENHANCED.md` for complete setup instructions
```

### Step 4: Request Review
Tag relevant team members for review.

### Step 5: Merge
Once approved, click "Merge pull request" → "Confirm merge"

## 🔄 Method 2: Direct Push (If You Have Write Access)

**⚠️ Only use this if you have direct push access to ICHydro/ichydro.github.io**

### Option A: Fast-Forward Merge
```bash
# Add upstream remote if not already added
git remote add upstream https://github.com/ICHydro/ichydro.github.io.git

# Fetch upstream
git fetch upstream

# Switch to your local main branch
git checkout main

# Merge your changes
git merge people-page-update

# Push to upstream
git push upstream main
```

### Option B: Rebase and Push
```bash
# Ensure you're on people-page-update
git checkout people-page-update

# Rebase onto upstream main
git fetch upstream
git rebase upstream/main

# Force push to your fork (if needed)
git push fork people-page-update --force

# Then create PR as in Method 1
```

## 📦 Post-Merge Tasks

### 1. Update Local Repository
```bash
# After PR is merged
git fetch upstream
git checkout main
git merge upstream/main
git push fork main
```

### 2. Clean Up Branch
```bash
# Delete remote branch
git push fork --delete people-page-update

# Delete local branch
git branch -d people-page-update
```

### 3. Deploy Slack Bot
If merging to production:
1. Deploy bot to Render.com or similar
2. Update Slack app URLs to production domain
3. Set environment variables on hosting platform
4. Test `/publish-news` and `/remove-news` commands

### 4. Verify Website
1. Check https://ichydro.github.io (or your domain)
2. Test interactive globe
3. Verify researcher profiles display correctly
4. Check news feed functionality

## 🔒 Secrets & Environment Variables

**NEVER commit these files:**
- `slackBot/.env` - Contains API tokens
- `slackBot/venv/` - Python virtual environment
- Any files with actual credentials

**For Slack bot deployment, you'll need:**
```env
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
GITHUB_TOKEN=ghp_...
```

Store these securely in your hosting platform's environment variables.

## 🐛 Troubleshooting

### "Merge Conflicts"
If you encounter conflicts:
```bash
# On your branch
git fetch upstream
git merge upstream/main
# Resolve conflicts in your editor
git add .
git commit -m "Resolve merge conflicts"
git push fork people-page-update
```

### "Behind Upstream"
If your fork is behind:
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push fork main
```

### "Diverged History"
If histories have diverged significantly, consider squashing commits:
```bash
# Interactive rebase to clean up history
git rebase -i upstream/main
# Follow prompts to squash/reword commits
```

## 📞 Support

If you need help:
1. Check GitHub's [Pull Request documentation](https://docs.github.com/en/pull-requests)
2. Review Git's [merging guide](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
3. Contact repository maintainers

## ✅ Final Checklist Before PR

- [ ] All changes committed and pushed to fork
- [ ] `.gitignore` updated and committed
- [ ] No sensitive files (`.env`, credentials) in commits
- [ ] Documentation updated (READMEs)
- [ ] Tests pass (Jekyll builds, bot runs)
- [ ] Commit messages are clear
- [ ] Branch is up to date with upstream
- [ ] Ready for code review

---

**Branch:** `people-page-update`  
**Fork:** `trowan92/ichydro.github.io`  
**Upstream:** `ICHydro/ichydro.github.io`  
**Date:** December 2025
