import os
import re

with open(r'c:\Users\vigas\Desktop\learnora\components\header.html', 'r', encoding='utf-8') as f:
    header_html = f.read()

with open(r'c:\Users\vigas\Desktop\learnora\components\footer.html', 'r', encoding='utf-8') as f:
    footer_html = f.read()

header_logo_match = re.search(r'(<div class="logo-icon">.*?</div>)', header_html, re.DOTALL)
footer_logo_match = re.search(r'(<div class="logo-icon">.*?</div>)', footer_html, re.DOTALL)

if header_logo_match and footer_logo_match:
    footer_html = footer_html.replace(footer_logo_match.group(1), header_logo_match.group(1))
    with open(r'c:\Users\vigas\Desktop\learnora\components\footer.html', 'w', encoding='utf-8') as f:
        f.write(footer_html)

# Escape backticks since we are embedding inside a JS template literal
header_html = header_html.replace('`', '\\`')
footer_html = footer_html.replace('`', '\\`')

components_js = f"""const headerHTML = `{header_html}`;
const footerHTML = `{footer_html}`;
"""

with open(r'c:\Users\vigas\Desktop\learnora\js\components.js', 'w', encoding='utf-8') as f:
    f.write(components_js)

print('components.js written successfully.')
