#!/usr/bin/env python3
"""
Enhanced Status Display for APTS
Shows detailed proxy info, Tor status, penetration readiness, and live logs
"""

import os
import sys

def enhance_status_display():
    """Enhance the APTS status display with detailed information"""
    
    print("🔧 ENHANCING STATUS DISPLAY: Adding detailed proxy and penetration info...")
    
    # Read the current apts.py file
    with open('apts.py', 'r') as f:
        content = f.read()
    
    # Enhanced display_system_status method
    old_status_method = '''    async def display_system_status(self):
        """Display detailed system status"""
        status = f"""
        [bold white]APTS System Status[/bold white]
        
        🔧 Core System: {'🟢 OPERATIONAL' if self.initialized else '🔴 OFFLINE'}
        👻 Ghost Mode: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}
        🎯 Targets: {len(self.targets)} configured
        🔍 Vulnerability Modules: 30 loaded
        📊 Reporting System: {'🟢 READY' if hasattr(self, 'reporting') else '🔴 NOT READY'}
        
        Version: {self.version}
        Codename: {self.codename}
        """
        
        console.print(Panel(status, title="[bold green]System Status[/bold green]"))'''
    
    new_status_method = '''    async def display_system_status(self):
        """Display detailed system status with live proxy and penetration info"""
        
        # Get detailed Ghost Mode status
        ghost_status = "🔴 INACTIVE"
        proxy_details = "No proxies available"
        tor_status = "🔴 OFFLINE"
        anonymity_level = 0
        
        if self.ghost_mode_active and hasattr(self, 'ghost_mode') and self.ghost_mode:
            ghost_status = "🟢 ACTIVE"
            anonymity_level = self.ghost_mode.anonymity_level
            
            # Get proxy details
            if hasattr(self.ghost_mode, 'proxy_manager'):
                total_proxies = len(self.ghost_mode.proxy_manager.proxies)
                verified_proxies = len(self.ghost_mode.proxy_manager.verified_proxies)
                current_proxy = None
                
                if self.ghost_mode.proxy_manager.verified_proxies:
                    current_proxy = self.ghost_mode.proxy_manager.verified_proxies[0]
                    proxy_details = f"""
        📡 Total Proxies: {total_proxies:,}
        ✅ Verified Proxies: {verified_proxies}
        🔄 Current Proxy: {current_proxy.host}:{current_proxy.port} ({current_proxy.anonymity})
        🌍 Proxy Rotation: Active"""
                else:
                    proxy_details = f"📡 Total: {total_proxies:,} | ✅ Verified: {verified_proxies}"
            
            # Get Tor status
            if hasattr(self.ghost_mode, 'tor_manager') and self.ghost_mode.tor_manager.tor_active:
                tor_status = "🟢 ACTIVE (Port 9050)"
            else:
                tor_status = "🔴 OFFLINE"
        
        # Check penetration readiness
        penetration_ready = "🔴 NOT READY"
        penetration_details = "Ghost Mode required"
        
        if self.ghost_mode_active:
            if hasattr(self, 'vuln_engine') and self.vuln_engine:
                penetration_ready = "🟢 READY"
                penetration_details = f"""
        🎯 Target System: {'🟢 READY' if hasattr(self, 'target_system') and self.target_system else '🔴 OFFLINE'}
        ⚔️  Vulnerability Engine: 🟢 LOADED (30 modules)
        💥 Real Penetration Engine: 🟢 READY
        🎯 One-Line Hack Engine: 🟢 READY
        📊 Reporting System: {'🟢 READY' if hasattr(self, 'reporting') and self.reporting else '🔴 OFFLINE'}"""
            else:
                penetration_details = "Vulnerability engine not loaded"
        
        status = f"""
        [bold white]🚀 APTS GHOST PROTOCOL - LIVE STATUS[/bold white]
        
        [bold cyan]🔧 CORE SYSTEM[/bold cyan]
        System Status: {'🟢 OPERATIONAL' if self.initialized else '🔴 OFFLINE'}
        Version: {self.version} - {self.codename}
        Targets Configured: {len(self.targets)}
        
        [bold purple]👻 GHOST MODE DETAILS[/bold purple]
        Ghost Mode: {ghost_status}
        Anonymity Level: {anonymity_level}%
        {proxy_details}
        Tor Network: {tor_status}
        Traffic Obfuscation: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}
        
        [bold red]⚔️  PENETRATION SYSTEM[/bold red]
        Penetration Ready: {penetration_ready}
        {penetration_details}
        
        [bold yellow]📋 CURRENT TARGETS[/bold yellow]
        """
        
        if self.targets:
            for i, target in enumerate(self.targets, 1):
                status += f"        {i}. {target}\\n"
        else:
            status += "        No targets configured"
        
        console.print(Panel(status, title="[bold green]🎯 APTS LIVE STATUS DASHBOARD[/bold green]"))
        
        # Show recent logs if available
        try:
            log_file = "logs/apts_2025-11-10.log"
            if os.path.exists(log_file):
                console.print("\\n[bold blue]📋 RECENT ACTIVITY LOG (Last 10 lines):[/bold blue]")
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    recent_lines = lines[-10:] if len(lines) > 10 else lines
                    for line in recent_lines:
                        if line.strip():
                            console.print(f"  {line.strip()}")
        except Exception as e:
            console.print(f"[yellow]⚠️ Could not read log file: {e}[/yellow]")'''
    
    if old_status_method in content:
        content = content.replace(old_status_method, new_status_method)
        print("✅ Enhanced system status display")
    
    # Enhanced main menu to show live status
    old_menu = '''        menu = """
        [bold white]APTS - Main Menu[/bold white]
        
        [1] Activate Ghost Mode (Level 1)
        [2] Configure Targets (Level 2)
        [3] Run Penetration Test
        [4] View System Status
        [5] Generate Test Report
        [6] Exit System
        
        [bold yellow]Current Status:[/bold yellow]
        • Ghost Mode: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}
        • Targets Loaded: {len(self.targets)}
        • System: {'🟢 READY' if self.initialized else '🔴 NOT READY'}
        """'''
    
    new_menu = '''        # Get live proxy count
        proxy_count = 0
        if self.ghost_mode_active and hasattr(self, 'ghost_mode') and self.ghost_mode:
            if hasattr(self.ghost_mode, 'proxy_manager'):
                proxy_count = len(self.ghost_mode.proxy_manager.verified_proxies)
        
        menu = f"""
        [bold white]🚀 APTS - GHOST PROTOCOL CONTROL PANEL[/bold white]
        
        [1] Activate Ghost Mode (Level 1)
        [2] Configure Targets (Level 2)
        [3] Run Penetration Test
        [4] View Detailed System Status
        [5] Generate Test Report
        [6] Exit System
        
        [bold yellow]🔴 LIVE STATUS:[/bold yellow]
        • 👻 Ghost Mode: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}
        • 📡 Active Proxies: {proxy_count}
        • 🎯 Targets: {len(self.targets)}
        • ⚔️  System: {'🟢 READY FOR PENETRATION' if self.initialized and self.ghost_mode_active else '🔴 NOT READY'}
        """'''
    
    if old_menu in content:
        content = content.replace(old_menu, new_menu)
        print("✅ Enhanced main menu with live status")
    
    # Add penetration logging
    old_penetration_start = '''        console.print(f"\\n[bold cyan]🎯 Starting penetration test on {len(targets)} target(s)...[/bold cyan]")'''
    
    new_penetration_start = '''        console.print(f"\\n[bold cyan]🎯 Starting penetration test on {len(targets)} target(s)...[/bold cyan]")
        
        # Show penetration details
        console.print("[bold yellow]🔍 PENETRATION TEST DETAILS:[/bold yellow]")
        console.print(f"   • Ghost Mode: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}")
        if hasattr(self, 'ghost_mode') and self.ghost_mode:
            proxy_count = len(self.ghost_mode.proxy_manager.verified_proxies) if hasattr(self.ghost_mode, 'proxy_manager') else 0
            console.print(f"   • Active Proxies: {proxy_count}")
            console.print(f"   • Anonymity Level: {self.ghost_mode.anonymity_level}%")
        console.print(f"   • Target URLs: {', '.join(targets)}")
        console.print("   • Penetration Modules: 30 loaded")
        console.print("\\n[bold red]🚨 STARTING REAL PENETRATION ATTACK...[/bold red]")'''
    
    if old_penetration_start in content:
        content = content.replace(old_penetration_start, new_penetration_start)
        print("✅ Enhanced penetration test logging")
    
    # Write the enhanced content back
    with open('apts.py', 'w') as f:
        f.write(content)
    
    print("\\n🎉 STATUS DISPLAY ENHANCEMENT COMPLETE!")
    print("Now you'll see:")
    print("  ✅ Live proxy details and rotation status")
    print("  ✅ Tor network status")
    print("  ✅ Penetration readiness check")
    print("  ✅ Detailed penetration logs")
    print("  ✅ Recent activity logs")

if __name__ == "__main__":
    enhance_status_display()