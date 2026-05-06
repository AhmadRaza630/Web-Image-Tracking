# 🎯 Web-Based Image Tracking System with 360° Model Viewer

A complete web-based AR image tracking system that displays 3D models and rotates them 360 degrees.

## ✨ Features

- ✅ Real-time image marker tracking (Tracker 1 & 2)
- ✅ 360-degree model rotation
- ✅ Dual model support (Model 1 & Model 2)
- ✅ Live status display
- ✅ Toggle rotation on/off
- ✅ Works on mobile and desktop browsers

## 📁 Project Structure

```
Web-Image-Tracking/
├── index.html                 # Main web application
├── Models/
│   ├── Model 1.glb           # 3D model for Tracker 1
│   └── Model 2.glb           # 3D model for Tracker 2
├── Tracker/
│   ├── Tracker 1.png         # Marker image for Model 1
│   ├── Tracker 2.png         # Marker image for Model 2
│   ├── Tracker 1.patt        # Generated pattern file (to be created)
│   └── Tracker 2.patt        # Generated pattern file (to be created)
├── generate_markers.py        # Python script to generate .patt files
└── SETUP.sh                   # Setup instructions
```

## 🚀 Quick Setup

### Step 1: Generate Pattern Marker Files

Your tracker PNG images need to be converted to `.patt` pattern files for AR.js to recognize them.

#### Option A: Online Tool (Easiest - Recommended)

1. Open this link in your browser:
   https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html

2. **For Tracker 1:**
   - Click "Upload" and select `Tracker/Tracker 1.png`
   - Click "Download marker" 
   - Save as `Tracker/Tracker 1.patt`

3. **For Tracker 2:**
   - Click "Upload" and select `Tracker/Tracker 2.png`
   - Click "Download marker"
   - Save as `Tracker/Tracker 2.patt`

#### Option B: Python Script (If Python 3 is installed)

```bash
cd /Users/ghurki/Desktop/Ahmad\ Ghurki/Web-Image-Tracking
python3 generate_markers.py
```

### Step 2: Start the Web Server

You need to run a local web server because browsers block file:// protocol for security.

#### Using Python 3 (Easiest):
```bash
cd /Users/ghurki/Desktop/Ahmad\ Ghurki/Web-Image-Tracking
python3 -m http.server 8000
```

#### Using Python 2:
```bash
cd /Users/ghurki/Desktop/Ahmad\ Ghurki/Web-Image-Tracking
python -m SimpleHTTPServer 8000
```

#### Using Node.js (if installed):
```bash
cd /Users/ghurki/Desktop/Ahmad\ Ghurki/Web-Image-Tracking
npx http-server
```

### Step 3: Open in Browser

Once the server is running:
- Open: **http://localhost:8000** in your web browser
- Grant camera permission when prompted
- Point your camera at **Tracker 1.png** or **Tracker 2.png**
- Click **"Start Rotation"** to enable 360° model rotation

## 🎮 How to Use

### Tracking
- Point your **webcam** at the printed marker image
- The corresponding 3D model will appear and track the marker
- The model follows the marker position and rotation

### Rotation
- Click the **"Start Rotation"** button to enable automatic 360° rotation
- Click again to stop rotation
- Rotation happens around the Y-axis (vertical)

### Status Information
- **Top-left**: Shows which model is being tracked
- **Top-right**: Current tracking status
- **Bottom**: Rotation control button

## 🔧 Customization

### Change Rotation Speed
Edit `index.html`, find this line:
```javascript
let rotationSpeed = 2; // degrees per frame
```
Increase the value for faster rotation, decrease for slower.

### Adjust Model Scale
Edit `index.html`, find:
```xml
<a-entity
    id="model1"
    gltf-model="url(./Models/Model%201.glb)"
    position="0 0 0"
    rotation="0 0 0"
    scale="1 1 1"  <!-- Change this value (1 1 1) -->
></a-entity>
```

Examples:
- `scale="2 2 2"` → 2x larger
- `scale="0.5 0.5 0.5"` → 50% smaller

### Change Model Position
Modify the `position` attribute (x, y, z values)

## 📱 Mobile Use

1. **On Mobile Device:**
   - Connect to the same WiFi as your computer
   - Find your computer's IP address (usually 192.168.x.x)
   - Open: `http://YOUR_IP:8000` on your mobile browser
   - Allow camera access
   - Point camera at printed marker

## 🔗 Technologies Used

- **A-Frame** - 3D web framework
- **AR.js** - JavaScript AR library with image tracking
- **GLB Models** - 3D model format
- **WebGL** - For 3D rendering

## 📝 Required File Formats

- **Models**: `.glb` (3D model format)
- **Markers**: `.png` (PNG images for tracking)
- **Generated Markers**: `.patt` (Pattern files generated from PNG)

## ⚠️ Troubleshooting

### Models don't appear
- ✅ Check that `.patt` files are generated correctly
- ✅ Verify model file names and paths (spaces matter!)
- ✅ Open browser console (F12) to check for errors

### Camera not working
- ✅ Check browser permissions (Settings → Camera)
- ✅ Use HTTPS or localhost (most browsers require this for camera access)
- ✅ Try a different browser (Chrome/Firefox recommended)

### Models not rotating
- ✅ Click "Start Rotation" button
- ✅ Check that a marker is detected (watch the status display)

### Marker not detected
- ✅ Ensure `.patt` files exist in Tracker/ folder
- ✅ Good lighting is important
- ✅ Print the marker image on paper for best results
- ✅ Marker needs good contrast and distinct patterns

## 📸 Marker Best Practices

For best tracking results:

1. **Print Markers:** Print the PNG images on paper (A4 size recommended)
2. **Good Lighting:** Ensure adequate lighting when scanning
3. **Contrast:** Markers work best with high-contrast patterns
4. **Distance:** Keep marker 20-100cm from camera
5. **Angle:** Avoid extreme angles (optimal: 0-45 degrees)

## 🎓 Learning Resources

- [A-Frame Documentation](https://aframe.io/docs/)
- [AR.js Documentation](https://ar-js-org.github.io/AR.js-Docs/)
- [GLB Model Format](https://www.khronos.org/gltf/)

## 📞 Support

If you encounter issues:
1. Check the browser console (F12) for error messages
2. Verify all files are in correct locations
3. Ensure `.patt` files were generated correctly
4. Try using a different browser
5. Check internet connection (libraries are loaded from CDN)

## ✅ Checklist

- [ ] `.patt` files generated for both trackers
- [ ] Web server running (http://localhost:8000)
- [ ] Browser camera permission granted
- [ ] Models appear when markers are shown
- [ ] Rotation works when button is clicked

---

**Ready?** Start the server and point your camera at the markers! 🎯
