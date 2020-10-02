import revitron
import rpm

if not revitron.Document().isFamily():
	
	rpm.Update.extensions()
	rpm.system.Session.reload()