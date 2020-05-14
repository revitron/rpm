import constants
import update
import os
from pyrevit import script
from pyrevit import output

out = script.get_output()
pwd = os.path.dirname(__file__)
update = update.jarvisUpdater()

output.set_stylesheet(pwd + '\\outputstyles.css')
out.set_height(900)
out.set_width(500)
out.print_image('{}/jarvis-core.svg'.format(pwd))
out.center()

update.jarvis(constants.JRVS_DIR)
update.extensions(constants.JRVS_EXTENSIONS_DIR)