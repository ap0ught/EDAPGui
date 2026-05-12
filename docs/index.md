---
title: Home
nav_order: 1
description: EDAPGui — A Computer Vision based autopilot for Elite Dangerous.
permalink: /
---

# ED Autopilot (EDAPGui)
{: .no_toc }

A Computer Vision-based autopilot for Elite Dangerous (ED) that automates FSD jumping, supercruise approach, trading, and more — entirely external to the game with no runtime modifications.
{: .fs-5 }

[Get Started](installation){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/ap0ught/EDAPGui){: .btn .fs-5 .mb-4 .mb-md-0 }

---

> See the [Changelog](changelog) for the latest updates.  
> Join [Discord](https://discord.gg/HCgkfSc) for support or to share feedback.

---

![EDAPGui Main Tab]({{ "/assets/images/screen_cap_main.png" | relative_url }})

---

## Main Features
{: .no_toc }

### FSD Route Assist

Select your destination in the Galaxy Map, enable the assist, and EDAPGui will perform all the jumps to get you there AFK. During each jump it performs a detailed system scan (honk) and optionally runs FSS scanning to identify Earth-Like, Water, or Ammonia worlds.

### Supercruise Assist

Keeps your ship aligned to the target in supercruise. When the *"TO DISENGAGE"* prompt appears the assist drops out of SC, requests docking at the targeted station, and hands control to the Advanced Docking Computer.

### Waypoint Assist

Define a route as a JSON waypoints file and the assist jumps through each waypoint automatically. Supports docking at stations, automated trading (buy / sell commodities), Fleet Carrier transfers, and System Colonisation Ship deliveries.  
→ [Waypoints reference](waypoint) · [Waypoint Editor](waypoint-editor)

### Robigo Mines Assist

Automates the Robigo Mines → Sirius Atmospherics passenger-mission loop: mission completion, cabin filling, route execution, and docking.  
→ [Robigo Mines guide](robigo)

### AFK Combat Escape Assist

Monitors shield health while in a Rez Zone. When shields drop it boosts away, enters supercruise briefly, then returns and deploys a replacement fighter.

### Single Waypoint Assist

Paste a system name from Inara / Spansh and the assist plots a route and jumps there. Available on the Debug tab.

---

## Additional Features

| Feature | Description |
|---------|-------------|
| **Voice** | Text-to-speech announcements of autopilot actions. |
| **ELW Scanner** | Passive FSS scanning for Earth-Like, Water, and Ammonia worlds during FSD jumps. Results logged to `elw.txt`. |
| **TCE Integration** | Load current TCE (Trade Computer Extension) destination as a Single Waypoint target. |
| **CV View** | Debug overlay showing template matching in real time. |
| **Calibration** | One-time screen-region and template-scale calibration for your display and Field of View. |

---

## Screenshots

| Main Tab | Settings Tab | Debug Tab |
|----------|-------------|-----------|
| ![Main]({{ "/assets/images/screen_cap_main.png" | relative_url }}) | ![Settings]({{ "/assets/images/screen_cap_settings.png" | relative_url }}) | ![Debug]({{ "/assets/images/screen_cap_debug.png" | relative_url }}) |

---

## How It Works

EDAPGui uses **Computer Vision** (screen capture + template matching) and Python's `win32` APIs to issue keystrokes to Elite Dangerous. It does not modify the game binary or memory — it is an external tool, similar to a human CMDR watching the screen and pressing keys.

{: .note }
This project is based on [EDAutopilot by skai2](https://github.com/skai2/EDAutopilot). Many routines were adapted, refactored into classes, and extended with new features.

{: .note }
This repository is also provided as an educational example of computer vision, file-based data integration, voice feedback, Win32 Python integration, threading, and Python class design.

---

## Limitations

- **Windows only** — `win32` APIs are used for screen capture and keyboard injection.
- **Default HUD colours** — Changed HUD colours break template matching.
- **Borderless window** required — Windowed mode cannot be screen-captured correctly.
- **ED must retain focus** while a assist is active — keyboard events go to the focused window.
- **Advanced Docking Computer** required for autodock.
- **Navigation panel** must be on the Navigation tab when SC Assist is active.
- Resolution templates were created at **3440 × 1440**. Other resolutions need calibration. See [Calibration](calibration).
- Economical routing may cause issues — use Fastest routing for best results.

---

## Quick Links

| | |
|--|--|
| 📦 [Installation & Running](installation) | First install, running the app |
| 🎮 [Getting Started](installation#getting-started) | First-run checklist |
| ⌨️ [Keybindings & Configuration](configuration) | Required keybindings, hotkeys, advanced settings |
| 🔭 [Calibration](calibration) | Screen region and template calibration |
| 🎯 [Roll, Pitch, Yaw Tuning](roll-pitch-yaw) | Ship manoeuvring rates |
| 🗺️ [Waypoints](waypoint) | Waypoint file format and reference |
| ✏️ [Waypoint Editor](waypoint-editor) | Using the built-in editor |
| 🪐 [Robigo Mines](robigo) | Passenger mission loop |
| 📋 [Changelog](changelog) | Version history |
