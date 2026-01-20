# 🌍 Multi-OS Verification Guide

The Living README Generator now supports verification across **macOS, Ubuntu, and Windows**!

## 🎯 What This Means

Your README setup instructions are tested on **three operating systems** to ensure they work everywhere:

- 🍎 **macOS** (latest)
- 🐧 **Ubuntu** (latest)
- 🪟 **Windows** (latest)

## 🚀 Quick Start

### Option 1: Use Multi-OS Workflow (Recommended)

```bash
# Copy the multi-OS workflow
cp .github/workflows/verify-readme-multi-os.yml your-project/.github/workflows/

# That's it! Push and it runs on all 3 OSes
git add .github/workflows/verify-readme-multi-os.yml
git commit -m "Add multi-OS verification"
git push
```

### Option 2: Single OS Workflow

Keep using the single-OS workflow if you only need one platform:

```bash
# This runs on macOS only
cp .github/workflows/verify-readme.yml your-project/.github/workflows/
```

## 📊 What You Get

### Multi-OS Badges

When using the multi-OS workflow, your README will show:

```
Multi-OS Status: passing
macOS: ✓ 100%
Ubuntu: ✓ 100%
Windows: ✓ 95%
Last Verified: 1/20/2026
```

### Individual OS Results

Each OS gets its own verification results:

```
.github/readme-verifier/
├── combined-results.json       # Aggregated results
└── history/
    ├── results-macOS.json      # macOS specific
    ├── results-Ubuntu.json     # Ubuntu specific
    └── results-Windows.json    # Windows specific
```

## 🔧 How It Works

### Workflow Strategy

The workflow uses a **matrix strategy** to run in parallel:

```yaml
strategy:
  matrix:
    os: [macos-latest, ubuntu-latest, windows-latest]
```

### Execution Flow

```
Trigger (schedule/manual/push)
    ↓
┌────────────┬────────────┬────────────┐
│            │            │            │
macOS        Ubuntu       Windows
│            │            │
Verify       Verify       Verify
│            │            │
Save         Save         Save
│            │            │
└────────────┴────────────┴────────────┘
    ↓
Aggregate Results
    ↓
Update Badges
    ↓
Create Issue (if any OS failed)
```

## 📝 Writing OS-Specific Steps

### Platform Detection

Some steps might be OS-specific:

```markdown
### macOS Setup

---
verify: true
step: "install-brew-deps"
description: "Install Homebrew dependencies (macOS only)"
required: false
---
```bash
if [ "$(uname)" == "Darwin" ]; then
  brew install your-package
fi
```

### Windows-Specific Commands

Use PowerShell-compatible commands for Windows:

```markdown
### Check Python (Cross-Platform)

---
verify: true
step: "check-python"
description: "Verify Python installation"
---
```bash
python --version
```

### Ubuntu-Specific

```markdown
### Install System Dependencies (Ubuntu)

---
verify: true
step: "install-apt-packages"
description: "Install system packages (Linux)"
required: false
---
```bash
if [ -f /etc/debian_version ]; then
  sudo apt-get update
  sudo apt-get install -y build-essential
fi
```

## 🎨 Badge Customization

### Default Multi-OS Badges

```markdown
![Multi-OS Status](https://img.shields.io/badge/multi--os-passing-brightgreen)
![macOS](https://img.shields.io/badge/macOS-✓%20100%25-brightgreen)
![Ubuntu](https://img.shields.io/badge/Ubuntu-✓%20100%25-brightgreen)
![Windows](https://img.shields.io/badge/Windows-✓%2095%25-yellow)
```

### Generate Custom Badges

```bash
python3 scripts/generate-multi-os-badges.py README.md
```

## 🧪 Testing

### Test All OSes

Trigger manually in GitHub Actions:

1. Go to **Actions** tab
2. Select **"Verify README Setup Instructions (Multi-OS)"**
3. Click **"Run workflow"**
4. Choose **"all"** for OS
5. Click **"Run workflow"**

### Test Specific OS

Choose specific OS from the dropdown:
- `macos` - Test only on macOS
- `ubuntu` - Test only on Ubuntu  
- `windows` - Test only on Windows

### Local Testing

Test on your current OS:

```bash
# macOS or Linux
python3 scripts/verify-readme.py README.md

# Windows (PowerShell)
python scripts/verify-readme.py README.md
```

## 📋 Best Practices

### ✅ Write Cross-Platform Commands

**Good:**
```bash
python --version
npm install
git --version
```

**Avoid:**
```bash
brew install something     # macOS only
apt-get install something  # Ubuntu only
choco install something    # Windows only
```

### ✅ Use Conditional Logic

```bash
# Detect OS and run appropriate command
if [ "$(uname)" == "Darwin" ]; then
  echo "Running on macOS"
elif [ "$(uname)" == "Linux" ]; then
  echo "Running on Linux"
else
  echo "Running on Windows"
fi
```

### ✅ Mark OS-Specific Steps as Optional

```markdown
---
verify: true
step: "macos-specific"
description: "macOS-only step"
required: false
---
```

### ✅ Test Path Separators

**Cross-platform:**
```bash
cd src
python -m mymodule
```

**Avoid:**
```bash
cd src\mymodule  # Windows-style backslash
```

## 🚨 Common Issues

### Issue 1: Commands Don't Work on Windows

**Problem:** Bash-specific commands fail on Windows

**Solution:** Use Python script instead:

```markdown
---
verify: true
step: "cross-platform-check"
---
```bash
python -c "import sys; print(sys.version)"
```

### Issue 2: Different Package Managers

**Problem:** `apt`, `brew`, `choco` aren't universal

**Solution:** Make OS-specific steps optional:

```markdown
---
verify: true
step: "install-deps"
required: false
---
```bash
if command -v brew &> /dev/null; then
  brew install pkg
elif command -v apt-get &> /dev/null; then
  sudo apt-get install -y pkg
fi
```

### Issue 3: Line Endings

**Problem:** Git converts line endings differently on Windows

**Solution:** Configure git:

```bash
git config --global core.autocrlf input
```

## 📊 Viewing Results

### In GitHub Actions

1. Go to **Actions** tab
2. Click latest workflow run
3. Expand **"Aggregate Multi-OS Results"**
4. See summary table

### In Results Files

```bash
# View combined results
cat .github/readme-verifier/combined-results.json

# View OS-specific
cat .github/readme-verifier/history/results-macOS.json
cat .github/readme-verifier/history/results-Ubuntu.json
cat .github/readme-verifier/history/results-Windows.json
```

### Sample Combined Results

```json
{
  "timestamp": "2026-01-20T02:00:00.000Z",
  "results_by_os": {
    "macOS": {
      "total": 5,
      "success": 5,
      "failed": 0,
      "warnings": 0,
      "timestamp": "2026-01-20T02:01:23.456Z"
    },
    "Linux": {
      "total": 5,
      "success": 5,
      "failed": 0,
      "warnings": 0,
      "timestamp": "2026-01-20T02:01:45.789Z"
    },
    "Windows": {
      "total": 5,
      "success": 4,
      "failed": 1,
      "warnings": 0,
      "timestamp": "2026-01-20T02:02:12.345Z"
    }
  }
}
```

## 🔄 Migration from Single-OS

### Step 1: Backup Current Workflow

```bash
cp .github/workflows/verify-readme.yml .github/workflows/verify-readme-single.yml.bak
```

### Step 2: Add Multi-OS Workflow

```bash
cp .github/workflows/verify-readme-multi-os.yml your-project/.github/workflows/
```

### Step 3: Update Badge Script

```bash
cp scripts/generate-multi-os-badges.py your-project/scripts/
```

### Step 4: Test

```bash
# Commit and push
git add .github/workflows/verify-readme-multi-os.yml
git add scripts/generate-multi-os-badges.py
git commit -m "Add multi-OS verification support"
git push

# Trigger manually to test
```

### Step 5: Remove Old Workflow (Optional)

Once multi-OS works, you can remove the single-OS workflow:

```bash
git rm .github/workflows/verify-readme.yml
git commit -m "Remove single-OS workflow"
```

## 💡 Pro Tips

### 1. Use Matrix Selectively

If you only care about 2 OSes:

```yaml
strategy:
  matrix:
    os: [macos-latest, ubuntu-latest]  # Skip Windows
```

### 2. Different Steps Per OS

Use conditionals in your commands:

```bash
# macOS
[ "$(uname)" = "Darwin" ] && brew install pkg

# Linux
[ "$(uname)" = "Linux" ] && apt-get install pkg

# Windows (PowerShell)
if ($env:OS -eq "Windows_NT") { choco install pkg }
```

### 3. Fail Fast vs Continue

**Fail fast** (stop if one OS fails):
```yaml
strategy:
  fail-fast: true
```

**Continue** (test all OSes regardless):
```yaml
strategy:
  fail-fast: false  # Recommended for multi-OS
```


## ❓ FAQ

**Q: Does multi-OS cost more in GitHub Actions?**  
A: Yes, ~3x the minutes (running on 3 OSes). But for daily runs, it's usually within free tier.

**Q: Can I test only on 2 OSes?**  
A: Yes! Edit the matrix in the workflow file.

**Q: What if a step only works on one OS?**  
A: Mark it as `required: false` and use OS detection in the command.

**Q: How do I debug Windows-specific failures?**  
A: Check the Actions logs for the Windows job, or test locally on Windows.

**Q: Can I run different commands per OS?**  
A: Yes, use shell conditionals or create separate verification blocks.

---

## 🎉 Summary

Multi-OS verification ensures your README works **everywhere**:

- ✅ Tested on 3 operating systems
- ✅ Individual badges per OS
- ✅ Aggregated results
- ✅ Auto-creates issues when any OS fails
- ✅ Easy migration from single-OS

**Your documentation now works for everyone!** 🌍

---

**Questions?** See [FAQ.md](FAQ.md) or open an issue.
