import sys
import os

RPM_PYREVIT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
RPM_PYREVIT_BIN = RPM_PYREVIT_DIR + '\\bin\\pyrevit'
RPM_EXTENSIONS_DIR = RPM_PYREVIT_DIR + '\\extensions'
RPM_CORE_EXTENSIONS = [
    'revitron.lib',
    'revitron-ui.extension',
    'revitron-tests.extension',
    'rpm.lib',
    'rpm-ui.extension'
]

sys.path.append(RPM_EXTENSIONS_DIR + '\\revitron.lib')