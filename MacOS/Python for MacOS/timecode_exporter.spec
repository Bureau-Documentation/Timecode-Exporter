# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['timecode_exporter.py'],
    pathex=[],
    binaries=[],
    datas=[('timecode_exporter.icns', '.'), ('/opt/miniconda3/envs/timecode_exporter/lib/python3.9/site-packages/tkinterdnd2/tkdnd/osx-arm64', 'TkinterDnD2')],
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
    a.binaries,
    a.datas,
    [],
    name='timecode_exporter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['timecode_exporter.icns'],
)
app = BUNDLE(
    exe,
    name='timecode_exporter.app',
    icon='timecode_exporter.icns',
    bundle_identifier=None,
)
