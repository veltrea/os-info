# OS Info Tool Specification

## Overview

The OS Info Tool is a Python-based command-line utility designed to collect and display comprehensive system information. It provides details about the operating system, network configuration, and user environment in various output formats.

## Features

### Core Functionality

1. **System Information Collection**
   - Operating system details (platform, version, architecture)
   - Hardware information (processor, machine type)
   - Python environment details
   - Windows-specific information (build number, version)

2. **Network Information Collection**
   - Hostname and FQDN
   - Local IP address detection
   - Network interface details (Windows)

3. **User Information Collection**
   - Current user details
   - Home and current directories
   - Environment variables

4. **Multiple Output Formats**
   - JSON (default, with pretty-print option)
   - YAML (requires PyYAML)
   - CSV
   - Minimal text format

### Command Line Interface

```
Usage: python os-info.py [options]

Options:
  --format FORMAT    Output format: json, yaml, csv, minimal (default: json)
  --pretty          Pretty print JSON output
  --minimal         Use minimal output format
  --help           Show help message
```

### Examples

```bash
# Basic usage (JSON output)
python os-info.py

# YAML output
python os-info.py --format yaml

# Pretty JSON output
python os-info.py --format json --pretty

# Minimal output
python os-info.py --minimal

# CSV output
python os-info.py --format csv
```

## Architecture

### Module Structure

```
os-info/
├── os-info.py              # Main entry point
├── os_info/
│   ├── __init__.py         # Package initialization
│   ├── collector.py        # Information collection logic
│   └── formatter.py        # Output formatting logic
├── test_os_info.py         # Unit tests
├── requirements.txt        # Dependencies
├── setup.bat              # Setup script for Windows
├── os-info.spec           # PyInstaller specification
└── README.md              # Documentation
```

### Classes

#### OSInfoCollector

Responsible for collecting system information.

**Methods:**
- `collect_system_info()`: Collects OS and hardware information
- `collect_network_info()`: Collects network configuration
- `collect_user_info()`: Collects user and environment information
- `collect_all()`: Collects all available information

#### OSInfoFormatter

Responsible for formatting collected data into various output formats.

**Methods:**
- `to_json(pretty=False)`: Formats data as JSON
- `to_yaml()`: Formats data as YAML
- `to_csv()`: Formats data as CSV
- `to_minimal()`: Formats data in minimal text format

## Dependencies

### Required
- Python 3.7 or later
- Standard library modules only for basic functionality

### Optional
- PyYAML: For YAML output format
- pytest: For running tests
- pytest-cov: For test coverage
- PyInstaller: For creating standalone executable

## Installation and Setup

### Manual Setup

1. Clone or download the project
2. Install optional dependencies: `pip install PyYAML`
3. Run the tool: `python os-info.py`

### Automated Setup (Windows)

1. Run `setup.bat`
2. The script will:
   - Check Python installation
   - Create virtual environment
   - Install dependencies
   - Run tests
   - Test the tool

### Building Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller os-info.spec

# The executable will be in dist/os-info.exe
```

## Testing

The project includes comprehensive unit tests:

```bash
# Run tests
python -m pytest test_os_info.py -v

# Run tests with coverage
python -m pytest test_os_info.py --cov=os_info
```

## Error Handling

- Graceful handling of missing information
- Error messages for failed operations
- Fallback values for unavailable data
- Cross-platform compatibility considerations

## Security Considerations

- No sensitive information is collected by default
- Environment variables are limited to common, non-sensitive ones
- Network information is limited to basic configuration
- No authentication or credential information is collected

## Future Enhancements

1. **Additional Information Sources**
   - Disk usage information
   - Memory and CPU details
   - Installed software list
   - Service status

2. **Output Enhancements**
   - HTML output format
   - XML output format
   - Custom templates

3. **Platform Support**
   - Enhanced Linux support
   - macOS-specific information
   - Cross-platform network details

4. **Configuration**
   - Configuration file support
   - Selective information collection
   - Custom output fields

## License

This project is released under the MIT License.
