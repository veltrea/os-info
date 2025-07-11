#!/usr/bin/env python3
"""
OS Information Formatter Module

This module provides functionality to format collected system information
in various output formats including JSON, YAML, and CSV.
"""

import json
import csv
import io
from typing import Dict, Any, List


class OSInfoFormatter:
    """Formats OS information in various formats"""
    
    def __init__(self, data: Dict[str, Any]):
        self.data = data
    
    def to_json(self, pretty: bool = False) -> str:
        """Format data as JSON"""
        if pretty:
            return json.dumps(self.data, indent=2, ensure_ascii=False)
        return json.dumps(self.data, ensure_ascii=False)
    
    def to_yaml(self) -> str:
        """Format data as YAML"""
        try:
            import yaml
            return yaml.dump(self.data, default_flow_style=False, allow_unicode=True)
        except ImportError:
            return "YAML library not available. Install with: pip install PyYAML"
    
    def to_csv(self) -> str:
        """Format data as CSV"""
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow(['Category', 'Key', 'Value'])
        
        # Flatten the data
        for category, category_data in self.data.items():
            if isinstance(category_data, dict):
                for key, value in category_data.items():
                    if isinstance(value, (dict, list)):
                        value = json.dumps(value, ensure_ascii=False)
                    writer.writerow([category, key, str(value)])
            else:
                writer.writerow([category, '', str(category_data)])
        
        return output.getvalue()
    
    def to_minimal(self) -> str:
        """Format data in minimal format"""
        lines = []
        
        # System info
        if 'system' in self.data and isinstance(self.data['system'], dict):
            system = self.data['system']
            lines.append(f"OS: {system.get('system', 'Unknown')} {system.get('release', '')}")
            lines.append(f"Machine: {system.get('machine', 'Unknown')}")
            lines.append(f"Processor: {system.get('processor', 'Unknown')}")
        
        # Network info
        if 'network' in self.data and isinstance(self.data['network'], dict):
            network = self.data['network']
            lines.append(f"Hostname: {network.get('hostname', 'Unknown')}")
            lines.append(f"Local IP: {network.get('local_ip', 'Unknown')}")
        
        # User info
        if 'user' in self.data and isinstance(self.data['user'], dict):
            user = self.data['user']
            lines.append(f"User: {user.get('username', 'Unknown')}")
            lines.append(f"Home: {user.get('home_directory', 'Unknown')}")
        
        return '\n'.join(lines)
