# Living README Generator 📝✨
> **Stop the rot.** Automatically verify your README setup instructions so they never lie again.

<!-- VERIFICATION-BADGES -->
## 📊 Multi-OS Verification Status

**Last Verified:** February 17, 2026 at 04:18 AM UTC

| OS | Total | Success | Failed | Warnings | Success Rate |
|---|---|---|---|---|---|
| ✅ macOS (Darwin) | 1 | 1 | 0 | 0 | 100% |
| ✅ Ubuntu (Linux) | 1 | 1 | 0 | 0 | 100% |
| ✅ Windows | 1 | 1 | 0 | 0 | 100% |

**Overall Statistics:**
- Total Steps Across All Platforms: 3
- Total Successful: 3
- Total Failed: 0
- Total Warnings: 0
- Combined Success Rate: 100%

<!-- END-VERIFICATION-BADGES -->

### ✅ Verification Demonstration (This Project)

````text
---
verify: true
step: "check-node"
description: "Ensure Node.js 18+"
required: true            
timeout: 60000            
workingDir: "."           
---
```bash
node -e "const v = parseInt(process.version.slice(1)); if (v < 18) { console.error('Node.js 18+ required'); process.exit(1); } console.log('✓ Node.js v' + v);"
```
````

## Demo
![Demo](demo/living-readme-generator.gif)

## 🎯 Problem

READMEs are the first thing developers see, but they're often:
- ❌ Outdated within weeks
- ❌ Broken on different operating systems
- ❌ Missing critical environment setup steps
- ❌ Never tested after the initial commit

**This is a universal frustration.**

## 💡 Solution

The Living README Generator automatically:
- ✅ Executes your setup instructions in CI
- ✅ Marks each step as verified/broken
- ✅ Updates badges showing "last verified: X days ago"
- ✅ Creates issues when setup breaks
- ✅ Tests on real macOS environments

## 🚀 Quick Start

### Choose Your Path

**Option 1: Use a Template (Recommended)**
```bash
# Copy the minimal template
cp -r templates/minimal/* your-project/
# Or choose nodejs/python template based on your stack
```

**Option 2: Manual Setup**
```bash
# Copy the verification script
cp scripts/verify-readme.py your-project/scripts/
# (or verify-readme.js if you prefer Node.js)

# Copy the GitHub workflow
mkdir -p .github/workflows
cp .github/workflows/verify-readme.yml your-project/.github/workflows/

# Install dependencies
pip install pyyaml  # for Python
# or: npm install js-yaml --save-dev  # for Node.js
```

### Quick Links
- 📖 **New here?** Start with [`docs/INDEX.md`](docs/INDEX.md)
- ⚡ **Quick setup?** See [`docs/QUICKSTART.md`](docs/QUICKSTART.md)
- 📋 **Templates?** Browse [`templates/`](templates/)
- 💡 **Examples?** Check [`examples/`](examples/)

### 2. Mark Your Setup Steps

Add YAML frontmatter above code blocks in your README:

````markdown
---
verify: true
step: "install-dependencies"
description: "Install all project dependencies"
---
\`\`\`bash
npm install
\`\`\`
````

### 3. Add Badge Placeholder

Add the BADGES to your README (typically after the title as shown in this file under title).

### 4. Run Locally

Test your setup:

\`\`\`bash
node scripts/verify-readme.js README.md
\`\`\`bash

### 5. Commit & Let CI Run

Push to your repository. The GitHub Action will:
- Run daily at 2 AM UTC
- Execute all marked steps on macOS
- Update badges automatically
- Create issues if steps fail

## 📖 Documentation

### YAML Frontmatter Options

Mark any code block for verification:

````yaml
---
verify: true              # Enable verification (required)
step: "unique-step-name"  # Unique identifier (auto-generated if omitted)
description: "What this step does"  # Human-readable description
required: true            # Stop verification if this fails (default: true)
timeout: 60000            # Max execution time in ms (default: 60000)
workingDir: "."           # Directory to run command in (default: current)
---
````

### Example: Complete Setup Flow

````markdown
## Installation

Check Node.js version:

---
verify: true
step: "check-node"
description: "Verify Node.js 18+ is installed"
---
\`\`\`bash
node --version | grep -E "v(18|19|20|21)"
\`\`\`

Install dependencies:

---
verify: true
step: "install-deps"
description: "Install all project dependencies"
timeout: 120000
---
\`\`\`bash
npm install
\`\`\`

Optional: Run linter

---
verify: true
step: "lint"
description: "Check code style"
required: false
---
\`\`\`bash
npm run lint
\`\`\`
````

### Sequential Execution

Steps execute **sequentially** by design:
- Mirrors real user experience
- Step 3 can depend on steps 1-2 completing
- Better debugging: know exactly where setup breaks

### Badge States

| Badge | Meaning |
|-------|---------|
| ![passing](https://img.shields.io/badge/setup-passing-brightgreen) | All required steps pass |
| ![partial](https://img.shields.io/badge/setup-partial-yellow) | Required steps pass, optional steps fail |
| ![failing](https://img.shields.io/badge/setup-failing-red) | One or more required steps fail |

## 🎨 Advanced Usage

### Multi-Directory Projects

```markdown
---
verify: true
step: "backend-setup"
workingDir: "./backend"
---
\`\`\`bash
npm install
\`\`\`

---
verify: true
step: "frontend-setup"
workingDir: "./frontend"
---
\`\`\`bash
npm install
\`\`\`
```

### Long-Running Operations

```markdown
---
verify: true
step: "build"
timeout: 300000  # 5 minutes
---
\`\`\`bash
npm run build
\`\`\`
```

### Conditional Steps

```markdown
---
verify: true
step: "optional-cache"
description: "Warm up cache (optional)"
required: false
---
\`\`\`bash
npm run cache:warm
\`\`\`
```

## 📊 Results & Monitoring

### View Results Locally

```bash
node scripts/verify-readme.js README.md
```

Output includes:
- Per-step status (✅/❌/⚠️)
- Execution duration
- Error messages
- Success rate

### View Results in CI

Check the GitHub Actions summary for:
- ✅ Success/failure counts
- 📈 Success rate percentage
- 🕐 Last verification timestamp

### View Historical Data

Results are saved to `.github/readme-verifier/results.json`:

```json
{
  "timestamp": "2026-01-19T02:00:00.000Z",
  "environment": {
    "os": "macOS",
    "arch": "arm64",
    "nodeVersion": "v18.17.0"
  },
  "steps": [
    {
      "name": "check-node",
      "status": "success",
      "duration": 45,
      "output": "v18.17.0"
    }
  ]
}
```

## 🔧 Configuration

Customize behavior in `.github/readme-verifier/config.yml`:

```yaml
settings:
  schedule: "0 2 * * *"        # Daily at 2 AM UTC
  defaultTimeout: 60000         # 1 minute default
  stopOnFailure: true           # Stop on first failure
  createIssues: true            # Auto-create issues

execution:
  sequential: true              # Run steps in order
  preserveEnv: true             # Keep env between steps

badges:
  enabled: true
  location: "top"               # or "bottom"
```

## 🔒 Security

The verifier runs in GitHub Actions with standard security:
- ✅ No sudo/root access
- ✅ Isolated environment per run
- ✅ Same permissions as regular CI
- ⚠️ Be cautious with secrets in setup steps

Blocked commands (configurable):
- `rm -rf`
- `sudo`
- `chmod 777`

## 🚧 Limitations

Current limitations:
- macOS only (Ubuntu/Windows coming soon)
- Sequential execution only
- No Docker isolation yet
- Commands must complete within timeout

## 🗺️ Roadmap

- [ ] Support Ubuntu and Windows runners
- [ ] Docker isolation for safer execution
- [ ] Visual dashboard for verification history
- [ ] Slack/Discord notifications
- [ ] Per-OS badge variants
- [ ] Parallel step execution option
- [ ] Integration with other CI systems

## 🤝 Contributing

Contributions welcome! To add features:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## 📄 License

MIT License - feel free to use in your projects!

## 💬 FAQ

**Q: Does this replace writing good documentation?**  
A: No! This ensures your good documentation stays accurate.

**Q: What if I don't want to verify every code block?**  
A: Only blocks with `verify: true` are executed. The rest are ignored.

**Q: Can I test on multiple operating systems?**  
A: Currently macOS only. Ubuntu/Windows support coming soon.

**Q: How much does this cost?**  
A: GitHub Actions minutes. ~2-5 minutes per run = ~60-150 min/month.

**Q: What if a step needs user input?**  
A: Verification steps should be non-interactive. Use env vars or config files.

**Q: Can I run this outside GitHub Actions?**  
A: Yes! Run `node scripts/verify-readme.js` locally anytime.

---

**Made with ❤️ to end README rot forever.**

[⭐ Star this repo](https://github.com/Vasanthakumar95/Living-README-Generator) if you're tired of outdated docs!
