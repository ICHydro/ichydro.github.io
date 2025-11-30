# People Page Update Branch - Changes Summary

This document outlines all changes made on the `people-page-update` branch.

## Branch Information
- **Branch Name**: `people-page-update`
- **Base Branch**: `main`
- **Repository**: trowan92/ichydro.github.io (fork)
- **Deployed Site**: https://trowan92.github.io/ichydro.github.io/

---

## Major Changes

### 1. Projects Page Improvements
**Files Modified**: `projects.md`

- ✅ Restructured projects into **Active** and **Past** projects sections
- ✅ Past projects now display as a bulleted list with project name, period, and description
- ✅ Fixed image paths for all project logos (removed `/assets/img/` prefix)
- ✅ Added keywords and locations to all active projects:
  - **FLOODTWIN**: Digital Twin, Flood risk, Forecasting, Real-time monitoring | UK
  - **SMARTWATER**: Water quality, Sensor networks, Data analytics | UK
  - **Deplete and Retreat**: Climate Change, Glacier retreat, Water security | Andes
  - **FDRI**: Research Infrastructure, Floods, Droughts, Climate Resilience | UK locations
- ✅ Added digital twin icon (`fas fa-project-diagram`) to FLOODTWIN project

---

### 2. People Page Enhancement
**Files Modified**: `people.md`, `_data/researchers.yml`

#### Team Member Profile Updates
- ✅ Added **short_name** field for cleaner hover text display
- ✅ Added **keywords** and **locations** to all team members
- ✅ Added **ORCID IDs** from team member submissions:
  - Dr Rike Becker: 0000-0002-9040-1355
  - Dr Ben Howard: 0000-0003-4010-8131
  - Dr Estefania Quenta Herrera: 0000-0002-2724-5804
  - Dr Tom Rowan: 0000-0002-9106-2375
  - Luke Tumelty: 0009-0002-3554-2646
  - Olivia Atkins: 0009-0003-3988-6275
  - Jose Cuadros Adriazola: 0000-0002-6809-2111
  - Martha Day: 0009-0006-9205-7806
  - Anthony C. Ross: 0000-0003-3106-8131
  - Dalal Sadeqi: 0000-0003-0286-9802
  - Professor Wouter Buytaert: 0000-0001-6994-4454

#### Title Updates
- ✅ Updated Wouter's title from "Dr" to "Professor"

#### UI/UX Improvements
- ✅ **Fixed hover overlay text**: Now shows "More info" on line 1, person's short name on line 2
  - Example: "Dr Estefania Quenta Herrera" displays as "More info" / "Estefania"
- ✅ **Removed ORCID links from cards**: ORCID only appears in modal popups to prevent empty blue circles
- ✅ **Added event.stopPropagation()** to all social links to prevent modal trigger when clicking social icons
- ✅ **Fixed blue circle bug**: Changed `<a id="main content">` to `<div id="main-content">` in `_layouts/page.html`

#### Badge System Enhancements
**Files Modified**: `_sass/layout/_team.scss`, `people.md`

##### Location Badge Icons
Added contextual Font Awesome icons to location badges:
- 🏔️ **Mountain icon** (`fa-mountain`): Mountain ranges (Andes, Rwenzori Mountains)
- 🚩 **Flag icon** (`fa-flag`): Countries (Peru, Bolivia, Ecuador, Uganda, Ghana, Rwanda, Kuwait, etc.)
- 🌎 **Globe icon** (`fa-globe-americas`): Continents (Africa, South America, Asia, Europe)
- 📍 **Pin icon** (`fa-map-marker-alt`): Specific cities/regions (default)

##### Master Keyword Color Scheme
Implemented **consistent, semantic color coding** across all cards using CSS attribute selectors:

| Theme | Keywords | Color |
|-------|----------|-------|
| **Climate** | Climate Change, Climate Adaptation | Red shades (#ffebee, #fce4ec) |
| **Water** | Water Security, Hydrology, Floods, Droughts | Blue shades (#e3f2fd) |
| **Mountains** | Mountain Hydrology, Andes | Brown/Earth tones (#efebe9) |
| **Ecosystems** | Wetlands, Ecosystems, Biogeochemistry | Green shades (#e8f5e9) |
| **Technology** | Machine Learning, IoT, Sensors, Digital Twin | Purple shades (#f3e5f5) |
| **Modeling** | Forecasting, Simulation | Teal shades (#e0f2f1) |
| **Policy** | Water Management, Governance | Orange shades (#fff3e0) |
| **Risk** | Flood Risk, Wildfire, Hazards | Deep red (#ffebee) |
| **Methods** | Co-creation, Participatory, Systems Thinking | Indigo (#e8eaf6) |
| **Default** | Unmatched keywords | Gray (#f5f5f5) |

---

### 3. Publications Page Updates
**Files Modified**: `_bibliography/references.bib`

#### Bibliography Cleanup
- ✅ Removed abstracts from 8+ bibliography entries
- ✅ Added missing DOI fields to multiple entries
- ✅ Added **clickable title URLs** to recent papers:
  - Howard2025-up: "Four principles of transformative adaptation..."
  - Howard2025-yl: "Effects of instream wood reintroduction..."
  - Clayton2025-vq: "Associations of anthropogenic activity..."
  - Agyei-Mensah2024-yw: "Chiefs and floods..."
  - Marcotte2024-ub: "Enhanced hydrologic connectivity..."

#### Author Highlighting
- ✅ Made ICHydro group member names **bold** in all publication author lists
- ✅ Created complete, properly formatted author lists for all publications

---

## Technical Improvements

### CSS/Styling
- Updated badge styling to support icons (`inline-flex`, `gap: 4px`)
- Added data attributes for keyword-based color matching
- Implemented sophisticated CSS attribute selectors for semantic coloring

### Layout Templates
- Fixed `_layouts/page.html` empty anchor tag issue
- Added proper event handling for clickable cards with nested links

### Data Structure
- Added `short_name` field to researchers.yml schema
- Expanded social links to include ORCID in modal popups only
- Added `icon` field to projects.yml for custom project icons

---

## How to Update the Site

### Adding a New Team Member
1. Open `_data/researchers.yml`
2. Add entry under appropriate section (`staff`, `researchers`, or `phd_students`):
```yaml
  - name: "Dr Full Name"
    short_name: "FirstName"  # Used in hover overlay
    title: "Position Title"
    image: "filename.jpg"  # Place in assets/img/
    bio: "Biography text..."
    keywords:
      - "Keyword 1"  # Will auto-color based on theme
      - "Keyword 2"
    locations:
      - "Location 1"  # Will auto-icon (mountain/flag/globe/pin)
    social:
      researchgate: "https://..."
      linkedin: "https://..."
      orcid: "https://orcid.org/####-####-####-####"
```

### Adding a New Publication
1. Open `_bibliography/references.bib`
2. Add BibTeX entry with these required fields:
```bibtex
@ARTICLE{AuthorYear-id,
  title     = "Paper Title",
  author    = "LastName, FirstName and ...",
  journal   = "Journal Name",
  volume    = X,
  year      = YYYY,
  url       = "https://doi.org/XX.XXXX/...",  # Makes title clickable
  doi       = "XX.XXXX/..."
}
```
3. Bold ICHydro member names in author field

### Adding a New Project
1. Open `_data/projects.yml`
2. Add under `active:` or `past:` section:
```yaml
  - name: "Project Name"
    period: "YYYY - YYYY"
    funding: "Funder (£Amount)"
    role: "PI/Co-PI"
    lead: "Lead Name, Institution"
    logo: "filename.png"  # In assets/img/
    website: "https://..."
    description: "Project description..."
    keywords:
      - "Keyword 1"
      - "Keyword 2"
    locations:
      - "Location 1"
    icon: "fas fa-icon-name"  # Optional Font Awesome icon
```

### Updating Keywords/Locations
Keywords auto-color based on content matching in CSS. Current themes:
- Climate keywords → Red
- Water keywords → Blue
- Mountain keywords → Brown
- Ecosystem keywords → Green
- Technology keywords → Purple
- etc.

To add new color themes, edit `_sass/layout/_team.scss` around line 380.

---

## Deployment

### Testing Changes
1. Push to `people-page-update` branch on trowan92/ichydro.github.io
2. View at: https://trowan92.github.io/ichydro.github.io/
3. Wait 1-2 minutes for GitHub Pages to rebuild

### Merging to Main
When ready to deploy to production:
1. Create Pull Request from `people-page-update` to `main` on ICHydro/ichydro.github.io
2. Review all changes
3. Merge PR
4. Production site updates automatically

---

## Files Modified Summary

### Configuration
- `_layouts/page.html` - Fixed empty anchor tag bug

### Content
- `projects.md` - Restructured active/past projects
- `people.md` - Updated hover overlays, added icons to badges
- `_data/researchers.yml` - Added short names, keywords, locations, ORCIDs
- `_data/projects.yml` - Added keywords, locations to active projects
- `_bibliography/references.bib` - Added URLs, cleaned formatting

### Styling
- `_sass/layout/_team.scss` - Badge icons, keyword color scheme

---

## Commit History Highlights
1. `ac3d5a2` - Remove ORCID social links from cards
2. `0ac60f0` - Update hover overlay text formatting
3. `732cb71` - Update Wouter's title to Professor
4. `544f5bc` - Fix blue circle issue in page layout
5. `b27daa5` - Add icons and color scheme to badges
6. `5bf5ec7` - Add ORCID IDs and short names
7. `6befd38` - Update Tom Rowan's profile
8. `539bb69` - Add URL fields to bibliography entries

---

## Known Issues
- None currently

## Future Enhancements
- Consider adding profile photos for team members without them
- Add publication count badges to team member cards
- Implement search/filter functionality for publications page
- Add project status indicators (ongoing/completed)
