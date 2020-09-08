import os
import sys
from pyrevit import script
from pyrevit import output
from rpm import config
import revitron

class UI:
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(revitron.LIB_DIR + '/svg/revitron-white.svg')
        
    @staticmethod  
    def setStyle():
        output.set_stylesheet(revitron.LIB_DIR + '\\css\\output.css')
