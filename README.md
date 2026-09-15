# ExifScrubber

A lightweight, automated EXIF and metadata sanitizer designed for photographers, digital artists, and privacy-conscious creators.

## ✨ Key Features
- **Privacy-First Stripping**: Removes GPS coordinates, camera serial numbers, lens profiles, and capture timestamps.
- **Batch Processing**: Automatically scans the current working directory and sanitizes all JPG, PNG, and WebP assets.
- **Non-Destructive**: Original images remain completely untouched; cleaned files are saved into a dedicated `sanitized_images` directory.

## 🛠 Requirements
Requires Python 3 and the Pillow imaging library:

```bash
pip install pillow
