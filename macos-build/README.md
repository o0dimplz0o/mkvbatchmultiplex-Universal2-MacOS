# macOS Universal2 Build (Intel + Apple Silicon)

This fork adds native macOS support for MKVBatchMultiplex.

## Requirements

- macOS (Ventura or later recommended)
- Python 3.12 universal2 from python.org
- MKVToolNix (mkvmerge on PATH)
- MediaInfo CLI (mediainfo on PATH)

## Build steps

```bash
# 1. Create and activate a venv
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 \
  -m venv ~/mkvbm-universal-env

source ~/mkvbm-universal-env/bin/activate
python -m pip install --upgrade pip setuptools wheel

# 2. Install dependencies
pip install PySide6 pymediainfo natsort lxml babel pyinstaller

# 3. Install patched vsutillib from this fork
pip install --no-build-isolation \
  git+https://github.com/o0dimplz0o/vsutillib.git

# 4. Build the app
cd /path/to/your/mkvbatchmultiplex/clone
pyinstaller --clean --noconfirm MKVBatchMultiplex.spec

# The app will be in dist/MKVBatchMultiplex.app.
