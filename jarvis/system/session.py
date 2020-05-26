import jarvis
from pyrevit import script

class Session:
    
    @staticmethod
    def prepare():
        out = script.get_output()
        out.unlock_size()
        out.set_height(700)
        out.set_width(1000)
        out.center()
        jarvis.system.UI.setStyle()
        jarvis.system.UI.printLogo()
        out.print_html('<hr>')
        jarvis.system.Update()
        out.print_html('<hr>')
        out.print_html('Starting session ...')
        