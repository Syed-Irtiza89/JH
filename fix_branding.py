import os

ROOT_DIR = r"c:\Users\hp\OneDrive\Desktop\j-h-main\j-h-main"

def fix_branding(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace('Tiya Golf Club', 'J&H Painting')
    new_content = new_content.replace('Tiya', 'J&H')
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed branding in: {file_path}")

def main():
    root_files = ['event-listing.html', 'event-detail.html']
    for filename in root_files:
        path = os.path.join(ROOT_DIR, filename)
        if os.path.exists(path):
            fix_branding(path)

if __name__ == "__main__":
    main()
