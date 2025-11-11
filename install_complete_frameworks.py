#!/usr/bin/env python3
"""
COMPLETE PENETRATION FRAMEWORKS INSTALLER
Installs nation-state level penetration testing frameworks
"""

import subprocess
import os
import sys
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import time

console = Console()

class CompleteFrameworksInstaller:
    """Installer for complete penetration testing frameworks"""
    
    def __init__(self):
        self.frameworks = {
            'metasploit': {
                'name': 'Metasploit Framework',
                'description': 'World\'s most used penetration testing framework',
                'commands': [
                    'curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > /tmp/msfinstall',
                    'chmod 755 /tmp/msfinstall',
                    'sudo /tmp/msfinstall'
                ]
            },
            'empire': {
                'name': 'Empire Framework',
                'description': 'Post-exploitation framework',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y git python3-pip',
                    'git clone --recursive https://github.com/EmpireProject/Empire.git /tmp/Empire',
                    'cd /tmp/Empire && sudo ./setup/install.sh'
                ]
            },
            'beef': {
                'name': 'BeEF Framework',
                'description': 'Browser Exploitation Framework',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y git ruby ruby-dev bundler',
                    'git clone https://github.com/beefproject/beef /opt/beef',
                    'cd /opt/beef && sudo bundle install'
                ]
            },
            'set': {
                'name': 'Social Engineer Toolkit',
                'description': 'Social engineering penetration testing framework',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y git python3-pip',
                    'git clone https://github.com/trustedsec/social-engineer-toolkit/ /opt/set/',
                    'cd /opt/set && sudo pip3 install -r requirements.txt',
                    'cd /opt/set && sudo python3 setup.py install'
                ]
            },
            'zaproxy': {
                'name': 'OWASP ZAP',
                'description': 'Web application security scanner',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y wget gnupg',
                    'wget -q -O - https://download.opensuse.org/repositories/home:cabelo/xUbuntu_20.04/Release.key | sudo apt-key add -',
                    'echo "deb http://download.opensuse.org/repositories/home:/cabelo/xUbuntu_20.04/ ./" | sudo tee /etc/apt/sources.list.d/home:cabelo.list',
                    'sudo apt update',
                    'sudo apt install -y zaproxy'
                ]
            },
            'openvas': {
                'name': 'OpenVAS',
                'description': 'Vulnerability assessment system',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y openvas',
                    'sudo gvm-setup',
                    'sudo gvm-check-setup'
                ]
            },
            'nmap': {
                'name': 'Nmap Security Scanner',
                'description': 'Network discovery and security auditing',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y nmap nmap-common'
                ]
            },
            'sqlmap': {
                'name': 'SQLMap',
                'description': 'Automatic SQL injection tool',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y sqlmap'
                ]
            },
            'nikto': {
                'name': 'Nikto',
                'description': 'Web server scanner',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y nikto'
                ]
            },
            'wpscan': {
                'name': 'WPScan',
                'description': 'WordPress security scanner',
                'commands': [
                    'sudo apt update',
                    'sudo apt install -y ruby ruby-dev',
                    'sudo gem install wpscan'
                ]
            }
        }
        
    def display_banner(self):
        """Display installer banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ███████╗██████╗  █████╗ ███╗   ███╗███████╗██╗    ██╗    ║
║    ██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██║    ██║    ║
║    █████╗  ██████╔╝███████║██╔████╔██║█████╗  ██║ █╗ ██║    ║
║    ██╔══╝  ██╔══██╗██╔══██║██║╚██╔╝██║██╔══╝  ██║███╗██║    ║
║    ██║     ██║  ██║██║  ██║██║ ╚═╝ ██║███████╗╚███╔███╔╝    ║
║    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝ ╚══╝╚══╝     ║
║                                                              ║
║         COMPLETE FRAMEWORKS INSTALLER                        ║
║           Nation-State Level Capabilities                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        console.print(banner, style="bold red")
        
    def install_framework(self, framework_key):
        """Install a specific framework"""
        framework = self.frameworks[framework_key]
        
        console.print(f"\n[bold green]📦 Installing {framework['name']}...[/bold green]")
        console.print(f"[bold yellow]Description: {framework['description']}[/bold yellow]")
        
        for i, command in enumerate(framework['commands'], 1):
            console.print(f"\n[bold cyan]Step {i}/{len(framework['commands'])}: {command}[/bold cyan]")
            
            try:
                result = subprocess.run(
                    command, 
                    shell=True, 
                    capture_output=True, 
                    text=True, 
                    timeout=600
                )
                
                if result.returncode == 0:
                    console.print(f"[bold green]✅ Step {i} completed successfully[/bold green]")
                else:
                    console.print(f"[bold red]❌ Step {i} failed: {result.stderr}[/bold red]")
                    return False
                    
            except subprocess.TimeoutExpired:
                console.print(f"[bold red]❌ Step {i} timed out[/bold red]")
                return False
            except Exception as e:
                console.print(f"[bold red]❌ Step {i} failed: {e}[/bold red]")
                return False
                
        console.print(f"[bold green]🎉 {framework['name']} installed successfully![/bold green]")
        return True
        
    def install_all_frameworks(self):
        """Install all frameworks"""
        console.print("\n[bold red]🚀 INSTALLING ALL PENETRATION FRAMEWORKS[/bold red]")
        console.print("[bold yellow]This will install nation-state level capabilities...[/bold yellow]")
        console.print("[bold yellow]⚠️ This process may take 30-60 minutes[/bold yellow]")
        
        confirm = console.input("\n[bold cyan]Continue with full installation? (y/N): [/bold cyan]")
        
        if confirm.lower() not in ['y', 'yes']:
            console.print("[bold yellow]Installation cancelled.[/bold yellow]")
            return
            
        success_count = 0
        total_count = len(self.frameworks)
        
        for framework_key in self.frameworks:
            if self.install_framework(framework_key):
                success_count += 1
                
        console.print(f"\n[bold green]🎉 INSTALLATION COMPLETED![/bold green]")
        console.print(f"[bold yellow]Successfully installed: {success_count}/{total_count} frameworks[/bold yellow]")
        
        if success_count == total_count:
            console.print("[bold green]🚀 ALL FRAMEWORKS INSTALLED SUCCESSFULLY![/bold green]")
            console.print("[bold green]Your system now has nation-state level capabilities![/bold green]")
        else:
            console.print(f"[bold yellow]⚠️ {total_count - success_count} frameworks failed to install[/bold yellow]")
            console.print("[bold yellow]Check the error messages above for details[/bold yellow]")
            
    def install_essential_only(self):
        """Install only essential frameworks"""
        essential = ['metasploit', 'nmap', 'sqlmap', 'nikto', 'wpscan']
        
        console.print("\n[bold green]📦 Installing essential frameworks only...[/bold green]")
        
        success_count = 0
        for framework_key in essential:
            if self.install_framework(framework_key):
                success_count += 1
                
        console.print(f"\n[bold green]🎉 Essential frameworks installation completed![/bold green]")
        console.print(f"[bold yellow]Successfully installed: {success_count}/{len(essential)} frameworks[/bold yellow]")
        
    def check_system_requirements(self):
        """Check system requirements"""
        console.print("\n[bold yellow]🔍 Checking system requirements...[/bold yellow]")
        
        # Check if running as root or with sudo access
        if os.geteuid() != 0:
            console.print("[bold red]❌ This installer requires root privileges[/bold red]")
            console.print("[bold yellow]Please run with: sudo python3 install_complete_frameworks.py[/bold yellow]")
            return False
            
        # Check available disk space (need at least 5GB)
        try:
            statvfs = os.statvfs('/')
            free_space_gb = (statvfs.f_frsize * statvfs.f_bavail) / (1024**3)
            
            if free_space_gb < 5:
                console.print(f"[bold red]❌ Insufficient disk space: {free_space_gb:.1f}GB available, need 5GB+[/bold red]")
                return False
            else:
                console.print(f"[bold green]✅ Disk space: {free_space_gb:.1f}GB available[/bold green]")
                
        except Exception as e:
            console.print(f"[bold yellow]⚠️ Could not check disk space: {e}[/bold yellow]")
            
        # Check internet connection
        try:
            result = subprocess.run(['ping', '-c', '1', 'google.com'], 
                                  capture_output=True, timeout=10)
            if result.returncode == 0:
                console.print("[bold green]✅ Internet connection: Available[/bold green]")
            else:
                console.print("[bold red]❌ Internet connection: Not available[/bold red]")
                return False
        except Exception as e:
            console.print(f"[bold red]❌ Internet connection check failed: {e}[/bold red]")
            return False
            
        console.print("[bold green]✅ System requirements check passed![/bold green]")
        return True

def main():
    """Main entry point"""
    installer = CompleteFrameworksInstaller()
    installer.display_banner()
    
    # Check system requirements
    if not installer.check_system_requirements():
        console.print("\n[bold red]❌ System requirements not met. Exiting.[/bold red]")
        sys.exit(1)
        
    while True:
        console.print("\n" + "="*60)
        console.print("[bold white]COMPLETE FRAMEWORKS INSTALLER - MAIN MENU[/bold white]")
        console.print("="*60)
        console.print("[bold green][1][/bold green] Install ALL Frameworks (Full Nation-State Capabilities)")
        console.print("[bold green][2][/bold green] Install Essential Frameworks Only")
        console.print("[bold green][3][/bold green] Install Individual Framework")
        console.print("[bold green][4][/bold green] List Available Frameworks")
        console.print("[bold green][5][/bold green] Exit")
        
        choice = console.input("\n[bold cyan]Select option (1-5): [/bold cyan]")
        
        if choice == "1":
            installer.install_all_frameworks()
        elif choice == "2":
            installer.install_essential_only()
        elif choice == "3":
            console.print("\n[bold yellow]Available frameworks:[/bold yellow]")
            for i, (key, framework) in enumerate(installer.frameworks.items(), 1):
                console.print(f"[bold green][{i}][/bold green] {framework['name']}")
                
            try:
                framework_choice = int(console.input("\n[bold cyan]Select framework number: [/bold cyan]"))
                framework_keys = list(installer.frameworks.keys())
                
                if 1 <= framework_choice <= len(framework_keys):
                    installer.install_framework(framework_keys[framework_choice - 1])
                else:
                    console.print("[bold red]❌ Invalid framework number![/bold red]")
            except ValueError:
                console.print("[bold red]❌ Please enter a valid number![/bold red]")
                
        elif choice == "4":
            console.print("\n[bold yellow]Available Frameworks:[/bold yellow]")
            for key, framework in installer.frameworks.items():
                console.print(f"[bold green]• {framework['name']}[/bold green] - {framework['description']}")
                
        elif choice == "5":
            console.print("[bold green]👋 Exiting installer...[/bold green]")
            break
        else:
            console.print("[bold red]❌ Invalid option![/bold red]")

if __name__ == "__main__":
    main()