import os
import sys
from pyrevit import script
from pyrevit import output
import jarvis

class UI:
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(jarvis.JRVS_CORE_DIR + '/svg/jarvis-dark.svg')
        
    @staticmethod  
    def setStyle():
        output.set_stylesheet(jarvis.JRVS_CORE_DIR + '\\output.css')
