from dataclasses import dataclass
import psutil

@dataclass
class Hardware:

    @staticmethod
    def getCPU() -> float:
        """Retorna o uso da CPU em %"""
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def getRAM() -> dict:
        """Retorna informações da memória RAM"""
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "used": mem.used,
            "free": mem.available,
            "percent": mem.percent
        }

    @staticmethod
    def getSwap() -> dict:
        """Retorna informações da memória swap"""
        swap = psutil.swap_memory()
        return {
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "percent": swap.percent
        }

    @staticmethod
    def getDisk() -> dict:
        """Retorna info do disco root (/)"""
        disk = psutil.disk_usage("/")
        return {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }

    @staticmethod
    def getAll() -> dict:
        """Retorna tudo em um único dicionário"""
        return {
            "cpu_percent": Hardware.getCPU(),
            "ram": Hardware.getRAM(),
            "swap": Hardware.getSwap(),
            "disk": Hardware.getDisk()
        }
