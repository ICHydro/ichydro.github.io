# ICHydro Website

This repository contains the source code for the ICHydro research group website, built with [Jekyll](https://jekyllrb.com/docs/) and hosted on GitHub Pages.

## 🌐 Deployment

The site is automatically deployed via GitHub Pages when changes are pushed to the `master` branch. No manual deployment needed.

**Live Site**: [https://ichydro.github.io](https://ichydro.github.io)

## 💻 Contributing to the website

### 🛠️ Local Development

#### Prerequisites

- [Ruby (2.7+)](https://www.ruby-lang.org/en/)
- [Bundler](https://bundler.io/)

#### Setup

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

### 🔄 Making changes

The website repository structure is shown below. Instructions on how to make routine updates are provided below.

```
├── _config.yml             # Jekyll configuration
├── _data/                  # YAML data files
│   ├── news.yml            # News items
│   ├── researchers.yml     # Team member profiles
│   ├── projects.yml        # Project information
│   └── navigation.yml      # Site navigation
├── _layouts/               # Page templates
│   ├── home.html           # Homepage with globe
│   └── page.html           # Standard page layout
├── _includes/              # Reusable components
├── _sass/                  # SCSS stylesheets
├── assets/                 # Static files
│   ├── css/
│   ├── img/                # Images
│   │   └── news/           # News item images
│   └── js/
├── slackBot/               # Slack integration (optional)
└── projects/               # Project-specific pages
```

#### Publishing news items

News items are stored in [`_data/news.yml`](_data/news.yml) and written in the following format:

```yaml
- id: [NEXT_NUMBER]                       # Unique number; use the next available number
  short_title: "[Brief Title]"            # Brief title used in listings
  title: "[Full Title]"                   # Full title for news page
  date: YYYY-MM-DD                        # Publication date
  description: "[1-2 sentence summary]"   # Brief summary
  link: "[URL if applicable]"             # Optional URL, e.g. LinkedIn post or article
  author: "[Author name]"                 # Name of team member associated with news
  image: "[Image URL or path]"            # Optional URL or path to image in assets/img folder
```

**Note**: You can link directly to a LinkedIn image address (LinkedIn image URLs are long and may change over time, so consider downloading and hosting it instead).

For example:

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

To add an image for a news item, place the image in `/assets/img/news/` and reference in news item as `image: "/assets/img/news/filename.jpg"`. The recommended size is 1200px wide, under 500KB.

#### Updating the People page

Researcher profiles are stored in [`_data/researchers.yml`](_data/researchers.yml) and written in the following format:

```yaml
- name: "Dr Jonathan Doe"
  short_name: "John"
  title: ""Postdoctoral Researcher"
  image: "john-doe.jpg"
  bio: "Brief bio..."
  keywords:
    - "Water quality"
  locations:
    - "Peru"
    - "UK"
  social:
    researchgate: "link-to-research-gate"
    linkedin: "link-to-linkedin-page"
```

Pictures for group members should be saved in [`assets/img/`](assets/img/).

#### Updating publications

Publications are managed in [`_bibliography/references.bib`](_bibliography/references.bib) and are written in APA citation style:

```bibtex
@article{author2024,
  title = {Article Title},
  author = {Author, Name and Other, Person},
  journal = {Journal Name},
  year = {2024},
  doi = {10.1234/example}
}
```

#### Adding project locations
Project locations are stored in [`_data/projects.yml`](_data/projects.yml), for example:

```yaml
- name: "HYDROFLUX"
  location: "Peru, Ecuador, Colombia"
  countries: ["Peru", "Ecuador", "Colombia"]
```

### 📚 Documentation

See the [contributing guidelines](CONTRIBUTING.md) for additional information on how to make changes. For more information on how to use the Slack Bot, which allows team members to publish news directly from Slack, see [`slackBot/README_ENHANCED.md`](slackBot/README_ENHANCED.md).

---

**Repository**: https://github.com/ICHydro/ichydro.github.io  
**Maintained by**: ICHydro Web Team  
**Last Updated**: April 2026
