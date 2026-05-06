# 🚀 QUICK START GUIDE (5 Minutes)

## اردو میں ہدایات

یہ سسٹم تین چیزوں کے ساتھ کام کرتا ہے:
1. **Tracker 1.png** → **Model 1.glb** کو دکھاتا ہے
2. **Tracker 2.png** → **Model 2.glb** کو دکھاتا ہے
3. **360° Rotation** - ماڈل کو گھومانے کے لیے

---

## Step 1: Generate Marker Files (5 min)

### سب سے آسان طریقہ:

1. یہ لنک کھولیں:
   https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html

2. **Tracker 1.png** اپ لوڈ کریں
   - Download کریں اور **Tracker/ folder** میں **Tracker 1.patt** کے نام سے رکھیں

3. **Tracker 2.png** اپ لوڈ کریں  
   - Download کریں اور **Tracker/ folder** میں **Tracker 2.patt** کے نام سے رکھیں

---

## Step 2: Start Server (2 min)

**Terminal/CMD میں یہ کمانڈ چلائیں:**

```bash
cd /Users/ghurki/Desktop/Ahmad\ Ghurki/Web-Image-Tracking
python3 -m http.server 8000
```

---

## Step 3: Open in Browser (1 min)

1. اپنے براؤزر میں کھولیں:
   ```
   http://localhost:8000
   ```

2. **کیمرہ اجازت دیں** جب پوچھا جائے

3. **Tracker 1.png یا Tracker 2.png** کو کیمرے کے سامنے رکھیں

4. **"Start Rotation"** بٹن دبائیں

---

## ✅ مکمل!

### کام کرنا چاہیے:
✓ ماڈل نظر آئے  
✓ ماڈل Marker کے ساتھ حرکت کرے  
✓ Rotation شروع ہو جائے

### اگر کام نہ ہو تو:
- `.patt` فائلیں **Tracker/** فولڈر میں ہیں؟
- Server چل رہا ہے؟
- کیمرہ اجازت دی گئی؟
- مختلف براؤزر میں کوشش کریں (Chrome بہتر ہے)

---

## 🎮 استعمال

| کیا کریں | نتیجہ |
|---------|--------|
| Marker کو کیمرے کے سامنے رکھیں | ماڈل ظاہر ہو |
| Marker کو حرکت دیں | ماڈل اتبع کرے |
| "Start Rotation" دبائیں | 360° گھومنا شروع ہو |
| دوبارہ دبائیں | گھومنا رکیں |

---

## 🔧 Customization

### Rotation کی رفتار بدلنا:

`index.html` میں تلاش کریں:
```javascript
let rotationSpeed = 2; // درجے فی فریم
```

بڑی تعداد = تیز گھومنا  
چھوٹی تعداد = سست گھومنا

### ماڈل کا سائز بدلنا:

`index.html` میں تلاش کریں:
```xml
scale="1 1 1"
```

- `scale="2 2 2"` = 2x بڑا
- `scale="0.5 0.5 0.5"` = 50% چھوٹا

---

## 📱 موبائل پر استعمال

1. اپنے کمپیوٹر کا IP ڈھونڈیں (عام طور پر `192.168.x.x`)
2. موبائل پر کھولیں: `http://YOUR_IP:8000`
3. باقی وہی ہے!

---

## ❓ عام مسائل

| مسئلہ | حل |
|------|-----|
| ماڈل نہیں دکھ رہا | `.patt` فائلیں بنائی گئی ہیں؟ |
| Marker نہیں پہچانا جا رہا | اچھی روشنی رکھیں، marker پرنٹ کریں |
| Camera نہیں کھل رہا | Permissions چیک کریں (Settings) |
| Rotation کام نہیں کر رہی | "Start Rotation" بٹن دبایا؟ |

---

**تیار ہیں؟ سرور شروع کریں اور مارکر دیکھیں! 🎯**
