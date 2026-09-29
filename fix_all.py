import re

# 1. FIX PROJECT.HTML
with open('project.html', 'r') as f:
    html = f.read()

# Bust CSS cache
html = html.replace('href="style.css"', 'href="style.css?v=2"')

# Fix JS image loading
js_old = """
                    // Check for project-specific image
                    var img = new Image();
                    img.onload = function() {
                        document.getElementById("project-image").style.background = 
                            "url('source/projects/" + projectId + "/image.png') no-repeat center center/cover";
                    };
                    img.src = "source/projects/" + projectId + "/image.png";
"""
js_new = """
                    // Check for project-specific image
                    var img = new Image();
                    img.onload = function() {
                        var el = document.getElementById("project-image");
                        el.src = img.src;
                        el.style.display = "block";
                    };
                    img.src = "source/projects/" + projectId + "/image.png";
"""
if js_old.strip() in html:
    html = html.replace(js_old.strip(), js_new.strip())
else:
    # use regex
    html = re.sub(r'var img = new Image\(\);.*?img\.src = "source/projects/" \+ projectId \+ "/image\.png";', js_new.strip(), html, flags=re.DOTALL)

with open('project.html', 'w') as f:
    f.write(html)

# 2. FIX STYLE.CSS (more aggressive styling to override existing ones)
with open('style.css', 'a') as f:
    f.write("""

/* Aggressive Markdown Content Styling */
.markdown-body {
    font-family: 'Inter', sans-serif !important;
    color: var(--text-color) !important;
    line-height: 1.8 !important;
    font-size: 1.15rem !important;
    max-width: 800px !important;
    margin: 0 auto !important;
    padding: 1rem 0 !important;
}

.markdown-body h3 {
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: var(--primary-cyan) !important;
    margin-top: 3.5rem !important;
    margin-bottom: 1.5rem !important;
    padding-bottom: 0.5rem !important;
    border-bottom: 2px solid var(--accent-color) !important;
    display: inline-block !important;
    width: 100% !important;
}

.markdown-body p {
    margin-bottom: 2rem !important;
}

.markdown-body ul {
    margin-bottom: 2.5rem !important;
    padding-left: 2rem !important;
}

.markdown-body li {
    margin-bottom: 0.8rem !important;
}

.markdown-body strong {
    font-weight: 700 !important;
    color: var(--primary-blue) !important;
}
""")

print("Fixes applied.")
