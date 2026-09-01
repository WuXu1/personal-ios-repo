# Personal iOS Repository & AltStore Source — Claude Code Context

This document provides complete, self-contained context and operating guidelines for managing **Max's iOS Repository** (`personal-ios-repo`), which serves as a private, self-hosted AltStore source for custom iOS apps.

---

## 1. Project Overview & Architecture

- **GitHub Repository:** `WuXu1/personal-ios-repo` (Local path: `/Users/maxk/Documents/GitHub/personal-ios-repo`)
- **Primary Source Manifest:** `apps.json`
- **Distribution Method:** The source is served publicly to AltStore via a **GitHub Secret Gist**.
- **Secret Gist ID:** `7bb9258857f12767e3b1b092c6dfb959`
- **Raw Gist URL (AltStore Source URL):**
  `https://gist.githubusercontent.com/WuXu1/7bb9258857f12767e3b1b092c6dfb959/raw/apps.json`
- **Static Assets (Icons & Screenshots):** Hosted in the repository under `/icons/` and `/screenshots/` and referenced via GitHub `raw.githubusercontent.com` URLs.

---

## 2. Core Workflow & Deployment Commands

Whenever modifying `apps.json` or adding static assets (icons/screenshots), **always sync to the Secret Gist and push to GitHub**:

```bash
# 1. Update the Secret Gist (this updates the live AltStore source immediately)
gh gist edit 7bb9258857f12767e3b1b092c6dfb959 apps.json

# 2. Commit and push changes to the GitHub repository
git add apps.json icons/ screenshots/
git commit -m "Your descriptive commit message"
git push
```

> **Pro-tip:** When modifying `apps.json`, always use a small Python script (`json.load` / `json.dump`) to modify the JSON structure safely. This prevents JSON escaping errors with multiline changelogs. Clean up any temporary python scripts before committing.

---

## 3. Strict Formatting Conventions & Rules

When the user asks you to add a new version or edit an app, you **must adhere to these rules**:

1. **No Hashtags:** Never include `#`, `##`, or `###` in changelogs or descriptions. AltStore renders these as literal characters, which looks unpolished.
2. **No Emojis:** Do not include emojis in version changelogs.
3. **App Store Style Changelogs:** Format changelogs with clean section headers ending in a colon, followed by Unicode bullet points (`• `) with bolded feature titles:
   ```text
   Section Title:
   • Feature Name: Description of the change.
   • Another Improvement: Description of the change.
   ```
4. **No "WHAT'S NEW IN..." Headers:** Do not prepend `WHAT'S NEW IN VERSION X.X` to the changelog text. Jump straight into the bullet points.
5. **Always Maintain Full Version History (Prepend New Releases):**
   - When adding a new version, **prepend** the new entry to the top of the `versions` array (index `0`) so it is the latest release.
   - Keep all previous version objects intact in the `versions` array.
   - Update the top-level app fields (`version`, `versionDate`, `versionDescription`, `downloadURL`) to match the new latest release.
6. **Prevent Countdown Timers (Safe Release Dates):**
   - If `versionDate` or `date` is set to a timestamp in the future (even by minutes due to timezone/UTC differences), AltStore replaces the install button with a countdown timer.
   - **Always** set `date` and `versionDate` to the start of the day in UTC (e.g. `YYYY-MM-DDT00:00:00-00:00` or `YYYY-MM-DD`).
7. **Google Drive Direct Download Links:**
   - Standard Google Drive sharing links must be converted to direct download URLs:
     `https://drive.google.com/uc?export=download&id=FILE_ID`
8. **Device-Specific Screenshots:**
   - iPad landscape screenshots (`1024x768`) must be placed under `"screenshots": { "ipad": [ { "imageURL": "...", "width": 1024, "height": 768 } ] }` so AltStore on iPhone does not rotate them sideways.
   - iPhone screenshots must be placed under `"screenshots": { "iphone": [ { "imageURL": "...", "width": 470, "height": 1024 } ] }`.
9. **No Empty String URLs:**
   - Never set optional URL keys to an empty string (`"headerURL": ""`). AltStore's Swift decoder crashes if a URL field contains an empty string instead of being omitted or having a valid URL.
10. **Consistent App Tint Colors:**
    - Match app `tintColor` and news `tintColor` to the app's visual identity:
      - **Restring Helper:** `#E5A817` (Golden Yellow matching the icon tick badge) / News card: `#0F203C` (Dark Navy)
      - **Sales Assistant:** `#007AFF` (Apple System Blue)
      - **SaunaScout:** `#E07326` (Warm Orange)

---

## 4. Current Apps in Source

### App 1: Restring Helper
- **Bundle ID:** `com.stringsports.restringhelper`
- **Developer:** `Max`
- **Current Version:** `3.6` (History: `3.6`, `3.5`, `3.4`, `3.3`, `3.2`, `3.1`, `3.0`, `2.1`, `2.0`, `1.0`)
- **Subtitle:** `Dedicated Stringing Manager for String Sports Glasgow`
- **Tint Color:** `#E5A817`
- **Permissions:** `NSBluetoothAlwaysUsageDescription` (Zebra label printer Bluetooth)
- **Local Xcode Project:** `/Users/maxk/Documents/GitHub/restring-helper-ios`

### App 2: Sales Assistant
- **Bundle ID:** `com.stringsports.salesassistant`
- **Developer:** `Max`
- **Current Version:** `2.0` (History: `2.0`, `1.0`)
- **Subtitle:** `AI-Powered Equipment Recommender for String Sports`
- **Tint Color:** `#007AFF`
- **Permissions:** Standard / None required
- **Local Xcode Project:** `/Users/maxk/Documents/GitHub/ai-sales-assistant-ios`

### App 3: SaunaScout
- **Bundle ID:** `com.maxreuben.SaunaScout`
- **Developer:** `Max`
- **Current Version:** `1.5` (History: `1.5`, `1.4`, `1.3`, `1.2`, `1.1`, `1.0`)
- **Subtitle:** `Discover & Bag Wild Saunas Across Scotland`
- **Tint Color:** `#E07326`
- **Permissions:** `NSLocationWhenInUseUsageDescription` (Map location tracking)

---

## 5. Standard `apps.json` Schema Reference

```json
{
  "name": "Max's iOS Repository",
  "identifier": "com.max.altstore.repo",
  "subtitle": "Private iOS Applications by Max",
  "description": "A private repository hosting personal iOS applications and utilities built by Max...",
  "iconURL": "https://raw.githubusercontent.com/WuXu1/personal-ios-repo/main/icons/repo_icon.jpg",
  "website": "https://github.com/WuXu1/personal-ios-repo",
  "tintColor": "#FF3B30",
  "sourceURL": "https://gist.githubusercontent.com/WuXu1/7bb9258857f12767e3b1b092c6dfb959/raw/apps.json",
  "apps": [
    {
      "name": "App Name",
      "bundleIdentifier": "com.example.app",
      "developerName": "Max",
      "subtitle": "One sentence summary.",
      "version": "1.0",
      "versionDate": "YYYY-MM-DDT00:00:00-00:00",
      "versionDescription": "Category:\n• Feature: Description.",
      "downloadURL": "https://drive.google.com/uc?export=download&id=...",
      "localizedDescription": "Full app description...\n\nKey Features:\n• Feature 1\n• Feature 2",
      "iconURL": "https://raw.githubusercontent.com/WuXu1/personal-ios-repo/main/icons/...",
      "tintColor": "#HEX",
      "size": 10485760,
      "versions": [
        {
          "version": "1.0",
          "date": "YYYY-MM-DDT00:00:00-00:00",
          "localizedDescription": "Category:\n• Feature: Description.",
          "downloadURL": "https://drive.google.com/uc?export=download&id=...",
          "size": 10485760,
          "minOSVersion": "17.0"
        }
      ],
      "screenshots": {
        "ipad": [],
        "iphone": []
      },
      "appPermissions": {
        "entitlements": [],
        "privacy": {}
      }
    }
  ],
  "news": [
    {
      "title": "App Released!",
      "identifier": "app-released",
      "caption": "Short announcement text.",
      "date": "YYYY-MM-DDT00:00:00-00:00",
      "tintColor": "#HEX",
      "imageURL": "https://raw.githubusercontent.com/...",
      "notify": true,
      "appID": "com.example.app"
    }
  ]
}
```
