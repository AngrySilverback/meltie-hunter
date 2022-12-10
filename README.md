# Meltie Hunter

## Overview
A basic Reddit bot that assists in hunting down r/gme_meltdown shills that post
 in Superstonk. It streams r/Superstonk posts in real-time, and scans each
 user's comment history, dumping any r/GME_Meltdown posts to the terminal.

## Getting Started

### Install using pip

**Prerequisites:**
- python >= 3.7
- pip

**Installation:**

```sh
pip install .
```

### Usage

1. Copy `praw-template.ini` to `praw.ini`, and configure the parameters.
2. From the same directory as `praw.ini`, run `meltie-hunter` via CLI.

## License

GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
