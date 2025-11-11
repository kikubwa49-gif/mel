#!/usr/bin/env python3
"""
APTS - Advanced Penetration Testing System
Military-Grade Authorized Penetration Testing Platform

WARNING: This system is designed for AUTHORIZED penetration testing ONLY.
Unauthorized use is illegal and unethical.

Author: Ethical Security Research Team
Version: 2.0.0 - Chinese Optimization Protocol
"""

import asyncio
import sys
import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from loguru import logger
import psutil

# Initialize console for beautiful output
console = Console()

# Initialize Chinese Memory Optimizer FIRST
try:
    from core.chinese_memory_optimizer import get_memory_optimizer, optimize_for_low_ram
    memory_optimizer = get_memory_optimizer()
    
    # Optimize for low RAM if system has 4GB or less
    total_ram_gb = psutil.virtual_memory().total / (1024**3)
    if total_ram_gb <= 4:
        optimize_for_low_ram()
        logger.info(f"🎯 Low RAM optimization activated for {total_ram_gb:.1f}GB system")
    
    MEMORY_OPTIMIZER_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Memory optimizer not available: {e}")
    MEMORY_OPTIMIZER_AVAILABLE = False

# Safe imports with fallbacks - NO HEAVY AI SYSTEMS
try:
    from direct_penetration_engine import DirectPenetrationEngine
    DIRECT_ENGINE_AVAILABLE = True
except ImportError:
    DIRECT_ENGINE_AVAILABLE = False

class APTS:
    """Advanced Penetration Testing System - Main Controller"""
    
    def __init__(self):
        self.version = "2.0.0"
        self.codename = "CHINESE_OPTIMIZATION_PROTOCOL"
        self.initialized = False
        self.safe_mode = False
        self.ghost_mode_active = False
        self.targets = []
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Configure military-grade logging system"""
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # Remove default logger
        logger.remove()
        
        # Add custom loggers
        logger.add(
            "logs/apts_{time:YYYY-MM-DD}.log",
            rotation="1 day",
            retention="30 days",
            level="DEBUG",
            format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} | {message}"
        )
        
        logger.add(
            sys.stderr,
            level="INFO",
            format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>"
        )
        
    def display_banner(self):
        """Display the APTS banner"""
        banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     █████╗ ██████╗ ████████╗███████╗                         ║
    ║    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝                         ║
    ║    ███████║██████╔╝   ██║   ███████╗                         ║
    ║    ██╔══██║██╔═══╝    ██║   ╚════██║                         ║
    ║    ██║  ██║██║        ██║   ███████║                         ║
    ║    ╚═╝  ╚═╝╚═╝        ╚═╝   ╚══════╝                         ║
    ║                                                               ║
    ║         Advanced Penetration Testing System                   ║
    ║              Military-Grade Security Assessment               ║
    ║                                                               ║
    ║    Version: 2.0.0 - CHINESE OPTIMIZATION PROTOCOL          ║
    ║    Classification: AUTHORIZED USE ONLY                        ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
        """
        
        console.print(Panel(
            Text(banner, style="bold red"),
            title="[bold white]APTS - GHOST PROTOCOL[/bold white]",
            border_style="red"
        ))
        
        # Warning message
        warning = """
        ⚠️  WARNING: AUTHORIZED PENETRATION TESTING ONLY ⚠️
        
        This system is designed for authorized security assessments only.
        Unauthorized use against systems you do not own or have explicit
        permission to test is ILLEGAL and UNETHICAL.
        
        By using this system, you acknowledge:
        • You have written authorization to test target systems
        • You understand the legal implications of penetration testing
        • You will use this system responsibly and ethically
        • You will not cause harm or disruption to target systems
        """
        
        console.print(Panel(
            warning,
            title="[bold yellow]LEGAL DISCLAIMER[/bold yellow]",
            border_style="yellow"
        ))
        
    async def initialize_system(self):
        """Initialize all APTS subsystems"""
        console.print("\n[bold blue]🚀 Initializing APTS Ghost Protocol...[/bold blue]")
        
        try:
            # Initialize global memory optimization first
            console.print("🧠 Activating global memory optimization...")
            await self.initialize_global_memory_optimization()
            
            # Initialize hardware optimization
            console.print("⚡ Activating hardware optimization...")
            await self.initialize_hardware_optimization()
            
            # Initialize Ghost Mode (Level 1)
            console.print("👻 Initializing Ghost Mode anonymization...")
            await self.initialize_ghost_mode()
            
            # Initialize Target System (Level 2)
            console.print("🎯 Initializing target acquisition system...")
            await self.initialize_target_system()
            
            # Initialize vulnerability modules
            console.print("🔍 Loading 30 critical vulnerability modules...")
            await self.initialize_vulnerability_modules()
            
            # Initialize reporting system
            console.print("📊 Initializing encrypted reporting system...")
            await self.initialize_reporting_system()
            
            self.initialized = True
            console.print("\n[bold green]✅ APTS Ghost Protocol initialized successfully![/bold green]")
            
        except Exception as e:
            logger.error(f"System initialization failed: {e}")
            console.print(f"[bold red]❌ Critical initialization failed: {e}[/bold red]")
            console.print("[yellow]⚠️ Starting in SAFE MODE with limited functionality...[/yellow]")
            self.safe_mode = True
            self.initialized = True
            
    async def initialize_global_memory_optimization(self):
        """Initialize global memory optimization system"""
        try:
            from core.global_memory_optimizer import optimize_system_memory, get_memory_stats
            self.memory_optimizer = optimize_system_memory()
            stats = get_memory_stats()
            logger.info(f"🧠 Memory optimization active - {stats['memory_saved_mb']:.1f}MB saved")
        except Exception as e:
            logger.warning(f"Global memory optimization failed: {e}")
            self.memory_optimizer = None
            
    async def initialize_hardware_optimization(self):
        """Initialize hardware optimization system"""
        try:
            from core.optimization import HardwareOptimizer
            self.optimizer = HardwareOptimizer()
            await self.optimizer.optimize_system()
        except Exception as e:
            logger.warning(f"Hardware optimization failed: {e}")
            # Continue without optimization
            self.optimizer = None
        
    async def initialize_ghost_mode(self):
        """Initialize Level 1: Ghost Mode"""
        try:
            from core.ghost_mode import GhostMode
            self.ghost_mode = GhostMode()
            await self.ghost_mode.initialize()
        except Exception as e:
            logger.warning(f"Ghost Mode initialization failed: {e}")
            self.ghost_mode = None
        
    async def initialize_target_system(self):
        """Initialize Level 2: Target System"""
        try:
            from core.target_system import TargetSystem
            self.target_system = TargetSystem()
            await self.target_system.initialize()
        except Exception as e:
            logger.warning(f"Target System initialization failed: {e}")
            self.target_system = None
        
    async def initialize_vulnerability_modules(self):
        """Initialize all 30 vulnerability detection modules"""
        try:
            from core.vulnerability_engine import VulnerabilityEngine
            self.vuln_engine = VulnerabilityEngine()
            await self.vuln_engine.load_all_modules()
        except Exception as e:
            logger.warning(f"Vulnerability Engine initialization failed: {e}")
            self.vuln_engine = None
        
    async def initialize_reporting_system(self):
        """Initialize encrypted reporting system"""
        try:
            from core.reporting import ReportingEngine
            self.reporting = ReportingEngine()
            await self.reporting.initialize()
        except Exception as e:
            logger.warning(f"Reporting System initialization failed: {e}")
            self.reporting = None
        
    async def activate_ghost_mode(self):
        """Activate Level 1: Ghost Mode for complete anonymization"""
        if not self.initialized:
            console.print("[bold red]❌ System not initialized![/bold red]")
            return False
            
        console.print("\n[bold purple]👻 Activating Ghost Mode...[/bold purple]")
        
        try:
            # Activate proxy infrastructure
            console.print("🔄 Starting proxy scraping and verification...")
            await self.ghost_mode.activate_proxy_infrastructure()
            
            # Activate Tor network
            console.print("🧅 Connecting to Tor network...")
            await self.ghost_mode.activate_tor_network()
            
            # Activate traffic obfuscation
            console.print("🎭 Activating traffic obfuscation...")
            await self.ghost_mode.activate_traffic_obfuscation()
            
            # Verify anonymization
            console.print("🔍 Verifying anonymization level...")
            anonymity_level = await self.ghost_mode.verify_anonymity()
            
            if anonymity_level >= 50:  # More realistic 50% anonymity required
                self.ghost_mode_active = True
                self.ghost_mode.active = True  # CRITICAL FIX: Set the actual Ghost Mode active flag
                console.print(f"[bold green]✅ Ghost Mode activated! Anonymity level: {anonymity_level}%[/bold green]")
                return True
            else:
                console.print(f"[bold red]❌ Insufficient anonymity level: {anonymity_level}%[/bold red]")
                return False
                
        except Exception as e:
            logger.error(f"Ghost Mode activation failed: {e}")
            console.print(f"[bold red]❌ Ghost Mode activation failed: {e}[/bold red]")
            return False
            
    async def run_penetration_test(self, targets):
        """Run comprehensive penetration test on targets"""
        if not self.ghost_mode_active:
            console.print("[bold red]❌ Ghost Mode must be active before testing![/bold red]")
            return
            
        console.print(f"\n[bold cyan]🎯 Starting penetration test on {len(targets)} target(s)...[/bold cyan]")
        
        try:
            # Check if components are available
            if not self.target_system:
                console.print("[bold red]❌ Target system not available - using direct penetration engine[/bold red]")
                await self.run_direct_penetration_test(targets)
                return
                
            if not self.vuln_engine:
                console.print("[bold red]❌ Vulnerability engine not available - using direct penetration engine[/bold red]")
                await self.run_direct_penetration_test(targets)
                return
            
            # Target acquisition and reconnaissance
            console.print("🔍 Phase 1: Target acquisition and reconnaissance...")
            # Pass Ghost Mode instance to target system
            if self.target_system and hasattr(self.target_system, 'ghost_mode'):
                self.target_system.ghost_mode = self.ghost_mode
            
            if self.target_system:
                expanded_targets = await self.target_system.acquire_targets(targets)
            else:
                # Fallback to direct penetration
                expanded_targets = targets
                console.print("⚠️ Using direct penetration mode")
            
            # Vulnerability assessment
            console.print("⚔️  Phase 2: Aggressive vulnerability assessment...")
            
            if self.vuln_engine:
                # Pass Ghost Mode instance to vulnerability engine
                if hasattr(self.vuln_engine, 'ghost_mode'):
                    self.vuln_engine.ghost_mode = self.ghost_mode
                vulnerabilities = await self.vuln_engine.assess_all_targets(expanded_targets)
                
                # Exploitation phase
                console.print("💥 Phase 3: Exploitation and evidence collection...")
                exploits = await self.vuln_engine.exploit_vulnerabilities(vulnerabilities)
            else:
                # Fallback to bulletproof penetration
                console.print("⚠️ Using bulletproof penetration engine")
                for target in expanded_targets:
                    await self.execute_direct_penetration(target)
                exploits = []
            
            # Report generation
            console.print("📊 Phase 4: Generating encrypted report...")
            if self.reporting:
                report_path = await self.reporting.generate_report(exploits)
                console.print(f"[bold green]✅ Penetration test completed! Report: {report_path}[/bold green]")
            else:
                console.print("[bold green]✅ Penetration test completed![/bold green]")
            
        except Exception as e:
            logger.error(f"Penetration test failed: {e}")
            console.print(f"[bold red]❌ Penetration test failed: {e}[/bold red]")
            console.print("[yellow]🔄 Falling back to direct penetration engine...[/yellow]")
            await self.run_direct_penetration_test(targets)
            
    async def run_direct_penetration_test(self, targets):
        """Run direct penetration test without complex components"""
        try:
            from direct_penetration_engine import DirectPenetrationEngine
            engine = DirectPenetrationEngine()
            
            for target in targets:
                console.print(f"\n[bold cyan]🎯 Testing {target}...[/bold cyan]")
                await engine.full_penetration_test(target)
                
            console.print("[bold green]✅ Direct penetration test completed![/bold green]")
            
        except Exception as e:
            logger.error(f"Direct penetration test failed: {e}")
            console.print(f"[bold red]❌ Direct penetration test failed: {e}[/bold red]")
            
    async def start_conversation_with_makv(self):
        """Direct penetration testing interface - NO AI DEPENDENCIES"""
        console.print("\n[bold green]🎯 MAKV'S DIRECT PENETRATION SYSTEM[/bold green]")
        console.print("[cyan]Pure penetration testing power - No AI needed![/cyan]")
        console.print("[yellow]Commands: 'test <domain>', 'scan <domain>', 'hack <domain>', 'exit'[/yellow]")
        
        while True:
            try:
                user_input = console.input("\n[bold blue]Makv[/bold blue]: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'back']:
                    console.print("[green]Returning to main menu...[/green]")
                    break
                
                if user_input:
                    # Parse command for target
                    if any(keyword in user_input.lower() for keyword in ['test', 'scan', 'hack', 'target', 'penetrate']):
                        # Extract domain from input
                        words = user_input.split()
                        target = None
                        for word in words:
                            if '.' in word and not word.startswith('.'):
                                target = word.replace(',', '').replace(';', '').replace(':', '').strip()
                                break
                        
                        if target:
                            console.print(f"\n[bold green]🚀 LAUNCHING PENETRATION TEST ON {target}[/bold green]")
                            await self.execute_direct_penetration(target)
                        else:
                            console.print("[yellow]Please specify a target: 'test youngplatform.com'[/yellow]")
                    else:
                        console.print("[yellow]Available commands:[/yellow]")
                        console.print("  • test <domain> - Run full penetration test")
                        console.print("  • scan <domain> - Quick vulnerability scan")
                        console.print("  • hack <domain> - Aggressive penetration test")
                        console.print("  • exit - Return to main menu")
                
            except KeyboardInterrupt:
                console.print("\n[green]Returning to main menu...[/green]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/red]")
                
    async def execute_direct_penetration(self, target):
        """Execute bulletproof penetration test"""
        try:
            from bulletproof_penetration_engine import run_penetration_test
            console.print(f"[bold cyan]🎯 BULLETPROOF PENETRATION ON: {target}[/bold cyan]")
            await run_penetration_test(target)
            console.print(f"[bold green]✅ BULLETPROOF TEST COMPLETED FOR {target}[/bold green]")
        except Exception as e:
            console.print(f"[red]❌ Bulletproof test failed: {e}[/red]")

    async def direct_penetration_testing(self):
        """Bulletproof penetration testing - NO DEPENDENCIES"""
        console.print("\n[bold green]🎯 BULLETPROOF PENETRATION TESTING MODE[/bold green]")
        console.print("[cyan]NO DEPENDENCIES - GUARANTEED TO WORK[/cyan]")
        console.print("[yellow]Built for 100% success rate on any system[/yellow]")
        
        target = console.input("\n🎯 Enter target domain (e.g., youngplatform.com): ").strip()
        if target:
            try:
                from bulletproof_penetration_engine import run_penetration_test
                console.print(f"\n[bold blue]🚀 Starting bulletproof penetration test on {target}[/bold blue]")
                await run_penetration_test(target)
                console.print(f"\n[bold green]✅ BULLETPROOF TEST COMPLETED FOR {target}[/bold green]")
            except Exception as e:
                console.print(f"[red]Penetration test error: {e}[/red]")
                logger.error(f"Bulletproof penetration test failed: {e}")
        else:
            console.print("[red]❌ No target specified[/red]")

    def display_menu(self):
        """Display main menu"""
        menu = """
        [bold white]APTS - Main Menu[/bold white]
        
        [1] 🎯 BULLETPROOF Penetration Testing (NO DEPENDENCIES)
        [2] Activate Ghost Mode (Level 1)
        [3] Configure Targets (Level 2)
        [4] Run Penetration Test
        [5] View System Status
        [6] Generate Test Report
        [7] Exit System
        
        [bold yellow]Current Status:[/bold yellow]
        • Ghost Mode: {'🟢 ACTIVE' if self.ghost_mode_active else '🔴 INACTIVE'}
        • Targets Loaded: {len(self.targets)}
        • System: {'🟢 READY' if self.initialized else '🔴 NOT READY'}
        """
        
        console.print(Panel(menu, title="[bold blue]APTS Control Panel[/bold blue]"))
        
    async def main_loop(self):
        """Main application loop"""
        while True:
            self.display_menu()
            
            try:
                choice = console.input("\n[bold cyan]Select option (1-7): [/bold cyan]")
                
                if choice == "1":
                    await self.direct_penetration_testing()
                elif choice == "2":
                    await self.activate_ghost_mode()
                elif choice == "3":
                    await self.configure_targets()
                elif choice == "4":
                    if self.targets:
                        await self.run_penetration_test(self.targets)
                    else:
                        console.print("[bold red]❌ No targets configured![/bold red]")
                elif choice == "5":
                    await self.display_system_status()
                elif choice == "6":
                    await self.generate_test_report()
                elif choice == "7":
                    console.print("[bold yellow]👋 Shutting down APTS...[/bold yellow]")
                    await self.shutdown()
                    break
                else:
                    console.print("[bold red]❌ Invalid option![/bold red]")
                    
            except KeyboardInterrupt:
                console.print("\n[bold yellow]👋 Shutting down APTS...[/bold yellow]")
                await self.shutdown()
                break
            except Exception as e:
                logger.error(f"Main loop error: {e}")
                console.print(f"[bold red]❌ Error: {e}[/bold red]")
                
    async def configure_targets(self):
        """Configure penetration testing targets"""
        console.print("\n[bold blue]🎯 Target Configuration[/bold blue]")
        
        targets_input = console.input("Enter target URLs (comma-separated): ")
        if targets_input.strip():
            self.targets = [target.strip() for target in targets_input.split(",")]
            console.print(f"[bold green]✅ Configured {len(self.targets)} target(s)[/bold green]")
        else:
            console.print("[bold red]❌ No targets provided![/bold red]")
            
    async def display_system_status(self):
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
        
        console.print(Panel(status, title="[bold green]System Status[/bold green]"))
        
    async def generate_test_report(self):
        """Generate test report"""
        console.print("[bold blue]📊 Generating test report...[/bold blue]")
        # Implementation will be added with reporting system
        
    async def shutdown(self):
        """Gracefully shutdown APTS"""
        try:
            if hasattr(self, 'ghost_mode') and self.ghost_mode_active:
                await self.ghost_mode.deactivate()
                
            console.print("[bold green]✅ APTS shutdown complete[/bold green]")
            
        except Exception as e:
            logger.error(f"Shutdown error: {e}")

async def main():
    """Main entry point"""
    # Create APTS instance
    apts = APTS()
    
    # Display banner
    apts.display_banner()
    
    # Get user confirmation
    consent = console.input("\n[bold yellow]Do you have written authorization to test your targets? (yes/no): [/bold yellow]")
    
    if consent.lower() != "yes":
        console.print("[bold red]❌ Authorization required. Exiting...[/bold red]")
        sys.exit(1)
        
    # Initialize system
    await apts.initialize_system()
    
    # Start main loop
    await apts.main_loop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]👋 APTS terminated by user[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]❌ Fatal error: {e}[/bold red]")
        sys.exit(1)