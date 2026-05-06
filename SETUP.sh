#!/bin/bash
# IMPORTANT: You need to generate .patt files from your PNG tracker images
# 
# Method 1: Online Tool (Easiest)
# ================================
# 1. Go to: https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html
# 2. Upload Tracker 1.png → Download the .patt file → Save as Tracker/Tracker 1.patt
# 3. Upload Tracker 2.png → Download the .patt file → Save as Tracker/Tracker 2.patt
#
# Method 2: Using Python (If installed)
# ======================================
# Install required package:
# pip install opencv-python numpy
#
# Then run:
# python3 generate_markers.py
#
# Method 3: Docker (Recommended for automation)
# ==============================================
# docker run --rm -v $(pwd):/work node:18 \
#   sh -c "cd /work && npm install ar.js && npm run generate-markers"

echo "=========================================="
echo "AR.js Image Marker Setup Instructions"
echo "=========================================="
echo ""
echo "Your tracker images are located at:"
echo "  - Tracker/Tracker 1.png"
echo "  - Tracker/Tracker 2.png"
echo ""
echo "Required .patt files must be generated from these images."
echo ""
echo "QUICKEST SOLUTION:"
echo "1. Open in browser: https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html"
echo "2. Upload Tracker/Tracker 1.png"
echo "3. Download and save as Tracker/Tracker 1.patt"
echo "4. Repeat for Tracker/Tracker 2.png → Tracker/Tracker 2.patt"
echo ""
echo "Then open index.html in a web browser to use the tracking system!"
echo "=========================================="
