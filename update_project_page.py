import re

with open('project.html', 'r') as f:
    html = f.read()

# Add marked.js to head if not present
if 'marked.min.js' not in html:
    html = html.replace('</head>', '    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>\n</head>')

# Update the renderProject function to fetch the markdown
replacement_js = """
                    function renderProject() {
                        lang = localStorage.getItem("sparc_lang") || "en";
                        document.getElementById("project-title").textContent = project["title_" + lang];
                        // document.getElementById("project-desc").textContent = project["desc_" + lang];
                        document.title = project["title_" + lang] + " | SPARC";
                        
                        // Fetch the details markdown file
                        var mdFile = "source/projects/" + projectId + "/details_" + lang + ".md";
                        fetch(mdFile)
                            .then(function(response) {
                                if (response.ok) return response.text();
                                throw new Error("Details not found");
                            })
                            .then(function(text) {
                                document.getElementById("project-details").innerHTML = marked.parse(text);
                            })
                            .catch(function(error) {
                                document.getElementById("project-details").innerHTML = "<p><em>Details coming soon...</em></p>";
                            });
                    }
"""

# We need to replace the old renderProject function
pattern = re.compile(r'function renderProject\(\) \{.*?\}(?=\n\n                    renderProject\(\);)', re.DOTALL)
html = pattern.sub(replacement_js.strip(), html)

with open('project.html', 'w') as f:
    f.write(html)

print("project.html updated to render Markdown dynamically!")
