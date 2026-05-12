---
title: Keybindings & Configuration
nav_order: 3
description: Required Elite Dangerous keybindings, EDAPGui hotkeys, and advanced configuration settings.
---

# Keybindings & Configuration
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Required Keybindings

The bindings below must be assigned in Elite Dangerous (**Options → Controls**) for EDAPGui to function correctly. After changing keybindings, restart EDAPGui so the new assignments are read.

{: .important }
> The `autopilot.log` file lists any missing bindings detected at startup.

| Binding | Name | Location |
|---------|------|----------|
| `UI_Up` | UI PANEL UP | GENERAL CONTROLS › INTERFACE MODE |
| `UI_Down` | UI PANEL DOWN | GENERAL CONTROLS › INTERFACE MODE |
| `UI_Left` | UI PANEL LEFT | GENERAL CONTROLS › INTERFACE MODE |
| `UI_Right` | UI PANEL RIGHT | GENERAL CONTROLS › INTERFACE MODE |
| `UI_Select` | UI PANEL SELECT | GENERAL CONTROLS › INTERFACE MODE |
| `UI_Back` | UI BACK | GENERAL CONTROLS › INTERFACE MODE |
| `CycleNextPanel` | NEXT PANEL TAB | GENERAL CONTROLS › INTERFACE MODE |
| `MouseReset` | RESET MOUSE | SHIP CONTROLS › MOUSE CONTROLS |
| `YawLeftButton` | YAW LEFT | SHIP CONTROLS › FLIGHT ROTATION |
| `YawRightButton` | YAW RIGHT | SHIP CONTROLS › FLIGHT ROTATION |
| `RollLeftButton` | ROLL LEFT | SHIP CONTROLS › FLIGHT ROTATION |
| `RollRightButton` | ROLL RIGHT | SHIP CONTROLS › FLIGHT ROTATION |
| `PitchUpButton` | PITCH UP | SHIP CONTROLS › FLIGHT ROTATION |
| `PitchDownButton` | PITCH DOWN | SHIP CONTROLS › FLIGHT ROTATION |
| `ThrustUpButton` | THRUST UP | SHIP CONTROLS › FLIGHT THRUST |
| `SetSpeedZero` | SET SPEED TO 0% | SHIP CONTROLS › FLIGHT THROTTLE |
| `SetSpeed50` | SET SPEED TO 50% | SHIP CONTROLS › FLIGHT THROTTLE |
| `SetSpeed100` | SET SPEED TO 100% | SHIP CONTROLS › FLIGHT THROTTLE |
| `UseBoostJuice` | ENGINE BOOST | SHIP CONTROLS › FLIGHT MISCELLANEOUS |
| `HyperSuperCombination` | TOGGLE FRAME SHIFT DRIVE | SHIP CONTROLS › FLIGHT MISCELLANEOUS |
| `Supercruise` | SUPERCRUISE | SHIP CONTROLS › FLIGHT MISCELLANEOUS |
| `SelectTarget` | SELECT TARGET AHEAD | SHIP CONTROLS › TARGETING |
| `PrimaryFire` | PRIMARY FIRE | SHIP CONTROLS › WEAPONS |
| `SecondaryFire` | SECONDARY FIRE | SHIP CONTROLS › WEAPONS |
| `DeployHardpointToggle` | DEPLOY HARDPOINTS | SHIP CONTROLS › WEAPONS |
| `DeployHeatSink` | DEPLOY HEATSINK | SHIP CONTROLS › COOLING |
| `IncreaseEnginesPower` | DIVERT POWER TO ENGINES | SHIP CONTROLS › MISCELLANEOUS |
| `IncreaseWeaponsPower` | DIVERT POWER TO WEAPONS | SHIP CONTROLS › MISCELLANEOUS |
| `IncreaseSystemsPower` | DIVERT POWER TO SYSTEMS | SHIP CONTROLS › MISCELLANEOUS |
| `LandingGearToggle` | LANDING GEAR | SHIP CONTROLS › MISCELLANEOUS |
| `UIFocus` | UI FOCUS | SHIP CONTROLS › MODE SWITCHES |
| `GalaxyMapOpen` | OPEN GALAXY MAP | SHIP CONTROLS › MODE SWITCHES |
| `SystemMapOpen` | OPEN SYSTEM MAP | SHIP CONTROLS › MODE SWITCHES |
| `ExplorationFSSEnter` | ENTER FSS MODE | SHIP CONTROLS › MODE SWITCHES |
| `HeadLookReset` | RESET HEADLOOK | SHIP CONTROLS › HEADLOOK MODE |
| `ExplorationFSSQuit` | LEAVE FSS | SHIP CONTROLS › FULL SPECTRUM SYSTEM SCANNER |

---

## Hotkeys

The default EDAPGui hotkeys are:

| Key | Action |
|-----|--------|
| **Home** | Start FSD Route Assist |
| **Ins** | Start Supercruise Assist |
| **Pg Up** | Start Robigo Assist |
| **End** | Stop all running assists |

{: .warning }
> Make sure these keys are **not** mapped to any ED function. Any key that is mapped in ED will be triggered when EDAPGui presses it.

Hotkeys are configurable in `configs/AP.json`. For valid key names see the [pynput keyboard documentation](https://pythonhosted.org/pynput/keyboard.html).

---

## Autopilot Options

### FSD Route Assist
Executes the plotted Galaxy Map route jump by jump. During each jump:
- Performs a detailed system scan (honk).
- Optionally runs FSS scanning for Earth-Like, Water, or Ammonia worlds.
- Fuel-scoops at scoopable stars; waits for full refuel if fuel drops below the threshold (default 10%). Aborts refuel wait after 35 seconds and continues.
- Terminates if fuel drops below the critical threshold (configurable, default 10%).

### Supercruise Assist
Keeps the ship aligned to the target. When *"TO DISENGAGE"* appears:
- Drops out of supercruise.
- Requests docking at the targeted station.
- Sets throttle to zero for the Docking Computer to take over.
- Auto-refuels after docking.

Additional behaviours:
- **Interdiction response** — attempts evasion when interdicted.
- **Planet occlusion** — navigates around the planet when the station is occluded.

### Waypoint Assist
Reads a JSON waypoint file and processes each entry:
- Plots the system in the Galaxy Map and executes FSD Route Assist.
- If a station is defined, transitions to SC Assist and docks.
- Executes any defined trades after docking.
- Supports `"REPEAT"` as a final waypoint to loop continuously.

### Robigo Mines Assist
Performs the Robigo Mines → Sirius Atmospherics passenger-mission loop. See [Robigo Mines](robigo).

### AFK Combat Escape Assist
Monitors shield health in a Rez Zone. When shields drop:
1. Boosts away.
2. Engages supercruise for ~10 seconds.
3. Drops back, redistributes pips, deploys fighter.
4. Terminates. Deploys a replacement fighter if the current fighter is destroyed.

### ELW Scanner
During FSD jumps, passively scans FSS signals for Earth-Like, Water, and Ammonia worlds. Detections are announced by voice and logged to `elw.txt`.

---

## Advanced Configuration (AP.json)

The following settings are in `configs/AP.json` and are **not** exposed in the GUI. Open the file in any text editor to change them.

```json
{
  "Robigo_Single_Loop": false,
  "EnableRandomness": false,
  "OverlayTextFont": "Eurostyle",
  "OverlayGraphicEnable": false,
  "DiscordWebhook": false,
  "DiscordWebhookURL": "",
  "DiscordUserID": "",
  "VoiceID": 1,
  "Language": "en",

  "DisengageUseMatch": false,

  "Debug_ShowCompassOverlay": false,
  "Debug_ShowTargetOverlay": false,

  "GalMap_SystemSelectDelay": 2.0,

  "target_align_outer_lim": 1.0,
  "target_align_inner_lim": 0.5,

  "FCDepartureAngle": 90.0,
  "FCDepartureTime": 30.0,
  "OCDepartureAngle": 90.0
}
```

| Key | Default | Description |
|-----|---------|-------------|
| `Robigo_Single_Loop` | `false` | When `true`, execute only one Robigo loop and terminate upon docking without mission processing. |
| `EnableRandomness` | `false` | Add random 0–3 second pauses at key points to reduce detectability. |
| `OverlayTextFont` | `"Eurostyle"` | Font used for the overlay text. |
| `OverlayGraphicEnable` | `false` | Enable graphic overlay elements (not yet fully implemented). |
| `DiscordWebhook` | `false` | Discord webhook integration (not yet implemented). |
| `DiscordWebhookURL` | `""` | Discord webhook URL. |
| `DiscordUserID` | `""` | Discord user ID for mentions. |
| `VoiceID` | `1` | Index of the TTS voice to use (Windows voices 0–2). |
| `Language` | `"en"` | OCR language code (e.g. `"en"`, `"fr"`, `"de"`). |
| `DisengageUseMatch` | `false` | Use legacy image matching instead of OCR for disengage detection. |
| `Debug_ShowCompassOverlay` | `false` | Draw debug overlay on compass region. |
| `Debug_ShowTargetOverlay` | `false` | Draw debug overlay on target region. |
| `GalMap_SystemSelectDelay` | `2.0` | Seconds to wait after entering a system name in the Galaxy Map. |
| `target_align_outer_lim` | `1.0` | Outer deadband for target alignment. |
| `target_align_inner_lim` | `0.5` | Inner deadband for target alignment. |
| `FCDepartureAngle` | `90.0` | Degrees to pitch up when departing a Fleet Carrier. |
| `FCDepartureTime` | `30.0` | Seconds to fly away from a Fleet Carrier after enabling SC. |
| `OCDepartureAngle` | `90.0` | Degrees to pitch up when departing an Orbital Construction Site. |
