from pathlib import Path

def convert_to_utf8(filename):
    p = Path(filename)
    if p.exists():
        print(f"Found {filename}, converting...")
        try:
            # Try reading as UTF-16
            content = p.read_text(encoding='utf-16')
            # Write as UTF-8
            p.write_text(content, encoding='utf-8')
            print(f"Successfully converted {filename} to UTF-8")
        except Exception as e:
            print(f"Error converting {filename}: {e}")
    else:
        print(f"{filename} not found.")

if __name__ == "__main__":
    for f in ['test_output.txt', 'test_output2.txt', 'log_16_2.txt']:
        convert_to_utf8(f)
