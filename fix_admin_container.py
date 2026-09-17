import os

css_path = r'c:\Users\vigas\Desktop\learnora\css\admin.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

fixes = '''
    /* Force containers to stay within screen */
    .admin-panel, .view-section, .admin-content, .stats-grid {
        max-width: 100%;
        box-sizing: border-box;
    }
    
    /* Override inline grid column styles on mobile */
    .stats-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px;
    }

    /* Stack panel actions on mobile to prevent overflow */
    .panel-actions {
        flex-direction: column;
        width: 100%;
        gap: 8px;
    }
    .panel-actions > * {
        width: 100% !important;
        box-sizing: border-box;
    }
    
    /* Ensure table td content wraps properly */
    .admin-table td {
        word-wrap: break-word;
        white-space: normal;
    }
'''

# Find the end of the media query or just inject inside it
# Actually, let's inject it right after .admin-table td:last-child { ... }
search_target = '.panel-header {\n        flex-direction: column;\n        align-items: flex-start;\n    }'

idx = css_content.find(search_target)
if idx != -1:
    css_content = css_content[:idx + len(search_target)] + '\n' + fixes + css_content[idx + len(search_target):]
else:
    # Just insert it inside the media query block at the end (before the last '}')
    last_brace = css_content.rfind('}')
    css_content = css_content[:last_brace] + fixes + '\n' + css_content[last_brace:]

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Admin dashboard container fixes applied.")
