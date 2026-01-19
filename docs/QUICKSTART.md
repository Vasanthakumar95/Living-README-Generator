# 🚀 Quick Start Guide

Get your Living README Generator running in 5 minutes!

## TL;DR

```bash
# 1. Copy files to your project
cp scripts/verify-readme.py your-project/scripts/
cp .github/workflows/verify-readme.yml your-project/.github/workflows/
cp .github/readme-verifier/config.yml your-project/.github/readme-verifier/

# 2. Add badges to your README
Add this after your title:
<!-- VERIFICATION-BADGES -->
<!-- END-VERIFICATION-BADGES -->

# 3. Mark a code block for verification
---
verify: true
step: "install-deps"
---
```bash
npm install
```

# 4. Test it
python3 scripts/verify-readme.py README.md

# 5. Push and you're done!
```

## File Structure

You'll need these files in your project:

```
your-project/
├── .github/
│   ├── workflows/
│   │   └── verify-readme.yml       ← GitHub Action workflow
│   └── readme-verifier/
│       ├── config.yml              ← Settings (optional)
│       └── results.json            ← Auto-generated results
├── scripts/
│   ├── verify-readme.js            ← Node.js version (if you use Node)
│   └── verify-readme.py            ← Python version (works anywhere)
└── README.md                        ← Your README with verification
```

## Option A: Use Node.js Version

**Prerequisites:** Node.js installed

```bash
# 1. Install dependency
npm install js-yaml --save-dev

# 2. Run verification
node scripts/verify-readme.js README.md
```

## Option B: Use Python Version

**Prerequisites:** Python 3.7+ with PyYAML

```bash
# 1. Install dependency (if needed)
pip install pyyaml

# 2. Run verification
python3 scripts/verify-readme.py README.md
```

## Minimal Example

Here's the absolute minimum to get started:

### 1. Update your README.md

```markdown
# My Project

<!-- VERIFICATION-BADGES -->
<!-- END-VERIFICATION-BADGES -->

## Installation

---
verify: true
step: "install"
---
\`\`\`bash
npm install
\`\`\`
```

### 2. Test locally

```bash
python3 scripts/verify-readme.py README.md
```

### 3. See the magic

```
🚀 Starting README verification...

Found 1 verification step(s)

🔍 Executing: install
   ✅ Success (1523ms)

📊 VERIFICATION REPORT
Total Steps:    1
✅ Success:      1
Success Rate: 100%

📝 README.md updated with verification badges
```

Your README now has badges:

```markdown
# My Project

<!-- VERIFICATION-BADGES -->
![Setup Status](https://img.shields.io/badge/setup-passing-brightgreen)
![Last Verified](https://img.shields.io/badge/last%20verified-1%2F19%2F2026-lightgrey)
<!-- END-VERIFICATION-BADGES -->
```

## What Happens Next?

### In CI (GitHub Actions)

1. **Daily at 2 AM UTC** - Workflow runs automatically
2. **Executes all steps** - Runs commands in sequence
3. **Updates badges** - Commits new badges to README
4. **Creates issues** - If steps fail, auto-creates GitHub issue

### Manual Runs

You can trigger manually:
- In GitHub: Actions → "Verify README" → "Run workflow"
- Locally: `python3 scripts/verify-readme.py README.md`

## Common Patterns

### Pattern 1: Prerequisites Check

```markdown
---
verify: true
step: "check-node"
---
\`\`\`bash
node --version
\`\`\`
```

### Pattern 2: Multi-step Setup

```markdown
---
verify: true
step: "install-deps"
---
\`\`\`bash
npm install
\`\`\`

---
verify: true
step: "setup-config"
---
\`\`\`bash
cp .env.example .env
\`\`\`

---
verify: true
step: "run-tests"
---
\`\`\`bash
npm test
\`\`\`
```

### Pattern 3: Optional Steps

```markdown
---
verify: true
step: "optional-build"
required: false
---
\`\`\`bash
npm run build
\`\`\`
```

### Pattern 4: Long Operations

```markdown
---
verify: true
step: "slow-build"
timeout: 300000
---
\`\`\`bash
npm run build:prod
\`\`\`
```

## Troubleshooting

### "No verification steps found"
➜ Make sure you have `verify: true` in the YAML frontmatter

### "Command not found"
➜ Check that the command works in CI environment

### Badges not showing
➜ Make sure you have the `<!-- VERIFICATION-BADGES -->` markers

### Steps failing in CI but work locally
➜ CI runs in clean environment - might be missing dependencies

## Next Steps

Once you're comfortable:

1. **Read full docs**: Check `README.md` for all options
2. **Customize**: Edit `.github/readme-verifier/config.yml`
3. **Add more steps**: Verify your entire setup process
4. **Share**: Show your team the green badges! ✨

## Support

- **Issues**: Check `SETUP_GUIDE.md` for detailed troubleshooting
- **Examples**: See `README.example.md` for more patterns
- **Architecture**: Read `ARCHITECTURE.md` to understand how it works

---

**You're all set! Your README will never lie again.** 🎉
