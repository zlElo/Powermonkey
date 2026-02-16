from src.modules.logging import powermonkeyLogger
from src.modules.table import generate_ascii_table
from src.modules.coloring import bcolors
from src.infos import powermonkey_infos
from src.disk import test_disk
from src.cpu import test_cpu
from src.gpu import test_gpu
from src.systemcheck import *
from time import sleep

# init vars
logger = powermonkeyLogger('main')
infos = powermonkey_infos()
headers = ["Test Device", "Score"]

if __name__ == '__main__':
    # start tests
    logger.startup()
    print(bcolors.OKCYAN + 'Powermonkey - your crossplatform system benchmark tool' + bcolors.ENDC)
    
    # wait to accept
    accepted = input('Do you accept to run the benchmark tests? (y/n): ')
    if accepted.lower() != 'y':
        logger.log('Benchmark cancelled by user. Application will be closed in 5 seconds.')
        sleep(5)
        exit()

    # wait to confirm that all applications are closed
    applications_closed = input('Did you close all applications and background tasks? (y/n): ')
    if applications_closed.lower() != 'y':
        logger.warning('It is recommended to close all applications and background tasks for more accurate results. Please close them and run the benchmark again. The application will be closed in 5 seconds.')
        sleep(5)
        exit()
    
    # start tests
    logger.log('Starting tests...')
    category = 'a1-cdg'
    score_disk = test_disk(logger)
    score_cpu = test_cpu(logger)
    score_gpu, device = test_gpu(logger)

    if device == "cpu":
        category = 'a1-cd'

    logger.log('Test completed successfully!')
    logger.break_line()
    #logger.result()
    #print(bcolors.OKCYAN + 'Powermonkey results for test category: ' + category + bcolors.ENDC)

    logger.scoring(round(score_disk + score_cpu + score_gpu, 1), category)
    # generate results table
    rows = [
        ["Disk", round(score_disk, 1)],
        ["CPU", round(score_cpu, 1)],
        ["GPU", round(score_gpu, 1)]
    ]
    table = generate_ascii_table(headers, rows)

    logger.break_line()
    
    # system informations
    print(bcolors.OKCYAN + 'Your system informations' + bcolors.ENDC)
    print(table)
    print('CPU: ' + get_cpu_name())
    print('GPU: ' + get_gpu_name())
    print('System/OS: ' + get_system())
    print('Python version: ' + get_python_version())
    print(f'Powermonkey: {infos.version}')
    print(f'Test category: {category}')