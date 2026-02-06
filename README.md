# Thyrs

A markdown-based single-page documentation website with automatic table of contents generation, responsive sidebar navigation, and GitHub Pages deployment.

## Features

- 📝 **Markdown Source** - Write content in simple markdown format
- 📱 **Responsive Design** - Sidebar navigation on desktop, burger menu on mobile
- 📑 **Auto TOC** - Automatically generates table of contents from headers
- ⚡ **Fast Loading** - Lightweight with cache busting for CSS
- 🚀 **GitHub Pages** - Automated deployment with GitHub Actions
- ✨ **Smooth Navigation** - Smooth scrolling to sections

## Quick Start

### Local Development

1. Clone this repository:
   ```bash
   git clone https://github.com/SteffenBlake/Thyrs.git
   cd Thyrs
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Build the HTML from markdown:
   ```bash
   python build.py
   ```

4. Open `index.html` in your web browser or serve locally:
   ```bash
   python -m http.server 8000
   ```

### Deploy to GitHub Pages

The repository includes a GitHub Actions workflow that automatically builds and deploys your site when you push to the `main` branch.

**Setup Steps:**

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under "Build and deployment" → "Source", select **GitHub Actions**
4. Push changes to the `main` branch, and the workflow will automatically:
   - Build the HTML from `content.md`
   - Apply cache busting to CSS
   - Deploy to GitHub Pages
5. Your site will be published at `https://steffenblake.github.io/Thyrs/`

## Customization

### Update Content

Edit `content.md` to customize your documentation:
- Use `#` for top-level sections
- Use `##` for subsections
- Use `###` for sub-subsections
- The table of contents will be automatically generated from these headers

Example:
```markdown
# Getting Started

This is the intro to the getting started section.

## Installation

Instructions for installation.

### Prerequisites

What you need before installing.
```

### Modify Styles

Edit `styles.css` to customize:
- Color scheme (sidebar, links, etc.)
- Typography and fonts
- Layout and spacing
- Responsive breakpoints

### Rebuild

After making changes to `content.md` or `styles.css`, rebuild the site:
```bash
python build.py
```

## File Structure

```
Thyrs/
├── content.md              # Markdown source file
├── build.py                # Build script to generate HTML
├── index.html              # Generated HTML file (auto-generated)
├── styles.css              # CSS stylesheet
├── requirements.txt        # Python dependencies
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
└── README.md               # This file
```

## How It Works

1. **Content**: Write your documentation in `content.md` using standard markdown
2. **Build**: Run `build.py` to convert markdown to HTML with automatic TOC generation
3. **Deploy**: GitHub Actions automatically builds and deploys on push to main
4. **Cache Busting**: CSS files get a unique hash to prevent caching issues

## Browser Support

This template works on all modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

Feel free to use this template for your projects.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.