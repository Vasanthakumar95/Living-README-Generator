# 🌍 Multi-OS Support - Feature Summary

## 🎉 New Feature: Multi-OS Verification

Your Living README Generator now supports verification across **multiple operating systems**!

---

## 📦 What's Included

### 1. Multi-OS GitHub Actions Workflow
**File:** `.github/workflows/verify-readme-multi-os.yml`

**Features:**
- ✅ Runs on macOS, Ubuntu, and Windows simultaneously
- ✅ Matrix strategy for parallel execution
- ✅ Manual trigger with OS selection
- ✅ Aggregated results from all platforms
- ✅ Auto-creates issues when any OS fails
- ✅ Individual results per OS

### 2. Multi-OS Badge Generator
**File:** `scripts/generate-multi-os-badges.py`

**Features:**
- ✅ Generates badges for each OS
- ✅ Overall multi-OS status badge
- ✅ Success rate per platform
- ✅ Automatic badge updates

### 3. Comprehensive Documentation
**File:** `docs/MULTI_OS_GUIDE.md`

**Covers:**
- ✅ Quick start guide
- ✅ How it works
- ✅ Writing cross-platform steps
- ✅ Platform-specific commands
- ✅ Best practices
- ✅ Troubleshooting
- ✅ Migration guide

### 4. Cross-Platform Example
**File:** `examples/README.cross-platform.md`

**Shows:**
- ✅ Cross-platform verification steps
- ✅ OS-specific optional steps
- ✅ Platform detection techniques
- ✅ Multi-OS badges in action

---

## 🚀 Quick Start

### Option 1: New Projects

```bash
# Copy the multi-OS workflow
cp .github/workflows/verify-readme-multi-os.yml your-project/.github/workflows/

# Copy the badge generator
cp scripts/generate-multi-os-badges.py your-project/scripts/

# Push and watch it run on all 3 OSes!
git add .github/workflows/verify-readme-multi-os.yml
git add scripts/generate-multi-os-badges.py
git commit -m "Add multi-OS verification"
git push
```

### Option 2: Existing Projects

If you already use the single-OS workflow:

```bash
# Keep existing workflow as backup
mv .github/workflows/verify-readme.yml .github/workflows/verify-readme-single.yml.bak

# Add multi-OS workflow
cp .github/workflows/verify-readme-multi-os.yml your-project/.github/workflows/

# Test it
git add .github/workflows/
git commit -m "Upgrade to multi-OS verification"
git push
```

---

## 📊 What You'll See

### Multi-OS Badges

Your README will display badges like this:

```markdown
![Multi-OS Status](https://img.shields.io/badge/multi--os-passing-brightgreen)
![macOS](https://img.shields.io/badge/macOS-✓%20100%25-brightgreen)
![Ubuntu](https://img.shields.io/badge/Ubuntu-✓%20100%25-brightgreen)
![Windows](https://img.shields.io/badge/Windows-✓%2095%25-yellow)
![Last Verified](https://img.shields.io/badge/last%20verified-01%2F20%2F2026-lightgrey)
```

### Results Structure

```
.github/readme-verifier/
├── combined-results.json          # Aggregated multi-OS results
└── history/
    ├── results-macOS.json         # macOS-specific results
    ├── results-Ubuntu.json        # Ubuntu-specific results
    └── results-Windows.json       # Windows-specific results
```

### GitHub Actions Summary

In the Actions tab, you'll see:

```
📊 Multi-OS Verification Summary

| OS       | Total | Success | Failed | Warnings | Success Rate |
|----------|-------|---------|--------|----------|--------------|
| ✅ macOS   | 5     | 5       | 0      | 0        | 100%         |
| ✅ Ubuntu  | 5     | 5       | 0      | 0        | 100%         |
| ⚠️ Windows | 5     | 4       | 1      | 0        | 80%          |
```

---

## 🎯 Use Cases

### Use Case 1: Cross-Platform CLI Tools

Perfect for command-line tools that must work everywhere:

```markdown
---
verify: true
step: "check-cli"
description: "Verify CLI works on all platforms"
---
```bash
your-cli --version
```

### Use Case 2: Development Environment Setup

Ensure your setup works for all contributors:

```markdown
---
verify: true
step: "install-deps"
description: "Install dependencies (cross-platform)"
---
```bash
npm install
```

### Use Case 3: Platform-Specific Features

Test optional platform-specific features:

```markdown
---
verify: true
step: "macos-feature"
description: "macOS-specific feature (optional)"
required: false
---
```bash
if [ "$(uname)" = "Darwin" ]; then
  echo "macOS-specific setup"
fi
```

---

## 📋 Comparison: Single-OS vs Multi-OS

| Feature | Single-OS | Multi-OS |
|---------|-----------|----------|
| **OSes Tested** | 1 (macOS) | 3 (macOS, Ubuntu, Windows) |
| **CI Minutes** | ~2-5 min/run | ~6-15 min/run |
| **Badges** | 3-4 badges | 4-5 badges |
| **Results Files** | 1 file | 4 files (1 combined + 3 per OS) |
| **Manual Trigger** | Yes | Yes (with OS selection) |
| **Issue Creation** | Yes | Yes (shows which OS failed) |
| **Best For** | Single-platform projects | Cross-platform projects |

---

## 💰 Cost Consideration

### GitHub Actions Free Tier

- **Free tier:** 2,000 minutes/month for public repos
- **Single-OS:** ~5 min/day × 30 days = 150 min/month
- **Multi-OS:** ~15 min/day × 30 days = 450 min/month

**Still well within free tier!** ✅

### Optimization Options

If you want to reduce costs:

1. **Run less frequently:**
   ```yaml
   schedule:
     - cron: '0 2 * * 1'  # Weekly instead of daily
   ```

2. **Test fewer OSes:**
   ```yaml
   matrix:
     os: [macos-latest, ubuntu-latest]  # Skip Windows
   ```

3. **Use fail-fast:**
   ```yaml
   strategy:
     fail-fast: true  # Stop if one OS fails
   ```

---

## 🔧 Advanced Features

### 1. Manual OS Selection

Trigger workflow and choose which OS to test:

1. Go to Actions tab
2. Click "Verify README (Multi-OS)"
3. Click "Run workflow"
4. Select OS: all / macos / ubuntu / windows
5. Run!

### 2. Per-OS Results

View individual OS results:

```bash
# View macOS results
cat .github/readme-verifier/history/results-macOS.json

# View Ubuntu results
cat .github/readme-verifier/history/results-Ubuntu.json

# View Windows results
cat .github/readme-verifier/history/results-Windows.json
```

### 3. Combined Summary

```bash
# View aggregated results
cat .github/readme-verifier/combined-results.json
```

Sample output:

```json
{
  "timestamp": "2026-01-20T02:00:00.000Z",
  "results_by_os": {
    "macOS": {"total": 5, "success": 5, "failed": 0},
    "Linux": {"total": 5, "success": 5, "failed": 0},
    "Windows": {"total": 5, "success": 4, "failed": 1}
  }
}
```

---

## 📚 Documentation

### Complete Guides

1. **[MULTI_OS_GUIDE.md](docs/MULTI_OS_GUIDE.md)**
   - Complete multi-OS documentation
   - Best practices
   - Troubleshooting
   - Migration guide

2. **[README.cross-platform.md](examples/README.cross-platform.md)**
   - Working example
   - Shows all patterns
   - Copy-paste ready

3. **[Workflow file](.github/workflows/verify-readme-multi-os.yml)**
   - Fully commented
   - Ready to use
   - Customizable

---

## 🎓 Migration Guide

### Step 1: Backup

```bash
cp .github/workflows/verify-readme.yml .github/workflows/verify-readme-single.yml.bak
```

### Step 2: Add Multi-OS Files

```bash
cp .github/workflows/verify-readme-multi-os.yml your-project/.github/workflows/
cp scripts/generate-multi-os-badges.py your-project/scripts/
```

### Step 3: Update README

Add multi-OS badge markers (already have the standard markers? You're good!):

```markdown
<!-- VERIFICATION-BADGES -->
<!-- Badges will update automatically -->
<!-- END-VERIFICATION-BADGES -->
```

### Step 4: Test

```bash
git add .github/ scripts/
git commit -m "Add multi-OS verification"
git push

# Manually trigger to test
# Go to Actions tab → Run workflow → Select "all"
```

### Step 5: Monitor

Check Actions tab to see all 3 OSes running!

### Step 6: Clean Up (Optional)

Once satisfied, remove single-OS workflow:

```bash
git rm .github/workflows/verify-readme.yml
git commit -m "Remove single-OS workflow"
```

---

## ❓ FAQ

**Q: Do I need multi-OS if my project only runs on Linux?**  
A: No, stick with single-OS. Multi-OS is for cross-platform projects.

**Q: Can I test only 2 OSes?**  
A: Yes! Edit the matrix to remove one OS.

**Q: Will this use 3x the GitHub Actions minutes?**  
A: Approximately, yes. But it's still within free tier for most projects.

**Q: What if a step fails on Windows but not macOS?**  
A: The workflow creates an issue showing which OS failed. You can mark the step as `required: false` or fix it to work cross-platform.

**Q: Can I have different steps per OS?**  
A: Yes! Use shell conditionals to detect the OS and run different commands.

**Q: How do I test locally on all OSes?**  
A: You need access to all 3 OSes. Most developers test on their primary OS and let CI test the others.

---

## 🎉 Summary

**Multi-OS support gives you:**

- ✅ Verification on macOS, Ubuntu, and Windows
- ✅ Individual badges per OS
- ✅ Aggregated results
- ✅ Better cross-platform compatibility
- ✅ More confidence in your documentation

**Perfect for:**
- Cross-platform CLI tools
- Libraries used on multiple OSes
- Development environment setups
- Open-source projects with diverse users

**Your documentation now works everywhere!** 🌍

---

## 🔗 Related Documentation

- [QUICK_REFERENCE.md](docs/QUICK_REFERENCE.md) - Format reference
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) - Common issues
- [FAQ.md](docs/FAQ.md) - Questions answered
- [examples/](examples/) - More examples

---

**Ready to go multi-OS?** Copy the workflow file and you're done! 🚀
