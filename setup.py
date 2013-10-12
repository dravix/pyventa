# bb_setup2.py
from bbfreeze import Freezer

app = Freezer('exe')
 
app.addScript("pyventa.py", gui_only=True)
app.addScript("padmin.py", gui_only=True)
app.addScript("check.py", gui_only=True)
 
app.use_compression = 4
app.include_py = True
app()