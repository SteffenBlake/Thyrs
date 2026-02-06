#!/usr/bin/env python3
"""
Build script to convert markdown to HTML with table of contents.
"""
import markdown
import re
import hashlib
from datetime import datetime

def generate_cache_buster():
    """Generate a cache buster based on current timestamp."""
    return hashlib.md5(str(datetime.now().timestamp()).encode()).hexdigest()[:8]

def build_html():
    """Build the HTML file from markdown content."""
    # Read markdown content
    with open('content.md', 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert markdown to HTML with extensions
    md = markdown.Markdown(extensions=[
        'toc',  # Table of contents
        'extra',  # Extra features like tables, code blocks, etc.
        'nl2br',  # New line to break
    ])
    
    html_content = md.convert(md_content)
    toc_html = md.toc
    
    # Generate cache buster for CSS
    cache_buster = generate_cache_buster()
    
    # Create the full HTML document
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Thyrs - Documentation">
    <title>Thyrs Documentation</title>
    <link rel="stylesheet" href="styles.css?v={cache_buster}">
</head>
<body>
    <div class="page-container">
        <!-- Mobile burger menu button -->
        <button class="burger-menu" id="burgerMenu" aria-label="Toggle menu">
            <span></span>
            <span></span>
            <span></span>
        </button>
        
        <!-- Sidebar navigation -->
        <nav class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h1>Thyrs</h1>
            </div>
            <div class="toc">
                {toc_html}
            </div>
        </nav>
        
        <!-- Main content -->
        <main class="content">
            <div class="content-wrapper">
                {html_content}
            </div>
        </main>
    </div>
    
    <script>
        // Toggle sidebar on mobile
        const burgerMenu = document.getElementById('burgerMenu');
        const sidebar = document.getElementById('sidebar');
        
        burgerMenu.addEventListener('click', () => {{
            sidebar.classList.toggle('active');
            burgerMenu.classList.toggle('active');
        }});
        
        // Close sidebar when clicking on a link (mobile only)
        const tocLinks = document.querySelectorAll('.toc a');
        tocLinks.forEach(link => {{
            link.addEventListener('click', () => {{
                if (window.innerWidth <= 768) {{
                    sidebar.classList.remove('active');
                    burgerMenu.classList.remove('active');
                }}
            }});
        }});
        
        // Close sidebar when clicking outside (mobile only)
        document.addEventListener('click', (e) => {{
            if (window.innerWidth <= 768) {{
                if (!sidebar.contains(e.target) && !burgerMenu.contains(e.target)) {{
                    sidebar.classList.remove('active');
                    burgerMenu.classList.remove('active');
                }}
            }}
        }});
    </script>
</body>
</html>"""
    
    # Write the HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"✓ Built index.html with cache buster: {cache_buster}")

if __name__ == '__main__':
    build_html()
