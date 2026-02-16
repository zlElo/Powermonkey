import numpy as np
from numba import cuda
import time

def _no_op_sync():
    """No-op synchronization for CPU fallback"""
    pass

def test_gpu(logger):
    # Check CUDA availability first
    if cuda.is_available():
        try:
            device = cuda.get_current_device()
            gpu_name = device.name
            total_mem = device.total_memory
            logger.log(f"Using GPU: {gpu_name}")
            sync = cuda.synchronize
        except:
            device = "cpu"
            total_mem = 4 * 1024**3
            logger.warning("CUDA detected but failed to init. Falling back to CPU.")
            sync = _no_op_sync
    else:
        device = "cpu"
        total_mem = 4 * 1024**3
        logger.log("Using CPU (CUDA not available)")
        sync = _no_op_sync
    
    # Matrix size (identical to original)
    size_ = total_mem // (4 * 2)
    size = min(int(size_ ** (1/3)), 8000 if device == "cuda" else 2000)
    
    a = np.random.randn(size, size).astype(np.float32)
    b = np.random.randn(size, size).astype(np.float32)
    
    logger.log("Warming up...")
    for _ in range(5):
        np.dot(a, b)
    sync()
    
    logger.log("Running GPU benchmark...")
    start = time.perf_counter()
    for _ in range(5000):
        c = np.dot(a, b)
    sync()
    end = time.perf_counter()
    
    gflops = 2 * size**3 * 5000 / (end - start) / 1e9
    score = gflops / 20
    
    logger.log(f"Score: {round(score, 1)}, GFLOPS achieved: {round(gflops, 1)}")
    return round(score, 1), device
