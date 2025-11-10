#!/usr/bin/env python3
"""
Quick syntax fix for the unterminated string literal error
"""

import re

def fix_syntax_error():
    """Fix the unterminated string literal in apts.py"""
    
    print("🔧 SYNTAX FIX: Fixing unterminated string literal...")
    
    # Read the current apts.py file
    with open('apts.py', 'r') as f:
        content = f.read()
    
    # Fix common unterminated string issues
    fixes_applied = 0
    
    # Fix 1: Look for unterminated strings with "console_output_only
    if 'report_path = "console_output_only' in content and 'report_path = "console_output_only"' not in content:
        content = content.replace('report_path = "console_output_only', 'report_path = "console_output_only"')
        fixes_applied += 1
        print("✅ Fixed unterminated string: console_output_only")
    
    # Fix 2: Look for other common unterminated strings
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check for lines with unterminated strings
        if line.strip().endswith('= "') and not line.strip().endswith('""'):
            # This might be an unterminated string, add closing quote
            line = line + 'PLACEHOLDER"'
            fixes_applied += 1
            print(f"✅ Fixed potential unterminated string on line {i+1}")
        
        # Check for specific patterns that might be broken
        if 'report_path = "console_output_only' in line and not line.endswith('"'):
            line = line + '"'
            fixes_applied += 1
            print(f"✅ Fixed report_path string on line {i+1}")
        
        fixed_lines.append(line)
    
    # Rejoin the content
    content = '\n'.join(fixed_lines)
    
    # Remove any PLACEHOLDER quotes we added
    content = content.replace('PLACEHOLDER"', '"')
    
    # Write the fixed content back
    with open('apts.py', 'w') as f:
        f.write(content)
    
    print(f"\n🎉 SYNTAX FIX COMPLETE! Applied {fixes_applied} fixes")
    
    # Test the syntax
    try:
        with open('apts.py', 'r') as f:
            test_content = f.read()
        compile(test_content, 'apts.py', 'exec')
        print("✅ Syntax check passed!")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error still exists: {e}")
        print(f"   Line {e.lineno}: {e.text}")
        return False

if __name__ == "__main__":
    success = fix_syntax_error()
    if success:
        print("\n🚀 Ready to run: python3 apts.py")
    else:
        print("\n⚠️ Manual fix needed - check the syntax error above")