#!/usr/bin/env python3
"""
Living README Verifier (Python Implementation)
Parses README.md, executes verification steps, and updates status badges
"""

import re
import json
import subprocess
import sys
import yaml
from datetime import datetime
from pathlib import Path
import platform
import os

# Fix Windows encoding issues with emojis
IS_WINDOWS = sys.platform == 'win32'

# Set UTF-8 encoding for Windows
if IS_WINDOWS:
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')
    except:
        pass

# Emoji replacements for Windows terminal
EMOJI_MAP = {
    '🚀': '[START]',
    '✅': '[OK]',
    '❌': '[FAIL]',
    '⚠️': '[WARN]',
    '🔍': '[RUN]',
    '📊': '[REPORT]',
    '💾': '[SAVE]',
    '📝': '[UPDATE]',
    '📈': '[RATE]',
}

def format_output(text):
    """Format output text, replacing emojis on Windows"""
    if IS_WINDOWS:
        for emoji, replacement in EMOJI_MAP.items():
            text = text.replace(emoji, replacement)
    return text

def safe_print(text):
    """Print text safely, handling Windows encoding"""
    try:
        print(format_output(text))
    except UnicodeEncodeError:
        # Fallback: remove all non-ASCII characters
        print(text.encode('ascii', 'ignore').decode('ascii'))

class ReadmeVerifier:
    def __init__(self, readme_path, config_path=None):
        self.readme_path = readme_path
        self.config_path = config_path
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'environment': self.get_environment(),
            'steps': []
        }
    
    def get_environment(self):
        return {
            'os': platform.system(),
            'arch': platform.machine(),
            'pythonVersion': sys.version.split()[0],
            'platform': platform.platform()
        }
    
    def parse_readme(self):
        """Parse README.md and extract verification steps"""
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        steps = []
        # Regex to match YAML frontmatter followed by code block
        # Pre-filter to only match blocks that contain 'verify' keyword
        pattern = r'---\n(.*?verify.*?)\n---\n```(\w+)?\n(.*?)```'
        
        for match in re.finditer(pattern, content, re.DOTALL):
            try:
                frontmatter = yaml.safe_load(match.group(1))
                
                if frontmatter and frontmatter.get('verify'):
                    steps.append({
                        'name': frontmatter.get('step', f'step-{len(steps) + 1}'),
                        'description': frontmatter.get('description', ''),
                        'language': match.group(2) or 'bash',
                        'code': match.group(3).strip(),
                        'required': frontmatter.get('required', True),
                        'timeout': frontmatter.get('timeout', 60),
                        'workingDir': frontmatter.get('workingDir', '.')
                    })
                # Silently skip YAML blocks without 'verify: true' (likely documentation)
            except Exception as e:
                # Only warn if we found potential verification blocks with errors
                has_verify_keyword = 'verify' in match.group(1).lower()
                if has_verify_keyword:
                    safe_print(f'Warning: Found YAML with "verify" but failed to parse: {e}')
                # Otherwise silently skip (likely documentation examples)
        
        return steps
    
    def execute_step(self, step):
        """Execute a single verification step"""
        safe_print(f'\n🔍 Executing: {step["name"]}')
        safe_print(f'   {step["description"] or "No description"}')
        
        result = {
            'name': step['name'],
            'description': step['description'],
            'status': 'pending',
            'output': '',
            'error': '',
            'duration': 0,
            'timestamp': datetime.now().isoformat()
        }
        
        start_time = datetime.now()
        
        try:
            # Execute the code
            process = subprocess.run(
                step['code'],
                shell=True,
                cwd=step['workingDir'],
                timeout=step['timeout'],
                capture_output=True,
                text=True
            )
            
            duration = (datetime.now() - start_time).total_seconds() * 1000
            
            if process.returncode == 0:
                result['status'] = 'success'
                result['output'] = process.stdout
                result['duration'] = duration
                safe_print(f'   ✅ Success ({duration:.0f}ms)')
            else:
                raise subprocess.CalledProcessError(
                    process.returncode, 
                    step['code'], 
                    process.stdout, 
                    process.stderr
                )
                
        except subprocess.TimeoutExpired:
            result['status'] = 'failed'
            result['error'] = f'Timeout after {step["timeout"]}s'
            result['duration'] = step['timeout'] * 1000
            safe_print(f'   ❌ Failed (timeout)')
            
            if not step['required']:
                result['status'] = 'warning'
                safe_print(f'   ⚠️  Non-required step, continuing...')
            else:
                raise
                
        except subprocess.CalledProcessError as e:
            duration = (datetime.now() - start_time).total_seconds() * 1000
            result['status'] = 'failed'
            result['error'] = e.stderr or str(e)
            result['output'] = e.stdout or ''
            result['duration'] = duration
            safe_print(f'   ❌ Failed ({duration:.0f}ms)')
            safe_print(f'   Error: {e.stderr or e}')
            
            if not step['required']:
                result['status'] = 'warning'
                safe_print(f'   ⚠️  Non-required step, continuing...')
            else:
                raise
        
        return result
    
    def verify(self):
        """Execute all verification steps sequentially"""
        safe_print('🚀 Starting README verification...\n')
        safe_print(f'Environment: {self.results["environment"]["os"]} ({self.results["environment"]["arch"]})')
        safe_print(f'Python: {self.results["environment"]["pythonVersion"]}\n')
        
        steps = self.parse_readme()
        
        if not steps:
            safe_print('⚠️  No verification steps found in README.md')
            return self.results
        
        safe_print(f'Found {len(steps)} verification step(s)\n')
        
        for step in steps:
            try:
                result = self.execute_step(step)
                self.results['steps'].append(result)
            except Exception as e:
                # If a required step fails, stop execution
                self.results['steps'].append({
                    'name': step['name'],
                    'status': 'failed',
                    'error': str(e),
                    'duration': 0,
                    'timestamp': datetime.now().isoformat()
                })
                break
        
        return self.results
    
    def get_summary(self):
        """Generate summary statistics"""
        total = len(self.results['steps'])
        success = sum(1 for s in self.results['steps'] if s['status'] == 'success')
        failed = sum(1 for s in self.results['steps'] if s['status'] == 'failed')
        warnings = sum(1 for s in self.results['steps'] if s['status'] == 'warning')
        
        return {
            'total': total,
            'success': success,
            'failed': failed,
            'warnings': warnings,
            'successRate': round((success / total * 100) if total > 0 else 0)
        }
    
    def save_results(self, output_path='.github/readme-verifier/results.json'):
        """Save results to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2)
        
        safe_print(f'\n💾 Results saved to {output_path}')
    
    def generate_badges(self):
        """Generate badge markdown - uses multi-OS results if available"""
        # Check if combined multi-OS results exist
        combined_results_path = Path('.github/readme-verifier/combined-results.json')
        
        if combined_results_path.exists():
            # Use multi-OS combined results
            try:
                with open(combined_results_path, 'r', encoding='utf-8') as f:
                    combined = json.load(f)
                
                last_verified = datetime.fromisoformat(combined['timestamp']).strftime('%m/%d/%Y')
                
                # Calculate overall statistics
                total_steps = combined['total_steps']
                total_success = combined['total_success']
                total_failed = combined['total_failed']
                total_warnings = combined['total_warnings']
                success_rate = round((total_success / total_steps * 100)) if total_steps > 0 else 0
                
                # Determine overall status
                if total_failed == 0 and total_warnings == 0:
                    status_color = 'brightgreen'
                    status_text = 'passing'
                elif total_failed == 0:
                    status_color = 'yellow'
                    status_text = 'partial'
                else:
                    status_color = 'red'
                    status_text = 'failing'
                
                # Count passing OSes
                os_results = combined.get('results_by_os', {})
                passing_oses = [os_name for os_name, stats in os_results.items() if stats['failed'] == 0]
                total_oses = len(os_results)
                
                # Generate OS badges
                os_badge_parts = []
                for os_name in ['macOS', 'Ubuntu', 'Windows']:
                    if os_name in os_results:
                        stats = os_results[os_name]
                        if stats['failed'] == 0:
                            os_badge_parts.append(f'{os_name}%20OK')
                        else:
                            os_badge_parts.append(f'{os_name}%20FAIL')
                
                os_badge_text = '%20|%20'.join(os_badge_parts) if os_badge_parts else 'Multi--OS'
                
                badges = [
                    f'![Multi-OS Status](https://img.shields.io/badge/multi--os-{status_text}-{status_color})',
                    f'![Platforms](https://img.shields.io/badge/{os_badge_text}-blue)',
                    f'![Last Verified](https://img.shields.io/badge/last%20verified-{last_verified.replace("/", "%2F")}-lightgrey)',
                    f'![Success Rate](https://img.shields.io/badge/success%20rate-{success_rate}%25-{status_color})'
                ]
                
                return ' '.join(badges)
                
            except Exception as e:
                # Fall back to single-OS if combined results can't be read
                pass
        
        # Fall back to single-OS results
        summary = self.get_summary()
        last_verified = datetime.fromisoformat(self.results['timestamp']).strftime('%m/%d/%Y')
        os_name = self.results['environment']['os']
        
        if summary['failed'] == 0 and summary['warnings'] == 0:
            status_color = 'brightgreen'
            status_text = 'passing'
        elif summary['failed'] == 0:
            status_color = 'yellow'
            status_text = 'partial'
        else:
            status_color = 'red'
            status_text = 'failing'
        
        badges = [
            f'![Setup Status](https://img.shields.io/badge/setup-{status_text}-{status_color})',
            f'![Verified On](https://img.shields.io/badge/verified%20on-{os_name}-blue)',
            f'![Last Verified](https://img.shields.io/badge/last%20verified-{last_verified.replace("/", "%2F")}-lightgrey)',
            f'![Success Rate](https://img.shields.io/badge/success%20rate-{summary["successRate"]}%25-{status_color})'
        ]
        
        return ' '.join(badges)
    
    def update_readme(self):
        """Update README with verification badges"""
        with open(self.readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        badges = self.generate_badges()
        
        badge_marker = '<!-- VERIFICATION-BADGES -->'
        badge_end_marker = '<!-- END-VERIFICATION-BADGES -->'
        
        badge_section = f'{badge_marker}\n{badges}\n{badge_end_marker}'
        
        if badge_marker in content:
            # Replace existing badges
            pattern = f'{re.escape(badge_marker)}.*?{re.escape(badge_end_marker)}'
            content = re.sub(pattern, badge_section, content, flags=re.DOTALL)
        else:
            # Add badges after first header
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('# '):
                    lines.insert(i + 1, '')
                    lines.insert(i + 2, badge_section)
                    lines.insert(i + 3, '')
                    break
            content = '\n'.join(lines)
        
        with open(self.readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        safe_print('📝 README.md updated with verification badges')
    
    def print_report(self):
        """Print verification report"""
        summary = self.get_summary()
        
        safe_print('\n' + '=' * 60)
        safe_print('📊 VERIFICATION REPORT')
        safe_print('=' * 60)
        safe_print(f'Total Steps:    {summary["total"]}')
        safe_print(f'✅ Success:      {summary["success"]}')
        safe_print(f'❌ Failed:       {summary["failed"]}')
        safe_print(f'⚠️  Warnings:     {summary["warnings"]}')
        safe_print(f'📈 Success Rate: {summary["successRate"]}%')
        safe_print('=' * 60)
        
        safe_print('\nStep Details:')
        for i, step in enumerate(self.results['steps'], 1):
            icon = '✅' if step['status'] == 'success' else '⚠️' if step['status'] == 'warning' else '❌'
            safe_print(f'  {i}. {icon} {step["name"]} ({step["duration"]:.0f}ms)')
            if step.get('error'):
                safe_print(f'     Error: {step["error"]}')
        
        safe_print('')

def main():
    readme_path = sys.argv[1] if len(sys.argv) > 1 else 'README.md'
    config_path = sys.argv[2] if len(sys.argv) > 2 else '.github/readme-verifier/config.yml'
    
    verifier = ReadmeVerifier(readme_path, config_path)
    
    try:
        verifier.verify()
        verifier.print_report()
        verifier.save_results()
        verifier.update_readme()
        
        summary = verifier.get_summary()
        
        # Exit with error code if any steps failed
        if summary['failed'] > 0:
            sys.exit(1)
    
    except Exception as e:
        safe_print(f'\n❌ Verification failed: {e}')
        sys.exit(1)

if __name__ == '__main__':
    main()