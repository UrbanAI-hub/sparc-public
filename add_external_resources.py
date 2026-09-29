import json
import re

# 1. Update projects.json to add paper_url to proj_1
with open('source/projects/projects.json', 'r') as f:
    projects = json.load(f)

for p in projects:
    if p['id'] == 'proj_1':
        p['paper_url'] = "https://www.sciencedirect.com/science/article/pii/S0264275126002982"
    else:
        # initialize empty for others so it exists
        p['paper_url'] = ""

with open('source/projects/projects.json', 'w') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

# 2. Update project.html to render the external resources dynamically
with open('project.html', 'r') as f:
    html = f.read()

# Add the container inside the glass-card, right after project-details
container_html = """
                <div id="project-details" class="markdown-body">
                    <p style="color: var(--text-gray);"><em>Detailed information, methodologies, and outcomes for this project will be added here soon...</em></p>
                </div>
                
                <!-- External Resources Container -->
                <div id="external-resources" style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(128, 128, 128, 0.2); display: none;">
                </div>
"""
html = html.replace("""
                <div id="project-details" class="markdown-body">
                    <p style="color: var(--text-gray);"><em>Detailed information, methodologies, and outcomes for this project will be added here soon...</em></p>
                </div>
""", container_html.strip('\n'))

# Update the renderProject JS to populate it
js_to_insert = """
                        // Handle external resources
                        var extRes = document.getElementById("external-resources");
                        if (project.paper_url && project.paper_url.trim() !== "") {
                            var titleRes = lang === 'en' ? 'External Resources' : 'Externe Bronnen';
                            var btnText = lang === 'en' ? 'Read Full Paper' : 'Lees het volledige onderzoek';
                            extRes.innerHTML = '<h3 style="color: var(--primary-cyan); font-size: 1.3rem; margin-bottom: 1rem; font-weight: 700;">' + titleRes + '</h3>' +
                                               '<a href="' + project.paper_url + '" target="_blank" style="display: inline-block; padding: 12px 24px; background-color: var(--primary-blue); color: white; text-decoration: none; border-radius: 8px; font-weight: 600; transition: opacity 0.2s;">🔗 ' + btnText + '</a>';
                            extRes.style.display = "block";
                        } else {
                            extRes.style.display = "none";
                        }
"""
# Insert it into renderProject right after document.title setting
html = re.sub(
    r'(document\.title = project\["title_" \+ lang\] \+ " \| SPARC";)',
    r'\1\n' + js_to_insert,
    html
)

with open('project.html', 'w') as f:
    f.write(html)

print("Added External Resources logic!")
