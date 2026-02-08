import os
import time
import shutil

def test_disk(logger):
    disk = os.statvfs('/')
    path = f'{disk.f_fsid}disktest'
    path2 = f'{path}/local'
    os.makedirs(path, exist_ok=True)
    os.makedirs(path2, exist_ok=True)

    logger.log('Initialised disk test...')

    # create a test file
    with open(f'{path}/test.bench', 'w') as f:
        size = 1024 * 1024 * 10000 # 10GB
        f.seek(size - 1)
        f.write('\0')

    # copy test file to destination for testing speed
    start_time = time.time()
    shutil.copy(f'{path}/test.bench', f'{path2}/test.bench')
    end_time = time.time()

    # collect results
    duration = end_time - start_time
    speed = size / duration / (1024 * 1024) # MB/s
    score = speed/30 # calculate score based on speed
    logger.log(f'DONE. Wrote test file in {duration:.2f} seconds at {speed:.2f} MB/s')

    # cleanup
    shutil.rmtree(path)
    logger.log(f'Cleaned workspace for next test')

    return score