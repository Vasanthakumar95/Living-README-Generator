# Test Project

<!-- VERIFICATION-BADGES -->
![Setup Status](https://img.shields.io/badge/setup-passing-brightgreen) ![Verified On](https://img.shields.io/badge/verified%20on-Linux-blue) ![Last Verified](https://img.shields.io/badge/last%20verified-01%2F19%2F2026-lightgrey) ![Success Rate](https://img.shields.io/badge/success%20rate-100%25-brightgreen)
<!-- END-VERIFICATION-BADGES -->

This is a simple test to demonstrate the Living README Generator.

## Setup Instructions

### Step 1: Check Node.js

---
verify: true
step: "check-node"
description: "Verify Node.js is installed"
---
```bash
node --version
```

### Step 2: Create a test file

---
verify: true
step: "create-test-file"
description: "Create a simple test file"
---
```bash
echo "Hello from Living README!" > test-output.txt
```

### Step 3: Verify the file

---
verify: true
step: "verify-file"
description: "Check that the file was created"
---
```bash
cat test-output.txt | grep "Hello"
```

### Step 4: Clean up

---
verify: true
step: "cleanup"
description: "Remove test file"
required: false
---
```bash
rm test-output.txt
```

That's it! All steps should pass.
