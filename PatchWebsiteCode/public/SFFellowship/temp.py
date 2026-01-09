from pathlib import Path
from PIL import Image
import pillow_heif

# Enable HEIC support in Pillow
pillow_heif.register_heif_opener()

# Change this if needed
INPUT_DIR = Path(".")

for heic_path in INPUT_DIR.glob("*.heic"):
    jpg_path = heic_path.with_suffix(".jpg")

    try:
        with Image.open(heic_path) as img:
            # Convert to RGB for JPEG compatibility
            img = img.convert("RGB")
            img.save(jpg_path, "JPEG", quality=95, subsampling=0)

        print(f"✓ {heic_path.name} → {jpg_path.name}")

    except Exception as e:
        print(f"✗ Failed on {heic_path.name}: {e}")
