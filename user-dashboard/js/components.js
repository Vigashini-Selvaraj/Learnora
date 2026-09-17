
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
