## Nuke Compatibility (PySide2 / PySide6)

This project supports:
- **Nuke 15 (Qt5 / PySide2)**
- **Nuke 16 (Qt6 / PySide6)**

To keep the codebase compatible across versions, UI code imports Qt via `qt_compat.py`, which prefers **PySide6** when available and falls back to **PySide2** for older Nuke versions. This also handles Qt6 module moves (e.g. `QAction`).
