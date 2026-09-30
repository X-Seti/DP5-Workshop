# -*- mode: python ; coding: utf-8 -*-
#this belongs in root /dp5_workshop.spec - Version: 1
# X-Seti - September30 2026 - DP5 Workshop - PyInstaller build spec (Windows)

"""
PyInstaller spec for the standalone DP5 Workshop Windows build.
Build: pyinstaller dp5_workshop.spec  ->  dist/DP5_Workshop/DP5_Workshop.exe
"""

##Methods list -
# _app_data
# _make_icon

import os

ROOT = os.path.abspath(SPECPATH)


def _app_data(): #vers 1
    """Every non-Python file under apps/, kept at the same relative path."""
    out = []
    for base, dirs, files in os.walk(os.path.join(ROOT, 'apps')):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for name in files:
            if name.endswith(('.py', '.pyc', '.log')):
                continue
            src = os.path.join(base, name)
            out.append((src, os.path.relpath(base, ROOT)))
    return out


def _make_icon(): #vers 1
    """Render the DP5 Workshop SVG app icon to build/dp5_workshop.ico."""
    import sys
    os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
    sys.path.insert(0, ROOT)
    from PyQt6.QtWidgets import QApplication
    app = QApplication.instance() or QApplication([])
    from apps.methods.imgfactory_svg_icons import get_dp5_workshop_icon
    out = os.path.join(ROOT, 'build', 'dp5_workshop.ico')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if not get_dp5_workshop_icon(256).pixmap(256, 256).toImage().save(out, 'ICO'):
        raise RuntimeError('ICO write failed')
    return out


a = Analysis(
    ['launch_dp5_workshop.py'],
    pathex=[ROOT],
    binaries=[],
    datas=_app_data() + [(os.path.join(ROOT, 'appfactory.settings.json'), '.')],
    hiddenimports=['PyQt6.QtSvg', 'PIL.Image', 'numpy',
                   'apps.components.DP5_Workshop.dp5_workshop',
                   'apps.components.DP5_Workshop.svg_icon_browser',
                   'apps.components.DP5_Workshop.depends.bitmaps_widget',
                   'apps.components.DP5_Workshop.depends.brushcolors_widget',
                   'apps.components.DP5_Workshop.depends.imagepalette_widget',
                   'apps.components.DP5_Workshop.depends.userpalette_widget'],
    excludes=['tkinter'],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name='DP5_Workshop',
    console=False,
    icon=_make_icon(),
    upx=False,
)
coll = COLLECT(exe, a.binaries, a.datas, upx=False, name='DP5_Workshop')
