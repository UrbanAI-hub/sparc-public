import re

with open('project.html', 'r') as f:
    html = f.read()

# The old JS block to replace
js_old = """
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

js_new = """
                        // Handle external resources
                        var extRes = document.getElementById("external-resources");
                        if (project.paper_url && project.paper_url.trim() !== "") {
                            var titleRes = lang === 'en' ? 'External Resources' : 'Externe Bronnen';
                            var descText = lang === 'en' ? 'If you want to dive deeper into the methodology and detailed results, you can access the full scientific publication below:' : 'Als u meer wilt weten over de methodologie en de gedetailleerde resultaten, kunt u hieronder de volledige wetenschappelijke publicatie raadplegen:';
                            var btnText = lang === 'en' ? 'Read Full Paper' : 'Lees het volledige onderzoek';
                            
                            extRes.innerHTML = '<h3 style="color: var(--primary-cyan); font-size: 1.5rem; margin-bottom: 0.5rem; font-weight: 700;">' + titleRes + '</h3>' +
                                               '<p style="color: var(--text-gray); margin-bottom: 1.5rem; line-height: 1.6; font-size: 1.05rem;">' + descText + '</p>' +
                                               '<a href="' + project.paper_url + '" target="_blank" style="display: inline-block; padding: 12px 24px; background-color: var(--primary-cyan); color: #fff; text-decoration: none; border-radius: 8px; font-weight: 600; transition: opacity 0.2s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">🔗 ' + btnText + '</a>';
                            extRes.style.display = "block";
                        } else {
                            extRes.style.display = "none";
                        }
"""

if js_old.strip() in html:
    html = html.replace(js_old.strip(), js_new.strip())
else:
    # Use regex if exact match fails
    pattern = re.compile(r'// Handle external resources.*?extRes\.style\.display = "none";\s*\}', re.DOTALL)
    html = pattern.sub(js_new.strip(), html)

with open('project.html', 'w') as f:
    f.write(html)

print("Button fixed!")
