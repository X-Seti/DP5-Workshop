# DP5 Workshop

Deluxe Paint 5 style bitmap editor, split from IMG Factory 1.6.

## Windows
Download `DP5_Workshop_Windows.zip` from the `windows-build` release, unzip, run `DP5_Workshop/DP5_Workshop.exe`.
Settings save in `settings/` beside the exe.

## Run from source
```
pip install PyQt6 numpy Pillow
python3 launch_dp5_workshop.py
```

## Features
- Paint tools, brushes, fills, shapes, text, selection, zoom lens.
- Bitmaps, Brush & Colors, Image Palette and User Palette docks.
- Import/export PNG, IFF, GIF, TGA, TIFF, ZX Spectrum, C64 Koala, Art Studio, NXI.
- Retro palettes (Amiga, C64, ZX, Atari), dither, quantise.
- Ribbon Manager, presets, themes.

## Code layout
| File | Job |
|------|-----|
| apps/components/DP5_Workshop/dp5_workshop.py | Main window, canvas, tools |
| apps/components/DP5_Workshop/depends/ | Dock widgets |
| apps/components/DP5_Workshop/svg_icon_browser.py | SVG icon browser |
| apps/methods/ | Shared IMG Factory code |

X-Seti - IMG Factory 1.6
