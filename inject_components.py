import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'components.js' not in content:
        # Just insert it before main.js
        content = content.replace('<script src="js/main.js"></script>', '<script src="js/components.js"></script>\n    <script src="js/main.js"></script>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
print('Injected components.js into all files successfully.')
