from dataclasses import dataclass
import os

@dataclass
class ShellTools:
    def clear_screen() -> None:
        os.system('clear')