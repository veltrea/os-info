#!/usr/bin/env python3

import platform
import socket
import psutil
from datetime import datetime

def get_system_info(no_timestamps=False):
    info = {
        'os_name': platform.system(),
        'version': platform.version(),
        'build_number': platform.release(),
        'architecture': platform.machine()
    }
    
    if not no_timestamps:
        info.update({
            'install_date': psutil.boot_time(),
            'last_boot_time': psutil.boot_time()
        })
    
    return info

def get_network_info():
    hostname = socket.gethostname()
    interfaces = []
    
    for iface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                interfaces.append({
                    'name': iface,
                    'ip_address': addr.address,
                    'mac_address': next((a.address for a in addrs if a.family == psutil.AF_LINK), None)
                })
                break
    
    return {
        'hostname': hostname,
        'interfaces': interfaces
    }

def get_user_info():
    return {
        'current_user': psutil.Process().username(),
        'all_users': [u.name for u in psutil.users()]
    }

def collect_all(minimal=False, no_timestamps=False):
    data = {
        'system': get_system_info(no_timestamps),
        'network': get_network_info(),
        'users': get_user_info()
    }
    
    if minimal:
        if 'system' in data:
            data['system'] = {
                'os_name': data['system']['os_name'],
                'version': data['system']['version']
            }
        if 'network' in data:
            data['network'] = {
                'hostname': data['network']['hostname']
            }
        if 'users' in data:
            data['users'] = {
                'current_user': data['users']['current_user']
            }
    
    return data