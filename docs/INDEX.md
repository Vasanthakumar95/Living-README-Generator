# 📚 Living README Generator - Documentation Index

**Stop the rot. Your README setup instructions, automatically verified.**

## 🎯 What is this?

A system that automatically tests your README setup instructions in CI, updates status badges, and alerts you when setup steps break. No more outdated, lying documentation!

## 🚀 Getting Started (Pick Your Path)

### I want to get started NOW (5 minutes)
→ **[QUICKSTART.md](QUICKSTART.md)** - Copy files, run once, done.

### I want to understand it first (10 minutes)
→ **[README.md](README.md)** - Full overview, features, and examples

### I want step-by-step instructions (20 minutes)
→ **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup with troubleshooting

### I want to see before/after (5 minutes)
→ **[BEFORE_AFTER.md](BEFORE_AFTER.md)** - Real examples and ROI analysis

## 📂 File Guide

### Core Files (You Need These)

| File | Purpose | When to Use |
|------|---------|-------------|
| **scripts/verify-readme.js** | Node.js verification engine | If your project uses Node.js |
| **scripts/verify-readme.py** | Python verification engine | Works on any system with Python |
| **.github/workflows/verify-readme.yml** | GitHub Actions workflow | To run verification in CI |
| **.github/readme-verifier/config.yml** | Configuration settings | To customize behavior (optional) |

### Documentation Files (For Learning)

| File | Purpose | When to Read |
|------|---------|--------------|
| **README.md** | Main documentation | Start here for overview |
| **QUICKSTART.md** | 5-minute setup guide | When you want to move fast |
| **SETUP_GUIDE.md** | Detailed setup instructions | For step-by-step setup |
| **BEFORE_AFTER.md** | Problem/solution examples | To understand the value |
| **ARCHITECTURE.md** | System design + diagram | To understand how it works |

### Example Files (For Reference)

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.example.md** | Full example with all features | Copy patterns from here |
| **TEST_README.md** | Minimal working example | See simplest possible setup |
| **.github/readme-verifier/results.json** | Sample results output | See what the output looks like |

### Supporting Files

| File | Purpose |
|------|---------|
| **package.json** | Node.js dependencies |
| **.gitignore** | Files to exclude from git |

## 🎓 Learning Path

### Beginner Path (30 minutes total)

1. **Start**: Read [README.md](README.md) - 10 min
   - Understand the problem
   - See what it does
   - Check if it fits your needs

2. **Setup**: Follow [QUICKSTART.md](QUICKSTART.md) - 5 min
   - Copy files
   - Add one verification step
   - Run locally

3. **Expand**: Review [README.example.md](README.example.md) - 10 min
   - See all YAML options
   - Copy patterns you need
   - Add more verification steps

4. **Deploy**: Push to GitHub - 5 min
   - Commit changes
   - Watch Actions run
   - See badges update

### Advanced Path (1-2 hours)

1. **Deep Dive**: Read [SETUP_GUIDE.md](SETUP_GUIDE.md) - 20 min
   - Learn all options
   - Understand troubleshooting
   - Master best practices

2. **Architecture**: Study [ARCHITECTURE.md](ARCHITECTURE.md) - 15 min
   - Understand the system
   - See data flow
   - Learn how components interact

3. **Customize**: Edit [config.yml](.github/readme-verifier/config.yml) - 15 min
   - Adjust schedule
   - Configure notifications
   - Set security options

4. **Optimize**: Refine your verification - 30 min
   - Add optional steps
   - Set appropriate timeouts
   - Test edge cases

## 💡 Common Use Cases

### Use Case 1: "I just want green badges on my README"
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Copy 3 files to your project
3. Add `verify: true` to your main setup step
4. Push to GitHub
5. Done!

### Use Case 2: "Our setup is complex (10+ steps)"
1. Read [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. Review [README.example.md](README.example.md) for patterns
3. Mark each major step with `verify: true`
4. Use `required: false` for optional steps
5. Set appropriate `timeout` values

### Use Case 3: "I want to verify on multiple OS"
Currently supports macOS. Ubuntu/Windows coming soon.
Check [README.md](README.md) roadmap section.

### Use Case 4: "I need this for my team's 20 repos"
1. Read [BEFORE_AFTER.md](BEFORE_AFTER.md) - make the case
2. Create a template repo with the setup
3. Share [QUICKSTART.md](QUICKSTART.md) with your team
4. Set up once, benefit everywhere

## 🔍 Quick Reference

### YAML Frontmatter Options

```yaml
---
verify: true                    # Enable verification (required)
step: "unique-name"             # Step identifier
description: "What this does"   # Human-readable description
required: true                  # Fail build if this fails (default)
timeout: 60000                  # Max time in milliseconds
workingDir: "."                 # Directory to run in
---
```

### Badge Markers

```markdown
<!-- VERIFICATION-BADGES -->
<!-- Badges auto-generated here -->
<!-- END-VERIFICATION-BADGES -->
```

### Running Verification

```bash
# Node.js version
node scripts/verify-readme.js README.md

# Python version
python3 scripts/verify-readme.py README.md
```

## 🎯 Decision Tree: Which Files Do I Need?

```
Do you use Node.js in your project?
├─ YES → Use verify-readme.js + install js-yaml
└─ NO  → Use verify-readme.py + install pyyaml

Do you use GitHub?
├─ YES → Copy verify-readme.yml to .github/workflows/
└─ NO  → Run verification manually or use other CI

Do you want to customize behavior?
├─ YES → Copy and edit config.yml
└─ NO  → Skip it (has sensible defaults)

Do you need examples?
├─ YES → Look at README.example.md
└─ NO  → Just start with QUICKSTART.md
```

## 📊 File Size Reference

| File | Size | Complexity |
|------|------|------------|
| verify-readme.js | ~300 lines | Medium |
| verify-readme.py | ~300 lines | Medium |
| verify-readme.yml | ~100 lines | Simple |
| config.yml | ~80 lines | Simple |

## ❓ FAQ Shortcuts

**Q: How much time will this take?**
→ Read: [QUICKSTART.md](QUICKSTART.md) → 5 minutes

**Q: What if my setup steps break?**
→ Read: [README.md](README.md) section "Monitoring"

**Q: Can I test this without committing?**
→ Read: [SETUP_GUIDE.md](SETUP_GUIDE.md) section "Test Locally"

**Q: What are the ROI benefits?**
→ Read: [BEFORE_AFTER.md](BEFORE_AFTER.md) section "Cost-Benefit Analysis"

**Q: How does it actually work?**
→ Read: [ARCHITECTURE.md](ARCHITECTURE.md)

## 🔗 External Resources

- **GitHub Actions Docs**: For understanding CI/CD
- **shields.io**: For understanding badges
- **YAML Spec**: For YAML frontmatter syntax

## 🆘 Getting Help

1. **Check docs**: 90% of questions answered in this repo
2. **Review examples**: See [README.example.md](README.example.md)
3. **Read troubleshooting**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
4. **Check logs**: Look at GitHub Actions output

## 🎉 Success Checklist

- [ ] Read overview in [README.md](README.md)
- [ ] Followed [QUICKSTART.md](QUICKSTART.md)
- [ ] Added badge markers to README
- [ ] Marked at least one step with `verify: true`
- [ ] Tested locally with verification script
- [ ] Pushed to GitHub
- [ ] Saw GitHub Action run successfully
- [ ] Badges appeared in README
- [ ] Verified badges update daily

## 🚀 Next Steps After Setup

1. **Monitor**: Watch for issues when setup breaks
2. **Expand**: Add more verification steps
3. **Share**: Show your team the green badges
4. **Contribute**: Suggest improvements or add features

## 📝 Contribution Areas

Want to help improve this?

- Add support for Ubuntu/Windows (see verify-readme.yml)
- Create Docker isolation feature
- Build visual dashboard for history
- Add more notification channels (Slack, Discord)
- Write additional examples for different tech stacks

---

## 🎓 Recommended Reading Order

### For Developers (Quick Setup)
1. README.md (overview)
2. QUICKSTART.md (setup)
3. README.example.md (copy patterns)

### For Teams (Understanding + Setup)
1. BEFORE_AFTER.md (see the value)
2. README.md (understand solution)
3. SETUP_GUIDE.md (detailed setup)
4. README.example.md (copy patterns)

### For Contributors (Deep Dive)
1. README.md (overview)
2. ARCHITECTURE.md (system design)
3. verify-readme.js or .py (implementation)
4. config.yml (configuration options)

---

**Pick your starting point above and get going! Your README will thank you.** ✨
