import sys

JRVS_DIR = 'C:\\HdM-DT\\jarvis'
JRVS_PYREVIT_BIN = JRVS_DIR + '\\jarvis-pyrevit\\bin\\pyrevit'
JRVS_EXTENSIONS_DIR = JRVS_DIR + '\\jarvis-pyrevit\\extensions'
JRVS_CORE_DIR = JRVS_EXTENSIONS_DIR + '\\jarvis-core.lib'
JRVS_CORE_EXTENSIONS = [
    'revitron.lib',
    'revitron-ui.extension',
    'jarvis-core.lib',
    'jarvis-system.extension'
]

sys.path.append(JRVS_EXTENSIONS_DIR + '\\revitron.lib')

from system import *
from extensions import *