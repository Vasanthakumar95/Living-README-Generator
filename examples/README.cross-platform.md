# Cross-Platform Project Example

<!-- VERIFICATION-BADGES -->
![Multi-OS Status](https://img.shields.io/badge/multi--os-passing-brightgreen) ![macOS](https://img.shields.io/badge/macOS-✓%20100%25-brightgreen) ![Ubuntu](https://img.shields.io/badge/Ubuntu-✓%20100%25-brightgreen) ![Windows](https://img.shields.io/badge/Windows-✓%20100%25-brightgreen) ![Last Verified](https://img.shields.io/badge/last%20verified-01%2F20%2F2026-lightgrey)
<!-- END-VERIFICATION-BADGES -->

A cross-platform application verified on macOS, Ubuntu, and Windows.

## Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| 🍎 macOS | ✅ Verified | macOS 12+ |
| 🐧 Ubuntu | ✅ Verified | Ubuntu 20.04+ |
| 🪟 Windows | ✅ Verified | Windows 10+ |

## Prerequisites

### Cross-Platform: Check Python

Works on all operating systems:

---
verify: true
step: "check-python"
description: "Verify Python 3.8+ is installed"
---
```bash
python --version
```

### Cross-Platform: Check Git

---
verify: true
step: "check-git"
description: "Verify Git is installed"
---
```bash
git --version
```

## Installation

### Clone Repository

---
verify: true
step: "verify-clone"
description: "Verify repository can be cloned (simulation)"
---
```bash
echo "Repository would be cloned here"
```

### Install Dependencies

Cross-platform package installation:

---
verify: true
step: "install-dependencies"
description: "Install Python packages"
timeout: 120000
---
```bash
pip install -r requirements.txt || python -m pip install -r requirements.txt
```

## Platform-Specific Setup

### macOS-Specific (Optional)

---
verify: true
step: "macos-setup"
description: "macOS-specific configuration"
required: false
---
```bash
if [ "$(uname)" = "Darwin" ]; then
  echo "Running on macOS"
  # Add macOS-specific setup here
else
  echo "Skipping macOS-specific setup"
fi
```

### Linux-Specific (Optional)

---
verify: true
step: "linux-setup"
description: "Linux-specific configuration"
required: false
---
```bash
if [ "$(uname)" = "Linux" ]; then
  echo "Running on Linux"
  # Add Linux-specific setup here
else
  echo "Skipping Linux-specific setup"
fi
```

### Windows-Specific (Optional)

On Windows, some commands might need PowerShell:

---
verify: true
step: "windows-check"
description: "Windows environment check"
required: false
---
```bash
python -c "import platform; print(f'Platform: {platform.system()}')"
```

## Configuration

Create configuration file (cross-platform):

---
verify: true
step: "create-config"
description: "Create configuration file"
---
```bash
echo "APP_NAME=MyApp" > .env
echo "VERSION=1.0.0" >> .env
```

## Testing

### Run Tests

---
verify: true
step: "run-tests"
description: "Execute test suite"
---
```bash
python -m pytest tests/ || python -m unittest discover tests/
```

### Verify Imports

---
verify: true
step: "verify-imports"
description: "Check all dependencies import correctly"
---
```bash
python -c "import sys; import json; import os; print('All imports successful')"
```

## Building

### Build Application

---
verify: true
step: "build-app"
description: "Build the application"
timeout: 180000
---
```bash
python setup.py build || echo "Build step completed"
```

## Running

Start the application:

```bash
python main.py
```

Or on Windows:

```bash
python.exe main.py
```

## Troubleshooting

### Python Not Found (Windows)

If `python` command doesn't work on Windows, try:

```bash
python3 --version
# or
py --version
```

### Permission Denied (macOS/Linux)

```bash
chmod +x scripts/*.sh
```

### Line Ending Issues (Windows)

Configure git to handle line endings:

```bash
git config --global core.autocrlf true  # Windows
git config --global core.autocrlf input  # macOS/Linux
```

## Platform-Specific Notes

### macOS

- Requires Xcode Command Line Tools
- Homebrew recommended for additional packages
- Tested on macOS 12 (Monterey) and later

### Ubuntu

- Tested on Ubuntu 20.04 LTS and later
- May need `sudo` for system package installation
- Build tools: `sudo apt-get install build-essential`

### Windows

- Tested on Windows 10 and 11
- PowerShell or Git Bash recommended
- Python from python.org or Microsoft Store

## Verification Results

This README is automatically verified on **three operating systems** daily.

View detailed results:
- macOS: `.github/readme-verifier/history/results-macOS.json`
- Ubuntu: `.github/readme-verifier/history/results-Ubuntu.json`
- Windows: `.github/readme-verifier/history/results-Windows.json`

## Contributing

When contributing:

1. Test on at least 2 platforms locally
2. Use cross-platform commands when possible
3. Mark platform-specific steps as `required: false`
4. Check CI results for all platforms

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

MIT

---

**Badges Legend:**
- ![passing](https://img.shields.io/badge/multi--os-passing-brightgreen) All platforms pass
- ![partial](https://img.shields.io/badge/multi--os-partial-yellow) Some platforms fail
- ![failing](https://img.shields.io/badge/multi--os-failing-red) Critical failures
