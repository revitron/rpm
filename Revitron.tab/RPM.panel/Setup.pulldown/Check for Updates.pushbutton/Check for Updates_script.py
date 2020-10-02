import revitron
import os
import sys 
parent = os.path.dirname
sys.path.append(parent(parent(parent(parent(parent(__file__))))))
from rpm.system.ui import UI 

__context__ = 'zero-doc'

UI.checkUpdates(False)