from dataclasses import dataclass
from Data.Config import Config
import subprocess
from typing import overload
import os

@dataclass
class Permision:
    def symbolic_to_octal(permission:str) -> str:
        if permission[0] not in "rwx-":
            permission = permission[1:]
            
        bin = "".join("0" if c == "-" else "1" for c in permission)

        octal = ""

        for i in range(0, len(bin), 3):
            block = bin[i:i+3]
            octal += Config.BIN_TO_OCTAL[block]

        return octal
    
    def symbolic_to_bin(permision:str) -> str:
        return "".join("0" if c == "-" else "1" for c in permision)
    
    def is_sysbolic_perm(permision:str) -> bool:
        return len(permision) in (3,9) and all(i in "rwx-" for i in permision )
    
    def octal_to_sysbolic_perm(permision:str|int) -> str:
        permision = str(permision)
        sysbolic = ""

        for i in permision:
            sysbolic += Config.OCTAL_TO_SYMBOLIC[i]

        return sysbolic


    @overload
    def make_dir_with_perm(permission: str, folders: list) -> bool | None: ...
    
    @overload
    def make_dir_with_perm(path: str, permission: str, folders: list) -> bool | None: ...

    def make_dir_with_perm(*args) -> bool | None:
        if len(args) == 2:
            permission, folders = args
            path = None
        elif len(args) == 3:
            path, permission, folders = args
        else:
            raise TypeError("make_dir_with_perm expected 2 or 3 arguments")

        try:
            for folder in folders:
                if path and os.path.exists(path):
                    subprocess.run(["mkdir", "-m", permission, folder], cwd=path, check=True)
                else:
                    subprocess.run(["mkdir", "-m", permission, folder], check=True)

            print(Config.COLORS["white"] + "[DEBUG] Folder created successfully")
            return True

        except subprocess.CalledProcessError as e:
            print(Config.COLORS["red"] + f"[ERROR] Subprocess failed to execute. Error: {e}")
            return False

        except FileNotFoundError as e:
            print(Config.COLORS["red"] + f"[ERROR] Command not found. Error: {e}")
            return False
