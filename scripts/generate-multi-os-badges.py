#!/usr/bin/env python3
"""
Multi-OS Badge Generator
Generates badges for multiple operating systems
"""

import json
import os
from pathlib import Path
from datetime import datetime

def generate_multi_os_badges(results_dir='.github/readme-verifier'):
    """Generate badges for all tested operating systems"""
    
    results_path = Path(results_dir)
    badges = []
    
    # Try to load combined results
    combined_file = results_path / 'combined-results.json'
    if combined_file.exists():
        with open(combined_file) as f:
            combined = json.load(f)
        
        # Generate overall status badge
        all_passed = all(
            stats['failed'] == 0 
            for stats in combined['results_by_os'].values()
        )
        
        if all_passed:
            status_color = 'brightgreen'
            status_text = 'passing'
        else:
            status_color = 'red'
            status_text = 'failing'
        
        badges.append(
            f'![Multi-OS Status](https://img.shields.io/badge/multi--os-{status_text}-{status_color})'
        )
        
        # Generate individual OS badges
        os_order = ['macOS', 'Linux', 'Windows']  # Preferred display order
        
        for os_name in os_order:
            # Try different possible OS names
            stats = None
            for key in combined['results_by_os'].keys():
                if os_name.lower() in key.lower():
                    stats = combined['results_by_os'][key]
                    break
            
            if not stats:
                continue
            
            total = stats['total']
            success = stats['success']
            failed = stats['failed']
            
            if failed == 0:
                color = 'brightgreen'
                icon = '✓'
            else:
                color = 'red'
                icon = '✗'
            
            success_rate = round((success/total)*100) if total > 0 else 0
            
            badges.append(
                f'![{os_name}](https://img.shields.io/badge/{os_name}-{icon}%20{success_rate}%25-{color})'
            )
        
        # Last verified timestamp
        timestamp = datetime.fromisoformat(combined['timestamp'])
        date_str = timestamp.strftime('%m/%d/%Y').replace('/', '%2F')
        
        badges.append(
            f'![Last Verified](https://img.shields.io/badge/last%20verified-{date_str}-lightgrey)'
        )
    
    else:
        # Fallback to single OS if combined results don't exist
        results_file = results_path / 'results.json'
        if results_file.exists():
            with open(results_file) as f:
                results = json.load(f)
            
            total = len(results['steps'])
            success = sum(1 for s in results['steps'] if s['status'] == 'success')
            failed = sum(1 for s in results['steps'] if s['status'] == 'failed')
            
            status_color = 'brightgreen' if failed == 0 else 'red'
            status_text = 'passing' if failed == 0 else 'failing'
            
            os_name = results['environment']['os']
            success_rate = round((success/total)*100) if total > 0 else 0
            
            badges.append(f'![Setup Status](https://img.shields.io/badge/setup-{status_text}-{status_color})')
            badges.append(f'![Verified On](https://img.shields.io/badge/verified%20on-{os_name}-blue)')
            badges.append(f'![Success Rate](https://img.shields.io/badge/success%20rate-{success_rate}%25-{status_color})')
            
            timestamp = datetime.fromisoformat(results['timestamp'])
            date_str = timestamp.strftime('%m/%d/%Y').replace('/', '%2F')
            badges.append(f'![Last Verified](https://img.shields.io/badge/last%20verified-{date_str}-lightgrey)')
    
    return ' '.join(badges)

def update_readme_with_multi_os_badges(readme_path='README.md'):
    """Update README with multi-OS badges"""
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    badges = generate_multi_os_badges()
    
    badge_marker = '<!-- VERIFICATION-BADGES -->'
    badge_end_marker = '<!-- END-VERIFICATION-BADGES -->'
    
    badge_section = f'{badge_marker}\n{badges}\n{badge_end_marker}'
    
    import re
    
    if badge_marker in content:
        # Replace existing badges
        pattern = f'{re.escape(badge_marker)}[\\s\\S]*?{re.escape(badge_end_marker)}'
        content = re.sub(pattern, badge_section, content)
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
    
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f'✅ Updated {readme_path} with multi-OS badges')

if __name__ == '__main__':
    import sys
    readme_path = sys.argv[1] if len(sys.argv) > 1 else 'README.md'
    update_readme_with_multi_os_badges(readme_path)
