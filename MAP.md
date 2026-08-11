# MAP — ARGUS-OS3

```
ARGUS-OS3/
├── README.md               # Homepage
├── CONCEPT.md              # Concept — ablation + micromanipulation
├── PARAMETERS.md           # Budget, laser specs, ablation protocol
├── TODO.md                 # Tasks
├── STATE.md                # Current status
├── MEMORY.md               # Decision history
├── _pi.md                  # Rules for pi
│
├── hardware/               # Laser integration, micromanipulator mount
│   └── README.md
│
├── software/               # AI agent, laser control, multi-camera NV
│   └── README.md
│
├── firmware/               # Laser shutter, UV-C, micromanipulator driver
│   └── README.md
│
├── docs/                   # Laser safety, ablation protocols
├── docs/ENTROPY_RESET_PROTOCOL.md  # v6.2 core protocol (12 hallmarks, 47 refs)
├── docs/ENTROPY_RESET_PROGRAM_COMPLETE.md  # consolidated package v6.2
├── docs/APPENDIX_SEARCH_PROTOCOL.md  # novelty search (PubMed+EuropePMC+Crossref+OpenAlex)
├── docs/ENTROPY_RESET_13_PUZZLES.png  # 13-puzzle visual
├── docs/RED_THREAD.md  # one-page mechanism
├── docs/GAKELY_TSOMAIA_PROTOTYPE_CHAIN_EN.md  # prototype chain (EN)
│
├── letters/                # EIC Pathfinder WP2 correspondence
│
├── grants/                 # EIC Pathfinder WP2 grant
│
└── refs/                   # Ablation literature
```

## Relationship

```
ARGUS-LP_OS (v1.0)          ARGUS-OS2 (v2.0)            ARGUS-OS3 (v3.0)
    │                            │                           │
    ├─ Observation              ├─ Causality (genetic)      ├─ Causality (physical)
    ├─ No laser                 ├─ No laser                 ├─ Femtosecond laser
    ├─ No micromanipulator      ├─ No micromanipulator      ├─ Micromanipulator
    ├─ Camera HQ                ├─ Camera HQ (shared)       ├─ sCMOS
    ├─ Jetson Orin NX           ├─ Jetson (shared)          ├─ Mac M4 Pro
    ├─ 1× NV camera             ├─ 1× NV (shared)           ├─ 2× NV cameras
    ├─ RPE1                     ├─ RPE1 Odf2 KO             ├─ hTERT-NPCs
    └─ $24,053                  └─ +$3,000                  └─ $40,600
```

## Links
- **ARGUS-LP_OS:** `~/Desktop/Marketing/ARGUS-LP_OS/`
- **ARGUS-OS2:** `~/Desktop/Marketing/ARGUS-OS2/`
- **EIC Pathfinder:** `~/Desktop/Marketing/MCARA_EIC_Pathfinder/wp2_argus/`
- **OpenFlexure upstream:** `https://github.com/openflexure/openflexure-microscope`
- **FOSH micromanipulator:** `https://github.com/FOSH-following-demand/Micro_Manipulator`
