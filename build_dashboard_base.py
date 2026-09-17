import os
import json

base_dir = 'user-dashboard'
os.makedirs(os.path.join(base_dir, 'css'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'js'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'assets'), exist_ok=True)

# 1. CSS Files
css_dashboard = """
/* Dashboard Layout & Grid */
:root {
    --sidebar-width: 260px;
    --header-height: 70px;
}

body {
    background-color: var(--background);
    margin: 0;
    padding: 0;
    font-family: 'Inter', sans-serif;
    color: var(--text);
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--primary-dark);
}

.dashboard-container {
    display: flex;
    min-height: 100vh;
}

/* Base Cards */
.dash-card {
    background: var(--white);
    border-radius: 12px;
    padding: 24px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.03);
    border: 1px solid rgba(0,0,0,0.05);
}

/* Grid Layouts */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    margin-bottom: 32px;
}

.content-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
    margin-bottom: 32px;
}

/* Stat Card specific */
.stat-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.stat-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    background: rgba(91, 58, 140, 0.1);
    color: var(--primary-purple);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
}
.stat-value {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 8px 0 4px;
}
.stat-label {
    color: var(--secondary-text);
    font-size: 0.9rem;
}

/* Utility Classes */
.btn-primary {
    background: var(--primary-purple);
    color: var(--white);
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s;
}
.btn-primary:hover {
    background: var(--primary-dark);
}
.btn-outline {
    background: transparent;
    color: var(--primary-purple);
    border: 1px solid var(--primary-purple);
    padding: 10px 20px;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s;
}
.btn-outline:hover {
    background: rgba(91, 58, 140, 0.05);
}

/* Badges */
.badge {
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}
.badge-pending { background: #FEF3C7; color: #D97706; }
.badge-submitted { background: #D1FAE5; color: #059669; }
.badge-upcoming { background: #E0E7FF; color: #4F46E5; }
.badge-overdue { background: #FEE2E2; color: #DC2626; }
"""

css_sidebar = """
/* Sidebar Styles */
.sidebar {
    width: var(--sidebar-width);
    background: var(--white);
    border-right: 1px solid rgba(0,0,0,0.05);
    display: flex;
    flex-direction: column;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    z-index: 100;
    transition: transform 0.3s ease;
}

.sidebar-header {
    padding: 24px;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
}
.sidebar-logo img {
    height: 40px;
}
.logo-text h2 {
    margin: 0;
    font-size: 1.2rem;
    color: var(--primary-dark);
}
.logo-text p {
    margin: 2px 0 0;
    font-size: 0.7rem;
    color: var(--secondary-text);
}

.sidebar-nav {
    padding: 20px 0;
    flex: 1;
    overflow-y: auto;
}

.nav-section {
    margin-bottom: 24px;
}
.nav-title {
    padding: 0 24px;
    font-size: 0.75rem;
    text-transform: uppercase;
    color: var(--secondary-text);
    margin-bottom: 10px;
    letter-spacing: 1px;
}

.nav-item {
    display: flex;
    align-items: center;
    padding: 12px 24px;
    color: var(--text);
    text-decoration: none;
    transition: all 0.2s;
    font-weight: 500;
    gap: 12px;
}

.nav-item i {
    width: 20px;
    text-align: center;
    font-size: 1.1rem;
    color: var(--secondary-text);
    transition: all 0.2s;
}

.nav-item:hover, .nav-item.active {
    background: rgba(91, 58, 140, 0.05);
    color: var(--primary-purple);
    border-right: 3px solid var(--primary-purple);
}

.nav-item:hover i, .nav-item.active i {
    color: var(--primary-purple);
}
"""

css_header = """
/* Top Header Styles */
.main-wrapper {
    flex: 1;
    margin-left: var(--sidebar-width);
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.top-header {
    height: var(--header-height);
    background: var(--white);
    border-bottom: 1px solid rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 32px;
    position: sticky;
    top: 0;
    z-index: 90;
}

.header-left {
    display: flex;
    align-items: center;
    gap: 16px;
}

.mobile-menu-btn {
    display: none;
    background: none;
    border: none;
    font-size: 1.5rem;
    color: var(--text);
    cursor: pointer;
}

.page-title {
    margin: 0;
    font-size: 1.25rem;
    font-weight: 600;
}

.header-right {
    display: flex;
    align-items: center;
    gap: 20px;
}

.notification-bell {
    position: relative;
    background: none;
    border: none;
    font-size: 1.25rem;
    color: var(--secondary-text);
    cursor: pointer;
}
.notification-dot {
    position: absolute;
    top: 0;
    right: 0;
    width: 8px;
    height: 8px;
    background: #EF4444;
    border-radius: 50%;
}

.user-profile {
    display: flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
}
.user-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    object-fit: cover;
}
.user-info {
    display: flex;
    flex-direction: column;
}
.user-name {
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--text);
}
.user-role {
    font-size: 0.75rem;
    color: var(--secondary-text);
}

.main-content {
    padding: 32px;
    flex: 1;
}

/* Dropdown */
.dropdown-menu {
    position: absolute;
    top: 60px;
    right: 32px;
    background: var(--white);
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    width: 250px;
    border: 1px solid rgba(0,0,0,0.05);
    display: none;
    flex-direction: column;
}
.dropdown-menu.show {
    display: flex;
}
.dropdown-item {
    padding: 12px 20px;
    color: var(--text);
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: background 0.2s;
}
.dropdown-item:hover {
    background: rgba(0,0,0,0.02);
    color: var(--primary-purple);
}
"""

css_pages = """
/* Page Specific Styles */
.class-list-item {
    display: flex;
    align-items: center;
    padding: 16px 0;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}
.class-list-item:last-child {
    border-bottom: none;
}
.class-time {
    font-weight: 600;
    width: 100px;
}
.class-details h4 {
    margin: 0 0 4px;
}
.class-details p {
    margin: 0;
    font-size: 0.85rem;
    color: var(--secondary-text);
}

/* Timetable */
.timetable {
    width: 100%;
    border-collapse: collapse;
}
.timetable th, .timetable td {
    border: 1px solid rgba(0,0,0,0.05);
    padding: 16px;
    text-align: center;
}
.timetable th {
    background: rgba(0,0,0,0.02);
    font-weight: 600;
}
.slot-active {
    background: rgba(91, 58, 140, 0.05);
    border-radius: 8px;
    padding: 8px;
}
.slot-active strong {
    display: block;
    color: var(--primary-purple);
}

/* Progress Bars */
.progress-bar-bg {
    width: 100%;
    height: 8px;
    background: rgba(0,0,0,0.05);
    border-radius: 4px;
    overflow: hidden;
    margin-top: 8px;
}
.progress-bar-fill {
    height: 100%;
    background: var(--primary-purple);
    border-radius: 4px;
}

/* Tabs */
.tabs {
    display: flex;
    gap: 24px;
    border-bottom: 1px solid rgba(0,0,0,0.1);
    margin-bottom: 24px;
}
.tab-item {
    padding: 12px 0;
    cursor: pointer;
    font-weight: 500;
    color: var(--secondary-text);
    border-bottom: 2px solid transparent;
}
.tab-item.active {
    color: var(--primary-purple);
    border-bottom-color: var(--primary-purple);
}

/* Table */
.data-table {
    width: 100%;
    border-collapse: collapse;
}
.data-table th {
    text-align: left;
    padding: 12px 16px;
    border-bottom: 1px solid rgba(0,0,0,0.1);
    color: var(--secondary-text);
    font-weight: 600;
}
.data-table td {
    padding: 16px;
    border-bottom: 1px solid rgba(0,0,0,0.05);
}

/* Forms */
.form-group {
    margin-bottom: 20px;
}
.form-group label {
    display: block;
    margin-bottom: 8px;
    font-weight: 500;
    color: var(--secondary-text);
}
.form-control {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid rgba(0,0,0,0.1);
    border-radius: 8px;
    font-family: inherit;
    box-sizing: border-box;
}
.form-control:focus {
    outline: none;
    border-color: var(--primary-purple);
}

/* Modals */
.modal-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.5);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}
.modal-overlay.show { display: flex; }
.modal-content {
    background: var(--white);
    padding: 32px;
    border-radius: 12px;
    width: 100%;
    max-width: 400px;
    text-align: center;
}
"""

css_responsive = """
/* Responsive Overrides */
@media (max-width: 992px) {
    .content-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 768px) {
    .sidebar {
        transform: translateX(-100%);
    }
    .sidebar.open {
        transform: translateX(0);
    }
    .main-wrapper {
        margin-left: 0;
    }
    .mobile-menu-btn {
        display: block;
    }
    .stats-grid {
        grid-template-columns: 1fr;
    }
}
"""

with open(os.path.join(base_dir, 'css', 'dashboard.css'), 'w', encoding='utf-8') as f: f.write(css_dashboard)
with open(os.path.join(base_dir, 'css', 'sidebar.css'), 'w', encoding='utf-8') as f: f.write(css_sidebar)
with open(os.path.join(base_dir, 'css', 'header.css'), 'w', encoding='utf-8') as f: f.write(css_header)
with open(os.path.join(base_dir, 'css', 'pages.css'), 'w', encoding='utf-8') as f: f.write(css_pages)
with open(os.path.join(base_dir, 'css', 'responsive.css'), 'w', encoding='utf-8') as f: f.write(css_responsive)

# 2. JS Files
js_theme = """
// theme.js
document.addEventListener('DOMContentLoaded', () => {
    // Check local storage for theme and dir
    const theme = localStorage.getItem('learnora-theme') || 'light';
    const dir = localStorage.getItem('learnora-direction') || 'ltr';

    if (theme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
    }
    if (dir === 'rtl') {
        document.body.setAttribute('dir', 'rtl');
    }
});
"""
js_sidebar = """
// sidebar.js
document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const sidebar = document.getElementById('sidebar');

    if (mobileBtn && sidebar) {
        mobileBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', (e) => {
        if (window.innerWidth <= 768 && sidebar && sidebar.classList.contains('open')) {
            if (!sidebar.contains(e.target) && !mobileBtn.contains(e.target)) {
                sidebar.classList.remove('open');
            }
        }
    });
});
"""
js_components = """
// components.js
document.addEventListener('DOMContentLoaded', () => {
    // Profile Dropdown
    const profileBtn = document.getElementById('user-profile-btn');
    const profileMenu = document.getElementById('profile-dropdown');
    
    if (profileBtn && profileMenu) {
        profileBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            profileMenu.classList.toggle('show');
            document.getElementById('notification-dropdown')?.classList.remove('show');
        });
    }

    // Notification Dropdown
    const notifBtn = document.getElementById('notification-btn');
    const notifMenu = document.getElementById('notification-dropdown');

    if (notifBtn && notifMenu) {
        notifBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            notifMenu.classList.toggle('show');
            document.getElementById('profile-dropdown')?.classList.remove('show');
        });
    }

    // Close dropdowns when clicking outside
    document.addEventListener('click', () => {
        if (profileMenu) profileMenu.classList.remove('show');
        if (notifMenu) notifMenu.classList.remove('show');
    });
    
    // Logout Modal Logic
    const logoutLinks = document.querySelectorAll('.logout-btn');
    const logoutModal = document.getElementById('logout-modal');
    const cancelLogout = document.getElementById('cancel-logout');
    const confirmLogout = document.getElementById('confirm-logout');

    logoutLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            if (logoutModal) logoutModal.classList.add('show');
        });
    });

    if (cancelLogout && logoutModal) {
        cancelLogout.addEventListener('click', () => logoutModal.classList.remove('show'));
    }

    if (confirmLogout) {
        confirmLogout.addEventListener('click', () => {
            // Demo behavior: redirect to login
            window.location.href = '../login.html';
        });
    }

    // Tabs functionality (if any tabs exist)
    const tabs = document.querySelectorAll('.tab-item');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-target');
            if(target) {
                // Remove active from all tabs in same group
                tab.parentElement.querySelectorAll('.tab-item').forEach(t => t.classList.remove('active'));
                tab.classList.add('active');
                
                // Hide all contents
                const contents = document.querySelectorAll('.tab-content');
                contents.forEach(c => c.style.display = 'none');
                
                // Show target
                const activeContent = document.getElementById(target);
                if(activeContent) activeContent.style.display = 'block';
            }
        });
    });
});
"""

with open(os.path.join(base_dir, 'js', 'theme.js'), 'w', encoding='utf-8') as f: f.write(js_theme)
with open(os.path.join(base_dir, 'js', 'sidebar.js'), 'w', encoding='utf-8') as f: f.write(js_sidebar)
with open(os.path.join(base_dir, 'js', 'components.js'), 'w', encoding='utf-8') as f: f.write(js_components)

print("Created base CSS and JS files.")
