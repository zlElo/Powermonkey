import multiprocessing as mp
import time
import gc
import math

def calculate_pi_leibniz(n_terms):
    pi_over_4 = 0
    for i in range(n_terms):
        term = (-1)**i / (2*i + 1)
        pi_over_4 += term
    return pi_over_4 * 4

def prime_worker(start, end):
    primes_found = 0
    for num in range(start, end):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes_found += 1
    return primes_found

def prime_cruncher(n=100000000, logger=None):
    cores = mp.cpu_count()
    logger.log(f'Using {cores} CPU cores for prime crunching...')
    chunk_size = n // cores
    
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(cores)]
    ranges[-1] = (ranges[-1][0], n)
    
    with mp.Pool(processes=cores) as pool:
        results = pool.starmap(prime_worker, ranges)
    
    return sum(results)

def test_cpu(logger):
    score = 0
    gc.disable()
    logger.log('Starting CPU benchmark...')

    # Pi approximation
    start_time = time.time()
    approx_pi = calculate_pi_leibniz(10**7)
    end_time = time.time()
    duration = end_time - start_time
    score += 200 / duration
    logger.log(f'Calculated pi approximation: {approx_pi} in {duration:.2f} seconds')

    # Prime crunching
    start_time = time.time()
    primes = prime_cruncher(25000000, logger)
    end_time = time.time()
    duration = end_time - start_time
    score += 200 / duration
    logger.log(f'Found {primes:,} primes up to 25 million in {duration:.2f} seconds')

    return score
