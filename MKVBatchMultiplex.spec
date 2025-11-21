# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['runApp.py'],
    pathex=['/Users/Michele-Phan/mkvbm-src/vsutillib'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MKVBatchMultiplex',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch='universal2',
    codesign_identity=None,
    entitlements_file=None,
    icon='/Users/Michele-Phan/mkvbm-src/mkvbatchmultiplex/mkvbm.icns',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MKVBatchMultiplex',
)
app = BUNDLE(
    coll,
    name='MKVBatchMultiplex.app',
    icon='/Users/Michele-Phan/mkvbm-src/mkvbatchmultiplex/mkvbm.icns',
    bundle_identifier=None,
)
