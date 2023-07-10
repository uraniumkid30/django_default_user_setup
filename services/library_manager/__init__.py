import os

from .enums import LibraryManagers
from .pip_manager import PipLibraryManager
from .pipenv_manager import PipenvLibraryManager


def lib_manager_factory(lib_manager: str = ""):
    lib_manager = lib_manager.upper()
    if not lib_manager or not LibraryManagers.in_choices(lib_manager):
        LIBRARY_MANAGER: str = os.environ.get(
            'LIBRARY_MANAGER',
            LibraryManagers.PIPENV
        )
    else:
        LIBRARY_MANAGER: str = lib_manager
    if LIBRARY_MANAGER == LibraryManagers.PIP:
        return PipLibraryManager()
    elif LIBRARY_MANAGER == LibraryManagers.PIPENV:
        return PipenvLibraryManager()
