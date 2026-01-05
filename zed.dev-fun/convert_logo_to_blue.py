#!/usr/bin/env python3
"""
Convert white Patch logo to blue to match the Zed design system
"""

# Define the blue color from the Zed design system
ACCENT_BLUE = "#0751cf"

# Read the white logo SVG
with open("WhiteLogoNoBackground.svg", "r") as f:
    svg_content = f.read()

# Replace white colors with blue
# Common white color representations
svg_content = svg_content.replace("#FEFEFE", ACCENT_BLUE)
svg_content = svg_content.replace("#fefefe", ACCENT_BLUE)
svg_content = svg_content.replace("#FFFFFF", ACCENT_BLUE)
svg_content = svg_content.replace("#ffffff", ACCENT_BLUE)
svg_content = svg_content.replace("#FFF", ACCENT_BLUE)
svg_content = svg_content.replace("#fff", ACCENT_BLUE)
svg_content = svg_content.replace("fill=\"white\"", f"fill=\"{ACCENT_BLUE}\"")
svg_content = svg_content.replace("fill='white'", f"fill='{ACCENT_BLUE}'")

# Write the blue logo
with open("PatchLogoBlue.svg", "w") as f:
    f.write(svg_content)

print("Created PatchLogoBlue.svg")

# Also create a version with padding for the repeating background pattern
# We'll add some padding around the logo so it repeats nicely
svg_lines = svg_content.split('\n')

# Find the SVG tag and modify dimensions to add padding
new_svg_lines = []
for line in svg_lines:
    if line.startswith('<svg') and 'width=' in line and 'height=' in line:
        # Original: width="784" height="760"
        # Add padding: make it square and centered
        size = 800  # Square size with padding
        new_svg_lines.append(f'<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 {size} {size}">')
        # Add a group with transform to center the original logo
        new_svg_lines.append('<g transform="translate(8, 20)">')
    elif '</svg>' in line:
        new_svg_lines.append('</g>')
        new_svg_lines.append(line)
    else:
        new_svg_lines.append(line)

padded_svg = '\n'.join(new_svg_lines)

with open("PatchLogoBlue_Padded.svg", "w") as f:
    f.write(padded_svg)

print("Created PatchLogoBlue_Padded.svg (for background pattern)")
print("\nNext steps:")
print("1. Use PatchLogoBlue_Padded.svg for the repeating background pattern")
print("2. Use PatchLogoBlue.svg for the spinning badge logo")
