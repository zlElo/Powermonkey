import platform
import cpuinfo
from numba import cuda

def get_cpu_name():
    return cpuinfo.get_cpu_info()['brand_raw']

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