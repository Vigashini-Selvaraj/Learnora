import os
import glob

files = glob.glob(r'c:\Users\vigas\Desktop\learnora\service-detail*.html')

replacement = """        .premium-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(31, 38, 135, 0.12);
        }
        [data-theme="dark"] .premium-card {
            background: var(--card-bg, rgba(30, 30, 45, 0.9));
            border-color: rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        [data-theme="dark"] .premium-card:hover {
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
        }"""

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # find where to inject
    if 'box-shadow: 0 15px 40px rgba(31, 38, 135, 0.12);' in content and '[data-theme="dark"] .premium-card' not in content:
        # replace the original hover to include dark mode
        old_str = """        .premium-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(31, 38, 135, 0.12);
        }"""
        content = content.replace(old_str, replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")

print("Done updating service detail pages.")
