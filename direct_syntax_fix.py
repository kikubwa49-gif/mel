#!/usr/bin/env python3
"""
Direct syntax fix - replace the problematic line
"""

def direct_fix():
    """Directly fix the syntax error"""
    
    print("🔧 DIRECT SYNTAX FIX: Fixing line 299...")
    
    # Read the file
    with open('apts.py', 'r') as f:
        lines = f.readlines()
    
    # Find and fix the problematic line
    for i, line in enumerate(lines):
        if 'report_path = "console_output_only' in line and not line.strip().endswith('"'):
            print(f"Found problematic line {i+1}: {line.strip()}")
            lines[i] = '                report_path = "console_output_only"\n'
            print(f"Fixed to: {lines[i].strip()}")
            break
    
    # Write back
    with open('apts.py', 'w') as f:
        f.writelines(lines)
    
    print("✅ Direct fix applied!")

if __name__ == "__main__":
    direct_fix()