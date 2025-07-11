#!/usr/bin/env python3
"""
Test suite for OS Info tool

This module contains unit tests for the OS information collection tool.
"""

import unittest
import json
from os_info.collector import OSInfoCollector
from os_info.formatter import OSInfoFormatter


class TestOSInfoCollector(unittest.TestCase):
    """Test cases for OSInfoCollector"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.collector = OSInfoCollector()
    
    def test_collect_system_info(self):
        """Test system information collection"""
        info = self.collector.collect_system_info()
        self.assertIsInstance(info, dict)
        
        # Check for required fields
        required_fields = ['platform', 'system', 'machine']
        for field in required_fields:
            self.assertIn(field, info)
    
    def test_collect_network_info(self):
        """Test network information collection"""
        info = self.collector.collect_network_info()
        self.assertIsInstance(info, dict)
        
        # Check for required fields
        required_fields = ['hostname', 'fqdn']
        for field in required_fields:
            self.assertIn(field, info)
    
    def test_collect_user_info(self):
        """Test user information collection"""
        info = self.collector.collect_user_info()
        self.assertIsInstance(info, dict)
        
        # Check for required fields
        required_fields = ['username', 'home_directory', 'current_directory']
        for field in required_fields:
            self.assertIn(field, info)
    
    def test_collect_all(self):
        """Test collecting all information"""
        info = self.collector.collect_all()
        self.assertIsInstance(info, dict)
        
        # Check for main categories
        categories = ['system', 'network', 'user', 'timestamp']
        for category in categories:
            self.assertIn(category, info)


class TestOSInfoFormatter(unittest.TestCase):
    """Test cases for OSInfoFormatter"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_data = {
            'system': {
                'platform': 'Windows-10',
                'machine': 'AMD64'
            },
            'network': {
                'hostname': 'test-host',
                'local_ip': '192.168.1.100'
            },
            'user': {
                'username': 'testuser',
                'home_directory': 'C:\\Users\\testuser'
            }
        }
        self.formatter = OSInfoFormatter(self.test_data)
    
    def test_to_json(self):
        """Test JSON formatting"""
        output = self.formatter.to_json()
        self.assertIsInstance(output, str)
        
        # Verify it's valid JSON
        parsed = json.loads(output)
        self.assertEqual(parsed, self.test_data)
    
    def test_to_json_pretty(self):
        """Test pretty JSON formatting"""
        output = self.formatter.to_json(pretty=True)
        self.assertIsInstance(output, str)
        self.assertIn('\n', output)  # Pretty format should have newlines
    
    def test_to_csv(self):
        """Test CSV formatting"""
        output = self.formatter.to_csv()
        self.assertIsInstance(output, str)
        self.assertIn('Category,Key,Value', output)
    
    def test_to_minimal(self):
        """Test minimal formatting"""
        output = self.formatter.to_minimal()
        self.assertIsInstance(output, str)
        self.assertIn('OS:', output)
        self.assertIn('Hostname:', output)
        self.assertIn('User:', output)


if __name__ == '__main__':
    unittest.main()
