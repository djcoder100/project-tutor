# gamedev

## 🎮 Python Arcade Collection – Pygame Games (with uv)

A mini collection of **arcade-style games** made in **Python** using **Pygame**, managed in a modern **`uv` environment**.

Games included:

1. 🧱 **Dodge the Falling Blocks**
2. 🌆 **Dodge Deluxe** (with music + background)
3. 👾 **Space Invaders**

Each game demonstrates different aspects of **game programming**, such as input handling, collision detection, scoring, and asset integration.

---

## 🧰 Setup Guide

### 1️⃣ Install `uv`

If you don’t have it already:

```bash
pip install uv
```

or check:
👉 [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

### 2️⃣ Create a Project Folder

```bash
mkdir python_arcade
cd python_arcade
```

---

### 3️⃣ Initialize a uv Environment

This sets up your virtual environment and project config.

```bash
uv init
```

You’ll see:

```
python_arcade/
├── pyproject.toml
├── uv.lock
└── .venv/
```

---

### 4️⃣ Add Dependencies

Install Pygame into the project:

```bash
uv add pygame
```

Your `pyproject.toml` will now include:

```toml
[project]
name = "python-arcade"
version = "0.1.0"
description = "Collection of simple Pygame-based arcade games"
requires-python = ">=3.10"

[project.dependencies]
pygame = "*"
```

---

### 5️⃣ Add Game Files

Place the Python scripts in the folder:

```
python_arcade/
├── dodge_game.py
├── dodge_game_deluxe.py
├── space_invaders.py
├── background.jpg         # optional
├── music.mp3              # optional
├── hit.wav                # optional
├── pyproject.toml
└── uv.lock
```

---

## 🕹️ Games Overview

---

### 🧱 **1. Dodge the Falling Blocks**

**Description:**
Control a blue square to dodge red blocks falling from the top of the screen.
The longer you survive, the higher your score.

**Controls:**

| Key   | Action             |
| ----- | ------------------ |
| ← / → | Move left or right |
| ESC   | Quit game          |

**Run:**

```bash
uv run python dodge_game.py
```

**Features:**

* Smooth movement and collision detection
* Increasing score over time
* Simple and fast-paced gameplay

---

### 🌆 **2. Dodge the Falling Blocks – Deluxe Edition**

**Description:**
An enhanced version with **background image**, **looping music**, and a **restart screen**.

**Extra Features:**

* 🎵 Background music (MP3 loop)
* 🖼️ Background image (JPG/PNG)
* 💥 Collision sound effects
* 🔁 Restart after Game Over
* ⚡ Gradually increasing difficulty

**Optional Assets (same folder):**

```
background.jpg
music.mp3
hit.wav
```

**Run:**

```bash
uv run python dodge_game_deluxe.py
```

---

### 👾 **3. Space Invaders**

**Description:**
Classic-style **Space Invaders** clone. Move your spaceship, shoot enemies, and rack up points before they reach Earth.

**Controls:**

| Key      | Action             |
| -------- | ------------------ |
| ← / →    | Move left or right |
| Spacebar | Shoot bullet       |
| ESC      | Quit game          |

**Run:**

```bash
uv run python space_invaders.py
```

**Features:**

* Multiple enemies that move and descend
* Player shooting system
* Collision-based scoring
* Simple game over condition
* 60 FPS smooth performance

---

## 🪄 Optional Improvements

Add more polish or features:

* 🌌 Scrolling backgrounds or parallax stars
* 🔊 Sound effects and explosion animations
* 🧱 Multiple levels and boss enemies
* 💾 High score saving system
* 🎨 Sprite-based art assets

---

## 🧾 Example Directory Tree

```
python_arcade/
├── dodge_game.py
├── dodge_game_deluxe.py
├── space_invaders.py
├── background.jpg
├── music.mp3
├── hit.wav
├── pyproject.toml
└── uv.lock
```

---

## ⚙️ Run Any Game

Use the same environment for all:

```bash
uv run python <game_name>.py
```

Example:

```bash
uv run python space_invaders.py
```

---

## 🧠 Credits

* Built with ❤️ using **Python 3** and **Pygame**
* Managed via **uv** for modern, reproducible environments
* Inspired by retro classics like *Space Invaders* and *Falling Blocks*
