from src.modules.logging import powermonkeyLogger
from src.disk import test_disk
from src.cpu import test_cpu

logger = powermonkeyLogger('main')

# start tests
logger.log('Starting tests...')
#score_disk = test_disk(logger)
score_cpu = test_cpu(logger)