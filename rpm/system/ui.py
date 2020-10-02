from pyrevit import script
from rpm import config


class UI:
        
    @staticmethod 
    def printLogo():
        out = script.get_output()
        out.print_image(config.RPM_DIR + '/svg/rpm-readme.svg')
