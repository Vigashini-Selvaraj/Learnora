
// ==========================================================================
// ADMIN DASHBOARD JAVASCRIPT
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

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

    
    // --- Navigation & View Switching ---
    const navItems = document.querySelectorAll('.nav-item[data-view]');
    const viewSections = document.querySelectorAll('.view-section');
    const pageTitle = document.getElementById('pageTitle');
    const pageDesc = document.getElementById('pageDesc');
    const mobileMenuToggle = document.getElementById('mobileMenuToggle');
    const adminSidebar = document.getElementById('adminSidebar');
    
    // View Descriptions mapping
    const viewMeta = {
        'dashboard': { title: 'Dashboard', desc: 'Overview and quick statistics' },
        'students': { title: 'Students', desc: 'Manage enrolled students, academic details, and batch assignments' },
        'tutors': { title: 'Tutors', desc: 'Manage teaching staff and profiles' },
        'classes': { title: 'Classes & Batches', desc: 'Organize groups and schedules' },
        'attendance': { title: 'Attendance', desc: 'Track daily attendance across batches' },
        'materials': { title: 'Study Materials', desc: 'Manage resources shared with students' },
        'tests': { title: 'Tests & Exams', desc: 'Schedule and manage assessments' },
        'schedule': { title: 'Schedule', desc: 'Center-wide weekly timetable' },
        'reports': { title: 'Reports & Analytics', desc: 'Performance and growth metrics' },
        'settings': { title: 'Settings', desc: 'Center preferences and admin profile' }
    };

    function switchView(viewId) {
        // Update nav active state
        navItems.forEach(item => {
            if (item.dataset.view === viewId) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });
        
        // Show correct section
        viewSections.forEach(sec => {
            if (sec.id === viewId) {
                sec.classList.add('active');
            } else {
                sec.classList.remove('active');
            }
        });
        
        // Update Header
        if (viewMeta[viewId]) {
            pageTitle.textContent = viewMeta[viewId].title;
            pageDesc.textContent = viewMeta[viewId].desc;
        }
        
        // Close mobile sidebar if open
        if (window.innerWidth <= 768) {
            adminSidebar.classList.remove('show');
        }
        
        // Render Charts if navigating to reports
        if (viewId === 'reports' && !window.chartsRendered) {
            renderCharts();
            window.chartsRendered = true;
        }
    }

    // Attach click listeners to sidebar items
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            switchView(item.dataset.view);
        });
    });

    // Mobile Menu Toggle
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', () => {
            adminSidebar.classList.toggle('show');
        });
    }
    
    // --- Modal Logic ---
    const openModalBtns = document.querySelectorAll('[data-modal-target]');
    const closeBtns = document.querySelectorAll('.close-modal, [data-close-modal]');
    
    openModalBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const modalId = btn.dataset.modalTarget;
            const modal = document.getElementById(modalId);
            if (modal) modal.classList.add('active');
        });
    });
    
    closeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.closest('.admin-modal').classList.remove('active');
        });
    });
    
    // Close modal on outside click
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('admin-modal')) {
            e.target.classList.remove('active');
        }
    });

    // --- Real Form Submissions (Mocked DOM append) ---
    // 1. Add Student
    const studentForm = document.getElementById('studentForm');
    if (studentForm) {
        studentForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const inputs = studentForm.querySelectorAll('input, select');
            const name = inputs[0].value;
            const email = inputs[1].value;
            const grade = inputs[2].value;
            const batch = inputs[3].value;
            
            const tbody = document.getElementById('studentsTableBody');
            if (tbody) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>
                        <div style="font-weight: 600;">${name}</div>
                        <div style="font-size: 0.8rem; color: var(--secondary-text);">${email}</div>
                    </td>
                    <td>STU-${Math.floor(Math.random() * 9000) + 1000}</td>
                    <td class="stu-grade">${grade}</td>
                    <td>General</td>
                    <td>${batch}</td>
                    <td><span class="status-badge success">100%</span></td>
                    <td><span class="status-badge purple">Active</span></td>
                    <td>
                        <div class="action-btns">
                            <button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button>
                            <button class="action-btn delete" title="Delete"><i class="fa-solid fa-trash"></i></button>
                        </div>
                    </td>
                `;
                tbody.appendChild(tr);
            }
            alert('Student saved successfully!');
            studentForm.reset();
            studentForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // Student Filter Logic
    const studentFilter = document.getElementById('studentFilter');
    if (studentFilter) {
        studentFilter.addEventListener('change', (e) => {
            const val = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('#studentsTableBody tr');
            rows.forEach(row => {
                const gradeCell = row.querySelector('.stu-grade') || row.querySelectorAll('td')[2];
                if (!val || gradeCell.textContent.toLowerCase().includes(val)) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    }

    // 2. Add Tutor
    const tutorForm = document.getElementById('tutorForm');
    if (tutorForm) {
        tutorForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(tutorForm);
            
            const grid = document.getElementById('tutorsGrid') || document.querySelector('#tutors .cards-grid');
            if (grid) {
                const div = document.createElement('div');
                div.className = 'profile-card';
                div.innerHTML = `
                    <img src="https://ui-avatars.com/api/?name=${encodeURIComponent(formData.get('name'))}&background=F4B942&color=fff" alt="${formData.get('name')}" class="profile-img">
                    <h4 class="profile-name">${formData.get('name')}</h4>
                    <div class="profile-role">${formData.get('role')}</div>
                    <div class="profile-meta">
                        <div class="meta-box">
                            <strong>${formData.get('experience')} Yrs</strong>
                            <span>Experience</span>
                        </div>
                        <div class="meta-box">
                            <strong>0</strong>
                            <span>Active Batches</span>
                        </div>
                    </div>
                    <div style="margin-bottom: 20px;">
                        <span class="status-badge purple">${formData.get('grades')}</span>
                        <span class="status-badge success">Available</span>
                    </div>
                    <div class="action-btns" style="justify-content: center;">
                        <button class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;">View Profile</button>
                        <button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.85rem;">Schedule</button>
                    </div>
                `;
                grid.appendChild(div);
            }
            alert('Tutor added successfully!');
            tutorForm.reset();
            tutorForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // 3. Add Batch
    const batchForm = document.getElementById('batchForm');
    if (batchForm) {
        batchForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(batchForm);
            const grid = document.getElementById('batchesGrid') || document.querySelector('#classes .cards-grid');
            if (grid) {
                const div = document.createElement('div');
                div.className = 'admin-panel';
                div.style.marginBottom = '0';
                div.innerHTML = `
                    <div style="padding: 24px; border-bottom: 1px solid var(--admin-border);">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                            <div>
                                <h4 style="margin: 0 0 4px 0; font-size: 1.2rem; color: var(--main-text);">${formData.get('batchName')}</h4>
                                <span style="color: var(--primary-purple); font-weight: 600; font-size: 0.9rem;">${formData.get('subject')}</span>
                            </div>
                            <span class="status-badge success">Active</span>
                        </div>
                        <div style="color: var(--secondary-text); font-size: 0.9rem; margin-bottom: 16px;">
                            <i class="fa-solid fa-chalkboard-user" style="width: 20px;"></i> Tutor: ${formData.get('tutor')}
                        </div>
                        <div style="display: flex; gap: 16px; font-size: 0.9rem; color: var(--main-text);">
                            <div><i class="fa-regular fa-clock" style="color: var(--primary-purple);"></i> ${formData.get('schedule')}</div>
                            <div><i class="fa-solid fa-location-dot" style="color: var(--primary-purple);"></i> Room ${formData.get('room')}</div>
                        </div>
                    </div>
                    <div style="padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.01);">
                        <span style="font-weight: 600; color: var(--main-text);"><i class="fa-solid fa-user-group"></i> 0 Students</span>
                        <div class="action-btns">
                            <button class="btn btn-outline" style="padding: 6px 12px; font-size: 0.8rem;">Manage</button>
                        </div>
                    </div>
                `;
                grid.appendChild(div);
            }
            alert('Batch created successfully!');
            batchForm.reset();
            batchForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // 4. Add Material
    const materialForm = document.getElementById('materialForm');
    if (materialForm) {
        materialForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(materialForm);
            const tbody = document.getElementById('materialsTableBody');
            if (tbody) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>
                        <div style="font-weight: 600;"><i class="fa-solid fa-file" style="color: var(--primary-purple); margin-right: 8px;"></i>${formData.get('title')}</div>
                    </td>
                    <td><span class="status-badge purple">${formData.get('type')}</span></td>
                    <td>${formData.get('subjectGrade')}</td>
                    <td>General</td>
                    <td>Just Now</td>
                    <td>0</td>
                    <td>
                        <div class="action-btns">
                            <button class="action-btn" title="Download"><i class="fa-solid fa-download"></i></button>
                            <button class="action-btn delete" title="Delete"><i class="fa-solid fa-trash"></i></button>
                        </div>
                    </td>
                `;
                tbody.appendChild(tr);
            }
            alert('Material uploaded successfully!');
            materialForm.reset();
            materialForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // 5. Add Test
    const testForm = document.getElementById('testForm');
    if (testForm) {
        testForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(testForm);
            const tbody = document.getElementById('testsTableBody');
            if (tbody) {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td><strong>${formData.get('testName')}</strong></td>
                    <td>${formData.get('subjectBatch')}</td>
                    <td>${formData.get('date')}<br><span style="color: var(--secondary-text); font-size: 0.85rem;">${formData.get('time')}</span></td>
                    <td>${formData.get('details')}</td>
                    <td><span class="status-badge warning">Upcoming</span></td>
                    <td>
                        <div class="action-btns">
                            <button class="action-btn" title="Edit"><i class="fa-solid fa-pen"></i></button>
                            <button class="action-btn" title="Results"><i class="fa-solid fa-chart-bar"></i></button>
                            <button class="action-btn delete" title="Cancel"><i class="fa-solid fa-trash"></i></button>
                        </div>
                    </td>
                `;
                tbody.appendChild(tr);
            }
            alert('Test scheduled successfully!');
            testForm.reset();
            testForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // 6. Add Class
    const classForm = document.getElementById('classForm');
    if (classForm) {
        classForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const formData = new FormData(classForm);
            // This is complex as it requires finding the right cell in a CSS grid
            // We'll mock it by just appending it randomly or alerting
            alert('Class added to schedule! (Functionality mocked)');
            classForm.reset();
            classForm.closest('.admin-modal').classList.remove('active');
        });
    }

    // --- Dynamic Status Toggles (Attendance Example) ---
    // If we click a status badge in attendance, toggle it for demo purposes
    const attBadges = document.querySelectorAll('.status-toggle');
    attBadges.forEach(badge => {
        badge.addEventListener('click', () => {
            if (badge.classList.contains('success')) {
                badge.className = 'status-badge danger status-toggle';
                badge.textContent = 'Absent';
            } else if (badge.classList.contains('danger')) {
                badge.className = 'status-badge warning status-toggle';
                badge.textContent = 'Late';
            } else {
                badge.className = 'status-badge success status-toggle';
                badge.textContent = 'Present';
            }
        });
        badge.style.cursor = 'pointer';
    });

    // --- Chart.js Rendering (Reports View) ---
    function renderCharts() {
        if (typeof Chart === 'undefined') return;
        
        // Enrollment Chart
        const ctxEnroll = document.getElementById('enrollmentChart');
        if (ctxEnroll) {
            new Chart(ctxEnroll, {
                type: 'line',
                data: {
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                    datasets: [{
                        label: 'Total Students',
                        data: [150, 180, 195, 210, 235, 248],
                        borderColor: '#5B3A8C',
                        backgroundColor: 'rgba(91, 58, 140, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });
        }
        
        // Subject Distribution Chart
        const ctxSubject = document.getElementById('subjectChart');
        if (ctxSubject) {
            new Chart(ctxSubject, {
                type: 'doughnut',
                data: {
                    labels: ['Mathematics', 'Science', 'English', 'Social Studies'],
                    datasets: [{
                        data: [40, 30, 20, 10],
                        backgroundColor: ['#5B3A8C', '#F4B942', '#8B6BB1', '#462C6B']
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });
        }
    }
});
