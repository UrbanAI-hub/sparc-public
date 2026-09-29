import fitz
import io
from PIL import Image
import os

pdf_path = "source/projects/proj_4/paper.pdf"
os.makedirs("scratch", exist_ok=True)

doc = fitz.open(pdf_path)

# The analyst said Page 42, 32, 29. 
# We'll check pages 28-44 to be safe against 0-indexing and roman numeral offsets.
for page_num in [28, 31, 41, 42, 43]:
    page = doc[page_num]
    images = page.get_images(full=True)
    if images:
        largest_img = None
        max_size = 0
        for img_info in images:
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            size = len(base_image["image"])
            if size > max_size:
                max_size = size
                largest_img = base_image
        
        if largest_img:
            img = Image.open(io.BytesIO(largest_img["image"]))
            img.save(f"scratch/proj4_page_{page_num}.png")
            print(f"Extracted image from physical page {page_num} to scratch/")

