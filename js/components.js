const headerHTML = `<header class="new-navbar" id="navbar">
    <div class="container new-navbar-container">
        <!-- Left: Logo -->
        <a href="index.html" class="new-logo" style="display: flex; align-items: center; text-decoration: none;">
            <img src="images/learnora_logo.jpg" alt="Learnora Logo" style="width: 48px; height: 48px; border-radius: 8px; object-fit: contain;">
            <div style="display: flex; flex-direction: column; margin-left: 10px;">
                <span style="font-weight: 800; font-size: 1.4rem; color: var(--main-text); line-height: 1; letter-spacing: -0.5px;">Learnora</span>
                <span style="font-size: 0.6rem; color: var(--primary-purple); font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 2px;">Education &amp; Tutoring</span>
            </div>
        </a>

        <!-- Center: Links -->
        <nav class="new-nav-links" id="nav-links">
            <a href="index.html" class="new-nav-link">Home</a>
            <a href="home2.html" class="new-nav-link">Home 2</a>
            <a href="about.html" class="new-nav-link">About Us</a>
            <a href="courses.html" class="new-nav-link">Courses</a>
            <a href="service.html" class="new-nav-link">Services</a>
            <a href="blog.html" class="new-nav-link">Blogs</a>
            <a href="contact.html" class="new-nav-link">Contact</a>

            <!-- Mobile Only Dropdown Links -->
            <div class="new-mobile-only">
                <hr>
                <a href="login.html" class="new-nav-link">Login / Register</a>
                <a href="admin-dashboard.html" class="new-nav-link">Admin Dashboard</a>
                <a href="user-dashboard/dashboard.html" class="new-nav-link">User Dashboard</a>
            </div>
        </nav>

        <!-- Right: Actions -->
        <div class="new-nav-actions">
            <!-- Mobile Toggles -->
            <div class="new-mobile-toggles">
                <button class="circle-btn rtl-toggle" aria-label="Toggle RTL">
                    <span class="rtl-text" style="font-size: 0.75rem; font-weight: 700;">LTR</span>
                </button>
                <button class="circle-btn theme-toggle" aria-label="Toggle Theme">
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px;">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px; display: none;">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                </button>
                <button class="new-menu-toggle" id="menu-toggle" aria-label="Menu">
                    <span></span><span></span><span></span>
                </button>
            </div>

            <!-- Desktop Actions -->
            <div class="new-desktop-actions">
                <button class="circle-btn rtl-toggle desktop-rtl" aria-label="Toggle RTL">
                    <span class="rtl-text" style="font-size: 0.75rem; font-weight: 700;">LTR</span>
                </button>
                <button class="circle-btn theme-toggle desktop-theme" aria-label="Toggle Theme">
                    <svg class="moon-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px;">
                        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
                    </svg>
                    <svg class="sun-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px; display: none;">
                        <circle cx="12" cy="12" r="5"></circle>
                        <line x1="12" y1="1" x2="12" y2="3"></line>
                        <line x1="12" y1="21" x2="12" y2="23"></line>
                        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
                        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
                        <line x1="1" y1="12" x2="3" y2="12"></line>
                        <line x1="21" y1="12" x2="23" y2="12"></line>
                        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
                        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
                    </svg>
                </button>

                <div class="new-profile-menu">
                    <button class="circle-btn" id="profile-btn">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 18px; height: 18px;">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                    </button>
                    <div class="new-dropdown" id="profile-dropdown">
                        <a href="login.html">Login / Register</a>
                        <a href="admin-dashboard.html">Admin Dashboard</a>
                        <a href="user-dashboard/dashboard.html">User Dashboard</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>`;

const footerHTML = `<footer class="new-footer" id="new-footer">
    <div class="container">
        <div class="new-footer-grid">
            <!-- Column 1 -->
            <div class="new-footer-col">
                <div style="display: flex; align-items: center; margin-bottom: 20px;">
                    <img src="images/learnora_logo.jpg" alt="Learnora Logo" style="width: 40px; height: 40px; border-radius: 8px; object-fit: contain;">
                    <span style="font-weight: 800; font-size: 1.4rem; color: var(--main-text); margin-left: 10px; letter-spacing: -0.5px;">Learnora</span>
                </div>
                
                <h3 class="new-footer-slogan">Learn. Practice. Achieve.</h3>
                <p class="new-footer-desc">A premium educational experience dedicated to knowledge, performance, and building a supportive community.</p>
                <div class="new-footer-social">
                    <a href="https://www.facebook.com/Learnora" target="_blank" aria-label="Facebook">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px;">
                            <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                        </svg>
                    </a>
                    <a href="https://www.instagram.com/Learnora" target="_blank" aria-label="Instagram">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px;">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                        </svg>
                    </a>
                    <a href="https://www.twitter.com/Learnora" target="_blank" aria-label="Twitter">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px;">
                            <path d="M4 4l16 16M4 20L20 4"></path>
                        </svg>
                    </a>
                    <a href="https://www.youtube.com/Learnora" target="_blank" aria-label="YouTube">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 16px; height: 16px;">
                            <path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33 2.78 2.78 0 0 0 1.94 2c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.33 29 29 0 0 0-.46-5.33z"></path>
                            <polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"></polygon>
                        </svg>
                    </a>
                </div>
            </div>

            <!-- Column 2 -->
            <div class="new-footer-col">
                <h4>Quick Links</h4>
                <ul class="new-footer-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="home2.html">Home 2</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="service.html">Services</a></li>
                    <li><a href="blog.html">Blog</a></li>
                </ul>
            </div>

            <!-- Column 3 -->
            <div class="new-footer-col">
                <h4>Support</h4>
                <ul class="new-footer-links">
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="pricing.html">Pricing Policy</a></li>
                    <li><a href="privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms &amp; Conditions</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>

            <!-- Column 4 -->
            <div class="new-footer-col">
                <h4>Contact</h4>
                <ul class="new-footer-contact">
                    <li>
                        <span class="icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px;">
                                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                                <circle cx="12" cy="10" r="3"></circle>
                            </svg>
                        </span>
                        <span>Chennai, Tamil Nadu</span>
                    </li>
                    <li>
                        <span class="icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px;">
                                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                            </svg>
                        </span>
                        <span>+91 98765 43210</span>
                    </li>
                    <li>
                        <span class="icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width: 18px; height: 18px;">
                                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                                <polyline points="22,6 12,13 2,6"></polyline>
                            </svg>
                        </span>
                        <span>hello@learnora.com</span>
                    </li>
                </ul>
            </div>
        </div>

        <div class="new-footer-bottom">
            <p>&copy; 2026 Learnora. All rights reserved.</p>
        </div>
    </div>
</footer>`;

// Ensure they render if called without a server
document.addEventListener('DOMContentLoaded', () => {
    // Only inject if placeholders exist and they are empty
    const headerPlaceholder = document.getElementById('header-placeholder');
    if (headerPlaceholder && !headerPlaceholder.innerHTML.trim()) {
        headerPlaceholder.innerHTML = headerHTML;
    }
    
    const footerPlaceholder = document.getElementById('footer-placeholder');
    if (footerPlaceholder && !footerPlaceholder.innerHTML.trim()) {
        footerPlaceholder.innerHTML = footerHTML;
    }
    
    // Re-initialize UI events so the injected buttons work!
    if (typeof initializeGlobalUI === 'function') {
        // Use setTimeout to ensure DOM has updated
        setTimeout(initializeGlobalUI, 50);
    }
});