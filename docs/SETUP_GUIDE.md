# Setup Guide: Living README Generator

This guide will walk you through setting up the Living README Generator in your project.

## Prerequisites

- Node.js 14+ installed
- A GitHub repository
- Basic familiarity with GitHub Actions

## Step-by-Step Setup

### 1. Add Files to Your Project

Copy these files to your repository:

```
your-project/
├── .github/
│   ├── workflows/
│   │   └── verify-readme.yml       # GitHub Action workflow
│   └── readme-verifier/
│       └── config.yml              # Configuration
├── scripts/
│   └── verify-readme.js            # Main verification script
└── package.json                    # Add js-yaml dependency
```

### 2. Install Dependencies

Add the required dependency to your `package.json`:

```bash
npm install js-yaml --save-dev
```

Or add manually:

```json
{
  "devDependencies": {
    "js-yaml": "^4.1.0"
  }
}
```

### 3. Update Your README

#### Add Badge Placeholder

Add this near the top of your README (typically after the title):

```markdown
# Your Project Name

<!-- VERIFICATION-BADGES -->
<!-- Badges will appear here -->
<!-- END-VERIFICATION-BADGES -->

Your project description...
```

#### Mark Setup Steps for Verification

Find your setup instructions and add YAML frontmatter:

**Before:**
```markdown
## Installation

Install dependencies:

\`\`\`bash
npm install
\`\`\`
```

**After:**
```markdown
## Installation

Install dependencies:

---
verify: true
step: "install-dependencies"
description: "Install all project dependencies"
---
\`\`\`bash
npm install
\`\`\`
```

### 4. Test Locally

Before committing, test your setup:

```bash
# Run verification
node scripts/verify-readme.js README.md

# Expected output:
# 🚀 Starting README verification...
# 
# Found 1 verification step(s)
# 
# 🔍 Executing: install-dependencies
#    Install all project dependencies
#    ✅ Success (1234ms)
# 
# ====================================================
# 📊 VERIFICATION REPORT
# ====================================================
# Total Steps:    1
# ✅ Success:      1
# ❌ Failed:       0
# ⚠️  Warnings:     0
# 📈 Success Rate: 100%
```

### 5. Configure GitHub Actions (Optional)

Review and customize `.github/readme-verifier/config.yml`:

```yaml
settings:
  # When to run (default: daily at 2 AM UTC)
  schedule: "0 2 * * *"
  
  # Create GitHub issues when verification fails
  createIssues: true

badges:
  enabled: true
  location: "top"  # or "bottom"
```

### 6. Commit and Push

```bash
git add .
git commit -m "Add Living README Generator"
git push
```

### 7. Enable GitHub Actions (If Needed)

1. Go to your repository on GitHub
2. Click "Actions" tab
3. If prompted, enable GitHub Actions
4. The workflow will run automatically on schedule

### 8. Manual Trigger (Optional)

To run verification immediately:

1. Go to **Actions** tab in your GitHub repo
2. Click **"Verify README Setup Instructions"**
3. Click **"Run workflow"**
4. Select the branch and click **"Run workflow"**

## Example: Real Project Setup

Let's say you have a typical Node.js project. Here's how to mark it:

```markdown
# My Awesome API

<!-- VERIFICATION-BADGES -->
<!-- END-VERIFICATION-BADGES -->

## Prerequisites

Ensure you have Node.js 18 or higher:

---
verify: true
step: "check-node-version"
description: "Verify Node.js 18+ is installed"
---
\`\`\`bash
node --version | grep -E "v1[8-9]|v2[0-9]"
\`\`\`

## Installation

Clone and install:

---
verify: true
step: "install-dependencies"
description: "Install all dependencies"
timeout: 120000
---
\`\`\`bash
npm install
\`\`\`

## Configuration

Copy the example environment file:

---
verify: true
step: "setup-env"
description: "Create .env file"
---
\`\`\`bash
cp .env.example .env
\`\`\`

## Database Setup

Run migrations:

---
verify: true
step: "run-migrations"
description: "Set up database schema"
---
\`\`\`bash
npm run migrate
\`\`\`

## Verify Installation

Run the test suite:

---
verify: true
step: "run-tests"
description: "Verify everything works"
---
\`\`\`bash
npm test
\`\`\`
```

## Troubleshooting

### "No verification steps found"

**Problem:** Verifier doesn't find any steps.

**Solution:** Check your YAML frontmatter syntax:
- Must have `---` before and after
- Must include `verify: true`
- Must be directly above a code block with \`\`\`

### "Command not found" errors

**Problem:** Verification fails because commands aren't available.

**Solution:** 
- Check that the command works in GitHub Actions environment
- Add any required setup steps first (e.g., install tools)
- Use absolute paths if needed

### Badges not updating

**Problem:** Badges don't appear or don't update.

**Solution:**
1. Check that `<!-- VERIFICATION-BADGES -->` tags exist in README
2. Verify the workflow has write permissions to the repo
3. Check Actions tab for errors
4. Ensure `[skip ci]` isn't in commit message

### Timeout errors

**Problem:** Steps fail with timeout errors.

**Solution:** Increase timeout in YAML frontmatter:

```yaml
---
verify: true
step: "slow-step"
timeout: 300000  # 5 minutes
---
```

### Steps fail in CI but work locally

**Problem:** Works on your machine, fails in CI.

**Solution:**
- CI runs on clean macOS environment
- Check for missing dependencies
- Verify no hardcoded paths
- Ensure no interactive prompts

## Best Practices

### ✅ Do

- **Mark critical setup steps** that users must complete
- **Use descriptive step names** like `install-dependencies` not `step1`
- **Add helpful descriptions** to explain what each step does
- **Set appropriate timeouts** for long-running operations
- **Mark optional steps** with `required: false`
- **Test locally first** before committing

### ❌ Don't

- **Don't mark every code block** - only setup instructions
- **Don't include interactive commands** that need user input
- **Don't rely on external services** that might be down
- **Don't use destructive commands** like `rm -rf`
- **Don't hardcode paths** that won't exist in CI
- **Don't skip the badge placeholder** - badges won't show up

## Getting Help

If you run into issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review the [FAQ](README.md#faq) in the main README
3. Check GitHub Actions logs for detailed error messages
4. Open an issue with:
   - Your README snippet
   - Error message
   - CI logs

## Next Steps

Once set up:

- ⭐ Watch your README badges update automatically
- 📊 Check `.github/readme-verifier/results.json` for detailed results
- 🔔 Get notified via GitHub issues when setup breaks
- 🎯 Keep your setup instructions fresh and trustworthy

---

**You're all set! Your README will now stay accurate forever.** 🎉
