#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const yaml = require('js-yaml');

/**
 * Living README Verifier
 * Parses README.md, executes verification steps, and updates status badges
 */

class ReadmeVerifier {
  constructor(readmePath, configPath) {
    this.readmePath = readmePath;
    this.configPath = configPath;
    this.results = {
      timestamp: new Date().toISOString(),
      environment: this.getEnvironment(),
      steps: []
    };
  }

  getEnvironment() {
    const platform = process.platform;
    const arch = process.arch;
    const nodeVersion = process.version;
    
    return {
      os: platform === 'darwin' ? 'macOS' : platform,
      arch,
      nodeVersion,
      platform
    };
  }

  /**
   * Parse README.md and extract verification steps
   * Format:
   * ---
   * verify: true
   * step: "install-dependencies"
   * ---
   * ```bash
   * npm install
   * ```
   */
  parseReadme() {
    const content = fs.readFileSync(this.readmePath, 'utf8');
    const steps = [];
    
    // Regex to match YAML frontmatter followed by code block
    const pattern = /---\n([\s\S]*?)\n---\n```(\w+)?\n([\s\S]*?)```/g;
    
    let match;
    while ((match = pattern.exec(content)) !== null) {
      try {
        const frontmatter = yaml.load(match[1]);
        
        if (frontmatter && frontmatter.verify) {
          steps.push({
            name: frontmatter.step || `step-${steps.length + 1}`,
            description: frontmatter.description || '',
            language: match[2] || 'bash',
            code: match[3].trim(),
            required: frontmatter.required !== false,
            timeout: frontmatter.timeout || 60000,
            workingDir: frontmatter.workingDir || process.cwd()
          });
        }
      } catch (e) {
        console.warn('Failed to parse frontmatter:', e.message);
      }
    }
    
    return steps;
  }

  /**
   * Execute a single verification step
   */
  async executeStep(step) {
    console.log(`\n🔍 Executing: ${step.name}`);
    console.log(`   ${step.description || 'No description'}`);
    
    const result = {
      name: step.name,
      description: step.description,
      status: 'pending',
      output: '',
      error: '',
      duration: 0,
      timestamp: new Date().toISOString()
    };

    const startTime = Date.now();

    try {
      // Execute the code
      const output = execSync(step.code, {
        cwd: step.workingDir,
        timeout: step.timeout,
        encoding: 'utf8',
        stdio: 'pipe'
      });

      result.status = 'success';
      result.output = output;
      result.duration = Date.now() - startTime;
      
      console.log(`   ✅ Success (${result.duration}ms)`);
      
    } catch (error) {
      result.status = 'failed';
      result.error = error.message;
      result.output = error.stdout || '';
      result.duration = Date.now() - startTime;
      
      console.log(`   ❌ Failed (${result.duration}ms)`);
      console.log(`   Error: ${error.message}`);
      
      if (!step.required) {
        result.status = 'warning';
        console.log(`   ⚠️  Non-required step, continuing...`);
      } else {
        throw error; // Stop execution for required steps
      }
    }

    return result;
  }

  /**
   * Execute all verification steps sequentially
   */
  async verify() {
    console.log('🚀 Starting README verification...\n');
    console.log(`Environment: ${this.results.environment.os} (${this.results.environment.arch})`);
    console.log(`Node: ${this.results.environment.nodeVersion}\n`);

    const steps = this.parseReadme();
    
    if (steps.length === 0) {
      console.log('⚠️  No verification steps found in README.md');
      return this.results;
    }

    console.log(`Found ${steps.length} verification step(s)\n`);

    for (const step of steps) {
      try {
        const result = await this.executeStep(step);
        this.results.steps.push(result);
      } catch (error) {
        // If a required step fails, stop execution
        this.results.steps.push({
          name: step.name,
          status: 'failed',
          error: error.message,
          duration: 0,
          timestamp: new Date().toISOString()
        });
        break;
      }
    }

    return this.results;
  }

  /**
   * Generate summary statistics
   */
  getSummary() {
    const total = this.results.steps.length;
    const success = this.results.steps.filter(s => s.status === 'success').length;
    const failed = this.results.steps.filter(s => s.status === 'failed').length;
    const warnings = this.results.steps.filter(s => s.status === 'warning').length;

    return {
      total,
      success,
      failed,
      warnings,
      successRate: total > 0 ? Math.round((success / total) * 100) : 0
    };
  }

  /**
   * Save results to JSON file
   */
  saveResults(outputPath = '.github/readme-verifier/results.json') {
    const dir = path.dirname(outputPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    fs.writeFileSync(outputPath, JSON.stringify(this.results, null, 2));
    console.log(`\n💾 Results saved to ${outputPath}`);
  }

  /**
   * Generate badge markdown
   */
  generateBadges() {
    const summary = this.getSummary();
    const lastVerified = new Date(this.results.timestamp).toLocaleDateString();
    const os = this.results.environment.os;
    
    let statusColor = 'red';
    let statusText = 'failing';
    
    if (summary.failed === 0 && summary.warnings === 0) {
      statusColor = 'brightgreen';
      statusText = 'passing';
    } else if (summary.failed === 0) {
      statusColor = 'yellow';
      statusText = 'partial';
    }

    const badges = [
      `![Setup Status](https://img.shields.io/badge/setup-${statusText}-${statusColor})`,
      `![Verified On](https://img.shields.io/badge/verified%20on-${os}-blue)`,
      `![Last Verified](https://img.shields.io/badge/last%20verified-${encodeURIComponent(lastVerified)}-lightgrey)`,
      `![Success Rate](https://img.shields.io/badge/success%20rate-${summary.successRate}%25-${statusColor})`
    ];

    return badges.join(' ');
  }

  /**
   * Update README with verification badges
   */
  updateReadme() {
    let content = fs.readFileSync(this.readmePath, 'utf8');
    const badges = this.generateBadges();
    
    // Look for existing badge section
    const badgeMarker = '<!-- VERIFICATION-BADGES -->';
    const badgeEndMarker = '<!-- END-VERIFICATION-BADGES -->';
    
    const badgeSection = `${badgeMarker}\n${badges}\n${badgeEndMarker}`;
    
    if (content.includes(badgeMarker)) {
      // Replace existing badges
      const regex = new RegExp(`${badgeMarker}[\\s\\S]*?${badgeEndMarker}`, 'g');
      content = content.replace(regex, badgeSection);
    } else {
      // Add badges at the top after the title
      const lines = content.split('\n');
      const titleIndex = lines.findIndex(line => line.startsWith('# '));
      
      if (titleIndex !== -1) {
        lines.splice(titleIndex + 1, 0, '', badgeSection, '');
        content = lines.join('\n');
      }
    }
    
    fs.writeFileSync(this.readmePath, content);
    console.log('📝 README.md updated with verification badges');
  }

  /**
   * Print verification report
   */
  printReport() {
    const summary = this.getSummary();
    
    console.log('\n' + '='.repeat(60));
    console.log('📊 VERIFICATION REPORT');
    console.log('='.repeat(60));
    console.log(`Total Steps:    ${summary.total}`);
    console.log(`✅ Success:      ${summary.success}`);
    console.log(`❌ Failed:       ${summary.failed}`);
    console.log(`⚠️  Warnings:     ${summary.warnings}`);
    console.log(`📈 Success Rate: ${summary.successRate}%`);
    console.log('='.repeat(60));
    
    console.log('\nStep Details:');
    this.results.steps.forEach((step, i) => {
      const icon = step.status === 'success' ? '✅' : 
                   step.status === 'warning' ? '⚠️' : '❌';
      console.log(`  ${i + 1}. ${icon} ${step.name} (${step.duration}ms)`);
      if (step.error) {
        console.log(`     Error: ${step.error}`);
      }
    });
    
    console.log('');
  }
}

// Main execution
async function main() {
  const readmePath = process.argv[2] || 'README.md';
  const configPath = process.argv[3] || '.github/readme-verifier/config.yml';

  const verifier = new ReadmeVerifier(readmePath, configPath);
  
  try {
    await verifier.verify();
    verifier.printReport();
    verifier.saveResults();
    verifier.updateReadme();
    
    const summary = verifier.getSummary();
    
    // Exit with error code if any steps failed
    if (summary.failed > 0) {
      process.exit(1);
    }
    
  } catch (error) {
    console.error('\n❌ Verification failed:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = ReadmeVerifier;
