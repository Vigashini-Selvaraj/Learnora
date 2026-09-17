import os

# 1. Append the CSS fixes to style.css
css_fixes = """
/* --- APPLIED NAVBAR FIXES --- */
.nav-actions {
    display: flex !important;
    align-items: center;
    gap: 12px;
    margin-left: auto !important;
}

.desktop-actions {
    display: flex !important;
    align-items: center;
    gap: 10px;
}

.mobile-toggles {
    display: none !important;
}

.icon-btn {
    width: 40px;
    height: 40px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 1px solid var(--border-color);
    border-radius: 10px;
    background: var(--card-bg);
    color: var(--main-text);
    cursor: pointer;
}

.icon-btn svg { width: 18px; height: 18px; }
.rtl-text { font-size: 11px; font-weight: 700; }

.profile-menu { position: relative; }

.profile-btn {
    width: 40px; height: 40px;
    display: flex; align-items: center; justify-content: center;
    border: 1px solid var(--border-color); border-radius: 50%;
    background: var(--card-bg); color: var(--main-text);
    cursor: pointer;
}
.profile-btn svg { width: 19px; height: 19px; }

.dropdown {
    position: absolute; top: calc(100% + 10px); right: 0;
    width: 190px; display: none; padding: 8px;
    background: var(--card-bg); border: 1px solid var(--border-color);
    border-radius: 12px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
    z-index: 9999;
}
.dropdown.show { display: block !important; opacity: 1 !important; visibility: visible !important; transform: translateY(0) !important; }
.dropdown a { display: block; padding: 10px 12px; color: var(--main-text); font-size: 14px; border-radius: 8px; }
.dropdown a:hover { background: rgba(91, 58, 140, 0.05); color: var(--primary-purple); }

.menu-toggle {
    display: none; width: 40px; height: 40px; padding: 8px;
    border: 1px solid var(--border-color); border-radius: 10px;
    background: var(--card-bg); cursor: pointer; flex-direction: column; justify-content: space-between; z-index: 1010;
}
.menu-toggle span { display: block; width: 20px; height: 2px; margin: 4px auto; background: var(--main-text); transition: 0.3s; }

@media (max-width: 900px) {
    .nav-links { display: none !important; }
    .desktop-actions { display: none !important; }
    .mobile-toggles { display: flex !important; align-items: center; gap: 8px; }
    .menu-toggle { display: block !important; }
    .nav-actions { gap: 8px; margin-left: auto !important; }
    
    .nav-links.mobile-open {
        display: flex !important; position: absolute; top: 100%; left: 0; right: 0;
        flex-direction: column; align-items: stretch; padding: 15px 20px;
        background: var(--card-bg); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.08); z-index: 999;
    }
    .nav-links.mobile-open .nav-link { padding: 12px 5px; }
    .mobile-only-menu { display: block; }
}

@media (min-width: 901px) {
    .mobile-only-menu { display: none !important; }
}
"""

with open(r'c:\Users\vigas\Desktop\learnora\css\style.css', 'a', encoding='utf-8') as f:
    f.write(css_fixes)


# 2. Fix main.js by replacing the old logic with the user's requested logic
with open(r'c:\Users\vigas\Desktop\learnora\js\main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

import re

# We will remove the old hamburger and profile logic and insert the new one
# The old logic is inside DOMContentLoaded, starting after await loadComponents();
# Actually we can just find 'const menuToggle = document.getElementById('menu-toggle');'
# and replace everything from there up to the Theme Toggle logic.

new_js = """
    // 1. Mobile Menu Toggle
    const menuToggle = document.getElementById("menu-toggle");
    const navLinks = document.getElementById("nav-links");
    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", () => {
            navLinks.classList.toggle("mobile-open");
            menuToggle.classList.toggle("active");
        });
    }

    // 2. Profile Dropdown Toggle
    const profileBtn = document.getElementById("profile-btn");
    const profileDropdown = document.getElementById("profile-dropdown");
    if (profileBtn && profileDropdown) {
        profileBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            profileDropdown.classList.toggle("show");
        });
        document.addEventListener("click", () => {
            profileDropdown.classList.remove("show");
        });
    }
    
    // 3. Theme Toggle"""

main_js = re.sub(r'// 1\. Mobile Menu Toggle.*?// 3\. Theme Toggle', new_js, main_js, flags=re.DOTALL)

with open(r'c:\Users\vigas\Desktop\learnora\js\main.js', 'w', encoding='utf-8') as f:
    f.write(main_js)

print('CSS and JS updated successfully with the exact fixes.')
