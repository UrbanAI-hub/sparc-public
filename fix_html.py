import re

with open('project.html', 'r') as f:
    html = f.read()

# Replace the div with an img tag
html = re.sub(
    r'<div id="project-image".*?</div>',
    r'<img id="project-image" style="width: 100%; max-height: 600px; object-fit: contain; margin-bottom: 2rem; border-radius: 12px; display: none;">',
    html,
    flags=re.DOTALL
)

# Update the JS that sets the image
js_replace = """
                var img = new Image();
                img.onload = function() {
                    var el = document.getElementById("project-image");
                    el.src = img.src;
                    el.style.display = "block";
                };
"""
html = re.sub(
    r'var img = new Image\(\);\s+img\.onload = function\(\) \{\s+document\.getElementById\("project-image"\)\.style\.backgroundImage =.*?;\s+\};',
    js_replace.strip(),
    html,
    flags=re.DOTALL
)

# Add the markdown-body class to the details container
html = html.replace('<div id="project-details">', '<div id="project-details" class="markdown-body">')

with open('project.html', 'w') as f:
    f.write(html)
print("Updated project.html layout!")
