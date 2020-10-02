import sys
import os.path as op
from rpw.ui.forms import CommandLink, TaskDialog
sys.path.append(op.dirname(__file__))
from rpm.system.ui import UI 

UI.checkUpdates()