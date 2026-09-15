#!/usr/bin/env python3
"""
ExifScrubber: High-efficiency, batch EXIF/metadata sanitizer for photographers.
Requires: Pillow ('pip install pillow')
"""

import os
import sys
from PIL import Image

def scrub_exif(source_folder="."):
    valid_exts = (".jpg", ".jpeg", ".png", ".webp")
    files = [f for f in os.listdir(source_folder) if f.lower().endswith(valid_exts)]
    
    if not files:
        print("[-] No matching image files found in the current directory.")
        return

    output_folder = os.path.join(source_folder, "sanitized_images")
    os.makedirs(output_folder, exist_ok=True)

    print(f"[+] Found {len(files)} images. Stripping metadata...")

    for idx, filename in enumerate(files, 1):
        src_path = os.path.join(source_folder, filename)
        dest_path = os.path.join(output_folder, filename)

        try:
            with Image.open(src_path) as img:
                # Reconstruct image buffer without EXIF dict
                data = list(img.getdata())
                clean_img = Image.new(img.mode, img.size)
                clean_img.putdata(data)
                clean_img.save(dest_path)
            print(f"  [{idx}/{len(files)}] Sanitized -> {filename}")
        except Exception as e:
            print(f"  [!] Failed to scrub {filename}: {e}")

    print(f"[✓] Completed! Clean images saved to: {output_folder}")

if __name__ == "__main__":
    scrub_exif()
