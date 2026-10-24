# SpatialLoom XR — Hands-First WebXR Spatial AI & Acoustic Fiber Workbench (`@iwsdk/core` + `IWER`)

[![Live WebXR App](https://img.shields.io/badge/Live_WebXR-GitHub_Pages-0284c7?style=for-the-badge)](https://kevin9327.github.io/MetaXRThreadSymphony/)
[![IWSDK](https://img.shields.io/badge/Meta_IWSDK-v1.0.1_super--three-7c3aed?style=for-the-badge)](./package.json)
[![IWER](https://img.shields.io/badge/IWER_Emulator-metaQuest3_Hands-10b981?style=for-the-badge)](./iwsdk.config.json)
[![60 FPS](https://img.shields.io/badge/Performance-60_FPS_Zero--Alloc_ECS-f59e0b?style=for-the-badge)](./backend/spatial_loom_engine.py)

> Built for the **Meta VR Start Developer Competition 2026 ($1,000,000 USD Cash Pool)** — a 100% **Hands-First WebXR** tabletop spatial AI systems engineering and physical-modeled acoustic fiber loom built with **`@iwsdk/core@1.0.1`**, **`@pmndrs/uikit-horizon`**, and **`iwer@2.5.0` (`metaQuest3`)**.

---

## Target Track & 5 Special Awards Architecture ($225,000 Combined Eligibility)

| Category / Special Award | Prize Pool | Implemented ECS System & Verification |
| :--- | :--- | :--- |
| **Main Track (`Productivity / Gaming — New Division`)** | **$70,000 – $100,000** | Tabletop 3D spatial node loom within a `0.45m` seated envelope where bare-hand pinch-pull gestures weave resonant optical threads across 6 multi-frequency pegs. |
| **1. `Best Agentic Interaction`** | **$25,000 Cash** | **`AgentCopilotSystem`**: Voice (`Web Speech API`) & 1-poke Ledge trigger that analyzes current 3D peg placement, procedurally weaves an optimal 7-thread resilient topology via `entity.getVectorView().set()`, and plays a 6-voice harmonic chord. |
| **2. `Best First Five Minutes`** | **$25,000 Cash** | **`OnboardingSystem`**: Zero wall-of-text tutorials. A translucent glowing 3D thumb+index **Ghost Hand** (`ignorePointer: pointerEvents = 'none'`) demonstrates pinching Peg A to Peg B and auto-dismisses on the user's first link (`< 45 seconds` to first harmonic chord). |
| **3. `Best Accessibility Forward Experience`** | **$25,000 Cash** | **Airplane Seat Test (`<= 2ft / 0.60m` reach)** via `z = -0.42m` Front Ledge + elevation toggle (`±15cm`), **`0.5x Slow-Motion`** simulation toggle, **4-way input parity** (Bare-hand pinch, Direct poke, Eye `gazeTracking: true` + pinch, Desktop mouse), and **Colorblind Dual Encoding** (Sphere `220Hz` / Hex Prism `330Hz` / Octahedron `440Hz`). |
| **4. `Best Reason to Come Back`** | **$25,000 Cash** | **`DailyChallengeSystem`**: Deterministic `YYYY-MM-DD` daily spool-budget puzzle + `localStorage` **Brass Streak Plaque (`Daily — Streak N`)** + **Melody Book** replay. |
| **5. `Boldest Original Concept`** | **$25,000 Cash** | Physical-modeled acoustic fiber workbench where system architecture routing is simultaneously a playable Just Intonation spatial string instrument. |

---

## Verification

```bash
python -m pytest tests/test_spatial_loom.py -v
```
