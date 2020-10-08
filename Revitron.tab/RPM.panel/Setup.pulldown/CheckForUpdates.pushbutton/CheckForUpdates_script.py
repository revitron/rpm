"""
Check for pyRevit core and extension updates and optionally install them. 
"""
from rpm.system.ui import UI 

__context__ = 'zero-doc'

UI.checkUpdates()