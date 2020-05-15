import os
import sys
from pyrevit import script
from pyrevit import output
import constants

class UI:
    
    @staticmethod 
    def prepareStartWindow():
        out = script.get_output()
        out.set_height(800)
        out.set_width(1000)
        #out.center()
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(constants.JRVS_DIR + '/svg/jarvis-light.svg')
        
    @staticmethod  
    def setStyle():
        output.set_stylesheet(constants.JRVS_CORE_DIR + '\\output.css')
