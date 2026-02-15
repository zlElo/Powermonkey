import os
import sys
import shutil
import subprocess
from pathlib import Path

class NuitkaBuilder:
    def __init__(self):
        self.main_file = "main.py"
        self.src_dir = "src"
        self.output_dir = "build"
        self.required_files = [self.main_file, self.src_dir]
        
    def check_prerequisites(self):
        print("Checking prerequisites...")
        missing = []
        for file in self.required_files:
            if not os.path.exists(file):
                missing.append(file)
        
        if missing:
            print(f"❌ Missing files: {', '.join(missing)}")
            sys.exit(1)
        
        try:
            subprocess.run([sys.executable, "-m", "nuitka", "--version"], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Nuitka not found. Install with: pip install nuitka")
            sys.exit(1)
        
        print("All prerequisites met.")
    
    def clean_build(self):
        if os.path.exists(self.output_dir):
            print(f"Delete Build-folder: {self.output_dir}")
            shutil.rmtree(self.output_dir)
    
    def build(self, onefile=True, debug=False):
        print(f"Start Nuitka Build (Onefile: {onefile})...")
        
        cmd = [
            sys.executable, "-m", "nuitka",
            "--standalone",
            f"--output-dir={self.output_dir}",
            "--follow-imports",
            f"--include-data-files={self.version_file}={self.version_file}",
            f"--include-data-dir={self.src_dir}={self.src_dir}",
            "--python-flag=-S",
            #"--nofollow-import-to=torch._dynamo", old torch version
            "--assume-yes-for-downloads",
            # "--module-parameter=torch-disable-jit=yes", old torch version
            self.main_file
        ]
        
        if onefile:
            cmd.append("--onefile")
        if debug:
            cmd.extend(["--debug", "--show-progress", "--verbose"])
        
        try:
            result = subprocess.run(cmd, check=True)
            print("Build sucessfully completed")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Build error (Code {e.returncode})")
            return False

def main():
    builder = NuitkaBuilder()
    
    print("Powermonkey Nuitka Build Script")
    print("=" * 50)
    
    builder.check_prerequisites()
    
    onefile = input("Onefile-Mode? (y/n, default=y): ").lower() != 'n'
    debug = input("Debug-Mode? (y/n, default=n): ").lower() == 'y'
    clean = input("Delete old build? (y/n, default=y): ").lower() != 'n'
    
    if clean:
        builder.clean_build()
    
    success = builder.build(onefile=onefile, debug=debug)
    
    if success:
        print(f"\nDone: {builder.output_dir}/")
    else:
        print("\nBuild error")
        sys.exit(1)

if __name__ == "__main__":
    main()
