"""
AR.js Marker Generator
Converts PNG images to .patt pattern files for AR.js image tracking
"""

import cv2
import numpy as np
import os
from pathlib import Path

def generate_patt_from_image(image_path, output_path):
    """
    Generate a .patt file from a PNG image for AR.js
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"❌ Error reading image: {image_path}")
            return False
        
        # Resize to 16x16 (standard marker size)
        resized = cv2.resize(image, (16, 16))
        
        # Convert BGR to RGB
        resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        
        # Create .patt file content
        patt_content = ""
        
        # Write marker data (16x16 pixels, 3 bytes per pixel)
        for row in resized:
            for pixel in row:
                r, g, b = pixel
                patt_content += f"{int(r):3d} {int(g):3d} {int(b):3d}\n"
        
        # Write to file
        with open(output_path, 'w') as f:
            f.write(patt_content)
        
        print(f"✓ Generated: {output_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {image_path}: {str(e)}")
        return False

def main():
    base_path = Path(__file__).parent
    tracker_dir = base_path / "Tracker"
    
    print("🔄 Generating AR.js Pattern Markers...\n")
    
    # Generate markers for both trackers
    trackers = [
        ("Tracker 1.png", "Tracker 1.patt"),
        ("Tracker 2.png", "Tracker 2.patt")
    ]
    
    for png_name, patt_name in trackers:
        png_path = tracker_dir / png_name
        patt_path = tracker_dir / patt_name
        
        if png_path.exists():
            generate_patt_from_image(str(png_path), str(patt_path))
        else:
            print(f"⚠️  Not found: {png_path}")
    
    print("\n✅ Pattern generation complete!")
    print("You can now use index.html for image tracking with 360° model rotation")

if __name__ == "__main__":
    main()
