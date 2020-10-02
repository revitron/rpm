import pyrevit
import os

RPM_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
RPM_PYREVIT_DIR = pyrevit.HOME_DIR
RPM_PYREVIT_BIN = pyrevit.BIN_DIR + '\\pyrevit'
RPM_EXTENSIONS_DIR = RPM_PYREVIT_DIR + '\\extensions'
RPM_CORE_EXTENSIONS = [
    'revitron.lib',
    'revitron-ui.extension',
    'revitron-tests.extension',
    'rpm.extension'
]