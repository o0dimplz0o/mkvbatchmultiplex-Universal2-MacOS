# MKVBatchMultiplex — macOS Universal2 Build Guide

This fork provides a complete macOS-native Universal2 build of MKVBatchMultiplex.
The resulting `.app` runs on both **Intel** and **Apple Silicon** (M1/M2/M3).

---

## Requirements

Install the following first:

### 1. Python Universal2 (must be the official python.org build)
Download the “universal2“ installer:
https://www.python.org/downloads/macos/

### 2. MKVToolNix (for mkvmerge)
Install from:
https://mkvtoolnix.download/downloads.html#macos

Verify:
```bash
mkvmerge --version

### 3. MediaInfo CLI
Install from:
https://mediaarea.net/en/MediaInfo/Download/Mac_OS

Verify:
```bash
mediainfo --version

## Build Instructions

### 1. Create a clean environment
```bash
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 \
  -m venv ~/mkvbm-universal-env

source ~/mkvbm-universal-env/bin/activate
python -m pip install --upgrade pip setuptools wheel

### 2. Install build dependencies
```bash
pip install pyinstaller PySide6 pymediainfo natsort lxml babel

### 3. Install patched vsutillib (required for MacOS compatibility)
```bash
pip install --no-build-isolation \
  git+https://github.com/o0dimplz0o/vsutillib.git

### 4. Build the Application
From the mkvbatchmultiplex source folder:
```bash
cd /path/to/mkvbatchmultiplex
pyinstaller --clean --noconfirm MKVBatchMultiplex.spec

The compiled .app will appear in:
```bash
dist/MKVBatchMultiplex.app

Move the app to your Applications folder (or other desired destination)

