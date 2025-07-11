#!/usr/bin/env python3
"""
OS Information Collection Tool

A comprehensive tool for collecting and displaying system information
including operating system details, network configuration, and user information.

Usage:
    python os-info.py [options]

Options:
    --format FORMAT    Output format: json, yaml, csv, minimal (default: json)
    --pretty          Pretty print JSON output
    --minimal         Use minimal output format
    --help           Show this help message

Examples:
    python os-info.py
    python os-info.py --format yaml
    python os-info.py --format json --pretty
    python os-info.py --minimal
"""

import sys
import argparse
from os_info.collector import OSInfoCollector
from os_info.formatter import OSInfoFormatter


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Collect and display OS information',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # JSON output
  %(prog)s --format yaml      # YAML output
  %(prog)s --format csv       # CSV output
  %(prog)s --minimal          # Minimal output
  %(prog)s --pretty           # Pretty JSON output
"""
    )
    
    parser.add_argument(
        '--format',
        choices=['json', 'yaml', 'csv', 'minimal'],
        default='json',
        help='Output format (default: json)'
    )
    
    parser.add_argument(
        '--pretty',
        action='store_true',
        help='Pretty print JSON output'
    )
    
    parser.add_argument(
        '--minimal',
        action='store_true',
        help='Use minimal output format (overrides --format)'
    )
    
    args = parser.parse_args()
    
    try:
        # Collect information
        collector = OSInfoCollector()
        data = collector.collect_all()
        
        # Format output
        formatter = OSInfoFormatter(data)
        
        if args.minimal:
            output = formatter.to_minimal()
        elif args.format == 'json':
            output = formatter.to_json(pretty=args.pretty)
        elif args.format == 'yaml':
            output = formatter.to_yaml()
        elif args.format == 'csv':
            output = formatter.to_csv()
        else:
            output = formatter.to_json()
        
        print(output)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
