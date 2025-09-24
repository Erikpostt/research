from pdf2image import convert_from_path
import os

pdf_dir = "./assets/pdf"
output_dir = "./assets/images/poster_thumbnails"
os.makedirs(output_dir, exist_ok=True)

pdf_files = [
    ("poster_ispgr_25.pdf", "poster_ispgr_25_thumb.jpg"),
    ("poster_dps_24.pdf", "poster_dps_24_thumb.jpg"),
    ("poster_wpc_23.pdf", "poster_wpc_23_thumb.jpg"),
]

for pdf, out in pdf_files:
    pages = convert_from_path(os.path.join(pdf_dir, pdf), dpi=150, first_page=1, last_page=1)
    pages[0].save(os.path.join(output_dir, out), "JPEG")
