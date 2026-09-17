import os

css_path = r'c:\Users\vigas\Desktop\learnora\user-dashboard\css\responsive.css'
js_path = r'c:\Users\vigas\Desktop\learnora\user-dashboard\js\theme.js'

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

fixes_css = '''
    /* ========================================================
       User Dashboard Responsive Tables & Containers
       ======================================================== */
    
    /* Force containers to fit screen */
    .dash-card, .dashboard-panel, .content-card, .main-wrapper, .stats-grid {
        max-width: 100% !important;
        box-sizing: border-box;
    }
    
    .stats-grid {
        grid-template-columns: 1fr !important;
        gap: 16px;
    }

    /* Prevent overflow issues */
    [style*="overflow-x: auto"], .table-responsive {
        border: none;
        overflow-x: hidden !important;
        width: 100%;
        max-width: 100%;
    }

    /* Responsive Tables (Data Table and Timetable) */
    .data-table, 
    .data-table thead, 
    .data-table tbody, 
    .data-table th, 
    .data-table td, 
    .data-table tr,
    .timetable,
    .timetable thead,
    .timetable tbody,
    .timetable th,
    .timetable td,
    .timetable tr { 
        display: block; 
        width: 100%;
        box-sizing: border-box;
    }
    
    .data-table thead tr, .timetable thead tr { 
        position: absolute;
        top: -9999px;
        left: -9999px;
    }
    
    .data-table tr, .timetable tr {
        border: 1px solid rgba(0,0,0,0.1);
        border-radius: 8px;
        margin-bottom: 16px;
        background: var(--card-bg);
        padding: 8px;
    }
    
    .data-table td, .timetable td { 
        border: none;
        border-bottom: 1px solid rgba(0,0,0,0.05); 
        position: relative;
        padding: 10px 10px 10px 45% !important; 
        text-align: right !important;
        min-height: 40px;
        display: block;
        word-wrap: break-word;
        white-space: normal;
    }
    
    .data-table td:last-child, .timetable td:last-child {
        border-bottom: 0;
    }
    
    .data-table td::before, .timetable td::before { 
        content: attr(data-label); 
        position: absolute;
        left: 12px;
        top: 10px;
        width: 40%; 
        padding-right: 10px; 
        white-space: normal;
        text-align: left;
        font-weight: 600;
        color: var(--secondary-text);
        font-size: 0.85rem;
    }
    
    .timetable {
        min-width: 100% !important;
    }

    .timetable td:empty {
        display: none !important;
    }
'''

# Find the media query block and inject at the end
last_brace = css_content.rfind('}')
if last_brace != -1:
    css_content = css_content[:last_brace] + fixes_css + '\n' + css_content[last_brace:]

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)


with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

js_snippet = '''
    // Auto-generate data-labels for user dashboard responsive tables
    document.querySelectorAll('.data-table, .timetable').forEach(table => {
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

# Inject the JS after DOMContentLoaded
dom_loaded_search = "document.addEventListener('DOMContentLoaded', () => {"
js_idx = js_content.find(dom_loaded_search)
if js_idx != -1:
    js_content = js_content[:js_idx + len(dom_loaded_search)] + '\n' + js_snippet + js_content[js_idx + len(dom_loaded_search):]

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("User dashboard responsive fixes applied.")
