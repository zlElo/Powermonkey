import platform
import subprocess
import re
from numba import cuda

def get_cpu_name():
    system = platform.system()
    
    if system == "Windows":
        try:
            result = subprocess.run(
                ["wmic", "cpu", "get", "Name"], 
                capture_output=True, text=True, encoding='utf-8'
            )
            lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            return lines[0] if lines else "Unknown"
        except:
            return platform.processor() or "Unknown"
    
    elif system == "Linux":
        try:
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if line.startswith("model name"):
                        return line.split(":", 1)[1].strip()
        except:
            pass
        
        # Fallback lscpu
        try:
            result = subprocess.run(["lscpu"], capture_output=True, text=True)
            match = re.search(r'Model name:\s*(.+)', result.stdout)
            return match.group(1).strip() if match else "Unknown"
        except:
            return "Unknown"
    
    elif system == "Darwin":
        try:
            result = subprocess.run(
                ["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"],
                capture_output=True, text=True
            )
            return result.stdout.strip()
        except:
            return "Unknown"
    
    return platform.processor() or "Unknown"

def get_system():
    return platform.system()

def get_gpu_name():
    try:
        if cuda.is_available():
            return cuda.get_current_device().name
    except:
        pass
    return "CPU only"

def get_python_version():
    return platform.python_version()