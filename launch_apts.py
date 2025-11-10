#!/usr/bin/env python3
"""
MAKV'S APTS LAUNCHER
Simple launcher that handles all setup automatically
"""

import sys
import subprocess
import os
from pathlib import Path

def ensure_dependencies():
    """Ensure core dependencies are installed"""
    core_packages = [
        "rich", "loguru", "aiohttp", "requests", 
        "beautifulsoup4", "lxml", "cryptography", "dnspython"
    ]
    
    missing = []
    for package in core_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing.append(package)
    
    if missing:
        print(f"📦 Installing missing packages: {', '.join(missing)}")
        try:
            # Try with --user flag first
            subprocess.run([sys.executable, "-m", "pip", "install", "--user"] + missing, 
                         check=True, capture_output=True)
            print("✅ Dependencies installed")
        except subprocess.CalledProcessError:
            try:
                # Try without --user flag
                subprocess.run([sys.executable, "-m", "pip", "install"] + missing, 
                             check=True, capture_output=True)
                print("✅ Dependencies installed")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install dependencies. Trying to run anyway...")
                print("⚠️ Some features may not work properly")
    
    return True

def main():
    """Main launcher"""
    print("🚀 LAUNCHING MAKV'S APTS SYSTEM...")
    
    # Ensure we're in the right directory
    if not Path("apts.py").exists():
        print("❌ apts.py not found. Run from the mel directory.")
        sys.exit(1)
    
    # Ensure dependencies
    if not ensure_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Launch APTS
    try:
        subprocess.run([sys.executable, "apts.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ APTS failed to start: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 APTS shutdown by user")

if __name__ == "__main__":
    main()
