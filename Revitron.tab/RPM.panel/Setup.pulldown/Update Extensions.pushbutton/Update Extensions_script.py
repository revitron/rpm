import revitron
import os
import sys 

parent = os.path.dirname
sys.path.append(parent(parent(parent(parent(parent(__file__))))))
import rpm

if not revitron.Document().isFamily():
	
	rpm.Update.extensions()
	rpm.system.Session.reload()