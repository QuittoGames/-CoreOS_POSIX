from moduleControl.ModuleControl import ModuleControl
import asyncio
from POSIX.ShellTools import ShellTools
from POSIX.Permision import Permision
from Data.Config import Config
from Karnel.KarnelTools import KarnelTools

lsit = ["Data","Karnel"]
ShellTools.clear_screen()
asyncio.run(ModuleControl.add_path_modules(lsit))

print(Config.COLORS["blue"] + Permision.symbolic_to_octal("rwxr-xr-x") + Config.COLORS["reset"])

# Permision.make_dir_with_perm("777", ["teste12", "teste22"])

print(KarnelTools.whereOS())
