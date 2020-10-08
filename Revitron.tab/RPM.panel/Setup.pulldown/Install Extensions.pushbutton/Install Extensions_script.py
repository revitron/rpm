# -*- coding: utf-8 -*-
import revitron
import os
import rpm

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
			print('Installing {}'.format(extName))
			extManager.install(extName, extRepo, extType)
		except:
			pass
		
	rpm.system.Session.reload()
