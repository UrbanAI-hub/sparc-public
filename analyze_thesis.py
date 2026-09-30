import fitz
import json

pdf_path = "source/projects/proj_5/paper.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {doc.page_count}")

# Get Table of Contents
toc = doc.get_toc()
print("Table of Contents:")
for item in toc:
    print(item)

# Extract first 20 pages (usually covers Title, Abstract, Intro)
intro_text = ""
for i in range(min(20, doc.page_count)):
    intro_text += doc[i].get_text()

# Extract last 15 pages before references (rough guess: page_count - 30 to page_count - 10)
conclusion_text = ""
start_conc = max(0, doc.page_count - 40)
for i in range(start_conc, doc.page_count):
    conclusion_text += doc[i].get_text()

with open("scratch/thesis_intro.txt", "w") as f:
    f.write(intro_text)
    
with open("scratch/thesis_conclusion.txt", "w") as f:
    f.write(conclusion_text)

print("Saved intro and conclusion to scratch.")
