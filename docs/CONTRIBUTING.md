# Contributing to Living README Generator

Thank you for your interest in contributing! This project aims to make READMEs trustworthy and up-to-date for everyone.

## 🎯 How You Can Help

We welcome contributions in several areas:

### 1. Documentation
- Improve existing docs
- Add more examples
- Fix typos or unclear explanations
- Translate documentation

### 2. Features
- Multi-OS support (Ubuntu, Windows)
- Docker isolation
- Additional notification channels (Slack, Discord)
- Visual dashboard for verification history
- Enhanced badge customization

### 3. Templates
- Industry-specific templates (e.g., React, Django, Go)
- Monorepo examples
- Docker-based projects
- Mobile development setups

### 4. Bug Fixes
- Fix parsing issues
- Improve error messages
- Handle edge cases
- Performance improvements

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/living-readme-generator.git
cd living-readme-generator
```

### 2. Install Dependencies

**Node.js version:**
```bash
npm install
```

**Python version:**
```bash
pip install -r requirements.txt
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 4. Make Your Changes

- Write clear, commented code
- Follow existing code style
- Add tests if applicable
- Update documentation

### 5. Test Your Changes

**Test the verification script:**
```bash
# Python
python3 scripts/verify-readme.py examples/README.simple.md

# Node.js
node scripts/verify-readme.js examples/README.simple.md
```

**Test with your own README:**
```bash
# Create a test README with verification steps
python3 scripts/verify-readme.py your-test-readme.md
```

### 6. Commit and Push

```bash
git add .
git commit -m "feat: add support for Ubuntu verification"
git push origin feature/your-feature-name
```

### 7. Open a Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Describe your changes clearly
- Link any related issues

## 📝 Commit Message Guidelines

We follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, etc.)
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance tasks

Examples:
```
feat: add Windows support for verification
fix: handle empty YAML frontmatter gracefully
docs: improve QUICKSTART guide with screenshots
```

## 🎨 Code Style

### Python
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small

### JavaScript
- Use ES6+ features
- Prefer `const` over `let`
- Add JSDoc comments
- Use meaningful variable names

### YAML
- Use 2-space indentation
- Add comments for complex configurations
- Keep structure consistent

## 🧪 Testing

### Manual Testing

1. Create a test README with various verification steps
2. Run the verification script locally
3. Check that:
   - Steps execute correctly
   - Badges generate properly
   - Error handling works
   - Results JSON is valid

### Automated Testing (Coming Soon)

We're working on adding:
- Unit tests for parsing
- Integration tests for execution
- End-to-end workflow tests

## 📋 Pull Request Checklist

Before submitting:

- [ ] Code follows project style guidelines
- [ ] Documentation updated (if applicable)
- [ ] Examples added/updated (if applicable)
- [ ] Tested locally with multiple scenarios
- [ ] Commit messages follow conventions
- [ ] PR description is clear and complete
- [ ] Related issues are linked

## 🌟 Feature Request Process

Have an idea? Great!

1. **Check existing issues** - Someone may have suggested it already
2. **Open an issue** with:
   - Clear description of the feature
   - Use cases and benefits
   - Potential implementation approach
3. **Discuss** - Get feedback from maintainers
4. **Implement** - Once approved, start coding!

## 🐛 Bug Report Process

Found a bug?

1. **Search existing issues** - May already be reported
2. **Open an issue** with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Node/Python version)
   - Relevant code snippets or logs
3. **Wait for triage** - Maintainers will prioritize
4. **Fix it** - Feel free to submit a PR!

## 📚 Areas Needing Help

Currently, we'd especially appreciate help with:

### High Priority
- [ ] Ubuntu/Linux support in workflow
- [ ] Windows support in workflow
- [ ] Automated tests
- [ ] More real-world examples

### Medium Priority
- [ ] Docker isolation for safer execution
- [ ] Slack/Discord notification integration
- [ ] Visual dashboard for history
- [ ] Multi-README support in single repo

### Low Priority
- [ ] Badge customization options
- [ ] Alternative badge providers
- [ ] Verification result API
- [ ] Browser extension for badge viewing

## 🤝 Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

In short:
- Be respectful and inclusive
- Welcome newcomers
- Focus on what's best for the project
- Show empathy towards others

## 💬 Communication

- **GitHub Issues** - Bug reports, feature requests
- **Pull Requests** - Code contributions
- **Discussions** - General questions, ideas

## 🎓 Resources for Contributors

### Understanding the Codebase

- `scripts/verify-readme.js|.py` - Core verification logic
- `.github/workflows/verify-readme.yml` - GitHub Actions workflow
- `docs/ARCHITECTURE.md` - System design overview

### Useful Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [shields.io Badge Documentation](https://shields.io/)
- [YAML Specification](https://yaml.org/spec/)

## 🏆 Recognition

Contributors will be:
- Listed in README.md (optional)
- Mentioned in release notes
- Given credit in commit history

Significant contributions may earn:
- Collaborator access
- Project leadership roles

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Every contribution makes this project better. Whether it's:
- Fixing a typo
- Adding a feature
- Improving documentation
- Reporting a bug

**Your help is appreciated!** 🎉

---

**Questions?** Open an issue or start a discussion. We're here to help!
