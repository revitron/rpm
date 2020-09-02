from rpm import config
import revitron
import glob
import os

class ExtensionsManager:
    
    def __init__(self):
        self.installed = self.getInstalled()
    
    def getInstalled(self):
        
        extensions = []
        for item in glob.glob('{}\\*.*\\.git'.format(config.RPM_EXTENSIONS_DIR)):
            
            extPath = os.path.dirname(item)
            ext = os.path.basename(extPath)
            
            if ext not in config.RPM_CORE_EXTENSIONS:
                extensions.append(extPath)
                
        return extensions
    
    def removeAll(self):
        for ext in self.installed:
            os.system('rmdir /Q /S {}'.format(ext))
    
    def install(self, name, repo, extType):
        cmd = '{} extend {} {} {} --dest="{}"'.format(config.RPM_PYREVIT_BIN, extType, name, repo, config.RPM_EXTENSIONS_DIR)
        os.system(cmd)
