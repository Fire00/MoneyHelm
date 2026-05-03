# Finance Planner PWA — Deployment Guide

## 📁 Files in this package
- `index.html` — Main app (all logic, UI, tips & suggestions)
- `manifest.json` — Makes it installable as an app
- `sw.js` — Service worker (offline support)
- `icons/icon-192.png` — App icon (small)
- `icons/icon-512.png` — App icon (large)

---

## 🚀 Option 1: Deploy on Netlify (Recommended — Free, 5 minutes)

1. Go to https://app.netlify.com/drop
2. Drag and drop the entire `finance-pwa` folder onto the page
3. Netlify gives you a live URL like: `https://your-app.netlify.app`
4. Done! Open that URL on your phone and install.

To set a custom name:
- Sign up / log in to Netlify
- Go to Site Settings → Change site name → e.g. `my-finance-planner`
- Your URL becomes: `https://my-finance-planner.netlify.app`

---

## 🚀 Option 2: Deploy on GitHub Pages (Free, ~10 minutes)

1. Create a free account at https://github.com
2. Create a new repository (e.g. `finance-planner`)
3. Upload all files from this folder to the repo
4. Go to Settings → Pages → Source: Deploy from branch → main → / (root)
5. Your URL: `https://yourusername.github.io/finance-planner`

---

## 📱 Installing on Android (Chrome)

1. Open the URL in Chrome
2. Tap the ⋮ menu → "Add to Home screen"
3. Tap "Add" — it appears on your home screen like a native app!
4. Chrome may also show an automatic "Install app" banner at the bottom

---

## 📱 Installing on iPhone (Safari)

1. Open the URL in Safari (must be Safari, not Chrome)
2. Tap the Share button (box with arrow)
3. Scroll down → tap "Add to Home Screen"
4. Tap "Add" — done!

---

## 💾 About your data

- All data is stored in your browser's `localStorage` — it stays on your device
- Data persists across sessions (closing/reopening the app)
- Use "Export Data" (History tab) to back up as a JSON file
- Use "Import Data" to restore from a backup
- Works fully offline once installed

---

## ⚠️ Important notes

- Each browser/device has its own separate data storage
- Clearing browser data/cache will delete your finance data — export a backup regularly!
- The app works on any modern browser (Chrome, Safari, Firefox, Edge)

