import fitz

pdf_path = "source/projects/proj_5/paper.pdf"
doc = fitz.open(pdf_path)

print("--- EXECUTIVE SUMMARY ---")
for i in range(2, 6): # pages 3 to 6
    print(doc[i].get_text())

print("--- CONCLUSION ---")
for i in range(75, 78): # pages 76 to 78
    print(doc[i].get_text())
