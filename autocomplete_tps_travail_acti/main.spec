# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[('libmySQL.dll', '.')],
    datas=[('request_actis_global.sql', '.'), ('request_actis_serre.sql', '.'), ('request_actis_recolte.sql', '.'), ('request_actis_condi.sql', '.'), ('request_time0.sql', '.'), ('request_time1.sql', '.'), ('request_time2.sql', '.'), ('request_time3.sql', '.')],
    hiddenimports=['openpyxl'],
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
