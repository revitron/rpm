from pyrevit import script
from pyrevit import output
from rpm import config
from rpm.system.update import Update 
from rpm.system.session import Session
from rpw.ui.forms import CommandLink, TaskDialog


class UI:
	
	@staticmethod 
	def checkUpdates():
	 
		UI.printLogo()
		updated = False		
  
		if Update.checkPyRevit():
			cmdPyRevit= [CommandLink('Install pyRevit update now', return_value = True), 
						CommandLink('Skip update', return_value = False)]
			dlgPyRevit = TaskDialog('There is a pyRevit update ready to be installed',
									title = 'pyRevit Update',
									title_prefix = False,
									commands = cmdPyRevit,
									show_close = True)
			if dlgPyRevit.show():
				Update.pyRevit()
				updated = True
  
		if Update.checkExtensions():
			cmdExt= [CommandLink('Install extension updates now', return_value = True), 
					CommandLink('Skip updates', return_value = False)]
			dlgExt = TaskDialog('There are extension updates ready to be installed',
								title = 'Extensions Updates',
								title_prefix = False,
								commands = cmdExt,
								show_close = True)
			if dlgExt.show():
				Update.extensions()
				updated = True
    
		if updated:
			Session.reload()
		else:
			output.get_output().close() 
		
	@staticmethod 
	def printLogo():
		out = script.get_output()
		out.print_image(config.RPM_DIR + '/svg/rpm-readme.svg')
		