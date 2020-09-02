from rpm import system
from pyrevit import script

class Session:
    
    @staticmethod
    def prepare():
        out = script.get_output()
        system.UI.setStyle()
        system.UI.printLogo()
        out.print_html('<hr>')
        system.Update()
        out.print_html('<hr>')
        out.print_html('Starting session ...')
        