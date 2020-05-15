import jarvis

class Session:
    
    @staticmethod
    def prepare():
        jarvis.system.UI.setStyle()
        jarvis.system.UI.printLogo()
        jarvis.system.UI.prepareStartWindow()
        jarvis.system.Update()
        