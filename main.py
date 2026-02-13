from src.modules.logging import powermonkeyLogger
from src.disk import test_disk
from src.cpu import test_cpu
from src.gpu import test_gpu
from src.systemcheck import *

logger = powermonkeyLogger('main')

if __name__ == '__main__':
    # start tests
    logger.log('Starting tests...')
    category = 'a1-crg'
    score_disk = test_disk(logger)
    score_cpu = test_cpu(logger)
    score_gpu, device = test_gpu(logger)

    if device == "cpu":
        category = 'a1-cr'
        score_gpu = 0

    logger.break_line()
    logger.result()
    
    # system informations
    print('Your system informations')
    print('CPU: ' + get_cpu_name())
    print('GPU: ' + get_gpu_name())
    print('System/OS: ' + get_system())
    print(f'Powermonkey: {open("version.powermonkey", "r").read().strip()}')
    print(f'Test category: {category}')
    
    logger.break_line()
    logger.scoring(round(score_disk + score_cpu + score_gpu, 1), category)