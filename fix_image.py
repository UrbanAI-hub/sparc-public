import fitz  # PyMuPDF
from PIL import Image
import io
import os

pdf_path = "/Users/fgarridovalenz/Documents/Repos/sparc-public/source/projects/proj_1/paper.pdf"
out_path = "/Users/fgarridovalenz/Documents/Repos/sparc-public/source/projects/proj_1/image.png"

# Open the PDF and get page 11 (index 10)
doc = fitz.open(pdf_path)
page = doc.load_page(10) # 0-indexed

# Figure 6 is on this page. We'll render the page at high res and crop roughly to the figure.
zoom_x = 3.0  # horizontal zoom
zoom_y = 3.0  # vertical zoom
mat = fitz.Matrix(zoom_x, zoom_y)
pix = page.get_pixmap(matrix=mat)

# Convert to PIL Image
img = Image.open(io.BytesIO(pix.tobytes("png")))

# The image is on the upper/middle part of page 11 usually.
# Let's crop out the margins.
width, height = img.size
# Crop margins: left, top, right, bottom (rough estimation to just remove white space and text)
# Actually, let's just save the whole page with margins trimmed.
bbox = img.getbbox()
img_cropped = img.crop(bbox)

# Save the high-res uncropped image
img_cropped.save(out_path)
print("Saved full image to", out_path)
