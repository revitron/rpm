import subprocess
import os
import glob
from pyrevit import script
from rpm import config


class Update:
		
	@staticmethod
	def check(repo):  
		try:
			if not os.path.isdir(repo + '\\.git'):
				return False
			status = Update.git('fetch origin --dry-run', repo)
			if status:
				out = script.get_output()
				out.print_html('<br><b>{}</b> &mdash; updates available'.format(os.path.basename(repo)))			
				print(status)
				return True
		except:
			pass	
   		return False
		
	@staticmethod
	def checkExtensions():
		for repo in Update.getExtensionRepos():
			if Update.check(repo):
				return True
		return False
				
	@staticmethod
	def checkPyRevit():
		return Update.check(config.RPM_PYREVIT_DIR)    
		
	@staticmethod
	def git(cmd, repo):
		return subprocess.check_output('git --git-dir={0}\\.git --work-tree={0} {1}'.format(repo, cmd), stderr=subprocess.STDOUT, shell=True, cwd='C:\\')
		
	@staticmethod
	def getExtensionRepos():
		repos = []
		for git in glob.glob('{}\\*\\.git'.format(config.RPM_EXTENSIONS_DIR)):
			repos.append(os.path.dirname(git))
		return repos
				
	@staticmethod
	def pyRevit():
		os.system('{}\\updatePyRevit.bat {}'.format(os.path.dirname(__file__), config.RPM_PYREVIT_DIR))
	
	@staticmethod 
	def extension(repo):
		status = Update.git('status --untracked-files=no --porcelain', repo)
		if status:
			print('Skipped update &mdash; repository not clean!')
		else:
			print(Update.git('pull', repo))
	
	@staticmethod
	def extensions():
		out = script.get_output()
		for repo in Update.getExtensionRepos():
			out.print_html('<br>')
			out.print_html('<b>{}</b> &mdash; updating ...'.format(os.path.basename(repo)))
			Update.extension(repo)
		