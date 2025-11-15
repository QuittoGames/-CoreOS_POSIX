from dataclasses import dataclass
import subprocess
import os
from Data.Config import Config
import re

@dataclass
class KarnelTools:
    def whereOS() -> str:
        if not subprocess.getoutput("dpkg -l | grep fastfetch"):
            subprocess.run(["sudo", "apt", "install", "fastfetch", "-y"], check=True)

        os_info_raw = subprocess.getoutput('fastfetch | grep "OS:"')
        os_info_clean = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', os_info_raw)
        os_info_clean = re.sub(r'[^ -~]', ' ', os_info_clean)
        os_info_clean = re.sub(r'\s+', ' ', os_info_clean).strip()
        os_info = Config.COLORS["green"] + os_info_clean + Config.COLORS["reset"]

        return f"Your OS is: {os_info}"