import importlib.metadata as meta

from .lib import fio, calc

__version__ = meta.version(str(__package__))
__all__ = ('__version__', 'fio', 'calc')
