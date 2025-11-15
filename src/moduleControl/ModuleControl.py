from dataclasses import dataclass
import os
import subprocess
import sys
from Data.Config import Config

@dataclass
class ModuleControl:
    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "requirements", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
            return
        
    async def add_path_modules(modules:list) -> None:
        if modules == None:return
        try:
            for i in modules:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
                if Config.Debug: print(f"{Config.COLORS["green"]}[INFO] Module: {i} is Loaded {Config.COLORS["reset"]}")
            return
        except Exception as E:
            print(f"[ERRO] Erro Al Adicionar Os Caminhos Brutos, Erro: {E}")
            return