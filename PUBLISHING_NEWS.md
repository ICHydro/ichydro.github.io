# Publishing News Items to the ICHydro Website

This guide explains how to publish news items directly to the ICHydro website by committing changes to the repository.

## Overview

News items on the ICHydro website are stored in a YAML data file (`_data/news.yml`) and are automatically displayed on the homepage and news page. You can add new news items by editing this file and committing the changes to the repository.

## Prerequisites

- Access to the GitHub repository (`ICHydro/ichydro.github.io`)
- Basic understanding of YAML syntax
- (Optional) A text editor with YAML syntax highlighting

## Quick Start

1. Navigate to the `_data/news.yml` file in the repository
2. Add your new news item at the top of the file (see format below)
3. Commit and push your changes
4. The website will automatically rebuild and display your news item

## News Item Format

Each news item follows this structure in YAML format:

```yaml
- id: [UNIQUE_NUMBER]
  short_title: "[Brief Title]"
  title: "[Full Title]"
  date: YYYY-MM-DD
  description: "[Brief description of the news item, 1-2 sentences]"
  link: "[URL to external link if applicable]"
  author: "[Author name]"
  image: "[URL or path to image]"
```

### Field Descriptions

- **id**: A unique number for the news item. Use the next available number (check the existing items)
- **short_title**: A brief, descriptive title for the news item (used in listings)
- **title**: The full title as it will appear on the news page
- **date**: Publication date in YYYY-MM-DD format (e.g., 2024-12-22)
- **description**: A brief summary of the news (1-2 sentences, can be longer if needed)
- **link**: (Optional) URL to an external page with more details (e.g., LinkedIn post, article)
- **author**: Name of the person or team associated with the news
- **image**: (Optional) URL to an image or path to an image in the `assets/img/` folder

## Step-by-Step Instructions

### Method 1: Direct Edit on GitHub (Easiest)

1. **Navigate to the file**
   - Go to https://github.com/ICHydro/ichydro.github.io
   - Click on `_data` folder
   - Click on `news.yml` file

2. **Edit the file**
   - Click the pencil icon (✏️) in the top right to edit
   - Add your new news item at the **top** of the file, after the opening `---` but before the first existing item
   - Follow the format shown in the examples below

3. **Commit changes**
   - Scroll to the bottom of the page
   - Add a commit message (e.g., "Add news: [brief description]")
   - Choose "Commit directly to the `main` branch" (or create a new branch for review)
   - Click "Commit changes"

4. **Wait for deployment**
   - GitHub will automatically rebuild the website
   - Changes typically appear within 2-5 minutes
   - Check the "Actions" tab to monitor the deployment

### Method 2: Local Edit and Push (For Multiple Changes)

1. **Clone the repository** (if you haven't already)
   ```bash
   git clone https://github.com/ICHydro/ichydro.github.io.git
   cd ichydro.github.io
   ```

2. **Open the news file**
   ```bash
   open _data/news.yml
   # or use your preferred text editor
   ```

3. **Add your news item** at the top of the file

4. **Commit and push**
   ```bash
   git add _data/news.yml
   git commit -m "Add news: [brief description]"
   git push origin main
   ```

## Examples

### Example 1: Simple News Item (No External Link)

```yaml
- id: 10
  short_title: "New Research Published"
  title: "ICHydro publishes groundbreaking study on mountain hydrology"
  date: 2024-12-22
  description: "Our latest research on water storage in páramo ecosystems has been published in Nature Water. This study reveals critical insights into how these unique ecosystems regulate water supply."
  author: "ICHydro Team"
```

### Example 2: News with LinkedIn Post Link

```yaml
- id: 11
  short_title: "Field Campaign Success"
  title: "Successful completion of Ecuador field campaign"
  date: 2024-12-20
  description: "After 6 weeks in the field, our team has successfully deployed 36 soil moisture sensors across three páramo sites. The data will help us understand how these ecosystems respond to climate variability."
  link: "https://www.linkedin.com/posts/..."
  author: "Martha Day"
  image: "https://media.licdn.com/dms/image/..."
```

### Example 3: News with Local Image

```yaml
- id: 12
  short_title: "Welcome New Team Member"
  title: "Dr. Jane Smith joins ICHydro as Research Associate"
  date: 2024-12-18
  description: "We are delighted to welcome Dr. Jane Smith to the ICHydro team. Jane will be working on our NERC-funded project investigating water security in mountain regions."
  author: "Wouter Buytaert"
  image: "/assets/img/news/jane-smith-welcome.jpg"
```

## Image Guidelines

### Using LinkedIn Images

When sharing LinkedIn posts, you can link directly to LinkedIn images:
1. Open the LinkedIn post
2. Right-click on the image and select "Copy image address"
3. Paste this URL in the `image` field

**Note**: LinkedIn image URLs are long and may change over time. For permanent news items, consider downloading and hosting the image locally.

### Using Local Images

For images you want to host on the website:

1. **Prepare your image**
   - Recommended size: 1200px wide (height will auto-adjust)
   - Format: JPG or PNG
   - File size: Keep under 500KB for fast loading

2. **Add to repository**
   - Place image in `/assets/img/news/` folder
   - Use a descriptive filename (e.g., `fieldwork-ecuador-2024.jpg`)

3. **Reference in news item**
   ```yaml
   image: "/assets/img/news/fieldwork-ecuador-2024.jpg"
   ```

## Best Practices

### Writing Descriptions

- Keep descriptions concise but informative (1-3 sentences)
- Front-load the most important information
- Use active voice when possible
- Avoid jargon unless necessary

### Choosing Dates

- Use the actual publication date of the news
- For announcements, use the date you're publishing the news
- Format: YYYY-MM-DD (e.g., 2024-12-22)

### Ordering News Items

- **Always add new items at the top** of the file
- News items are displayed in the order they appear in the file
- The most recent items should be at the top

### ID Numbers

- IDs should be unique integers
- Use sequential numbering for simplicity
- Check the file to find the highest existing ID and add 1

## Troubleshooting

### Website not updating after commit

1. Check the GitHub Actions tab to see if the build succeeded
2. Wait 5 minutes - builds can take time
3. Clear your browser cache (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
4. Check the commit history to ensure your changes were saved

### YAML syntax errors

If the website fails to build, you may have a YAML syntax error:
- Ensure all fields are properly indented (use spaces, not tabs)
- Check that strings with special characters are wrapped in quotes
- Verify that the date format is correct (YYYY-MM-DD)
- Ensure there's a dash (`-`) before each news item
- Make sure colons (`:`) have a space after them

### Images not displaying

- Check that the image URL is accessible
- For local images, verify the file path is correct
- Ensure the image file is committed to the repository
- Check that the image format is supported (JPG, PNG, GIF)

## Getting Help

If you encounter issues:
1. Check the GitHub Actions logs for error messages
2. Compare your YAML format with existing news items
3. Contact the website maintainer or create an issue on GitHub
4. Refer to the YAML syntax guide: https://yaml.org/

## Advanced: Automating News Posts

For team members who frequently post on LinkedIn, consider using the SlackBot integration (see `slackBot/README.md`) which can automatically create news items from LinkedIn posts.

## Example Workflow

Here's a complete workflow for adding a news item about a recent publication:

1. **Gather information**
   - Publication title and authors
   - Journal name and date
   - Brief summary (1-2 sentences)
   - DOI or URL link
   - (Optional) Associated image

2. **Create the news item**
   ```yaml
   - id: 15
     short_title: "New Publication in Water Research"
     title: "Framework for impact analysis of small hydropower published"
     date: 2024-12-15
     description: "Our latest paper presents a comprehensive framework for assessing the ecological impacts of small hydropower installations on river systems. This work has important implications for sustainable hydropower development."
     link: "https://doi.org/10.1016/j.watres.2024.123456"
     author: "Li et al."
   ```

3. **Add to repository**
   - Open `_data/news.yml` on GitHub
   - Click edit (✏️)
   - Paste your news item at the top
   - Commit with message: "Add news: New publication in Water Research"

4. **Verify**
   - Wait 3-5 minutes for deployment
   - Visit the website homepage
   - Check that your news item appears correctly

## File Structure Reference

```
ichydro.github.io/
├── _data/
│   └── news.yml           ← Edit this file to add news
├── assets/
│   └── img/
│       └── news/          ← Place news images here
└── index.md               ← Homepage displays latest news
```

---

**Last updated**: December 2024
**Maintained by**: ICHydro Web Team
