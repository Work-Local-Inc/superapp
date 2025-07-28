#!/usr/bin/env python3
"""
🔍 Debug Git Path Issues
"""

import os
from pathlib import Path

def debug_paths():
    repo_path = Path("clients-hub-wiki")
    
    print(f"Current working dir: {os.getcwd()}")
    print(f"Repo path: {repo_path}")
    print(f"Repo path absolute: {repo_path.resolve()}")
    print(f"Repo exists: {repo_path.exists()}")
    print(f"Git dir exists: {(repo_path / '.git').exists()}")
    
    # Test changing directory
    try:
        original_cwd = os.getcwd()
        os.chdir(repo_path.resolve())
        print(f"Changed to: {os.getcwd()}")
        
        # Test git command
        import subprocess
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        print(f"Git status exit code: {result.returncode}")
        if result.returncode == 0:
            print("✅ Git status works!")
        else:
            print(f"❌ Git status error: {result.stderr}")
        
        os.chdir(original_cwd)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    debug_paths() 