#!/usr/bin/env python3
"""
SIMPLE APTS RUNNER - No automatic dependency installation
Just runs APTS directly
"""

import sys
import subprocess
from pathlib import Path

def main():
    """Simple APTS runner"""
    print("🚀 STARTING MAKV'S APTS SYSTEM...")
    
    # Ensure we're in the right directory
    if not Path("apts.py").exists():
        print("❌ apts.py not found. Run from the mel directory.")
        sys.exit(1)
    
    # Launch APTS directly
    try:
        subprocess.run([sys.executable, "apts.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ APTS failed to start: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 APTS shutdown by user")

if __name__ == "__main__":
    main()