from pyrevit import script
from pyrevit import output
from pyrevit import forms
from rpm import config
from rpm.system.update import Update 
from rpm.system.session import Session


class UI:
	
	@staticmethod 
	def checkUpdates(notifyOnly = False):
	 
		updated = False	
		out = script.get_output()

		pyRevit = Update.checkPyRevit()
		extensions = Update.checkExtensions()
  
		if not pyRevit and not extensions:
			forms.alert('Everything is up to date!',
						title = 'pyRevit Extensions Updates')
  
		if pyRevit:
			install = 'Close open Revit sessions and install pyRevit core update now'
			skip = 'Skip update and keep Revit sessions open'
			res = forms.alert('A pyRevit core update is ready to be installed.\n'
					 		  'Note that all running Revit sessions will be closed automatically when installing the update.',
							  title = 'pyRevit Update',
						 	  options = [install, skip])
			if res == install:
				Update.pyRevit()
		
		if extensions:
			if notifyOnly:
				forms.alert('There are pyRevit extensions updates available and ready to be installed.',
							sub_msg = 'Please use the "Revitron > RPM > Setup > Check for Updates" button to run the updater.',
							title = 'pyRevit Extensions Updates')
			else:
				install = 'Install extension updates now'
				skip = 'Skip updates'
				res = forms.alert('There are pyRevit extension updates ready to be installed.',
								  title = 'pyRevit Extensions Updates',
						 	  	  options = [install, skip])
				if res == install:
					UI.addStyle()
					UI.printLogo()
					UI.printTitle()
					Update.extensions()
					out.print_html('<br><br>')
					Session.reload() 
		
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
		