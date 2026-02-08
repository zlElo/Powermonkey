from src.modules.logging import powermonkeyLogger
from src.disk import test_disk
from src.cpu import test_cpu

logger = powermonkeyLogger('main')

if __name__ == '__main__':
    # start tests
    logger.log('Starting tests...')
    score_disk = test_disk(logger)
    score_cpu = test_cpu(logger)

    logger.break_line()
    logger.result()
    logger.scoring(round(score_disk + score_cpu, 1))