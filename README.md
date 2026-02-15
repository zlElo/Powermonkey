# Powermonkey
<p align="center">
  <img src="https://raw.githubusercontent.com/zlElo/Powermonkey/refs/heads/main/data/icon_wbg.png" alt="Powermonkey Logo" width="160">
</p>

<p align="center">
  Lightweight tool for fast, repeatable performance benchmarking
</p>

--------

The idea behind Powermonkey was to build a lightweight, open-source benchmark that’s simple, fast, and efficient. I didn’t want to download gigabytes of data just to run a test that measures one aspect of performance at a time. I wanted a straightforward tool that shows how well my system performs — especially in comparison to others.

## Measurements
- CPU test using a Pi approximation and a parallel prime number calculation algorithm
- GPU test based on the raw matrix-multiplication performance
- Disk test based on copy speed

## Minimum Requirements
- CPU: 1 core
- RAM: 4GB
- Disk: 20GB (free space, just temporary for disk test)
- Python 3, recommended: 3.12

## Installation
To install powermonkey, you can download the executables in the releases. 
Alternatively you can use the python scripts like descriped below or build an own executable with the given script.

### Script
1. Clone repo ```git clone https://github.com/zlElo/Powermonkey.git```
2. Navigate ```cd Powermonkey```
3. Install requirements ```pip install -r requirements.txt```
4. run ```python3 main.py```

### Build by source
1. Clone repo ```git clone https://github.com/zlElo/Powermonkey.git```
2. Navigate ```cd Powermonkey```
3. Install requirements ```pip install -r requirements.txt```
4. Install additional requirements ```pip install -r requirements-advanced.txt```
5. run script ```python3 build.py```
6. Setup configuration using "y" for yes and "n" for no


## Test categories
Powermonkey seperates finished tests in two different categories: ```a1-cdg``` and ```a1-cd```. This function helps to enable fair comparisons between systems.

### a1-cdg
*a1-cpu-disk-graphicscard*
> This category describes a result of systems with a cuda compatible graphics card, a cpu and a disk. These systems usually have a high score.

### a1-cd
*a1-cpu-disk*
> This category describes a result of systems with an iGPU or an older graphics card with no modern cuda support, a cpu and a disk. These systems usually have a lower score than ```a1-cdg``` test-systems.
