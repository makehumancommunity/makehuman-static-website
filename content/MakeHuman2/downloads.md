---
title: "MakeHuman 2 Downloads"
draft: false
weight: 6
description: "Download MakeHuman 2 from Steam (Windows) or build it from source on Windows, Linux and macOS. Includes system requirements and asset pack information."
---

There are two ways to get MakeHuman 2: a ready-to-run Windows build on Steam, or the cross-platform source code
from GitHub. Both are free and open source (AGPL code, CC0 assets).

> **Note:** MakeHuman 2 is currently in alpha. If you need a stable tool you can also keep using
> [MakeHuman 1]({{% relref "../MakeHuman" %}}) alongside it.

## Steam (Windows)

The easiest way to install on Windows is via Steam:

- [MakeHuman 2 on Steam](https://store.steampowered.com/app/4676360/Makehuman_2/)

It is listed as a free Early Access title — just press the **Free** button to install. Steam will keep the build
up to date automatically.

### Minimum system requirements

- **OS:** Windows 10 64-bit
- **Processor:** Intel Core i5-4570 / AMD Ryzen 5 1500X
- **Memory:** 8 GB RAM
- **Graphics:** NVIDIA GeForce GTX 770 / Intel HD 530 / AMD Radeon R9 280X
- **Storage:** 5 GB available space

Windows 11, 16 GB RAM and a more modern GPU are recommended for the best experience.

## Source code (Windows, Linux and macOS)

On Linux and macOS, and for anyone who wants to follow the latest development, run MakeHuman 2 from source:

```bash
# Clone the repository
git clone https://github.com/makehumancommunity/makehuman2.git
cd makehuman2

# Linux/macOS: create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python3 makehuman.py
```

On Windows you can use the same steps after installing Python 3 from [python.org](https://www.python.org/).

A few notes:

- **Linux:** running inside a virtual environment is recommended. If you run into rendering issues on Mesa
  drivers, start with `python3 makehuman.py --noskybox`.
- **macOS:** rendering uses a GLSL 1.2 compatibility path, so the visual output may differ slightly from
  Windows and Linux.

## Asset packs

MakeHuman 2 shares its asset packs with [MPFB2]({{% relref "../MPFB" %}}) — the same base mesh and system
assets are used. The asset packs are downloaded from within the application using the built-in download manager,
so you do not need to fetch them manually before the first run.
