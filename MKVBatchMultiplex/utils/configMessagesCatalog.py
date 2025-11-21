"""
Configure language for localee
"""

import gettext

from typing import Optional

from PySide6.QtWidgets import QMainWindow

from .. import config

def configMessagesCatalog(app: QMainWindow, language: Optional[str] = None) -> None:
    """
    Set application language; the scheme permits runtime changes.
    If translation files are missing (e.g., in a frozen app),
    fall back to English instead of crashing.
    """

    if language is None:
        language = config.data.get(config.ConfigKey.Language)

    try:
        lang = gettext.translation(
            config.NAME,
            localedir=str(config.LOCALE),
            languages=[language]
        )
    except FileNotFoundError:
        # Fallback to a no-op translator if .mo files aren't bundled
        lang = gettext.NullTranslations()

    if app.uiTranslateInterface.setMessagesCatalog(language):
        pass

    lang.install(names=("ngettext",))
    config.data.set(config.ConfigKey.Language, language)
