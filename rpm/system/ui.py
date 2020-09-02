import os
import sys
from pyrevit import script
from pyrevit import output
from rpm import config

class UI:
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(config.RPM_CORE_DIR + '/svg/rpm.svg')
        
    @staticmethod  
    def setStyle():
        output.set_stylesheet(config.RPM_CORE_DIR + '\\output.css')
