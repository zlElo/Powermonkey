import os
import time
import shutil
import random

def test_disk(logger):
    testnumber = random.randint(1000,10000) # use random number to avoid conflicts with other directories
    path = f'{testnumber}disktest'
    path2 = f'{path}/local'
    os.makedirs(path, exist_ok=True)
    os.makedirs(path2, exist_ok=True)

    logger.log('Initialised disk test...')

    # create a test file
    try:
        with open(f'{path}/test.bench', 'w') as f:
            size = 1024 * 1024 * 10000 # 10GB
            f.seek(size - 1)
            f.write('\0')
    except Exception as e:
        logger.error(f'Error creating test file. That could be a permission problem. - {e}')
        return 0

    # copy test file to destination for testing speed
    start_time = time.time()
    shutil.copy(f'{path}/test.bench', f'{path2}/test.bench')
    end_time = time.time()

    # collect results
    duration = end_time - start_time
    speed = size / duration / (1024 * 1024) # MB/s
    score = speed/10 # calculate score based on speed
    logger.log(f'DONE. Wrote test file in {duration:.2f} seconds at {speed:.2f} MB/s')

    # cleanup
    shutil.rmtree(path)
    logger.log(f'Cleaned workspace for next test')

    return score