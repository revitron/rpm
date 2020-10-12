# -*- coding: utf-8 -*-
"""
Install all extensions defined for this project. You can define extensions for this project in the "Project Setup". 
"""
import revitron
import os
import rpm
from pyrevit.coreutils import logger


mlogger = logger.get_logger(__name__)

if not revitron.Document().isFamily():

	extManager = rpm.ExtensionsManager()
	extManager.removeAll()

	lines = revitron.DocumentConfigStorage().get('rpm.extensions', '').split('\r\n')
	 
	for line in lines:
		
		items = line.split('\t')
		
		try:
			extType = items[0].strip()
			extRepo = items[1].strip()
			extName = os.path.basename(extRepo).replace('.git', '')
			extManager.install(extName, extRepo, extType)
		except:
			try:
				mlogger.error('Installing {} failed'.format(extName))
			except:
				pass
		
	rpm.system.Session.reload()
