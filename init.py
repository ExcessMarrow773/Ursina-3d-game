from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
from ui import *
from playerSetup import *
from pathlib import Path

import sys, os

saveFile = f"{sys.path}/saveFile.txt"
savePath = Path(f"{sys.path}/saveFile.txt")
saveEnabled = savePath.exists()
