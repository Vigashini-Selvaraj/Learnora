
// theme.js
document.addEventListener('DOMContentLoaded', () => {

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

    // Check local storage for theme and dir
    const theme = localStorage.getItem('learnora-theme') || 'light';
    const dir = localStorage.getItem('learnora-direction') || 'ltr';

    if (theme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
    }
    if (dir === 'rtl') {
        document.body.setAttribute('dir', 'rtl');
    }

    // Toggle logic
    const themeToggles = document.querySelectorAll('.theme-toggle');
    const rtlToggles = document.querySelectorAll('.rtl-toggle');

    function updateIcons() {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        themeToggles.forEach(btn => {
            const moon = btn.querySelector('.moon-icon');
            const sun = btn.querySelector('.sun-icon');
            if (moon && sun) {
                moon.style.display = isDark ? 'none' : 'block';
                sun.style.display = isDark ? 'block' : 'none';
            }
        });
    }

    themeToggles.forEach(btn => {
        btn.addEventListener('click', () => {
            const isDark = document.body.getAttribute('data-theme') === 'dark';
            if (isDark) {
                document.body.removeAttribute('data-theme');
                localStorage.setItem('learnora-theme', 'light');
            } else {
                document.body.setAttribute('data-theme', 'dark');
                localStorage.setItem('learnora-theme', 'dark');
            }
            updateIcons();
            
            // if we are on settings page, update buttons there too
            if (typeof updateActiveBtns === 'function') {
                updateActiveBtns();
            }
        });
    });

    rtlToggles.forEach(btn => {
        btn.addEventListener('click', () => {
            const isRtl = document.body.getAttribute('dir') === 'rtl';
            if (isRtl) {
                document.body.removeAttribute('dir');
                localStorage.setItem('learnora-direction', 'ltr');
            } else {
                document.body.setAttribute('dir', 'rtl');
                localStorage.setItem('learnora-direction', 'rtl');
            }
            // if we are on settings page, update buttons there too
            if (typeof updateActiveBtns === 'function') {
                updateActiveBtns();
            }
        });
    });

    // initial icon state
    updateIcons();
});
