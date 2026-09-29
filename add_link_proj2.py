import json

with open('source/projects/projects.json', 'r') as f:
    projects = json.load(f)

for p in projects:
    if p['id'] == 'proj_2':
        p['paper_url'] = "https://www.tandfonline.com/doi/full/10.1080/13658816.2025.2595658"

with open('source/projects/projects.json', 'w') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

print("Link added successfully to proj_2!")
