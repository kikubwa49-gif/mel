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
        print(f"📦 Missing packages detected: {', '.join(missing)}")
        print("⚠️ Please install manually with:")
        print(f"   pip install --user {' '.join(missing)}")
        print("🚀 Continuing with available packages...")
    else:
        print("✅ All core dependencies available")
    
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
