import os
from pathlib import Path

def fix_all_utf16_files():
    search_root = Path('c:/Users/DELL/Downloads/demi 14.2')
    print(f"Scanning {search_root} for UTF-16 files...")
    
    count = 0
    for p in search_root.rglob('*'):
        if p.is_file() and p.suffix == '.txt':
            try:
                # Check for UTF-16 LE BOM
                with open(p, 'rb') as f:
                    header = f.read(2)
                
                is_target = p.name in ['test_output.txt', 'test_output2.txt', 'log_16_2.txt']
                
                if header == b'\xff\xfe' or is_target:
                    print(f"Processing: {p}")
                    try:
                        # Try reading as UTF-16
                        content = p.read_text(encoding='utf-16')
                        # Write as UTF-8
                        p.write_text(content, encoding='utf-8')
                        print(f"  Successfully converted to UTF-8")
                        count += 1
                    except UnicodeDecodeError:
                        print(f"  Already UTF-8 or other encoding (skipped)")
                    except Exception as e:
                        print(f"  Error converting: {e}")
            except Exception as e:
                pass
    
    print(f"\nTotal files converted: {count}")

if __name__ == "__main__":
    fix_all_utf16_files()
