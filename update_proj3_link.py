import json

with open('source/projects/projects.json', 'r') as f:
    projects = json.load(f)

for p in projects:
    if p['id'] == 'proj_3':
        p['paper_url'] = "https://www.sciencedirect.com/science/article/pii/S0965856426004155"
        break

with open('source/projects/projects.json', 'w') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

print("Link updated for proj_3")
