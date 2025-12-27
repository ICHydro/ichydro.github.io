# ICHydro Website

This repository contains the source code for the ICHydro research group website, built with Jekyll and hosted on GitHub Pages.

## 🚀 Quick Start

### Publishing News Items

News items are stored in `_data/news.yml` and displayed automatically on the homepage.

**To add a news item:**
1. Open `_data/news.yml`
2. Add your news at the top of the file:
   ```yaml
   - id: [NEXT_NUMBER]
     short_title: "[Brief Title]"
     title: "[Full Title]"
     date: YYYY-MM-DD
     description: "[1-2 sentence summary]"
     link: "[URL if applicable]"
     author: "[Author name]"
     image: "[Image URL or path]"
   ```
3. Commit and push - the site rebuilds automatically in 2-5 minutes

**Examples:**
```yaml
# Simple news item
- id: 10
  short_title: "New Research Published"
  title: "ICHydro publishes groundbreaking study on mountain hydrology"
  date: 2024-12-22
  description: "Our latest research on water storage in páramo ecosystems has been published in Nature Water."
  author: "ICHydro Team"

# With LinkedIn link and image
- id: 11
  short_title: "Field Campaign Success"
  title: "Successful completion of Ecuador field campaign"
  date: 2024-12-20
  description: "After 6 weeks in the field, our team has successfully deployed 36 soil moisture sensors across three páramo sites."
  link: "https://www.linkedin.com/posts/..."
  author: "Martha Day"
  image: "https://media.licdn.com/dms/image/..."
```

### Local Development

**Prerequisites:**
- Ruby (2.7+)
- Bundler
- Git

**Setup:**
```bash
# Clone the repository
git clone https://github.com/ICHydro/ichydro.github.io.git
cd ichydro.github.io

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# View at http://localhost:4000
```

## 📁 Repository Structure

```
├── _config.yml              # Jekyll configuration
├── _data/                   # YAML data files
│   ├── news.yml            # News items (EDIT THIS for news)
│   ├── researchers.yml     # Team member profiles
│   ├── projects.yml        # Project information
│   └── navigation.yml      # Site navigation
├── _layouts/               # Page templates
│   ├── home.html          # Homepage with globe
│   └── page.html          # Standard page layout
├── _includes/              # Reusable components
├── _sass/                  # SCSS stylesheets
├── assets/                 # Static files
│   ├── css/
│   ├── img/               # Images
│   │   └── news/         # News item images
│   └── js/
├── slackBot/              # Slack integration (optional)
└── projects/              # Project-specific pages
```

## 🌟 Key Features

### Interactive Globe
- D3.js-powered globe with 11 highlighted countries
- Tooltips show projects and researchers by location
- Automatic mapping of project locations to countries

### News Feed
- Integrated with LinkedIn posts
- Auto-scraping of content and images
- Short title display (10 words max)
- Date and author metadata

### Researcher Profiles
- Stored in `_data/researchers.yml`
- Photos, bios, research interests, and locations
- Automatic integration with project pages and globe

### Publications
- Bibliography managed in `_bibliography/references.bib`
- APA citation style
- Highlighted publications on homepage

## 🤖 Slack Bot (Optional)

The Slack bot allows team members to publish news directly from Slack.

**Commands:**
- `/publish-news` - Publish news, papers, press, or policy items
- `/remove-news` - Remove news entries

**Features:**
- Multi-content type selector (News, Papers, Press, Policy)
- Auto-numbering for news entries
- Paper submission with DOI, authors, journal, year
- Generic URL scraping (LinkedIn + others)
- Short title auto-truncation (10 words)
- Slack preview messages

**Setup:**
See `slackBot/README_ENHANCED.md` for complete instructions.

## 🔄 Contributing Changes

### Method 1: Direct Edit on GitHub (Simple)
1. Navigate to the file on GitHub
2. Click the pencil icon (✏️) to edit
3. Make your changes
4. Commit directly to `main` or create a branch for review

### Method 2: Pull Request (Recommended for Major Changes)
1. Fork the repository (if not a member)
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m "Description"`
4. Push to your fork: `git push origin feature-name`
5. Create a Pull Request on GitHub
6. Request review from team members
7. Merge after approval

### Method 3: Local Development
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

# Create PR on GitHub
```

## 📝 Common Tasks

### Update Researcher Profile
Edit `_data/researchers.yml`:
```yaml
- name: "John Doe"
  bio: "Brief bio..."
  photo: "/assets/img/team/john-doe.jpg"
  location: "Peru, Ecuador"
  role: "Postdoctoral Researcher"
```

### Add Publication
Edit `_bibliography/references.bib`:
```bibtex
@article{author2024,
  title = {Article Title},
  author = {Author, Name and Other, Person},
  journal = {Journal Name},
  year = {2024},
  doi = {10.1234/example}
}
```

### Add Project Location
Edit `_data/projects.yml`:
```yaml
- name: "HYDROFLUX"
  location: "Peru, Ecuador, Colombia"
  countries: ["Peru", "Ecuador", "Colombia"]
```

### Add Image for News
1. Place image in `/assets/img/news/`
2. Reference in news item: `image: "/assets/img/news/filename.jpg"`
3. Recommended size: 1200px wide, under 500KB

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

## 📚 Documentation

- **Slack Bot**: See `slackBot/README_ENHANCED.md`
- **Jekyll**: https://jekyllrb.com/docs/
- **GitHub Pages**: https://docs.github.com/en/pages
- **YAML Syntax**: https://yaml.org/

## 🌐 Deployment

The site is automatically deployed via GitHub Pages when changes are pushed to the `main` branch. No manual deployment needed.

**Live Site**: https://ichydro.github.io (or your custom domain)

## 📞 Support

- Create an issue on GitHub for bugs or feature requests
- Contact repository maintainers for access questions
- Check existing documentation in `/slackBot/` for bot-related help

## ✅ Checklist Before Merging Major Changes

- [ ] All changes committed and tested locally
- [ ] `.gitignore` updated if needed
- [ ] No sensitive files in commits
- [ ] Documentation updated
- [ ] Jekyll builds successfully
- [ ] Commit messages are clear and descriptive
- [ ] PR reviewed by team member (if applicable)

---

**Repository**: https://github.com/ICHydro/ichydro.github.io  
**Maintained by**: ICHydro Web Team  
**Last Updated**: December 2025
