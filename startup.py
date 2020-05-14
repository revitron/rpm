import os
import jarvis
from pyrevit import script
from pyrevit import output

out = script.get_output()
pwd = os.path.dirname(__file__)

output.set_stylesheet(pwd + '\\outputstyles.css')
out.set_height(900)
out.set_width(500)
out.print_image('{}/jarvis-core.svg'.format(pwd))
out.center()

js = jarvis.system

js.update.jarvis(js.constants.JRVS_DIR)
js.update.extensions(js.constants.JRVS_EXTENSIONS_DIR)