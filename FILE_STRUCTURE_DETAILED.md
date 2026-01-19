# 📁 Living README Generator - Complete File Structure

This document explains every file and directory in the project.

## 📂 Root Directory

```
living-readme-generator/
│
├── 📄 README.md                    Main project documentation & overview
├── 📄 LICENSE                      MIT License
├── 📄 .gitignore                   Git ignore rules
├── 📄 package.json                 Node.js dependencies and scripts
├── 📄 FILE_STRUCTURE.md           This file - explains the structure
│
├── 📂 docs/                        📚 All documentation
├── 📂 examples/                    💡 Example implementations
├── 📂 scripts/                     🔧 Verification engines
├── 📂 templates/                   📋 Quick-start templates
├── 📂 .github/                     ⚙️  GitHub-specific files
```

---

## 📚 Documentation (`docs/`)

All human-readable documentation for understanding and using the project.

```
docs/
├── 📄 INDEX.md                     📖 Navigation guide - START HERE
│   └── Helps you find the right documentation for your needs
│
├── 📄 QUICKSTART.md                ⚡ 5-minute setup guide
│   └── Minimal steps to get running immediately
│
├── 📄 SETUP_GUIDE.md               📋 Detailed installation instructions
│   └── Step-by-step with troubleshooting and best practices
│
├── 📄 BEFORE_AFTER.md              💡 Problem/solution comparison
│   └── Shows the value with real examples and ROI analysis
│
├── 📄 ARCHITECTURE.md              🏗️  System design documentation
│   └── How everything works together with diagrams
│
├── 📄 FAQ.md                       ❓ Frequently asked questions
│   └── Answers to common questions and troubleshooting
│
└── 📄 CONTRIBUTING.md              🤝 Contribution guidelines
    └── How to contribute code, docs, or ideas
```

**When to read:**
- **New user?** Start with `INDEX.md` → `QUICKSTART.md`
- **Want details?** Read `SETUP_GUIDE.md`
- **Understanding value?** Check `BEFORE_AFTER.md`
- **Deep dive?** Study `ARCHITECTURE.md`
- **Have questions?** See `FAQ.md`
- **Want to contribute?** Read `CONTRIBUTING.md`

---

## 💡 Examples (`examples/`)

Real-world examples you can reference and copy.

```
examples/
├── 📄 README.example.md            Complete example with all features
│   └── Shows every YAML option and verification pattern
```

**When to use:**
- Copy patterns from `README.example.md`
- Reference language-specific examples for your stack

---

## 🔧 Scripts (`scripts/`)

The core verification engines. Pick one based on your project.

```
scripts/
├── 📄 verify-readme.js             Node.js implementation
│   └── Use if: Your project already uses Node.js
│   └── Requires: js-yaml package
│   └── Features: Native Node.js, fast execution
│
├── 📄 verify-readme.py             Python implementation
│   └── Use if: You want universal compatibility
│   └── Requires: pyyaml package
│   └── Features: Works anywhere Python runs
│
└── 📄 README.md                    Scripts documentation
    └── Explains how each script works
```

**Which one to use?**
- **Node.js project?** Use `verify-readme.js`
- **Any other project?** Use `verify-readme.py`
- **Both work equally well** - pick your preference!

**What they do:**
1. Parse your README.md
2. Extract code blocks with `verify: true`
3. Execute commands sequentially
4. Generate badges
5. Update README
6. Save results to JSON

---

## 📋 Templates (`templates/`)

Copy-paste starting points for different project types.

```
templates/
│
├── 📂 minimal/                     Absolute minimum setup
│   ├── 📄 README.md                Template overview
│   ├── 📄 verify-readme.py         Python verification script
│   └── 📄 verify-readme.yml        GitHub Actions workflow
│   └── Use when: You want the simplest possible setup
│
├── 📂 nodejs/                      Node.js project template
│   ├── 📄 README.md                Template overview
│   ├── 📄 verify-readme.js         Node.js verification script
│   ├── 📄 package.json             npm dependencies
│   └── 📄 verify-readme.yml        GitHub Actions workflow
│   └── Use when: Node.js is your primary language
│
└── 📂 python/                      Python project template
    ├── 📄 README.md                Template overview
    ├── 📄 verify-readme.py         Python verification script
    └── 📄 verify-readme.yml        GitHub Actions workflow
    └── Use when: Python is your primary language
```

**How to use templates:**

1. **Choose your template** based on project type
2. **Copy files** to your project:
   ```bash
   cp templates/minimal/* your-project/
   ```
3. **Follow template README.md** for specific instructions
4. **Customize** the example README for your needs

---

## ⚙️ GitHub Configuration (`.github/`)

GitHub Actions workflows and verification configuration.

```
.github/
│
├── 📂 workflows/                   GitHub Actions workflows
│   ├── 📄 verify-readme.yml        Main verification workflow
│   │   └── Runs daily at 2 AM UTC
│   │   └── Executes verification steps
│   │   └── Updates badges and creates issues
│   │
│   ├── 📄 verify-multi-os.yml      Multi-OS verification (planned)
│      └── Will test on macOS, Ubuntu, Windows
│
├── 📂 readme-verifier/             Verification configuration & results
   ├── 📄 config.yml               Configuration settings
   │   └── Customize: schedule, timeouts, notifications
   │   └── Optional: has sensible defaults
   │
   ├── 📄 results.json             Latest verification results
   │   └── Auto-generated after each run
   │   └── Contains: timestamp, environment, step results
   │
   └── 📄 README.md                Config documentation
        └── Explains all configuration options

```

**What goes in your project:**
- ✅ `workflows/verify-readme.yml` (required for CI)
- ⚙️ `readme-verifier/config.yml` (optional customization)
- 📊 `readme-verifier/results.json` (auto-generated)

---

## 📊 File Dependency Map

Shows which files depend on which:

```
Your Project's README.md
    ↓
verify-readme.js or .py (parses README)
    ↓
.github/readme-verifier/config.yml (optional settings)
    ↓
.github/readme-verifier/results.json (output)
    ↓
README.md (badges updated)
```

**CI Flow:**
```
.github/workflows/verify-readme.yml
    ↓ triggers
scripts/verify-readme.js or .py
    ↓ reads
README.md
    ↓ executes steps
System (bash commands)
    ↓ generates
.github/readme-verifier/results.json
    ↓ updates
README.md (with new badges)
```

---

## 🎯 What You Need for Different Goals

### Goal: Quick Setup (5 min)
**You need:**
- `docs/QUICKSTART.md` (read)
- `templates/minimal/` (copy)
- Your README.md (modify)

### Goal: Full Understanding (30 min)
**You need:**
- `README.md` (read)
- `docs/SETUP_GUIDE.md` (read)
- `docs/ARCHITECTURE.md` (read)
- `examples/README.example.md` (reference)

### Goal: Node.js Integration
**You need:**
- `scripts/verify-readme.js` (copy)
- `templates/nodejs/` (reference)
- `.github/workflows/verify-readme.yml` (copy)
- `package.json` (add js-yaml)

### Goal: Python Integration
**You need:**
- `scripts/verify-readme.py` (copy)
- `templates/python/` (reference)
- `.github/workflows/verify-readme.yml` (copy)
- `requirements.txt` (add pyyaml)

### Goal: Customize Behavior
**You need:**
- `.github/readme-verifier/config.yml` (edit)
- `docs/SETUP_GUIDE.md` (reference)

### Goal: Contributing
**You need:**
- `docs/CONTRIBUTING.md` (read)
- `docs/ARCHITECTURE.md` (understand)
- `scripts/` (modify)

---

## 🔍 Finding Files Quickly

**By purpose:**
- **Getting started?** → `docs/INDEX.md` or `docs/QUICKSTART.md`
- **Need examples?** → `examples/`
- **Want templates?** → `templates/`
- **Configuring?** → `.github/readme-verifier/config.yml`
- **Understanding code?** → `scripts/` + `docs/ARCHITECTURE.md`
- **Troubleshooting?** → `docs/FAQ.md` + `docs/SETUP_GUIDE.md`

**By file type:**
- **Markdown (.md):** Documentation and examples
- **JavaScript (.js):** Node.js verification script
- **Python (.py):** Python verification script
- **YAML (.yml):** GitHub Actions workflows and config
- **JSON (.json):** Results and package definitions

---

## 🚀 Recommended Reading Order

**For New Users:**
1. `README.md` (project overview)
2. `docs/INDEX.md` (navigation)
3. `docs/QUICKSTART.md` (setup)
4. `examples/README.example.md` (reference)

**For Developers:**
1. `README.md` (overview)
2. `docs/ARCHITECTURE.md` (system design)
3. `scripts/verify-readme.py` or `.js` (implementation)
4. `docs/CONTRIBUTING.md` (if contributing)

**For Teams:**
1. `docs/BEFORE_AFTER.md` (value proposition)
2. `README.md` (overview)
3. `docs/SETUP_GUIDE.md` (deployment)
4. `templates/` (choose right template)

---

## 📝 Next Steps

1. **Start with** `docs/INDEX.md`
2. **Choose a template** from `templates/`
3. **Copy relevant files** to your project
4. **Follow setup guide** in template's README
5. **Test locally** with verification script
6. **Push and verify** in CI

---

**Questions about file structure?** See `docs/FAQ.md` or open an issue!
