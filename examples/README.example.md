# Example Project

<!-- VERIFICATION-BADGES -->
![Setup Status](https://img.shields.io/badge/setup-passing-brightgreen) ![Verified On](https://img.shields.io/badge/verified%20on-macOS-blue) ![Last Verified](https://img.shields.io/badge/last%20verified-1%2F19%2F2026-lightgrey) ![Success Rate](https://img.shields.io/badge/success%20rate-100%25-brightgreen)
<!-- END-VERIFICATION-BADGES -->

A living README that automatically verifies its setup instructions!

## 🚀 Quick Start

### Prerequisites

Make sure you have Node.js installed. You can verify by running:

---
verify: true
step: "check-node-version"
description: "Verify Node.js is installed"
required: true
---
```bash
node --version
```

### Installation

Clone the repository and install dependencies:

---
verify: true
step: "install-dependencies"
description: "Install project dependencies"
required: true
timeout: 120000
---
```bash
npm install
```

### Configuration

Create your environment configuration:

---
verify: true
step: "create-env-file"
description: "Create .env file from template"
required: true
---
```bash
cp .env.example .env
```

### Running the Application

Start the development server:

---
verify: true
step: "start-dev-server"
description: "Verify the dev server starts successfully"
required: false
timeout: 5000
---
```bash
npm run dev &
sleep 2
kill %1
```

### Running Tests

Execute the test suite:

---
verify: true
step: "run-tests"
description: "Run the test suite"
required: true
---
```bash
npm test
```

## 📝 YAML Frontmatter Options

Each verification block supports the following options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `verify` | boolean | false | Enable verification for this code block |
| `step` | string | auto-generated | Unique identifier for this step |
| `description` | string | "" | Human-readable description |
| `required` | boolean | true | If false, failures won't stop verification |
| `timeout` | number | 60000 | Max execution time in milliseconds |
| `workingDir` | string | current dir | Directory to execute the command in |

## 🔄 How Verification Works

1. **GitHub Actions** runs the verification workflow daily at 2 AM UTC
2. The workflow executes each code block marked with `verify: true`
3. Steps are executed **sequentially** (not isolated)
4. Results are saved to `.github/readme-verifier/results.json`
5. Badges are automatically updated in the README
6. If steps fail, an issue is automatically created

## 🎯 Benefits

- ✅ **Always up-to-date**: Setup instructions are tested daily
- 🔍 **Transparency**: See exactly when instructions were last verified
- 🚨 **Proactive**: Get notified when setup breaks
- 🌍 **Environment-specific**: Tested on actual macOS systems
- 📊 **Metrics**: Track success rates over time

## 🛠️ Manual Verification

You can manually verify the README at any time:

```bash
node scripts/verify-readme.js README.md
```

## 📚 Advanced Usage

### Custom Working Directory

Run commands in a specific directory:

---
verify: true
step: "backend-dependencies"
description: "Install backend dependencies"
workingDir: "./backend"
---
```bash
npm install
```

### Optional Steps

Mark steps as optional (won't fail the build):

---
verify: true
step: "optional-optimization"
description: "Optional performance optimization"
required: false
---
```bash
npm run optimize
```

### Extended Timeout

For long-running operations:

---
verify: true
step: "build-project"
description: "Build the entire project"
timeout: 300000
---
```bash
npm run build
```

## 🤝 Contributing

When updating setup instructions:

1. Add `verify: true` to the YAML frontmatter
2. Test locally: `node scripts/verify-readme.js README.md`
3. Commit both the README and updated results
4. The CI will verify on the next run

## 📊 Verification History

View detailed verification results in `.github/readme-verifier/results.json`

Each run includes:
- Timestamp
- Environment details (OS, Node version)
- Per-step results with duration and output
- Success/failure rates

---

**Status Legend:**
- ![passing](https://img.shields.io/badge/setup-passing-brightgreen) All steps verified successfully
- ![partial](https://img.shields.io/badge/setup-partial-yellow) Some optional steps failed
- ![failing](https://img.shields.io/badge/setup-failing-red) Required steps are broken
