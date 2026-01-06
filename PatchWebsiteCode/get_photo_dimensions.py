#!/usr/bin/env python3
"""Get dimensions of all photos in the public folder."""

import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Installing Pillow...")
    os.system("pip install Pillow")
    from PIL import Image

script_dir = Path(__file__).parent
public_dir = script_dir / "public"

# Image extensions to look for
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG'}

def get_image_info(path):
    """Get image dimensions and aspect ratio."""
    try:
        with Image.open(path) as img:
            w, h = img.size
            ratio = w / h
            if ratio > 1.3:
                orientation = "landscape"
            elif ratio < 0.77:
                orientation = "portrait"
            else:
                orientation = "square"
            return {
                "path": str(path.relative_to(public_dir)),
                "width": w,
                "height": h,
                "ratio": round(ratio, 2),
                "orientation": orientation
            }
    except Exception as e:
        return {"path": str(path), "error": str(e)}

# Find all images
images = []
for ext in image_extensions:
    images.extend(public_dir.glob(f"**/*{ext}"))

# Get info for each
results = []
for img_path in sorted(images):
    info = get_image_info(img_path)
    results.append(info)

# Print results grouped by orientation
print("\n=== LANDSCAPE PHOTOS (wide) ===")
for r in results:
    if r.get("orientation") == "landscape":
        print(f"  /{r['path']}: {r['width']}x{r['height']} (ratio: {r['ratio']})")

print("\n=== PORTRAIT PHOTOS (tall) ===")
for r in results:
    if r.get("orientation") == "portrait":
        print(f"  /{r['path']}: {r['width']}x{r['height']} (ratio: {r['ratio']})")

print("\n=== SQUARE-ISH PHOTOS ===")
for r in results:
    if r.get("orientation") == "square":
        print(f"  /{r['path']}: {r['width']}x{r['height']} (ratio: {r['ratio']})")

print("\n=== ERRORS ===")
for r in results:
    if "error" in r:
        print(f"  {r['path']}: {r['error']}")

print(f"\nTotal: {len(results)} images")
