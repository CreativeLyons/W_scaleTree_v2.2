"""
qt_compat.py

Small compatibility layer for Nuke versions that may ship either PySide2 (Qt5)
or PySide6 (Qt6). Import from here instead of importing PySide directly.

Design goals:
- Keep diffs minimal in the rest of the codebase.
- Prefer PySide6 when available (Nuke 16+).
"""

from __future__ import annotations

from typing import Any, Optional, Tuple


def _import_qt() -> Tuple[Any, Any, Any, Optional[Any], bool]:
    try:
        from PySide6 import QtCore, QtGui, QtWidgets  # type: ignore
        try:
            import shiboken6 as shiboken  # type: ignore
        except Exception:
            shiboken = None
        return QtCore, QtGui, QtWidgets, shiboken, True
    except Exception:
        from PySide2 import QtCore, QtGui, QtWidgets  # type: ignore
        try:
            import shiboken2 as shiboken  # type: ignore
        except Exception:
            shiboken = None
        return QtCore, QtGui, QtWidgets, shiboken, False


QtCore, QtGui, QtWidgets, shiboken, IS_QT6 = _import_qt()

# QAction moved in PySide6: PySide2.QtWidgets.QAction -> PySide6.QtGui.QAction
# (This affects menu actions in Nuke UI.) :contentReference[oaicite:1]{index=1}
try:
    QAction = QtGui.QAction if IS_QT6 else QtWidgets.QAction
except Exception:
    QAction = QtGui.QAction
