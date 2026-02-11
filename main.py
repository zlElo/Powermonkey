from src.modules.logging import powermonkeyLogger
from src.disk import test_disk
from src.cpu import test_cpu
from src.gpu import test_gpu
from src.systemcheck import *

logger = powermonkeyLogger('main')

if __name__ == '__main__':
    # start tests
    logger.log('Starting tests...')
    score_disk = test_disk(logger)
    score_cpu = test_cpu(logger)
    score_gpu = test_gpu(logger)

    logger.break_line()
    logger.result()
    
    # system informations
    print('Your system informations')
    print('CPU: ' + get_cpu_name())
    print('System/OS: ' + get_system())
    print(f'Powermonkey: {open("version.monkey", "r").read().strip()}')
    
    logger.break_line()
    logger.scoring(round(score_disk + score_cpu + score_gpu, 1))