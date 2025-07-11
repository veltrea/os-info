#!/usr/bin/env python3
"""
OS Information Collector Module

This module provides functionality to collect system information including:
- Operating system details
- Network configuration
- User information
"""

import os
import platform
import socket
import getpass
import subprocess
import json
from typing import Dict, List, Any, Optional


class OSInfoCollector:
    """Collects various system information"""
    
    def __init__(self):
        self.info = {}
    
    def collect_system_info(self) -> Dict[str, Any]:
        """Collect basic system information"""
        try:
            system_info = {
                'platform': platform.platform(),
                'system': platform.system(),
                'node': platform.node(),
                'release': platform.release(),
                'version': platform.version(),
                'machine': platform.machine(),
                'processor': platform.processor(),
                'architecture': platform.architecture(),
                'python_version': platform.python_version(),
                'python_implementation': platform.python_implementation(),
            }
            
            # Add Windows-specific information
            if platform.system() == 'Windows':
                try:
                    import winreg
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                      r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
                        system_info['windows_build'] = winreg.QueryValueEx(key, "CurrentBuild")[0]
                        system_info['windows_version'] = winreg.QueryValueEx(key, "DisplayVersion")[0]
                except Exception:
                    pass
            
            return system_info
        except Exception as e:
            return {'error': str(e)}
    
    def collect_network_info(self) -> Dict[str, Any]:
        """Collect network information"""
        try:
            network_info = {
                'hostname': socket.gethostname(),
                'fqdn': socket.getfqdn(),
            }
            
            # Get IP addresses
            try:
                # Get local IP address
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                network_info['local_ip'] = s.getsockname()[0]
                s.close()
            except Exception:
                network_info['local_ip'] = 'Unable to determine'
            
            # Get all network interfaces (Windows)
            if platform.system() == 'Windows':
                try:
                    result = subprocess.run(['ipconfig', '/all'], 
                                          capture_output=True, text=True, encoding='cp932')
                    if result.returncode == 0:
                        network_info['ipconfig_output'] = result.stdout
                except Exception:
                    pass
            
            return network_info
        except Exception as e:
            return {'error': str(e)}
    
    def collect_user_info(self) -> Dict[str, Any]:
        """Collect user information"""
        try:
            user_info = {
                'username': getpass.getuser(),
                'home_directory': os.path.expanduser('~'),
                'current_directory': os.getcwd(),
            }
            
            # Add environment variables
            env_vars = ['PATH', 'USERPROFILE', 'COMPUTERNAME', 'USERDOMAIN']
            user_info['environment'] = {}
            for var in env_vars:
                user_info['environment'][var] = os.environ.get(var, 'Not set')
            
            return user_info
        except Exception as e:
            return {'error': str(e)}
    
    def collect_all(self) -> Dict[str, Any]:
        """Collect all available information"""
        return {
            'system': self.collect_system_info(),
            'network': self.collect_network_info(),
            'user': self.collect_user_info(),
            'timestamp': self._get_timestamp()
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
