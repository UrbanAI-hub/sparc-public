# /// script
# requires-python = ">=3.9"
# dependencies = ["pymupdf", "Pillow"]
# ///
import fitz
import io
from PIL import Image

pdf_path = "source/projects/proj_1/paper.pdf"
out_path = "source/projects/proj_1/image.png"

doc = fitz.open(pdf_path)
page = doc[10] # Page 11 (0-indexed)

# Extract raw images embedded in the page
images = page.get_images(full=True)
if images:
    # Get the largest image on the page (which should be the map)
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
        print("Extracted exact figure directly from PDF!")
else:
    print("No images found.")
