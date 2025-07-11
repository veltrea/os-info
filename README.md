# OS Information Collection Tool (os-info)

A Python tool that collects operating system information and outputs it in various formats.

## Requirements

### Running from Source
- Python 3.7 or higher
- Windows OS

### Executable (exe)
- Windows OS

## Installation

```cmd
# Install using pip
pip install os-info

# Or install from source
git clone https://github.com/veltrea/os-info.git
cd os-info
pip install .
```

## Usage

```cmd
# Display to standard output
os-info

# Output to file
os-info --output os.json
os-info --utf8
```

## Collected Information

- OS name
- Version
- Build number
- Architecture
- Installation date
- Last boot time
- Logged-in user
- Hostname
- IP address
- MAC address
- User accounts
  - Username
  - User ID
  - Home directory
  - Service account

## Command Line Options

### Output Format
- `--format json|csv|yaml`: Output format (default: json)
- `--pretty`: Pretty print JSON output
- `--minimal`: Minimal information only

### Output Control
- `--output FILE`: Output to file
- `--no-timestamps`: Exclude timestamps

### Others
- `--quiet`: Suppress output except errors
- `--help`: Display help

## Exit Codes

- 0: Success
- 1: General error
- 2: Insufficient permissions
- 4: Partial success (some data collection failed)

## License

MIT

## Contributing

Please submit bug reports and feature requests to the [Issue Tracker](https://github.com/veltrea/os-info/issues).
Pull requests are welcome.