#!/usr/bin/env python3
"""
DIRECT PENETRATION ENGINE - NO AI DEPENDENCIES
Lightweight, fast, direct penetration testing without heavy AI models
Built for immediate results and reliable performance
"""

import asyncio
import aiohttp
import requests
import socket
import ssl
import subprocess
import json
import time
import re
from urllib.parse import urljoin, urlparse
from datetime import datetime
import dns.resolver
import whois
from bs4 import BeautifulSoup
import concurrent.futures
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class DirectPenetrationEngine:
    """Direct penetration testing engine - no AI required"""
    
    def __init__(self):
        self.target = None
        self.results = {
            'vulnerabilities': [],
            'open_ports': [],
            'subdomains': [],
            'technologies': [],
            'security_headers': {},
            'ssl_info': {},
            'whois_info': {},
            'endpoints': []
        }
        
    async def full_penetration_test(self, target):
        """Run complete penetration test suite"""
        self.target = target
        console.print(f"\n🎯 [bold red]STARTING PENETRATION TEST ON {target}[/bold red]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            
            # Phase 1: Reconnaissance
            task1 = progress.add_task("🔍 Reconnaissance & Information Gathering", total=None)
            await self.reconnaissance_phase()
            progress.update(task1, completed=True)
            
            # Phase 2: Vulnerability Scanning
            task2 = progress.add_task("🛡️ Vulnerability Detection", total=None)
            await self.vulnerability_scanning_phase()
            progress.update(task2, completed=True)
            
            # Phase 3: Exploitation Testing
            task3 = progress.add_task("⚡ Exploitation Testing", total=None)
            await self.exploitation_phase()
            progress.update(task3, completed=True)
            
        # Generate report
        self.generate_penetration_report()
        
    async def reconnaissance_phase(self):
        """Phase 1: Information gathering"""
        console.print("\n[bold yellow]🔍 RECONNAISSANCE PHASE[/bold yellow]")
        
        # DNS enumeration
        await self.dns_enumeration()
        
        # WHOIS lookup
        await self.whois_lookup()
        
        # Subdomain discovery
        await self.subdomain_discovery()
        
        # Port scanning
        await self.port_scanning()
        
        # Technology detection
        await self.technology_detection()
        
    async def vulnerability_scanning_phase(self):
        """Phase 2: Vulnerability detection"""
        console.print("\n[bold red]🛡️ VULNERABILITY SCANNING PHASE[/bold red]")
        
        # SSL/TLS analysis
        await self.ssl_analysis()
        
        # Security headers check
        await self.security_headers_check()
        
        # Directory enumeration
        await self.directory_enumeration()
        
        # SQL injection testing
        await self.sql_injection_testing()
        
        # XSS testing
        await self.xss_testing()
        
        # Authentication testing
        await self.authentication_testing()
        
    async def exploitation_phase(self):
        """Phase 3: Exploitation attempts"""
        console.print("\n[bold magenta]⚡ EXPLOITATION PHASE[/bold magenta]")
        
        # Admin panel discovery
        await self.admin_panel_discovery()
        
        # API endpoint testing
        await self.api_endpoint_testing()
        
        # File upload testing
        await self.file_upload_testing()
        
        # Business logic testing
        await self.business_logic_testing()
        
    async def dns_enumeration(self):
        """DNS enumeration and analysis"""
        try:
            console.print("📡 DNS Enumeration...")
            
            # A records
            try:
                answers = dns.resolver.resolve(self.target, 'A')
                for answer in answers:
                    console.print(f"   A: {answer}")
            except:
                pass
                
            # MX records
            try:
                answers = dns.resolver.resolve(self.target, 'MX')
                for answer in answers:
                    console.print(f"   MX: {answer}")
            except:
                pass
                
            # NS records
            try:
                answers = dns.resolver.resolve(self.target, 'NS')
                for answer in answers:
                    console.print(f"   NS: {answer}")
            except:
                pass
                
        except Exception as e:
            console.print(f"   [red]DNS enumeration failed: {e}[/red]")
            
    async def whois_lookup(self):
        """WHOIS information gathering"""
        try:
            console.print("🔍 WHOIS Lookup...")
            w = whois.whois(self.target)
            self.results['whois_info'] = {
                'registrar': str(w.registrar) if w.registrar else 'Unknown',
                'creation_date': str(w.creation_date) if w.creation_date else 'Unknown',
                'expiration_date': str(w.expiration_date) if w.expiration_date else 'Unknown',
                'name_servers': w.name_servers if w.name_servers else []
            }
            console.print(f"   Registrar: {self.results['whois_info']['registrar']}")
            console.print(f"   Created: {self.results['whois_info']['creation_date']}")
            
        except Exception as e:
            console.print(f"   [red]WHOIS lookup failed: {e}[/red]")
            
    async def subdomain_discovery(self):
        """Subdomain enumeration"""
        console.print("🌐 Subdomain Discovery...")
        
        common_subdomains = [
            'www', 'mail', 'ftp', 'admin', 'api', 'dev', 'test', 'staging',
            'blog', 'shop', 'app', 'mobile', 'secure', 'vpn', 'portal',
            'dashboard', 'panel', 'control', 'manage', 'support'
        ]
        
        found_subdomains = []
        
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
            tasks = []
            for subdomain in common_subdomains:
                full_domain = f"{subdomain}.{self.target}"
                tasks.append(self.check_subdomain(session, full_domain))
                
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            for i, result in enumerate(results):
                if result and not isinstance(result, Exception):
                    found_subdomains.append(common_subdomains[i])
                    console.print(f"   ✅ Found: {common_subdomains[i]}.{self.target}")
                    
        self.results['subdomains'] = found_subdomains
        
    async def check_subdomain(self, session, domain):
        """Check if subdomain exists"""
        try:
            async with session.get(f"http://{domain}", allow_redirects=False) as response:
                return True
        except:
            try:
                async with session.get(f"https://{domain}", allow_redirects=False) as response:
                    return True
            except:
                return False
                
    async def port_scanning(self):
        """Port scanning for common services"""
        console.print("🔌 Port Scanning...")
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3389, 5432, 3306, 1433, 6379, 27017]
        open_ports = []
        
        def scan_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.target, port))
                sock.close()
                return port if result == 0 else None
            except:
                return None
                
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            futures = [executor.submit(scan_port, port) for port in common_ports]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    open_ports.append(result)
                    console.print(f"   ✅ Port {result} OPEN")
                    
        self.results['open_ports'] = open_ports
        
    async def technology_detection(self):
        """Detect web technologies"""
        console.print("🔧 Technology Detection...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://{self.target}") as response:
                    headers = dict(response.headers)
                    content = await response.text()
                    
                    technologies = []
                    
                    # Server detection
                    if 'server' in headers:
                        technologies.append(f"Server: {headers['server']}")
                        console.print(f"   Server: {headers['server']}")
                        
                    # Framework detection
                    if 'x-powered-by' in headers:
                        technologies.append(f"Powered by: {headers['x-powered-by']}")
                        console.print(f"   Powered by: {headers['x-powered-by']}")
                        
                    # CMS detection
                    if 'wordpress' in content.lower():
                        technologies.append("CMS: WordPress")
                        console.print("   CMS: WordPress")
                    elif 'drupal' in content.lower():
                        technologies.append("CMS: Drupal")
                        console.print("   CMS: Drupal")
                        
                    self.results['technologies'] = technologies
                    
        except Exception as e:
            console.print(f"   [red]Technology detection failed: {e}[/red]")
            
    async def ssl_analysis(self):
        """SSL/TLS security analysis"""
        console.print("🔒 SSL/TLS Analysis...")
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.target, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=self.target) as ssock:
                    cert = ssock.getpeercert()
                    
                    self.results['ssl_info'] = {
                        'version': ssock.version(),
                        'cipher': ssock.cipher(),
                        'subject': dict(x[0] for x in cert['subject']),
                        'issuer': dict(x[0] for x in cert['issuer']),
                        'not_after': cert['notAfter']
                    }
                    
                    console.print(f"   SSL Version: {ssock.version()}")
                    console.print(f"   Cipher: {ssock.cipher()[0]}")
                    console.print(f"   Expires: {cert['notAfter']}")
                    
        except Exception as e:
            console.print(f"   [red]SSL analysis failed: {e}[/red]")
            
    async def security_headers_check(self):
        """Check security headers"""
        console.print("🛡️ Security Headers Analysis...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://{self.target}") as response:
                    headers = dict(response.headers)
                    
                    security_headers = {
                        'strict-transport-security': headers.get('strict-transport-security'),
                        'content-security-policy': headers.get('content-security-policy'),
                        'x-frame-options': headers.get('x-frame-options'),
                        'x-content-type-options': headers.get('x-content-type-options'),
                        'x-xss-protection': headers.get('x-xss-protection'),
                        'referrer-policy': headers.get('referrer-policy')
                    }
                    
                    self.results['security_headers'] = security_headers
                    
                    for header, value in security_headers.items():
                        if value:
                            console.print(f"   ✅ {header}: {value}")
                        else:
                            console.print(f"   ❌ Missing: {header}")
                            self.results['vulnerabilities'].append({
                                'type': 'Missing Security Header',
                                'severity': 'Medium',
                                'description': f"Missing {header} header",
                                'recommendation': f"Implement {header} header"
                            })
                            
        except Exception as e:
            console.print(f"   [red]Security headers check failed: {e}[/red]")
            
    async def directory_enumeration(self):
        """Directory and file enumeration"""
        console.print("📁 Directory Enumeration...")
        
        common_dirs = [
            'admin', 'administrator', 'panel', 'control', 'dashboard',
            'api', 'v1', 'v2', 'docs', 'documentation', 'swagger',
            'backup', 'backups', 'old', 'test', 'dev', 'staging',
            'config', 'configuration', 'settings', 'env', '.env',
            'robots.txt', 'sitemap.xml', '.htaccess', 'web.config'
        ]
        
        found_endpoints = []
        
        async with aiohttp.ClientSession() as session:
            for directory in common_dirs:
                try:
                    url = f"https://{self.target}/{directory}"
                    async with session.get(url, timeout=5) as response:
                        if response.status == 200:
                            found_endpoints.append(directory)
                            console.print(f"   ✅ Found: /{directory} (Status: {response.status})")
                            
                            if directory in ['admin', 'administrator', 'panel', 'control', 'dashboard']:
                                self.results['vulnerabilities'].append({
                                    'type': 'Exposed Admin Panel',
                                    'severity': 'High',
                                    'description': f"Admin panel accessible at /{directory}",
                                    'url': url,
                                    'recommendation': 'Restrict access to admin panels'
                                })
                                
                except:
                    pass
                    
        self.results['endpoints'] = found_endpoints
        
    async def sql_injection_testing(self):
        """Basic SQL injection testing"""
        console.print("💉 SQL Injection Testing...")
        
        # This is a basic test - in real scenarios, use specialized tools
        sql_payloads = ["'", "1' OR '1'='1", "'; DROP TABLE users; --"]
        
        # Test common parameters
        test_urls = [
            f"https://{self.target}/?id=1'",
            f"https://{self.target}/search?q=test'",
            f"https://{self.target}/login?user=admin'"
        ]
        
        async with aiohttp.ClientSession() as session:
            for url in test_urls:
                try:
                    async with session.get(url, timeout=5) as response:
                        content = await response.text()
                        
                        # Look for SQL error messages
                        sql_errors = [
                            'mysql_fetch_array', 'ORA-01756', 'Microsoft OLE DB',
                            'SQLServer JDBC Driver', 'PostgreSQL query failed',
                            'syntax error', 'mysql_num_rows'
                        ]
                        
                        for error in sql_errors:
                            if error.lower() in content.lower():
                                console.print(f"   ⚠️ Potential SQL injection: {url}")
                                self.results['vulnerabilities'].append({
                                    'type': 'SQL Injection',
                                    'severity': 'Critical',
                                    'description': f"Potential SQL injection vulnerability detected",
                                    'url': url,
                                    'recommendation': 'Use parameterized queries and input validation'
                                })
                                break
                                
                except:
                    pass
                    
    async def xss_testing(self):
        """Basic XSS testing"""
        console.print("🔥 XSS Testing...")
        
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "javascript:alert('XSS')",
            "<img src=x onerror=alert('XSS')>"
        ]
        
        # Test search and input fields
        test_params = ['q', 'search', 'query', 'input', 'data']
        
        async with aiohttp.ClientSession() as session:
            for param in test_params:
                for payload in xss_payloads:
                    try:
                        url = f"https://{self.target}/?{param}={payload}"
                        async with session.get(url, timeout=5) as response:
                            content = await response.text()
                            
                            if payload in content:
                                console.print(f"   ⚠️ Potential XSS: {param} parameter")
                                self.results['vulnerabilities'].append({
                                    'type': 'Cross-Site Scripting (XSS)',
                                    'severity': 'High',
                                    'description': f"Potential XSS vulnerability in {param} parameter",
                                    'url': url,
                                    'recommendation': 'Implement proper input validation and output encoding'
                                })
                                break
                                
                    except:
                        pass
                        
    async def authentication_testing(self):
        """Authentication mechanism testing"""
        console.print("🔐 Authentication Testing...")
        
        # Test for common login endpoints
        login_endpoints = ['/login', '/admin', '/signin', '/auth', '/panel']
        
        async with aiohttp.ClientSession() as session:
            for endpoint in login_endpoints:
                try:
                    url = f"https://{self.target}{endpoint}"
                    async with session.get(url, timeout=5) as response:
                        if response.status == 200:
                            content = await response.text()
                            
                            # Check for weak authentication indicators
                            if 'password' in content.lower() and 'login' in content.lower():
                                console.print(f"   🔍 Login form found: {endpoint}")
                                
                                # Test for default credentials
                                await self.test_default_credentials(session, url)
                                
                except:
                    pass
                    
    async def test_default_credentials(self, session, login_url):
        """Test common default credentials"""
        default_creds = [
            ('admin', 'admin'),
            ('admin', 'password'),
            ('admin', '123456'),
            ('root', 'root'),
            ('test', 'test')
        ]
        
        for username, password in default_creds:
            try:
                data = {'username': username, 'password': password}
                async with session.post(login_url, data=data, timeout=5) as response:
                    if 'dashboard' in str(response.url) or 'welcome' in await response.text():
                        console.print(f"   ⚠️ Default credentials work: {username}:{password}")
                        self.results['vulnerabilities'].append({
                            'type': 'Default Credentials',
                            'severity': 'Critical',
                            'description': f"Default credentials {username}:{password} are valid",
                            'url': login_url,
                            'recommendation': 'Change default credentials immediately'
                        })
                        break
            except:
                pass
                
    async def admin_panel_discovery(self):
        """Discover admin panels and control interfaces"""
        console.print("👑 Admin Panel Discovery...")
        
        admin_paths = [
            'admin', 'administrator', 'panel', 'control', 'dashboard',
            'manage', 'management', 'cpanel', 'wp-admin', 'admin.php',
            'administrator.php', 'admin/index.php', 'admin/login.php'
        ]
        
        async with aiohttp.ClientSession() as session:
            for path in admin_paths:
                try:
                    url = f"https://{self.target}/{path}"
                    async with session.get(url, timeout=5) as response:
                        if response.status == 200:
                            console.print(f"   🎯 Admin panel found: /{path}")
                            
                except:
                    pass
                    
    async def api_endpoint_testing(self):
        """Test API endpoints for vulnerabilities"""
        console.print("🔌 API Endpoint Testing...")
        
        api_paths = [
            'api', 'api/v1', 'api/v2', 'rest', 'graphql',
            'api/users', 'api/admin', 'api/config', 'api/status'
        ]
        
        async with aiohttp.ClientSession() as session:
            for path in api_paths:
                try:
                    url = f"https://{self.target}/{path}"
                    async with session.get(url, timeout=5) as response:
                        if response.status == 200:
                            content = await response.text()
                            
                            # Check for exposed sensitive data
                            if any(keyword in content.lower() for keyword in ['password', 'token', 'key', 'secret']):
                                console.print(f"   ⚠️ Sensitive data exposed: /{path}")
                                self.results['vulnerabilities'].append({
                                    'type': 'Information Disclosure',
                                    'severity': 'High',
                                    'description': f"API endpoint exposes sensitive information",
                                    'url': url,
                                    'recommendation': 'Implement proper access controls for API endpoints'
                                })
                                
                except:
                    pass
                    
    async def file_upload_testing(self):
        """Test file upload functionality"""
        console.print("📤 File Upload Testing...")
        
        # Look for upload forms
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://{self.target}") as response:
                    content = await response.text()
                    
                    if 'type="file"' in content:
                        console.print("   📁 File upload form detected")
                        self.results['vulnerabilities'].append({
                            'type': 'File Upload',
                            'severity': 'Medium',
                            'description': 'File upload functionality detected - requires manual testing',
                            'recommendation': 'Implement file type validation and virus scanning'
                        })
                        
        except:
            pass
            
    async def business_logic_testing(self):
        """Test business logic vulnerabilities"""
        console.print("🧠 Business Logic Testing...")
        
        # This would require more specific testing based on the application
        console.print("   ℹ️ Business logic testing requires manual analysis")
        
    def generate_penetration_report(self):
        """Generate comprehensive penetration test report"""
        console.print("\n" + "="*80)
        console.print("[bold green]🎯 PENETRATION TEST REPORT[/bold green]")
        console.print("="*80)
        
        # Summary
        total_vulns = len(self.results['vulnerabilities'])
        critical_vulns = len([v for v in self.results['vulnerabilities'] if v['severity'] == 'Critical'])
        high_vulns = len([v for v in self.results['vulnerabilities'] if v['severity'] == 'High'])
        
        summary_table = Table(title="Executive Summary")
        summary_table.add_column("Metric", style="cyan")
        summary_table.add_column("Count", style="magenta")
        
        summary_table.add_row("Target", self.target)
        summary_table.add_row("Total Vulnerabilities", str(total_vulns))
        summary_table.add_row("Critical Vulnerabilities", str(critical_vulns))
        summary_table.add_row("High Vulnerabilities", str(high_vulns))
        summary_table.add_row("Open Ports", str(len(self.results['open_ports'])))
        summary_table.add_row("Subdomains Found", str(len(self.results['subdomains'])))
        
        console.print(summary_table)
        
        # Vulnerabilities
        if self.results['vulnerabilities']:
            console.print("\n[bold red]🚨 VULNERABILITIES FOUND[/bold red]")
            
            vuln_table = Table()
            vuln_table.add_column("Type", style="cyan")
            vuln_table.add_column("Severity", style="red")
            vuln_table.add_column("Description", style="white")
            
            for vuln in self.results['vulnerabilities']:
                vuln_table.add_row(
                    vuln['type'],
                    vuln['severity'],
                    vuln['description']
                )
                
            console.print(vuln_table)
            
        # Open Ports
        if self.results['open_ports']:
            console.print(f"\n[bold yellow]🔌 OPEN PORTS: {', '.join(map(str, self.results['open_ports']))}[/bold yellow]")
            
        # Subdomains
        if self.results['subdomains']:
            console.print(f"\n[bold blue]🌐 SUBDOMAINS: {', '.join(self.results['subdomains'])}[/bold blue]")
            
        # Save report to file
        report_data = {
            'target': self.target,
            'timestamp': datetime.now().isoformat(),
            'results': self.results
        }
        
        with open(f'penetration_report_{self.target}_{int(time.time())}.json', 'w') as f:
            json.dump(report_data, f, indent=2)
            
        console.print(f"\n✅ [bold green]Report saved to penetration_report_{self.target}_{int(time.time())}.json[/bold green]")
        console.print("\n🎯 [bold]PENETRATION TEST COMPLETE![/bold]")

# Direct execution function
async def run_penetration_test(target):
    """Run direct penetration test"""
    engine = DirectPenetrationEngine()
    await engine.full_penetration_test(target)
    return engine.results

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target = sys.argv[1]
        asyncio.run(run_penetration_test(target))
    else:
        print("Usage: python3 direct_penetration_engine.py <target>")