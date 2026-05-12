---
title: Installation & Running
nav_order: 2
description: How to install and run EDAPGui on Windows.
---

# Installation & Running
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Requirements

- **Windows** (Win32 APIs are required — Linux is not supported)
- **Python 3.11** (recommended; 3.9 or 3.10 may also work)
- **git** (for the Advanced install method)
- **Elite Dangerous** running in **Borderless** window mode

{: .note }
> To avoid a *'py is not recognised'* error later, check **"Add Python 3.xx to PATH"** in the Python installer.

- [Python 3.11 installer download](https://www.python.org/downloads/release/python-3110/) — scroll to the bottom and pick the "Recommended" installer.

---

## Simple Install (recommended for most users)

Use this method if you just want to download and run EDAPGui without touching the source code.

1. Click the green **`<> Code`** button on the [GitHub page](https://github.com/ap0ught/EDAPGui) and choose **Download ZIP**.
2. Extract the ZIP to a folder of your choice.
3. Locate **`start_ed_ap.bat`** in that folder.
4. Double-click **`start_ed_ap.bat`** — it installs all required packages and completes setup automatically.
5. Double-click **`start_ed_ap.bat`** again to launch EDAPGui.

---

## Advanced Install (for developers / source exploration)

Use this method if you want to explore or modify the source code.

1. Clone the repository:
   ```sh
   git clone https://github.com/ap0ught/EDAPGui
   cd EDAPGui
   ```

2. Install Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Or run `install_requirements.bat` directly.

3. Launch the app:
   ```sh
   python EDAPGui.py
   # or, if you have both Python 2 and 3 installed:
   python3 EDAPGui.py
   ```

{: .note }
If `pip install` fails, try `python -m pip install -r requirements.txt`.

{: .note }
If you see `AttributeError: '_thread._local' object has no attribute 'srcdc'`, there is an `mss` version incompatibility.  
Try: `pip install mss==8.0.3`

---

## Running

With Elite Dangerous open, start ED_AP by:

- Double-clicking **`start_ed_ap.bat`** in Windows Explorer (preferred).
- Typing `python EDAPGui.py` in a terminal.
- Running `EDAPGui.py` directly from a Python-supporting IDE.

The EDAPGui window will open and the log area may show warnings about missing keybindings — see [Keybindings & Configuration](configuration) to resolve these.

---

## Getting Started

Complete these steps the first time you run EDAPGui:

1. **Calibrate your screen** — See [Calibration](calibration) for a step-by-step guide. Correct calibration resolves most issues.

2. **Check keybindings** — Open Elite Dangerous options and confirm all [required keybindings](configuration#required-keybindings) are assigned.  
   Pay particular attention that **Ins**, **Home**, **End**, and **Pg Up** are not already mapped in ED (EDAPGui uses these as hotkeys by default).  
   The `autopilot.log` file lists any missing bindings.

3. **Load your ship configuration** — Select the correct ship file to configure the Pitch, Roll, and Yaw rates. If needed, tune these values as described in [Roll, Pitch, Yaw Tuning](roll-pitch-yaw).

4. **In-system test** (SC Assist):
   - In ED, use the Left Panel to select a local target.
   - Enable **SC Assist** in EDAPGui, or press the **Ins** key.
   - The ship will undock (if docked), jump to supercruise, manoeuvre to the target, and attempt docking.
   - Any flight issues → check [ship tuning](roll-pitch-yaw).

5. **Out-of-system test** (FSD Assist):
   - In ED, use the Galaxy Map to select a target system.
   - Enable **FSD Assist** in EDAPGui, or press the **Home** key.
   - The ship will undock (if docked), jump to supercruise, manoeuvre to the target, perform an FSD jump, fuel-scoop as necessary, and either stop or continue to the next destination.
   - Any flight issues → check [ship tuning](roll-pitch-yaw).

---

## Updating

To update to the latest version (Advanced install):

```sh
cd EDAPGui
git pull
pip install -r requirements.txt
```

For Simple install, re-download the ZIP and replace your existing folder (keep your `configs/AP.json` and waypoint files to preserve settings).
