# bb_setup2.py
from bbfreeze import Freezer

bbFreeze_Class = Freezer('exe')
 
bbFreeze_Class.addScript("pyventa.py", gui_only=True)
bbFreeze_Class.addScript("padmin.py", gui_only=True)
bbFreeze_Class.addScript("check.py", gui_only=True)
 
bbFreeze_Class.use_compression = 4
bbFreeze_Class.include_py = True
bbFreeze_Class()