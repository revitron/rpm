import sys
import os

JRVS_PYREVIT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
JRVS_PYREVIT_BIN = JRVS_PYREVIT_DIR + '\\bin\\pyrevit'
JRVS_EXTENSIONS_DIR = JRVS_PYREVIT_DIR + '\\extensions'
JRVS_CORE_DIR = JRVS_EXTENSIONS_DIR + '\\jarvis.lib'
JRVS_CORE_EXTENSIONS = [
    'revitron.lib',
    'revitron-ui.extension',
    'jarvis.lib',
    'jarvis-ui.extension'
]

sys.path.append(JRVS_EXTENSIONS_DIR + '\\revitron.lib')

from system import *
from extensions import *