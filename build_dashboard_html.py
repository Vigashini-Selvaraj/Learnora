import os

base_dir = 'user-dashboard'

pages = [
    {"file": "dashboard.html", "title": "Dashboard", "icon": "fa-table-columns"},
    {"file": "classes.html", "title": "My Classes", "icon": "fa-chalkboard-user"},
    {"file": "timetable.html", "title": "Timetable", "icon": "fa-calendar-week"},
    {"file": "attendance.html", "title": "Attendance", "icon": "fa-clipboard-user"},
    {"file": "materials.html", "title": "Study Materials", "icon": "fa-book-open"},
    {"file": "assignments.html", "title": "Assignments", "icon": "fa-file-lines"},
    {"file": "tests.html", "title": "Tests & Exams", "icon": "fa-file-pen"},
    {"file": "progress.html", "title": "Progress", "icon": "fa-chart-line"},
    {"file": "announcements.html", "title": "Announcements", "icon": "fa-bullhorn"},
]

def generate_sidebar(active_file):
    nav_links = ""
    for p in pages:
        active_cls = " active" if p["file"] == active_file else ""
        nav_links += f'<a href="{p["file"]}" class="nav-item{active_cls}"><i class="fa-solid {p["icon"]}"></i> {p["title"]}</a>\n'

    return f"""
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <a href="dashboard.html" class="sidebar-logo">
                <img src="../images/learnora_logo.jpg" alt="Learnora Logo">
                <div class="logo-text">
                    <h2>Learnora</h2>
                    <p>Learn • Practice • Achieve</p>
                </div>
            </a>
        </div>
        <div class="sidebar-nav">
            <div class="nav-section">
                <div class="nav-title">Menu</div>
                {nav_links}
            </div>
            <div class="sidebar-footer" style="padding: 24px; border-top: 1px solid rgba(0,0,0,0.05); display: flex; gap: 12px; justify-content: center; margin-top: auto;">
                <button class="icon-btn rtl-toggle" aria-label="Toggle RTL" style="width: 40px; height: 40px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1); background: transparent; cursor: pointer; display: flex; align-items: center; justify-content: center; color: var(--text); transition: all 0.2s;">
                    <span class="rtl-text" style="font-size: 0.8rem; font-weight: 600;">RTL</span>
                </button>
                <button class="icon-btn theme-toggle" aria-label="Toggle Theme" style="width: 40px; height: 40px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1); background: transparent; cursor: pointer; display: flex; align-items: center; justify-content: center; color: var(--text); transition: all 0.2s;">
                    <i class="fa-solid fa-moon moon-icon"></i>
                    <i class="fa-solid fa-sun sun-icon" style="display: none;"></i>
                </button>
            </div>
        </div>
    </aside>
"""

def generate_header(title):
    return f"""
    <header class="top-header">
        <div class="header-left">
            <button class="mobile-menu-btn" id="mobile-menu-btn">
                <i class="fa-solid fa-bars"></i>
            </button>
            <h1 class="page-title">{title}</h1>
        </div>
        <div class="header-right">
            <button class="notification-bell" id="notification-btn">
                <i class="fa-regular fa-bell"></i>
                <span class="notification-dot"></span>
            </button>
            <div class="dropdown-menu" id="notification-dropdown">
                <div style="padding: 12px 16px; font-weight: 600; border-bottom: 1px solid rgba(0,0,0,0.05);">Notifications</div>
                <a href="#" class="dropdown-item" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                    <span style="font-size: 0.85rem;">New Physics material uploaded</span>
                    <span style="font-size: 0.75rem; color: var(--secondary-text);">10 min ago</span>
                </a>
                <a href="#" class="dropdown-item" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                    <span style="font-size: 0.85rem;">Mathematics test tomorrow</span>
                    <span style="font-size: 0.75rem; color: var(--secondary-text);">2 hours ago</span>
                </a>
                <div style="padding: 12px 16px; border-top: 1px solid rgba(0,0,0,0.05); text-align: center;">
                    <a href="#" style="font-size: 0.8rem; color: var(--primary-purple); text-decoration: none;">Mark all as read</a>
                </div>
            </div>

            <div class="user-profile" id="user-profile-btn">
                <img src="https://ui-avatars.com/api/?name=Vigashini+S&background=5B3A8C&color=fff" alt="User Avatar" class="user-avatar">
                <div class="user-info">
                    <span class="user-name">Vigashini S.</span>
                    <span class="user-role">Student</span>
                </div>
                <i class="fa-solid fa-chevron-down" style="color: var(--secondary-text); font-size: 0.8rem;"></i>
            </div>
            <div class="dropdown-menu" id="profile-dropdown">
                <a href="profile.html" class="dropdown-item"><i class="fa-regular fa-user"></i> My Profile</a>
                <a href="settings.html" class="dropdown-item"><i class="fa-solid fa-gear"></i> Settings</a>
                <a href="#" class="dropdown-item logout-btn" style="color: #EF4444;"><i class="fa-solid fa-arrow-right-from-bracket"></i> Logout</a>
            </div>
        </div>
    </header>
"""

def generate_html(file_name, title, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Learnora Student</title>
    <!-- Fonts & Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Base Styles -->
    <link rel="stylesheet" href="../css/style.css">
    <!-- Dashboard Styles -->
    <link rel="stylesheet" href="css/dashboard.css">
    <link rel="stylesheet" href="css/sidebar.css">
    <link rel="stylesheet" href="css/header.css">
    <link rel="stylesheet" href="css/pages.css">
    <link rel="stylesheet" href="css/responsive.css">
</head>
<body>

<div class="dashboard-container">
{generate_sidebar(file_name)}

    <div class="main-wrapper">
{generate_header(title)}
        
        <main class="main-content">
{content}
        </main>
    </div>
</div>

<!-- Logout Modal -->
<div class="modal-overlay" id="logout-modal">
    <div class="modal-content">
        <h3>Ready to leave?</h3>
        <p style="color: var(--secondary-text); margin-bottom: 24px;">Select "Logout" below if you are ready to end your current session.</p>
        <div style="display: flex; gap: 16px; justify-content: center;">
            <button class="btn-outline" id="cancel-logout">Cancel</button>
            <button class="btn-primary" id="confirm-logout">Logout</button>
        </div>
    </div>
</div>

<!-- Scripts -->
<script src="js/theme.js"></script>
<script src="js/sidebar.js"></script>
<script src="js/components.js"></script>
</body>
</html>
"""

# HTML Content for Pages

content_dashboard = """
            <div style="margin-bottom: 32px;">
                <h2 style="margin: 0 0 8px 0; font-size: 1.8rem;">Good Morning, Vigashini! 👋</h2>
                <p style="margin: 0; color: var(--secondary-text);">Ready to learn something new today? Today is September 16, 2026.</p>
                <a href="timetable.html" class="btn-outline" style="margin-top: 16px; padding: 8px 16px; font-size: 0.9rem;">View Schedule</a>
            </div>

            <div class="stats-grid">
                <div class="dash-card stat-item">
                    <div>
                        <div class="stat-label">Attendance</div>
                        <div class="stat-value">92%</div>
                        <div class="stat-label" style="font-size: 0.8rem;">This Month</div>
                    </div>
                    <div class="stat-icon"><i class="fa-solid fa-clipboard-user"></i></div>
                </div>
                <div class="dash-card stat-item">
                    <div>
                        <div class="stat-label">Upcoming Classes</div>
                        <div class="stat-value">04</div>
                        <div class="stat-label" style="font-size: 0.8rem;">This Week</div>
                    </div>
                    <div class="stat-icon" style="background: rgba(16, 185, 129, 0.1); color: #10B981;"><i class="fa-solid fa-school"></i></div>
                </div>
                <div class="dash-card stat-item">
                    <div>
                        <div class="stat-label">Assignments</div>
                        <div class="stat-value">03</div>
                        <div class="stat-label" style="font-size: 0.8rem; color: #D97706;">Pending</div>
                    </div>
                    <div class="stat-icon" style="background: rgba(245, 158, 11, 0.1); color: #F59E0B;"><i class="fa-solid fa-file-lines"></i></div>
                </div>
                <div class="dash-card stat-item">
                    <div>
                        <div class="stat-label">Tests</div>
                        <div class="stat-value">02</div>
                        <div class="stat-label" style="font-size: 0.8rem; color: #4F46E5;">Upcoming</div>
                    </div>
                    <div class="stat-icon" style="background: rgba(79, 70, 229, 0.1); color: #4F46E5;"><i class="fa-solid fa-file-pen"></i></div>
                </div>
            </div>

            <div class="content-grid">
                <!-- Today's Classes -->
                <div class="dash-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="margin: 0; font-size: 1.2rem;">Today's Classes</h3>
                        <a href="classes.html" style="color: var(--primary-purple); text-decoration: none; font-size: 0.9rem; font-weight: 500;">View All</a>
                    </div>
                    
                    <div class="class-list-item">
                        <div class="class-time">09:00 AM</div>
                        <div class="class-details" style="flex: 1;">
                            <h4>Mathematics</h4>
                            <p>Grade 12 - Batch A • Room 02</p>
                        </div>
                        <div><span class="badge badge-upcoming">Upcoming</span></div>
                    </div>
                    <div class="class-list-item">
                        <div class="class-time">11:00 AM</div>
                        <div class="class-details" style="flex: 1;">
                            <h4>Physics</h4>
                            <p>Grade 12 - Batch A • Room 02</p>
                        </div>
                        <div><span class="badge badge-upcoming">Upcoming</span></div>
                    </div>
                    <div class="class-list-item">
                        <div class="class-time">04:00 PM</div>
                        <div class="class-details" style="flex: 1;">
                            <h4>Computer Science</h4>
                            <p>Grade 12 - Batch A • Lab 01</p>
                        </div>
                        <div><span class="badge badge-upcoming">Upcoming</span></div>
                    </div>
                </div>

                <!-- Upcoming Tests -->
                <div class="dash-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="margin: 0; font-size: 1.2rem;">Upcoming Tests</h3>
                        <a href="tests.html" style="color: var(--primary-purple); text-decoration: none; font-size: 0.9rem; font-weight: 500;">View All</a>
                    </div>
                    
                    <div style="margin-bottom: 16px; padding: 16px; border: 1px solid rgba(0,0,0,0.05); border-radius: 8px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <span style="font-weight: 600; font-size: 0.95rem;">Mathematics</span>
                            <span style="font-size: 0.85rem; color: var(--secondary-text);">Sep 19</span>
                        </div>
                        <div style="font-size: 0.9rem; margin-bottom: 8px;">Unit Test - Algebra</div>
                        <div style="font-size: 0.8rem; color: var(--secondary-text);"><i class="fa-regular fa-clock"></i> 10:00 AM</div>
                    </div>

                    <div style="margin-bottom: 16px; padding: 16px; border: 1px solid rgba(0,0,0,0.05); border-radius: 8px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <span style="font-weight: 600; font-size: 0.95rem;">Physics</span>
                            <span style="font-size: 0.85rem; color: var(--secondary-text);">Sep 24</span>
                        </div>
                        <div style="font-size: 0.9rem; margin-bottom: 8px;">Chapter Test - Motion</div>
                        <div style="font-size: 0.8rem; color: var(--secondary-text);"><i class="fa-regular fa-clock"></i> 10:00 AM</div>
                    </div>
                </div>
            </div>

            <!-- Weekly Timetable Preview & Assignments -->
            <div class="content-grid">
                <div class="dash-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="margin: 0; font-size: 1.2rem;">Weekly Preview</h3>
                        <a href="timetable.html" style="color: var(--primary-purple); text-decoration: none; font-size: 0.9rem; font-weight: 500;">Full Timetable</a>
                    </div>
                    <div style="display: flex; gap: 8px; margin-bottom: 16px; overflow-x: auto;">
                        <div style="padding: 8px 16px; background: rgba(91, 58, 140, 0.1); color: var(--primary-purple); font-weight: 600; border-radius: 20px; font-size: 0.9rem;">Mon</div>
                        <div style="padding: 8px 16px; color: var(--secondary-text); font-weight: 500; font-size: 0.9rem;">Tue</div>
                        <div style="padding: 8px 16px; color: var(--secondary-text); font-weight: 500; font-size: 0.9rem;">Wed</div>
                        <div style="padding: 8px 16px; color: var(--secondary-text); font-weight: 500; font-size: 0.9rem;">Thu</div>
                        <div style="padding: 8px 16px; color: var(--secondary-text); font-weight: 500; font-size: 0.9rem;">Fri</div>
                    </div>
                    <table class="timetable">
                        <tr>
                            <td><strong>09:00 AM</strong><br>Mathematics</td>
                        </tr>
                        <tr>
                            <td><strong>11:00 AM</strong><br>Physics</td>
                        </tr>
                        <tr>
                            <td><strong>04:00 PM</strong><br>Computer Science</td>
                        </tr>
                    </table>
                </div>

                <div class="dash-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="margin: 0; font-size: 1.2rem;">Upcoming Assignments</h3>
                        <a href="assignments.html" style="color: var(--primary-purple); text-decoration: none; font-size: 0.9rem; font-weight: 500;">View All</a>
                    </div>
                    <div style="padding: 16px 0; border-bottom: 1px solid rgba(0,0,0,0.05);">
                        <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 4px;">Algebra Worksheet</div>
                        <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 8px;">Mathematics • Due: Sep 18</div>
                        <div><span class="badge badge-pending">Pending</span></div>
                    </div>
                    <div style="padding: 16px 0;">
                        <div style="font-weight: 600; font-size: 0.95rem; margin-bottom: 4px;">Motion Problems</div>
                        <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 8px;">Physics • Due: Sep 20</div>
                        <div><span class="badge badge-pending">Pending</span></div>
                    </div>
                </div>
            </div>
"""

content_classes = """
            <div class="dash-card">
                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 24px;">
                    <!-- Class Card -->
                    <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; overflow: hidden;">
                        <div style="background: rgba(91, 58, 140, 0.05); padding: 20px;">
                            <h3 style="margin: 0 0 4px; font-size: 1.2rem;">Mathematics</h3>
                            <span style="font-size: 0.9rem; color: var(--secondary-text);">Grade 12 - Batch A</span>
                        </div>
                        <div style="padding: 20px;">
                            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-solid fa-chalkboard-user" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Tutor: Priya Sharma</span>
                            </div>
                            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-regular fa-clock" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Mon & Wed (09:00 AM)</span>
                            </div>
                            <div style="display: flex; gap: 12px; margin-bottom: 20px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-solid fa-location-dot" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Room 02</span>
                            </div>
                            <div style="margin-bottom: 20px;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                                    <span style="color: var(--secondary-text);">Progress</span>
                                    <strong>85%</strong>
                                </div>
                                <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 85%;"></div></div>
                            </div>
                            <a href="class-details.html" class="btn-outline" style="width: 100%; text-align: center; box-sizing: border-box;">View Class</a>
                        </div>
                    </div>
                    
                    <!-- Class Card -->
                    <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; overflow: hidden;">
                        <div style="background: rgba(16, 185, 129, 0.05); padding: 20px;">
                            <h3 style="margin: 0 0 4px; font-size: 1.2rem;">Physics</h3>
                            <span style="font-size: 0.9rem; color: var(--secondary-text);">Grade 12 - Batch A</span>
                        </div>
                        <div style="padding: 20px;">
                            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-solid fa-chalkboard-user" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Tutor: Michael Chen</span>
                            </div>
                            <div style="display: flex; gap: 12px; margin-bottom: 12px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-regular fa-clock" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Tue & Thu (11:00 AM)</span>
                            </div>
                            <div style="display: flex; gap: 12px; margin-bottom: 20px; align-items: center; font-size: 0.9rem;">
                                <i class="fa-solid fa-location-dot" style="color: var(--secondary-text); width: 16px;"></i>
                                <span>Room 02</span>
                            </div>
                            <div style="margin-bottom: 20px;">
                                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; margin-bottom: 4px;">
                                    <span style="color: var(--secondary-text);">Progress</span>
                                    <strong>78%</strong>
                                </div>
                                <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 78%; background: #10B981;"></div></div>
                            </div>
                            <a href="class-details.html" class="btn-outline" style="width: 100%; text-align: center; box-sizing: border-box; color: #10B981; border-color: #10B981;">View Class</a>
                        </div>
                    </div>
                </div>
            </div>
"""

content_class_details = """
            <div class="dash-card" style="margin-bottom: 24px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <h2 style="margin: 0 0 8px; font-size: 1.8rem;">Mathematics</h2>
                        <div style="display: flex; gap: 16px; color: var(--secondary-text); font-size: 0.95rem;">
                            <span><i class="fa-solid fa-chalkboard-user"></i> Priya Sharma</span>
                            <span><i class="fa-solid fa-users"></i> Grade 12 - Batch A</span>
                        </div>
                    </div>
                    <span class="badge badge-submitted" style="font-size: 0.9rem; padding: 6px 12px;">Active Class</span>
                </div>
            </div>

            <div class="dash-card">
                <div class="tabs">
                    <div class="tab-item active" data-target="overview">Overview</div>
                    <div class="tab-item" data-target="schedule">Schedule & Attendance</div>
                    <div class="tab-item" data-target="materials">Materials</div>
                </div>
                
                <div id="overview" class="tab-content" style="display: block;">
                    <h3>Recent Activity</h3>
                    <div style="border-left: 2px solid rgba(0,0,0,0.1); padding-left: 20px; margin-left: 10px;">
                        <div style="margin-bottom: 24px; position: relative;">
                            <div style="position: absolute; left: -27px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: var(--primary-purple);"></div>
                            <div style="font-weight: 600;">Algebra Worksheet Uploaded</div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text);">Sep 15 • Due: Sep 18</div>
                        </div>
                        <div style="margin-bottom: 24px; position: relative;">
                            <div style="position: absolute; left: -27px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: rgba(0,0,0,0.2);"></div>
                            <div style="font-weight: 600;">Class Completed: Quadratic Equations</div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text);">Sep 14 • Attendance: Present</div>
                        </div>
                        <div style="position: relative;">
                            <div style="position: absolute; left: -27px; top: 0; width: 12px; height: 12px; border-radius: 50%; background: rgba(0,0,0,0.2);"></div>
                            <div style="font-weight: 600;">Study Material Added: Algebra Notes</div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text);">Sep 12</div>
                        </div>
                    </div>
                </div>
            </div>
"""

content_timetable = """
            <div class="dash-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                    <div style="display: flex; gap: 12px;">
                        <button class="btn-outline" style="padding: 8px 12px;"><i class="fa-solid fa-chevron-left"></i></button>
                        <button class="btn-outline" style="padding: 8px 12px;">Current Week</button>
                        <button class="btn-outline" style="padding: 8px 12px;"><i class="fa-solid fa-chevron-right"></i></button>
                    </div>
                    <span style="font-weight: 600; color: var(--secondary-text);">Sep 14 - Sep 19, 2026</span>
                </div>
                
                <div style="overflow-x: auto;">
                    <table class="timetable" style="min-width: 800px;">
                        <thead>
                            <tr>
                                <th>Time</th>
                                <th>Monday</th>
                                <th>Tuesday</th>
                                <th>Wednesday</th>
                                <th>Thursday</th>
                                <th>Friday</th>
                                <th>Saturday</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="font-weight: 600;">09:00 AM</td>
                                <td class="slot-active"><strong>Mathematics</strong>Room 02</td>
                                <td></td>
                                <td class="slot-active"><strong>Mathematics</strong>Room 02</td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600;">11:00 AM</td>
                                <td></td>
                                <td class="slot-active" style="background: rgba(16, 185, 129, 0.05); color: #10B981;"><strong>Physics</strong>Room 02</td>
                                <td></td>
                                <td class="slot-active" style="background: rgba(16, 185, 129, 0.05); color: #10B981;"><strong>Physics</strong>Room 02</td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600;">02:00 PM</td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td class="slot-active" style="background: rgba(245, 158, 11, 0.05); color: #F59E0B;"><strong>Chemistry</strong>Room 01</td>
                            </tr>
                            <tr>
                                <td style="font-weight: 600;">04:00 PM</td>
                                <td class="slot-active" style="background: rgba(59, 130, 246, 0.05); color: #3B82F6;"><strong>Comp Sci</strong>Lab 01</td>
                                <td></td>
                                <td class="slot-active" style="background: rgba(59, 130, 246, 0.05); color: #3B82F6;"><strong>Comp Sci</strong>Lab 01</td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

content_attendance = """
            <div class="stats-grid" style="grid-template-columns: repeat(4, 1fr);">
                <div class="dash-card" style="text-align: center;">
                    <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Overall Attendance</div>
                    <div style="font-size: 2.2rem; font-weight: 700; color: var(--primary-purple);">92%</div>
                </div>
                <div class="dash-card" style="text-align: center; border-bottom: 4px solid #10B981;">
                    <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Present</div>
                    <div style="font-size: 1.8rem; font-weight: 700;">44</div>
                </div>
                <div class="dash-card" style="text-align: center; border-bottom: 4px solid #EF4444;">
                    <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Absent</div>
                    <div style="font-size: 1.8rem; font-weight: 700;">3</div>
                </div>
                <div class="dash-card" style="text-align: center; border-bottom: 4px solid #F59E0B;">
                    <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Leave</div>
                    <div style="font-size: 1.8rem; font-weight: 700;">1</div>
                </div>
            </div>

            <div class="dash-card">
                <h3 style="margin: 0 0 20px 0; font-size: 1.2rem;">Attendance History</h3>
                <div style="overflow-x: auto;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Subject</th>
                                <th>Tutor</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Sep 15, 2026</td>
                                <td>Mathematics</td>
                                <td>Priya Sharma</td>
                                <td><span class="badge badge-submitted">Present</span></td>
                            </tr>
                            <tr>
                                <td>Sep 14, 2026</td>
                                <td>Physics</td>
                                <td>Michael Chen</td>
                                <td><span class="badge badge-submitted">Present</span></td>
                            </tr>
                            <tr>
                                <td>Sep 13, 2026</td>
                                <td>Chemistry</td>
                                <td>Sarah Connor</td>
                                <td><span class="badge badge-overdue">Absent</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

pages_map = {
    "dashboard.html": ("Dashboard", content_dashboard),
    "classes.html": ("My Classes", content_classes),
    "class-details.html": ("Class Details", content_class_details),
    "timetable.html": ("Timetable", content_timetable),
    "attendance.html": ("Attendance", content_attendance),
    "materials.html": ("Study Materials", """
            <div class="dash-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; flex-wrap: wrap; gap: 16px;">
                    <input type="text" placeholder="Search materials..." class="form-control" style="max-width: 300px;">
                    <div style="display: flex; gap: 12px;">
                        <select class="form-control" style="width: 150px;">
                            <option>All Subjects</option>
                            <option>Mathematics</option>
                            <option>Physics</option>
                        </select>
                        <select class="form-control" style="width: 150px;">
                            <option>All Types</option>
                            <option>PDF Notes</option>
                            <option>Worksheets</option>
                        </select>
                    </div>
                </div>
                <div style="overflow-x: auto;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>File Name</th>
                                <th>Subject</th>
                                <th>Date Uploaded</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-file-pdf" style="color: #EF4444; font-size: 1.2rem;"></i> <strong>Algebra - Complete Notes</strong></div></td>
                                <td>Mathematics</td>
                                <td>Sep 15, 2026</td>
                                <td><button class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">Download</button></td>
                            </tr>
                            <tr>
                                <td><div style="display: flex; align-items: center; gap: 12px;"><i class="fa-solid fa-file-pdf" style="color: #EF4444; font-size: 1.2rem;"></i> <strong>Newton's Laws Notes</strong></div></td>
                                <td>Physics</td>
                                <td>Sep 14, 2026</td>
                                <td><button class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">Download</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>"""),
    "assignments.html": ("Assignments", """
            <div class="dash-card">
                <div class="tabs">
                    <div class="tab-item active">All</div>
                    <div class="tab-item">Pending</div>
                    <div class="tab-item">Submitted</div>
                </div>
                <div style="overflow-x: auto;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Assignment</th>
                                <th>Subject</th>
                                <th>Due Date</th>
                                <th>Status</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Algebra Worksheet</strong></td>
                                <td>Mathematics</td>
                                <td>Sep 18, 2026</td>
                                <td><span class="badge badge-pending">Pending</span></td>
                                <td><a href="assignment-details.html" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">View</a></td>
                            </tr>
                            <tr>
                                <td><strong>Motion Problems</strong></td>
                                <td>Physics</td>
                                <td>Sep 15, 2026</td>
                                <td><span class="badge badge-submitted">Submitted</span></td>
                                <td><a href="assignment-details.html" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">View</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>"""),
    "assignment-details.html": ("Assignment Details", """
            <div class="dash-card">
                <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 24px;">
                    <div>
                        <h2 style="margin: 0 0 8px;">Algebra Worksheet</h2>
                        <div style="color: var(--secondary-text); font-size: 0.95rem;">Subject: Mathematics • Tutor: Priya Sharma</div>
                    </div>
                    <span class="badge badge-pending">Pending</span>
                </div>
                
                <div style="margin-bottom: 24px;">
                    <h4 style="margin-bottom: 8px;">Instructions:</h4>
                    <p style="color: var(--secondary-text); line-height: 1.6; margin: 0;">Please complete the attached worksheet containing 20 questions on quadratic equations. Show all your working steps clearly. Submit the scanned PDF document before the deadline.</p>
                </div>
                
                <div style="display: flex; gap: 24px; margin-bottom: 32px;">
                    <div style="padding: 16px; border: 1px solid rgba(0,0,0,0.1); border-radius: 8px; flex: 1;">
                        <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Due Date</div>
                        <div style="font-weight: 600;">Sep 18, 2026 11:59 PM</div>
                    </div>
                    <div style="padding: 16px; border: 1px solid rgba(0,0,0,0.1); border-radius: 8px; flex: 1;">
                        <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Attachment</div>
                        <a href="#" style="font-weight: 600; color: var(--primary-purple); text-decoration: none;"><i class="fa-solid fa-file-pdf"></i> algebra_worksheet.pdf</a>
                    </div>
                </div>

                <div style="padding: 32px; border: 2px dashed rgba(0,0,0,0.1); border-radius: 12px; text-align: center; background: rgba(0,0,0,0.01);">
                    <i class="fa-solid fa-cloud-arrow-up" style="font-size: 2.5rem; color: var(--secondary-text); margin-bottom: 16px;"></i>
                    <h4 style="margin: 0 0 8px;">Upload your submission</h4>
                    <p style="color: var(--secondary-text); font-size: 0.9rem; margin: 0 0 16px;">Drag and drop your file here, or click to browse</p>
                    <button class="btn-primary">Browse Files</button>
                </div>
            </div>"""),
    "tests.html": ("Tests & Exams", """
            <div class="dash-card" style="margin-bottom: 32px;">
                <h3 style="margin: 0 0 20px 0;">Upcoming Tests</h3>
                <div style="overflow-x: auto;">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>Test Name</th>
                                <th>Date & Time</th>
                                <th>Duration</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Mathematics Unit Test</strong><br><span style="font-size: 0.85rem; color: var(--secondary-text);">Algebra</span></td>
                                <td>Sep 19, 2026<br><span style="font-size: 0.85rem; color: var(--secondary-text);">10:00 AM</span></td>
                                <td>60 Mins</td>
                                <td><span class="badge badge-upcoming">Upcoming</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="dash-card">
                <h3 style="margin: 0 0 20px 0;">Previous Tests</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
                    <div style="border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; padding: 20px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 16px;">
                            <div>
                                <h4 style="margin: 0 0 4px;">Physics Chapter Test</h4>
                                <div style="font-size: 0.85rem; color: var(--secondary-text);">Sep 05, 2026</div>
                            </div>
                            <div style="text-align: right;">
                                <div style="font-size: 1.5rem; font-weight: 700; color: #10B981;">84%</div>
                            </div>
                        </div>
                        <div class="progress-bar-bg" style="margin-bottom: 16px;"><div class="progress-bar-fill" style="width: 84%; background: #10B981;"></div></div>
                        <a href="test-result.html" class="btn-outline" style="width: 100%; text-align: center; box-sizing: border-box;">View Result</a>
                    </div>
                </div>
            </div>"""),
    "test-result.html": ("Test Result", """
            <div class="dash-card">
                <h2 style="margin: 0 0 8px; text-align: center;">Physics Chapter Test</h2>
                <div style="text-align: center; color: var(--secondary-text); margin-bottom: 32px;">Conducted on Sep 05, 2026</div>
                
                <div class="stats-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 40px;">
                    <div style="text-align: center; padding: 24px; background: rgba(16, 185, 129, 0.05); border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.2);">
                        <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Score</div>
                        <div style="font-size: 2.5rem; font-weight: 700; color: #10B981; margin-bottom: 4px;">42 <span style="font-size: 1.2rem; color: var(--secondary-text);">/ 50</span></div>
                    </div>
                    <div style="text-align: center; padding: 24px; background: rgba(91, 58, 140, 0.05); border-radius: 12px; border: 1px solid rgba(91, 58, 140, 0.2);">
                        <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Percentage</div>
                        <div style="font-size: 2.5rem; font-weight: 700; color: var(--primary-purple); margin-bottom: 4px;">84%</div>
                    </div>
                    <div style="text-align: center; padding: 24px; background: rgba(245, 158, 11, 0.05); border-radius: 12px; border: 1px solid rgba(245, 158, 11, 0.2);">
                        <div style="font-size: 0.9rem; color: var(--secondary-text); margin-bottom: 8px;">Grade</div>
                        <div style="font-size: 2.5rem; font-weight: 700; color: #F59E0B; margin-bottom: 4px;">A</div>
                    </div>
                </div>

                <h4 style="margin: 0 0 16px;">Tutor Feedback</h4>
                <div style="padding: 20px; background: rgba(0,0,0,0.02); border-left: 4px solid var(--primary-purple); border-radius: 4px;">
                    <p style="margin: 0; color: var(--text); font-style: italic;">"Good understanding of kinematics concepts. Need a bit more focus on vector addition word problems. Keep it up!" - Michael Chen</p>
                </div>
            </div>"""),
    "progress.html": ("Progress", """
            <div class="stats-grid" style="grid-template-columns: 1fr 2fr;">
                <div class="dash-card" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                    <h3 style="margin: 0 0 20px;">Overall Progress</h3>
                    <div style="width: 150px; height: 150px; border-radius: 50%; border: 15px solid var(--primary-purple); display: flex; align-items: center; justify-content: center;">
                        <span style="font-size: 2.5rem; font-weight: 700; color: var(--primary-dark);">84%</span>
                    </div>
                </div>
                <div class="dash-card">
                    <h3 style="margin: 0 0 20px;">Subject Performance</h3>
                    
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-weight: 500;">Computer Science</span>
                            <span style="font-weight: 600;">91%</span>
                        </div>
                        <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 91%;"></div></div>
                    </div>
                    
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-weight: 500;">Mathematics</span>
                            <span style="font-weight: 600;">85%</span>
                        </div>
                        <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 85%;"></div></div>
                    </div>
                    
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-weight: 500;">Chemistry</span>
                            <span style="font-weight: 600;">82%</span>
                        </div>
                        <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 82%;"></div></div>
                    </div>
                    
                    <div style="margin-bottom: 16px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                            <span style="font-weight: 500;">Physics</span>
                            <span style="font-weight: 600;">78%</span>
                        </div>
                        <div class="progress-bar-bg"><div class="progress-bar-fill" style="width: 78%; background: #F59E0B;"></div></div>
                    </div>
                </div>
            </div>

            <div class="content-grid">
                <div class="dash-card" style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2);">
                    <h3 style="margin: 0 0 16px; color: #10B981;"><i class="fa-solid fa-arrow-trend-up"></i> Strengths</h3>
                    <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: var(--text);">
                        <li>Strong performance in <strong>Computer Science</strong> algorithms.</li>
                        <li>Consistent improvement in <strong>Mathematics</strong> algebra tests.</li>
                        <li>Perfect attendance record this month.</li>
                    </ul>
                </div>
                <div class="dash-card" style="background: rgba(245, 158, 11, 0.05); border: 1px solid rgba(245, 158, 11, 0.2);">
                    <h3 style="margin: 0 0 16px; color: #D97706;"><i class="fa-solid fa-bullseye"></i> Areas to Improve</h3>
                    <ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: var(--text);">
                        <li>Focus on Physics numerical problems.</li>
                        <li>Review Chemistry organic reactions.</li>
                    </ul>
                </div>
            </div>"""),
    "announcements.html": ("Announcements", """
            <div class="dash-card">
                <div style="display: flex; flex-direction: column; gap: 16px;">
                    
                    <div style="padding: 20px; border: 1px solid rgba(0,0,0,0.1); border-radius: 8px; background: rgba(91, 58, 140, 0.02); border-left: 4px solid var(--primary-purple);">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <h4 style="margin: 0; font-size: 1.1rem;">New Study Materials Available</h4>
                            <span style="font-size: 0.85rem; color: var(--secondary-text);">Sep 15, 2026</span>
                        </div>
                        <p style="margin: 0 0 12px; color: var(--secondary-text);">New Physics notes for the upcoming chapter have been uploaded to your portal.</p>
                        <a href="materials.html" class="btn-outline" style="padding: 6px 12px; font-size: 0.85rem;">View Materials</a>
                    </div>
                    
                    <div style="padding: 20px; border: 1px solid rgba(0,0,0,0.1); border-radius: 8px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                            <h4 style="margin: 0; font-size: 1.1rem;">Parent-Teacher Meeting</h4>
                            <span style="font-size: 0.85rem; color: var(--secondary-text);">Sep 10, 2026</span>
                        </div>
                        <p style="margin: 0; color: var(--secondary-text);">The monthly Parent-Teacher meeting is scheduled for September 25. Please inform your parents.</p>
                    </div>

                </div>
            </div>"""),
    "profile.html": ("My Profile", """
            <div class="dash-card" style="margin-bottom: 32px; display: flex; align-items: center; gap: 32px;">
                <img src="https://ui-avatars.com/api/?name=Vigashini+S&background=5B3A8C&color=fff&size=120" alt="Avatar" style="border-radius: 50%;">
                <div>
                    <h2 style="margin: 0 0 8px;">Vigashini Selvaraj</h2>
                    <div style="display: flex; gap: 24px; color: var(--secondary-text); font-size: 0.95rem; margin-bottom: 16px;">
                        <span><i class="fa-solid fa-id-badge"></i> LRN1024</span>
                        <span><i class="fa-solid fa-graduation-cap"></i> Grade 12 - Batch A</span>
                    </div>
                    <button class="btn-primary" onclick="alert('Demo: Edit profile functionality')">Edit Profile</button>
                </div>
            </div>

            <div class="content-grid">
                <div class="dash-card">
                    <h3 style="margin: 0 0 20px; padding-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.1);">Personal Information</h3>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Full Name</div>
                            <div style="font-weight: 500;">Vigashini Selvaraj</div>
                        </div>
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Email</div>
                            <div style="font-weight: 500;">vigashini@example.com</div>
                        </div>
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Phone</div>
                            <div style="font-weight: 500;">+91 98765 43210</div>
                        </div>
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Date of Birth</div>
                            <div style="font-weight: 500;">Oct 12, 2008</div>
                        </div>
                    </div>
                </div>
                <div class="dash-card">
                    <h3 style="margin: 0 0 20px; padding-bottom: 12px; border-bottom: 1px solid rgba(0,0,0,0.1);">Academic Info</h3>
                    <div style="display: flex; flex-direction: column; gap: 20px;">
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Enrollment Date</div>
                            <div style="font-weight: 500;">June 01, 2026</div>
                        </div>
                        <div>
                            <div style="font-size: 0.85rem; color: var(--secondary-text); margin-bottom: 4px;">Enrolled Subjects</div>
                            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px;">
                                <span class="badge" style="background: rgba(0,0,0,0.05); color: var(--text);">Mathematics</span>
                                <span class="badge" style="background: rgba(0,0,0,0.05); color: var(--text);">Physics</span>
                                <span class="badge" style="background: rgba(0,0,0,0.05); color: var(--text);">Chemistry</span>
                                <span class="badge" style="background: rgba(0,0,0,0.05); color: var(--text);">Computer Science</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""),
    "settings.html": ("Settings", """
            <div class="content-grid">
                <div class="dash-card">
                    <h3 style="margin: 0 0 24px;">Account Settings</h3>
                    <div class="form-group">
                        <label>Full Name</label>
                        <input type="text" class="form-control" value="Vigashini Selvaraj">
                    </div>
                    <div class="form-group">
                        <label>Email Address</label>
                        <input type="email" class="form-control" value="vigashini@example.com">
                    </div>
                    <div class="form-group">
                        <label>Phone Number</label>
                        <input type="tel" class="form-control" value="+91 98765 43210">
                    </div>
                    <button class="btn-primary" onclick="alert('Demo: Settings saved successfully')">Save Changes</button>
                </div>
                
                <div style="display: flex; flex-direction: column; gap: 24px;">
                    <div class="dash-card">
                        <h3 style="margin: 0 0 24px;">Appearance</h3>
                        
                        <div style="margin-bottom: 16px;">
                            <label style="display: block; font-weight: 500; margin-bottom: 8px;">Theme</label>
                            <div style="display: flex; gap: 12px;">
                                <button class="btn-outline" onclick="setTheme('light')" id="btn-light">Light Mode</button>
                                <button class="btn-outline" onclick="setTheme('dark')" id="btn-dark">Dark Mode</button>
                            </div>
                        </div>
                        
                        <div>
                            <label style="display: block; font-weight: 500; margin-bottom: 8px;">Language / Direction</label>
                            <div style="display: flex; gap: 12px;">
                                <button class="btn-outline" onclick="setDir('ltr')" id="btn-ltr">LTR (English)</button>
                                <button class="btn-outline" onclick="setDir('rtl')" id="btn-rtl">RTL (Arabic)</button>
                            </div>
                        </div>
                    </div>

                    <div class="dash-card">
                        <h3 style="margin: 0 0 24px;">Notifications</h3>
                        
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid rgba(0,0,0,0.05);">
                            <div>
                                <div style="font-weight: 500;">Class Reminders</div>
                                <div style="font-size: 0.85rem; color: var(--secondary-text);">Notify me before classes start</div>
                            </div>
                            <input type="checkbox" checked style="width: 20px; height: 20px; accent-color: var(--primary-purple);">
                        </div>
                        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid rgba(0,0,0,0.05);">
                            <div>
                                <div style="font-weight: 500;">Assignment Reminders</div>
                                <div style="font-size: 0.85rem; color: var(--secondary-text);">Notify me for upcoming due dates</div>
                            </div>
                            <input type="checkbox" checked style="width: 20px; height: 20px; accent-color: var(--primary-purple);">
                        </div>
                        <div style="display: flex; align-items: center; justify-content: space-between;">
                            <div>
                                <div style="font-weight: 500;">New Study Materials</div>
                                <div style="font-size: 0.85rem; color: var(--secondary-text);">When tutors upload new files</div>
                            </div>
                            <input type="checkbox" checked style="width: 20px; height: 20px; accent-color: var(--primary-purple);">
                        </div>
                    </div>
                </div>
            </div>

            <script>
                // Settings specific JS
                function updateActiveBtns() {
                    const theme = localStorage.getItem('learnora-theme') || 'light';
                    const dir = localStorage.getItem('learnora-direction') || 'ltr';
                    
                    document.getElementById('btn-light').style.background = theme === 'light' ? 'var(--primary-purple)' : 'transparent';
                    document.getElementById('btn-light').style.color = theme === 'light' ? '#fff' : 'var(--primary-purple)';
                    
                    document.getElementById('btn-dark').style.background = theme === 'dark' ? 'var(--primary-purple)' : 'transparent';
                    document.getElementById('btn-dark').style.color = theme === 'dark' ? '#fff' : 'var(--primary-purple)';

                    document.getElementById('btn-ltr').style.background = dir === 'ltr' ? 'var(--primary-purple)' : 'transparent';
                    document.getElementById('btn-ltr').style.color = dir === 'ltr' ? '#fff' : 'var(--primary-purple)';

                    document.getElementById('btn-rtl').style.background = dir === 'rtl' ? 'var(--primary-purple)' : 'transparent';
                    document.getElementById('btn-rtl').style.color = dir === 'rtl' ? '#fff' : 'var(--primary-purple)';
                }

                function setTheme(theme) {
                    localStorage.setItem('learnora-theme', theme);
                    if(theme === 'dark') document.body.setAttribute('data-theme', 'dark');
                    else document.body.removeAttribute('data-theme');
                    updateActiveBtns();
                }

                function setDir(dir) {
                    localStorage.setItem('learnora-direction', dir);
                    if(dir === 'rtl') document.body.setAttribute('dir', 'rtl');
                    else document.body.removeAttribute('dir');
                    updateActiveBtns();
                }

                document.addEventListener('DOMContentLoaded', updateActiveBtns);
            </script>
""")
}

for page_info in pages:
    file_name = page_info["file"]
    if file_name in pages_map:
        title, content = pages_map[file_name]
        full_html = generate_html(file_name, title, content)
        with open(os.path.join(base_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(full_html)

# Handle the extra nested pages (assignment-details, class-details, test-result)
for file_name, (title, content) in pages_map.items():
    if file_name not in [p["file"] for p in pages]:
        # active file string should just match parent link if possible, or stay empty
        parent = file_name.split('-')[0] + "s.html" # basic guess
        full_html = generate_html(parent, title, content)
        with open(os.path.join(base_dir, file_name), 'w', encoding='utf-8') as f:
            f.write(full_html)

print("Generated all HTML files.")
