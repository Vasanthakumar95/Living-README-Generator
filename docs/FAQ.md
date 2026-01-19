# Frequently Asked Questions (FAQ)

## General Questions

### What is Living README Generator?

A tool that automatically verifies your README setup instructions in CI, updates status badges, and alerts you when steps break. Think of it as continuous testing for your documentation.

### Why do I need this?

READMEs rot quickly. Setup instructions that worked last month often break due to:
- Dependency updates
- Command changes
- Configuration drift
- File moves/renames
- Environment changes

This tool catches these issues automatically before users do.

### How much does it cost?

**Free** if you're using GitHub Actions public repos (free tier includes 2,000 minutes/month).

For private repos, verification runs take ~2-5 minutes each. Running daily = ~60-150 minutes/month, well within free tier limits.

### How long does setup take?

- **Minimal setup**: 5 minutes
- **Full setup with multiple steps**: 15-30 minutes
- **Understanding + setup**: 1 hour

## Technical Questions

### Which programming language do I need?

You can choose:
- **Node.js version** - If your project already uses Node.js
- **Python version** - Works everywhere, no Node.js required

Both versions have identical features. Pick whichever fits your project better.

### Do I need to know GitHub Actions?

No! The workflow file is pre-configured. Just copy it and it works. You can customize it later if needed.

### Can I use this with other CI systems?

The verification scripts (`verify-readme.js` or `.py`) work standalone. You can run them in:
- GitLab CI
- CircleCI
- Travis CI
- Jenkins
- Any CI system that can run Node.js or Python

You'll just need to adapt the workflow file to your CI system's syntax.

### What operating systems are supported?

Currently: **macOS** (runs on GitHub's macOS runners)

Coming soon: Ubuntu, Windows

You can run the scripts locally on any OS that has Node.js or Python.

## Setup Questions

### Where do the files go in my project?

```
your-project/
├── .github/
│   └── workflows/
│       └── verify-readme.yml        ← GitHub Actions workflow
├── scripts/
│   └── verify-readme.py (or .js)    ← Verification script
└── README.md                         ← Your README with verification
```

### Can I test without committing?

**Yes!** Run locally:

```bash
# Python version
python3 scripts/verify-readme.py README.md

# Node.js version
node scripts/verify-readme.js README.md
```

This shows you exactly what will happen in CI.

### How do I mark steps for verification?

Add YAML frontmatter above any code block:

```markdown
---
verify: true
step: "unique-name"
description: "What this step does"
---
\`\`\`bash
your command here
\`\`\`
```

### Do I need to mark every code block?

No! Only mark the setup/installation steps you want verified. Code examples, usage snippets, etc. don't need verification.

### What if I have multiple code languages in my README?

No problem! Mark whichever steps make sense to verify:

```markdown
---
verify: true
step: "install-node-deps"
---
\`\`\`bash
npm install
\`\`\`

---
verify: true
step: "install-python-deps"
---
\`\`\`bash
pip install -r requirements.txt
\`\`\`
```

## Verification Questions

### When does verification run?

By default: **Daily at 2 AM UTC**

You can customize this in `.github/workflows/verify-readme.yml`:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Change this
```

### Can I run verification manually?

**Yes!** Two ways:

1. **Locally**: `python3 scripts/verify-readme.py README.md`
2. **In GitHub**: Actions tab → "Verify README" → "Run workflow"

### What happens if a step fails?

1. Verification stops (if step is required)
2. Badge turns red
3. GitHub issue is automatically created
4. Results are saved to `.github/readme-verifier/results.json`
5. Workflow fails (alerting maintainers)

### Can I make steps optional?

Yes! Use `required: false`:

```yaml
---
verify: true
step: "optional-lint"
required: false
---
\`\`\`bash
npm run lint
\`\`\`
```

Optional steps show warnings but don't fail the build.

### How do I handle long-running steps?

Set a custom timeout (in milliseconds):

```yaml
---
verify: true
step: "slow-build"
timeout: 300000  # 5 minutes
---
\`\`\`bash
npm run build
\`\`\`
```

Default timeout is 60 seconds.

## Badge Questions

### Where do badges appear?

Wherever you put the markers:

```markdown
<!-- VERIFICATION-BADGES -->
<!-- Badges auto-generated here -->
<!-- END-VERIFICATION-BADGES -->
```

Typically placed right after your project title.

### What do the badges show?

- **Setup Status**: passing/partial/failing
- **Verified On**: Which OS (macOS, Linux, etc.)
- **Last Verified**: Date of last successful check
- **Success Rate**: Percentage of steps passing

### Can I customize badge appearance?

Yes! Edit the badge generation in the verification script or use shields.io query parameters. See [shields.io documentation](https://shields.io/).

### Do badges update automatically?

Yes! The workflow commits badge updates back to your README after each verification run.

## Troubleshooting Questions

### "No verification steps found"

**Cause**: No code blocks have `verify: true` in YAML frontmatter.

**Fix**: Add YAML frontmatter above at least one code block.

### "Command not found" in CI

**Cause**: Command works locally but not in CI environment.

**Fix**: 
- Ensure tools are installed in CI (add setup steps)
- Check that paths are correct
- Verify commands work in clean environment

### Steps pass locally but fail in CI

**Cause**: CI runs in a clean environment without your local setup.

**Fix**:
- Don't rely on locally installed tools
- Make sure all dependencies are installed in prior steps
- Use relative paths, not absolute

### Badges not appearing

**Cause**: Missing badge markers or workflow didn't commit.

**Fix**:
1. Ensure `<!-- VERIFICATION-BADGES -->` markers exist
2. Check workflow has write permissions
3. Review GitHub Actions logs for errors

### How do I see detailed error messages?

Check these locations:
1. **Local**: Terminal output when running script
2. **CI**: GitHub Actions logs (Actions tab)
3. **Results**: `.github/readme-verifier/results.json`
4. **Issues**: Auto-created GitHub issue with details

## Advanced Questions

### Can I verify multiple READMEs?

Yes! Run the script multiple times:

```yaml
# In your workflow
- name: Verify main README
  run: python3 scripts/verify-readme.py README.md

- name: Verify docs README  
  run: python3 scripts/verify-readme.py docs/README.md
```

### Can steps depend on each other?

Yes, by default! Steps run **sequentially** in order. Step 3 can depend on steps 1-2 completing successfully.

### Can I run steps in different directories?

Yes! Use `workingDir`:

```yaml
---
verify: true
step: "backend-setup"
workingDir: "./backend"
---
\`\`\`bash
npm install
\`\`\`
```

### Can I skip certain steps in CI?

Use environment variables or CI detection:

```yaml
---
verify: true
step: "dev-only-step"
---
\`\`\`bash
if [ -z "$CI" ]; then npm run dev-setup; fi
\`\`\`
```

### How do I verify GUI/interactive commands?

You can't directly verify interactive commands. Instead:

1. Mock the interaction:
```bash
echo "y" | interactive-command
```

2. Just verify the tool exists:
```bash
which interactive-tool
```

3. Mark as optional and test manually

### Can I integrate with monitoring tools?

Yes! Parse `.github/readme-verifier/results.json`:

```json
{
  "timestamp": "2026-01-19T02:00:00Z",
  "steps": [...],
  "environment": {...}
}
```

Send to your monitoring system (Datadog, Prometheus, etc.).

## Contribution Questions

### How can I contribute?

See `CONTRIBUTING.md` for guidelines. Some areas:
- Add support for more operating systems
- Create additional templates
- Improve documentation
- Add features (notifications, dashboards, etc.)

### Can I use this in my company?

Yes! MIT licensed. Use freely in personal or commercial projects.

### Where do I report bugs?

Open a GitHub issue with:
- Description of the problem
- Your README snippet
- Error message
- CI logs if available

---

## Still have questions?

- **Check docs**: Review `docs/` folder
- **Search issues**: Someone may have asked already
- **Open an issue**: We're happy to help!
