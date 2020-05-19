import os
import sys
from pyrevit import script
from pyrevit import output
import constants

class UI:
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(constants.JRVS_DIR + '/svg/jarvis-dark.svg')
        
    @staticmethod  
    def setStyle():
        output.set_stylesheet(constants.JRVS_CORE_DIR + '\\output.css')
