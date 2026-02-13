import torch
import time

def _no_op_sync():
    """No-op synchronization for CPU fallback"""
    pass

def test_gpu(logger):
    # priority: CUDA(NVIDIA/ROCm) > CPU (iGPU-Fallback)
    if torch.cuda.is_available():
        device = "cuda"
        gpu_name = torch.cuda.get_device_name(0)
        total_mem = torch.cuda.get_device_properties(0).total_memory
        logger.log(f"Using GPU: {gpu_name}")
        sync = lambda: torch.cuda.synchronize()
    else:
        device = "cpu"
        total_mem = 4 * 1024**3  # 4GB RAM Fallback
        logger.log("Using CPU (iGPU not accelerated)")
        sync = _no_op_sync
    
    # Adjust matrix size
    size_ = total_mem // (4 * 2)  
    size = min(int(size_ ** (1/3)), 8000 if device=="cuda" else 2000)  # CPU smaller
    
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    
    # Warmup
    logger.log("Warming up...")
    for _ in range(5): 
        torch.matmul(a, b)
    sync()
    
    # Benchmark
    logger.log("Running GPU benchmark...")
    start = time.time()
    for _ in range(5000): 
        c = torch.matmul(a, b)
    sync()
    end = time.time()
    
    gflops = 2 * size**3 * 5000 / (end - start) / 1e9
    score = gflops / 20  # Scale down for scoring
    
    logger.log(f"Score: {round(score, 1)}, GFLOPS achieved: {round(gflops, 1)}")
    return round(score, 1), device
