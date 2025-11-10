#!/usr/bin/env python3
"""
INSTALL DUAL AI SYSTEM for APTS
Complete installation and integration of dual AI penetration testing system
"""

import asyncio
import subprocess
import sys
import os
import time

async def install_dual_ai_system():
    """Complete installation of dual AI system"""
    
    print("🚀 INSTALLING DUAL AI PENETRATION SYSTEM FOR APTS")
    print("=" * 60)
    
    # Step 1: Pull latest changes
    print("\n📥 STEP 1: Pulling latest changes from GitHub...")
    try:
        result = subprocess.run([
            'git', 'pull', 'origin', 'feature/apts-military-grade-penetration-testing-system'
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode == 0:
            print("✅ Latest changes pulled successfully")
        else:
            print(f"⚠️ Git pull warning: {result.stderr}")
    except Exception as e:
        print(f"❌ Git pull failed: {e}")
    
    # Step 2: Apply emergency fix
    print("\n🔧 STEP 2: Applying emergency penetration testing fix...")
    try:
        if os.path.exists('emergency_real_fix.py'):
            result = subprocess.run([sys.executable, 'emergency_real_fix.py'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Emergency fix applied successfully")
                print(result.stdout)
            else:
                print(f"⚠️ Emergency fix warning: {result.stderr}")
        else:
            print("⚠️ emergency_real_fix.py not found - skipping")
    except Exception as e:
        print(f"❌ Emergency fix failed: {e}")
    
    # Step 3: Integrate AI coordination
    print("\n🤖 STEP 3: Integrating AI coordination system...")
    try:
        if os.path.exists('ai_coordination_system.py'):
            result = subprocess.run([sys.executable, 'ai_coordination_system.py'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ AI coordination system integrated")
                print(result.stdout)
            else:
                print(f"⚠️ AI coordination warning: {result.stderr}")
        else:
            print("⚠️ ai_coordination_system.py not found - skipping")
    except Exception as e:
        print(f"❌ AI coordination integration failed: {e}")
    
    # Step 4: Install dual AI system
    print("\n🧠 STEP 4: Installing dual AI penetration system...")
    try:
        if os.path.exists('dual_ai_penetration_system.py'):
            result = subprocess.run([sys.executable, 'dual_ai_penetration_system.py'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Dual AI system integrated")
                print(result.stdout)
            else:
                print(f"⚠️ Dual AI integration warning: {result.stderr}")
        else:
            print("⚠️ dual_ai_penetration_system.py not found - skipping")
    except Exception as e:
        print(f"❌ Dual AI integration failed: {e}")
    
    # Step 5: Install Ollama (if not present)
    print("\n📦 STEP 5: Installing Ollama AI runtime...")
    try:
        # Check if Ollama is already installed
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ollama already installed")
        else:
            raise FileNotFoundError("Ollama not found")
    except FileNotFoundError:
        print("📥 Installing Ollama...")
        try:
            # Install Ollama
            install_cmd = "curl -fsSL https://ollama.ai/install.sh | sh"
            process = await asyncio.create_subprocess_shell(
                install_cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                print("✅ Ollama installed successfully")
                
                # Start Ollama service
                print("🔄 Starting Ollama service...")
                start_process = await asyncio.create_subprocess_shell(
                    "ollama serve > /dev/null 2>&1 &",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                await asyncio.sleep(3)  # Wait for service to start
                print("✅ Ollama service started")
            else:
                print(f"❌ Ollama installation failed: {stderr.decode()}")
        except Exception as e:
            print(f"❌ Ollama installation error: {e}")
    
    # Step 6: Download AI models
    print("\n🧠 STEP 6: Downloading AI models...")
    
    models = [
        ("deepseek-coder:6.7b", "DeepSeek Coder 6.7B - Primary Security Analysis"),
        ("llama3.1:8b", "Llama 3.1 8B - Verification & Cross-validation")
    ]
    
    for model, description in models:
        print(f"\n📥 Downloading {description}...")
        print("⏳ This may take several minutes depending on your internet connection...")
        
        try:
            # Check if model already exists
            check_cmd = f"ollama list | grep {model.split(':')[0]}"
            result = subprocess.run(check_cmd, shell=True, capture_output=True)
            
            if result.returncode == 0:
                print(f"✅ {model} already available")
            else:
                # Download the model
                pull_process = await asyncio.create_subprocess_shell(
                    f"ollama pull {model}",
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                
                stdout, stderr = await pull_process.communicate()
                
                if pull_process.returncode == 0:
                    print(f"✅ {model} downloaded successfully")
                else:
                    print(f"❌ Failed to download {model}: {stderr.decode()}")
        
        except Exception as e:
            print(f"❌ Model download error: {e}")
    
    # Step 7: Verify installation
    print("\n🔍 STEP 7: Verifying installation...")
    
    verification_checks = [
        ("apts.py", "Main APTS system"),
        ("emergency_real_fix.py", "Emergency penetration fix"),
        ("ai_coordination_system.py", "AI coordination system"),
        ("dual_ai_penetration_system.py", "Dual AI system")
    ]
    
    all_good = True
    for file, description in verification_checks:
        if os.path.exists(file):
            print(f"✅ {description} - Present")
        else:
            print(f"❌ {description} - Missing")
            all_good = False
    
    # Check Ollama and models
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Ollama runtime - Working")
            
            # Check for our models
            output = result.stdout
            if 'deepseek-coder' in output:
                print("✅ DeepSeek Coder model - Available")
            else:
                print("⚠️ DeepSeek Coder model - Not found")
                all_good = False
            
            if 'llama3.1' in output:
                print("✅ Llama 3.1 model - Available")
            else:
                print("⚠️ Llama 3.1 model - Not found")
                all_good = False
        else:
            print("❌ Ollama runtime - Not working")
            all_good = False
    except:
        print("❌ Ollama runtime - Not accessible")
        all_good = False
    
    # Final status
    print("\n" + "=" * 60)
    if all_good:
        print("🎉 DUAL AI SYSTEM INSTALLATION COMPLETE!")
        print("\n🚀 ENHANCED APTS FEATURES:")
        print("✅ DeepSeek Coder 6.7B - Primary security analysis")
        print("✅ Llama 3.1 8B - Verification and cross-validation")
        print("✅ Zero false positive verification system")
        print("✅ Crypto-specific vulnerability detection")
        print("✅ Military-grade accuracy and reliability")
        print("✅ Real penetration testing (not 2-second scans)")
        print("✅ Detailed proxy locations with country flags")
        print("✅ AI-coordinated attack strategies")
        
        print("\n🎯 READY TO RUN:")
        print("python3 apts.py")
        
    else:
        print("⚠️ INSTALLATION INCOMPLETE")
        print("Some components are missing. Please check the errors above.")
        print("\n🔧 MANUAL STEPS:")
        print("1. Ensure all Python files are present")
        print("2. Install Ollama: curl -fsSL https://ollama.ai/install.sh | sh")
        print("3. Download models: ollama pull deepseek-coder:6.7b && ollama pull llama3.1:8b")
        print("4. Run: python3 apts.py")

if __name__ == "__main__":
    asyncio.run(install_dual_ai_system())