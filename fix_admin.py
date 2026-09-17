import os

css_path = r'c:\Users\vigas\Desktop\learnora\css\admin.css'
js_path = r'c:\Users\vigas\Desktop\learnora\js\admin.js'

# 1. Update CSS
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

responsive_css = '''
    /* Responsive Tables */
    .table-responsive {
        border: none;
        overflow-x: hidden !important;
    }
    .admin-table, 
    .admin-table thead, 
    .admin-table tbody, 
    .admin-table th, 
    .admin-table td, 
    .admin-table tr { 
        display: block; 
        width: 100%;
        box-sizing: border-box;
    }
    .admin-table thead tr { 
        position: absolute;
        top: -9999px;
        left: -9999px;
    }
    .admin-table tr {
        border: 1px solid var(--admin-border);
        border-radius: 8px;
        margin-bottom: 16px;
        background: var(--admin-bg);
        padding: 8px;
    }
    .admin-table td { 
        border: none;
        border-bottom: 1px solid rgba(0,0,0,0.05); 
        position: relative;
        padding-left: 45% !important; 
        text-align: right !important;
        min-height: 40px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .admin-table td:last-child {
        border-bottom: 0;
    }
    .admin-table td::before { 
        content: attr(data-label); 
        position: absolute;
        left: 12px;
        width: 40%; 
        padding-right: 10px; 
        white-space: nowrap;
        text-align: left;
        font-weight: 600;
        color: var(--secondary-text);
        font-size: 0.85rem;
    }
    .action-btns {
        justify-content: flex-end;
    }
    
    /* Responsive Timetable Grid */
    .timetable-grid {
        display: flex;
        flex-direction: column;
        border: none;
    }
    .timetable-header {
        display: none;
    }
    .timetable-cell {
        display: flex;
        flex-direction: column;
        gap: 10px;
        border: 1px solid var(--admin-border);
        margin-bottom: 12px;
        border-radius: 8px;
        padding: 16px;
        background: var(--admin-bg);
    }
    .timetable-cell.time-label {
        background: var(--primary-purple);
        color: white;
        margin-bottom: -4px;
        border-radius: 8px 8px 0 0;
        border: none;
        padding: 12px 16px;
        display: block;
        text-align: left;
    }
'''

# Find the @media (max-width: 768px) block and inject this
media_query_search = '@media (max-width: 768px) {'
media_idx = css_content.find(media_query_search)
if media_idx != -1:
    css_content = css_content[:media_idx + len(media_query_search)] + '\n' + responsive_css + css_content[media_idx + len(media_query_search):]
else:
    # Append if not found
    css_content += '\n@media (max-width: 768px) {\n' + responsive_css + '\n}\n'

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)


# 2. Update JS
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Add the data-label injection logic right after DOMContentLoaded
js_snippet = '''
    // Auto-generate data-labels for responsive tables
    document.querySelectorAll('.admin-table').forEach(table => {
        const headers = Array.from(table.querySelectorAll('thead th')).map(th => th.textContent.trim());
        table.querySelectorAll('tbody tr').forEach(row => {
            Array.from(row.querySelectorAll('td')).forEach((td, index) => {
                if (headers[index]) {
                    td.setAttribute('data-label', headers[index]);
                }
            });
        });
    });
'''

# We also should fix the 'window.innerWidth <= 768' check. Sometimes visual viewport is tricky.
# Let's change it to check if mobileMenuToggle is visible instead, or just use a safer check.
# But with the horizontal scroll fixed, innerWidth <= 768 will work fine.
# Let's inject js_snippet
dom_loaded_search = "document.addEventListener('DOMContentLoaded', () => {"
js_idx = js_content.find(dom_loaded_search)
if js_idx != -1:
    js_content = js_content[:js_idx + len(dom_loaded_search)] + '\n' + js_snippet + js_content[js_idx + len(dom_loaded_search):]

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Admin dashboard responsive fixes applied.")
