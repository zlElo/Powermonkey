from src.modules.logging import powermonkeyLogger
from src.modules.table import generate_ascii_table
from src.modules.coloring import bcolors
from src.disk import test_disk
from src.cpu import test_cpu
from src.gpu import test_gpu
from src.systemcheck import *

# init vars
logger = powermonkeyLogger('main')
headers = ["Test Device", "Score"]

if __name__ == '__main__':
    # start tests
    logger.log('Starting tests...')
    category = 'a1-crg'
    score_disk = test_disk(logger)
    score_cpu = test_cpu(logger)
    score_gpu, device = test_gpu(logger)

    if device == "cpu":
        category = 'a1-cr'

    logger.break_line()
    logger.result()

    # generate results table
    rows = [
        ["Disk", round(score_disk, 1)],
        ["CPU", round(score_cpu, 1)],
        ["GPU", round(score_gpu, 1)]
    ]
    table = generate_ascii_table(headers, rows)
    print(table)
    logger.scoring(round(score_disk + score_cpu + score_gpu, 1), category)

    logger.break_line()
    
    # system informations
    print(bcolors.OKCYAN + '== Your system informations ==' + bcolors.ENDC)
    print('CPU: ' + get_cpu_name())
    print('GPU: ' + get_gpu_name())
    print('System/OS: ' + get_system())
    print('Python version: ' + get_python_version())
    print(f'Powermonkey: {open("version.powermonkey", "r").read().strip()}')
    print(f'Test category: {category}')