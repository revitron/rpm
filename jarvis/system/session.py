import jarvis
from pyrevit import script

class Session:
    
    @staticmethod
    def prepare():
        jarvis.system.UI.setStyle()
        jarvis.system.UI.printLogo()
        jarvis.system.Update()
        out = script.get_output()
        out.print_html('<br>')
        out.print_html('<em>Starting session ...</em>')
        