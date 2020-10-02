from pyrevit import script
from pyrevit import output
from rpm import config
from rpm.system.update import Update 
from rpm.system.session import Session
from rpw.ui.forms import CommandLink, TaskDialog


class UI:
	
	@staticmethod 
	def checkUpdates(close = True):
	 
		UI.addStyle()
		UI.printLogo()
		UI.printTitle()
		updated = False	
		out = script.get_output()
  
		if Update.checkPyRevit():
			cmdPyRevit= [CommandLink('Close all running Revit instances and install pyRevit update now', return_value = True), 
						CommandLink('Skip update', return_value = False)]
			dlgPyRevit = TaskDialog('There is a pyRevit update ready to be installed',
									title = 'pyRevit Update',
									title_prefix = False,
									commands = cmdPyRevit,
									show_close = True)
			if dlgPyRevit.show():
				Update.pyRevit()
				updated = True
		else:
			out.print_html('<b>pyRevit</b> is up to date')
  
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
		else:
			out.print_html('<b>Extensions</b> are up to date')
	
		if updated:
			Session.reload()
		else:
			if close:
				output.get_output().close() 
		
	@staticmethod 
	def printLogo():
		out = script.get_output()
		out.print_image(config.RPM_DIR + '/svg/rpm-readme.svg')
  
	@staticmethod 
	def printTitle():
		out = script.get_output()
		out.print_html('<h2>Revitron Package Manager</h2>')
  
	@staticmethod
	def addStyle():
		style = 'body {padding: 30px; color: #121212;} img {max-width: 500px;} span {display: block; text-align: center;}'
		output.get_output().add_style(style)
		