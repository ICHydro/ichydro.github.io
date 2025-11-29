# People Page TODO List

## Completed ✅
- [x] Interactive researcher cards with circular photos
- [x] Hover effects with grayscale and "More info on [NAME]" overlays  
- [x] Modal popups for detailed researcher bios
- [x] Social media links (ResearchGate, LinkedIn, Twitter, Website)
- [x] Responsive 3-column grid layout
- [x] Left-aligned staff section with Wouter and Ana side-by-side
- [x] Researcher data structure in `_data/researchers.yml`
- [x] Round bordered images with shadows
- [x] Height alignment fixes using flexbox

## Priority Tasks 🔥
- [ ] **Sort staff width/organization** for better visual alignment
- [ ] **Test all social media and website links** to ensure they work correctly
- [ ] **Add missing researcher photos** to replace placeholder images

## Enhancement Tasks 🚀  
- [ ] Verify modal popup content accuracy with actual researcher information
- [ ] Test responsive layout thoroughly on various screen sizes (mobile, tablet, desktop)
- [ ] Consider adding more researchers to fill grid gaps and balance layout
- [ ] Optimize image loading and file sizes for better performance
- [ ] Add animation transitions for smoother user experience
- [ ] Consider adding search/filter functionality for large researcher lists

## Technical Debt 💻
- [ ] Clean up any unused CSS rules
- [ ] Consolidate Jekyll compilation issues 
- [ ] Document the researcher data structure for future additions
- [ ] Add alt text and accessibility improvements
- [ ] Test cross-browser compatibility

## Notes 📝
- Current implementation uses Jekyll + SCSS + JavaScript
- Images should be 240x240px for optimal circular display
- Researcher data structure supports: name, title, bio, image, social links
- Grid system: Staff (2 cols), Researchers (3 cols), PhD Students (3 cols)