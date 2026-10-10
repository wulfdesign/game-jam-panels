# 🎮 Game Jams: Your Gateway to Fun, Friends, Indie Game Dev, & XR Realities

> **Event:** GeekGirlCon 2026 • Seattle Convention Center Arch Building  
> **Session:** Sunday, Oct 25, 2026 @ 1:30 PM (45-Minute Panel) • Room 'America'  
> **Moderator:** Larry James (UpLiftVR Studios / Wulf Design Studios)  
> **Panelists:** Tim Cullings (Seattle Indies), Heather Coles (Orbicular), Renee Gittins (Stumbling Cat)  
> **Production Port:** `3026` (Clean Public Slide Deck)  
> **Status:** 🧪 Ready for QA • **Version:** `v0.2.0`  

---

## 🎯 Panel Vision & Core Themes

Game jams are one of the best-kept secrets in creative technology—and one of the most welcoming on-ramps into game and XR development. This panel pulls back the curtain on what game jams actually are, why they work, and how they provide a direct pathway from *"I have an idea"* to shipped, festival-featured experiences:

1. **The 48-Hour Prototyping Crucible:**
   - Scope discipline: Distilling a game to a single atomic verb or core mechanic within the first 4 hours.
   - Managing exhaustion, avoiding MMORPG syndrome, and embracing the "License to Fail".
2. **Inclusive Game Development & Lowering the Barrier:**
   - Why you DON'T need to be a programmer: roles for artists, narrative writers, audio composers, and producers.
   - Finding your jam crew through welcoming communities like Seattle Indies.
3. **The Butterfly Effect & Serendipity:**
   - How weekend jams turn into lifelong friendships, studio co-founders, and surprise career opportunities.
4. **Virtual & Spatial Realities in Jams:**
   - Unreal Engine 5.4 + Meta Quest 3 rapid development pipeline.
   - Non-violent, contemplative XR case studies: *Maiden Flight* (SIFF VR-Zone) and *High Desert Eclipse*.
5. **Live Audience Interactive Social Experiment:**
   - Designing a 48-hour game live on stage in 5 minutes using 3 random audience prompts (Theme, Constraint, Atomic Verb).

---

## 📁 Repository Structure (KremFest-XR Architecture)

```text
projects/game-jams/panels/
├── README.md               # Public presentation overview & lineup
├── .gitignore              # Wards private/ vault and backups from public git
├── index.html              # Clean 24-slide production HTML5 presentation (Port 3026)
├── server.py               # Production multi-threaded server (Port 3026)
├── serve.bat               # Windows launcher
└── private/                # Untracked offline vault (Operator Dev Studio & Docs)
    ├── dev_dashboard/      # Operator Dev Studio & 45m rehearsal stopwatch (Port 3027)
    ├── dev_site/           # Active WIP slide canvas
    ├── docs/               # Ingested 33k Google Doc & 42-slide raw guide
    ├── tasks.md            # Speaker notes & rehearsal checklist
    ├── devlog.md           # Private versioned changelog
    ├── promote_to_production.py # 1-Click push from dev_site to public root
    └── server.py           # Private Dev Server (Port 3027)
```

---

## 🚀 Running the Presentation

```bash
# Launch public presentation deck (Port 3026)
serve.bat

# Or run via Python directly:
python server.py
```
Open `http://localhost:3026/` in any browser. Press `F` for fullscreen, `P` for presenter notes and rehearsal stopwatch, and `←` / `→` or `Space` to navigate.
