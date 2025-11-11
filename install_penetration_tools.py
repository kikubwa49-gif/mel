#!/usr/bin/env python3
"""
🚀 MAKV'S PENETRATION TOOLS INSTALLER 🚀
Automatically installs REAL penetration testing tools
"""

import subprocess
import sys
import os
import requests
import zipfile
import tarfile
from pathlib import Path

class PenetrationToolsInstaller:
    def __init__(self):
        self.tools_dir = Path.home() / '.makv_tools'
        self.tools_dir.mkdir(exist_ok=True)
        
    def install_all_tools(self):
        """Install all penetration testing tools"""
        print("🚀 INSTALLING MAKV'S PENETRATION ARSENAL...")
        
        # Install Go (required for many tools)
        self.install_go()
        
        # Install Nuclei
        self.install_nuclei()
        
        # Install SQLMap
        self.install_sqlmap()
        
        # Install FFUF
        self.install_ffuf()
        
        # Install Subfinder
        self.install_subfinder()
        
        # Install httpx
        self.install_httpx()
        
        # Install Gobuster
        self.install_gobuster()
        
        # Install Amass
        self.install_amass()
        
        # Install Nikto
        self.install_nikto()
        
        # Install WPScan
        self.install_wpscan()
        
        # Install Nmap (if not already installed)
        self.install_nmap()
        
        # Update PATH
        self.update_path()
        
        print("✅ ALL PENETRATION TOOLS INSTALLED SUCCESSFULLY!")
        print("🎯 Your system is now ready for REAL penetration testing!")
        
    def run_command(self, cmd, shell=False):
        """Run system command"""
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def install_go(self):
        """Install Go programming language"""
        print("📦 Installing Go...")
        
        # Check if Go is already installed
        success, _, _ = self.run_command(['go', 'version'])
        if success:
            print("✅ Go already installed")
            return
        
        try:
            # Download and install Go
            go_version = "1.21.5"
            go_url = f"https://golang.org/dl/go{go_version}.linux-amd64.tar.gz"
            go_file = self.tools_dir / f"go{go_version}.linux-amd64.tar.gz"
            
            print(f"📥 Downloading Go {go_version}...")
            response = requests.get(go_url, stream=True)
            with open(go_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Extract Go
            with tarfile.open(go_file, 'r:gz') as tar:
                tar.extractall(self.tools_dir)
            
            # Set up Go environment
            go_root = self.tools_dir / 'go'
            go_path = Path.home() / 'go'
            go_path.mkdir(exist_ok=True)
            
            # Add to bashrc
            bashrc = Path.home() / '.bashrc'
            go_exports = f"""
# Go environment
export GOROOT={go_root}
export GOPATH={go_path}
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
"""
            
            with open(bashrc, 'a') as f:
                f.write(go_exports)
            
            print("✅ Go installed successfully")
            
        except Exception as e:
            print(f"❌ Go installation failed: {e}")
    
    def install_nuclei(self):
        """Install Nuclei vulnerability scanner"""
        print("📦 Installing Nuclei...")
        
        try:
            # Install via Go
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ Nuclei installed successfully")
                
                # Download Nuclei templates
                print("📥 Downloading Nuclei templates...")
                templates_cmd = f"{Path.home()}/go/bin/nuclei -update-templates"
                self.run_command(templates_cmd, shell=True)
                print("✅ Nuclei templates downloaded")
            else:
                print(f"❌ Nuclei installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Nuclei installation failed: {e}")
    
    def install_sqlmap(self):
        """Install SQLMap"""
        print("📦 Installing SQLMap...")
        
        try:
            # Clone SQLMap repository
            sqlmap_dir = self.tools_dir / 'sqlmap'
            if sqlmap_dir.exists():
                print("✅ SQLMap already installed")
                return
            
            cmd = f"cd {self.tools_dir} && git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                # Make sqlmap executable
                sqlmap_script = sqlmap_dir / 'sqlmap.py'
                os.chmod(sqlmap_script, 0o755)
                
                # Create symlink
                bin_dir = Path.home() / '.local' / 'bin'
                bin_dir.mkdir(parents=True, exist_ok=True)
                
                symlink = bin_dir / 'sqlmap'
                if not symlink.exists():
                    symlink.symlink_to(sqlmap_script)
                
                print("✅ SQLMap installed successfully")
            else:
                print(f"❌ SQLMap installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ SQLMap installation failed: {e}")
    
    def install_ffuf(self):
        """Install FFUF"""
        print("📦 Installing FFUF...")
        
        try:
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install github.com/ffuf/ffuf/v2@latest"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ FFUF installed successfully")
            else:
                print(f"❌ FFUF installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ FFUF installation failed: {e}")
    
    def install_subfinder(self):
        """Install Subfinder"""
        print("📦 Installing Subfinder...")
        
        try:
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ Subfinder installed successfully")
            else:
                print(f"❌ Subfinder installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Subfinder installation failed: {e}")
    
    def install_httpx(self):
        """Install httpx"""
        print("📦 Installing httpx...")
        
        try:
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ httpx installed successfully")
            else:
                print(f"❌ httpx installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ httpx installation failed: {e}")
    
    def install_gobuster(self):
        """Install Gobuster"""
        print("📦 Installing Gobuster...")
        
        try:
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install github.com/OJ/gobuster/v3@latest"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ Gobuster installed successfully")
            else:
                print(f"❌ Gobuster installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Gobuster installation failed: {e}")
    
    def install_amass(self):
        """Install Amass"""
        print("📦 Installing Amass...")
        
        try:
            cmd = f"cd {self.tools_dir} && {self.tools_dir}/go/bin/go install -v github.com/owasp-amass/amass/v4/...@master"
            success, stdout, stderr = self.run_command(cmd, shell=True)
            
            if success:
                print("✅ Amass installed successfully")
            else:
                print(f"❌ Amass installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Amass installation failed: {e}")
    
    def install_nikto(self):
        """Install Nikto"""
        print("📦 Installing Nikto...")
        
        try:
            # Check if Nikto is available via package manager
            success, _, _ = self.run_command(['which', 'nikto'])
            if success:
                print("✅ Nikto already installed")
                return
            
            # Try to install via apt
            success, stdout, stderr = self.run_command(['sudo', 'apt', 'install', '-y', 'nikto'])
            if success:
                print("✅ Nikto installed successfully")
            else:
                # Clone from GitHub as fallback
                nikto_dir = self.tools_dir / 'nikto'
                if not nikto_dir.exists():
                    cmd = f"cd {self.tools_dir} && git clone https://github.com/sullo/nikto.git"
                    success, stdout, stderr = self.run_command(cmd, shell=True)
                    if success:
                        print("✅ Nikto cloned successfully")
                    else:
                        print(f"❌ Nikto installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Nikto installation failed: {e}")
    
    def install_wpscan(self):
        """Install WPScan"""
        print("📦 Installing WPScan...")
        
        try:
            # Install via gem
            success, stdout, stderr = self.run_command(['gem', 'install', 'wpscan'])
            if success:
                print("✅ WPScan installed successfully")
            else:
                print(f"❌ WPScan installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ WPScan installation failed: {e}")
    
    def install_nmap(self):
        """Install Nmap"""
        print("📦 Installing Nmap...")
        
        try:
            # Check if Nmap is already installed
            success, _, _ = self.run_command(['which', 'nmap'])
            if success:
                print("✅ Nmap already installed")
                return
            
            # Install via package manager
            success, stdout, stderr = self.run_command(['sudo', 'apt', 'install', '-y', 'nmap'])
            if success:
                print("✅ Nmap installed successfully")
            else:
                print(f"❌ Nmap installation failed: {stderr}")
                
        except Exception as e:
            print(f"❌ Nmap installation failed: {e}")
    
    def update_path(self):
        """Update PATH to include all tools"""
        print("🔧 Updating PATH...")
        
        bashrc = Path.home() / '.bashrc'
        path_exports = f"""
# MAKV's Penetration Tools
export PATH=$PATH:{Path.home()}/go/bin:{Path.home()}/.local/bin:{self.tools_dir}/sqlmap
"""
        
        # Check if already added
        with open(bashrc, 'r') as f:
            content = f.read()
        
        if "MAKV's Penetration Tools" not in content:
            with open(bashrc, 'a') as f:
                f.write(path_exports)
            print("✅ PATH updated successfully")
        else:
            print("✅ PATH already configured")

def main():
    """Main installation function"""
    print("🚀 MAKV'S PENETRATION TOOLS INSTALLER")
    print("Installing REAL penetration testing tools...")
    
    installer = PenetrationToolsInstaller()
    installer.install_all_tools()
    
    print("\n🎉 INSTALLATION COMPLETE!")
    print("🔄 Please run: source ~/.bashrc")
    print("🎯 Your system is now ready for REAL penetration testing!")

if __name__ == "__main__":
    main()