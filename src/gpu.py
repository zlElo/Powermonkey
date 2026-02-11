import torch
import time

def test_gpu(logger):
    if not torch.cuda.is_available():
        logger.warning("No CUDA-compatible GPU found. Skipping GPU benchmark.")
        return
    
    device = "cuda"
    print(f"GPU: {torch.cuda.get_device_name()}")
    
    size = 8192
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)
    
    # Warmup
    logger.log("Warming up GPU...")
    for _ in range(5): torch.matmul(a, b)
    torch.cuda.synchronize()
    
    # Benchmark
    logger.log("Running GPU benchmark...")
    start = time.time()
    for _ in range(50): 
        c = torch.matmul(a, b)
    torch.cuda.synchronize()
    end = time.time()
    
    # calculate GFLOPS
    gflops = 2 * size**3 * 50 / (end - start) / 1e9
    vram_used = torch.cuda.memory_allocated()
    score = (gflops / 1000)*vram_used
    logger.log('GPU benchmark completed')
    
    return round(score, 1)
