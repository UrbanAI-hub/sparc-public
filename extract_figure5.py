import fitz
import io
from PIL import Image

pdf_path = "source/projects/proj_5/paper.pdf"
out_path = "source/projects/proj_5/image.png"

doc = fitz.open(pdf_path)

# Look around page 63 (Routing Study) or page 90 (Routing Average Performance)
for page_num in [63, 64, 65, 89, 90]:
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
            img.save(out_path)
            print(f"Extracted image from page {page_num} to {out_path}")
            break
