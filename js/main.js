// ============================================================
// LEARNORA - GLOBAL MAIN JAVASCRIPT
// ============================================================


// ============================================================
// 1. IMMEDIATE THEME & RTL INITIALIZATION
//    Runs before the page finishes loading to reduce flickering
// ============================================================

(function initThemeAndRTL() {

    const savedTheme = localStorage.getItem("learnora-theme") || "light";
    const savedDirection = localStorage.getItem("learnora-direction") || "ltr";

    document.documentElement.setAttribute("data-theme", savedTheme);
    document.documentElement.setAttribute("dir", savedDirection);

})();


// ============================================================
// 2. GLOBAL INITIALIZATION
// ============================================================

document.addEventListener("DOMContentLoaded", () => {

    initializeGlobalUI();

});


// ============================================================
// 3. GLOBAL UI INITIALIZATION
// ============================================================

function initializeGlobalUI() {

    updateToggleUI();

    initializeNavigation();

    initializeMobileMenu();

    initializeProfileDropdown();

    initializeThemeToggle();

    initializeRTLToggles();

    initializeStickyNavbar();

    initializeScrollReveal();

    initializeCourseFilters();

    initializeFAQ();

    initializeCurriculum();

    initializeCourseSectionNavigation();

}


// ============================================================
// 4. UPDATE THEME + RTL TOGGLE UI
// ============================================================

function updateToggleUI() {

    const currentTheme =
        document.documentElement.getAttribute("data-theme") || "light";

    const currentDirection =
        document.documentElement.getAttribute("dir") || "ltr";


    // --------------------------------------------------------
    // Theme buttons
    // --------------------------------------------------------

    document.querySelectorAll(".theme-toggle").forEach(button => {

        const moonIcon = button.querySelector(".moon-icon");
        const sunIcon = button.querySelector(".sun-icon");

        if (currentTheme === "dark") {

            if (moonIcon) {
                moonIcon.style.display = "none";
            }

            if (sunIcon) {
                sunIcon.style.display = "block";
            }

        } else {

            if (moonIcon) {
                moonIcon.style.display = "block";
            }

            if (sunIcon) {
                sunIcon.style.display = "none";
            }

        }

    });


    // --------------------------------------------------------
    // RTL buttons
    // --------------------------------------------------------

    document.querySelectorAll(".rtl-toggle").forEach(button => {

        const textSpan = button.querySelector(".rtl-text");

        if (textSpan) {

            textSpan.textContent =
                currentDirection === "ltr" ? "RTL" : "LTR";

        }

    });

}


// ============================================================
// 5. NORMAL NAVIGATION
// ============================================================
// IMPORTANT:
// Do NOT use preventDefault() here.
// Normal links such as contact.html must navigate normally.
// ============================================================

function initializeNavigation() {

    const navLinks = document.querySelectorAll(".new-nav-link");

    const currentPath =
        window.location.pathname.split("/").pop() || "index.html";


    navLinks.forEach(link => {

        const href = link.getAttribute("href");

        if (!href) {
            return;
        }


        // Remove existing active state
        link.classList.remove("active");


        // Ignore anchor links such as #login
        if (href.startsWith("#")) {
            return;
        }


        // Get only the filename from the href
        const linkPath =
            href.split("/").pop().split("?")[0].split("#")[0];


        // Highlight current page
        if (
            linkPath === currentPath ||
            (currentPath === "" && linkPath === "index.html")
        ) {

            link.classList.add("active");

        }

    });

}


// ============================================================
// 6. MOBILE MENU
// ============================================================

function initializeMobileMenu() {

    const menuToggle =
        document.getElementById("menu-toggle");

    const navLinksContainer =
        document.getElementById("nav-links");


    if (!menuToggle || !navLinksContainer) {
        return;
    }


    // Prevent duplicate event listeners
    if (menuToggle.dataset.initialized === "true") {
        return;
    }

    menuToggle.dataset.initialized = "true";


    menuToggle.addEventListener("click", event => {

        event.stopPropagation();

        navLinksContainer.classList.toggle("mobile-open");

        menuToggle.classList.toggle("active");

    });


    // Close mobile menu when a navigation link is clicked
    navLinksContainer
        .querySelectorAll("a")
        .forEach(link => {

            link.addEventListener("click", () => {

                navLinksContainer.classList.remove("mobile-open");

                menuToggle.classList.remove("active");

            });

        });


    // Close mobile menu when clicking outside
    document.addEventListener("click", event => {

        if (
            !navLinksContainer.contains(event.target) &&
            !menuToggle.contains(event.target)
        ) {

            navLinksContainer.classList.remove("mobile-open");

            menuToggle.classList.remove("active");

        }

    });

}


// ============================================================
// 7. PROFILE DROPDOWN
// ============================================================

function initializeProfileDropdown() {

    const profileButton =
        document.getElementById("profile-btn");

    const profileDropdown =
        document.getElementById("profile-dropdown");


    if (!profileButton || !profileDropdown) {
        return;
    }


    if (profileButton.dataset.initialized === "true") {
        return;
    }

    profileButton.dataset.initialized = "true";


    // Open / close dropdown
    profileButton.addEventListener("click", event => {

        event.stopPropagation();

        profileDropdown.classList.toggle("show");

    });


    // Close when clicking outside
    document.addEventListener("click", event => {

        if (
            !profileButton.contains(event.target) &&
            !profileDropdown.contains(event.target)
        ) {

            profileDropdown.classList.remove("show");

        }

    });


    // Close dropdown after selecting a link
    profileDropdown
        .querySelectorAll("a")
        .forEach(link => {

            link.addEventListener("click", () => {

                profileDropdown.classList.remove("show");

            });

        });

}


// ============================================================
// 8. THEME TOGGLE
// ============================================================

function initializeThemeToggle() {

    const themeButtons =
        document.querySelectorAll(".theme-toggle");


    themeButtons.forEach(button => {

        if (button.dataset.initialized === "true") {
            return;
        }

        button.dataset.initialized = "true";


        button.addEventListener("click", event => {

            event.preventDefault();
            event.stopPropagation();


            const currentTheme =
                document.documentElement.getAttribute("data-theme") ||
                "light";


            const newTheme =
                currentTheme === "light"
                    ? "dark"
                    : "light";


            // Apply theme
            document.documentElement.setAttribute(
                "data-theme",
                newTheme
            );


            // Save theme
            localStorage.setItem(
                "learnora-theme",
                newTheme
            );


            // Update icons
            updateToggleUI();

        });

    });

}


// ============================================================
// 9. RTL TOGGLE
// ============================================================

function initializeRTLToggles() {

    const rtlButtons =
        document.querySelectorAll(".rtl-toggle");


    rtlButtons.forEach(button => {

        if (button.dataset.initialized === "true") {
            return;
        }

        button.dataset.initialized = "true";


        button.addEventListener("click", event => {

            event.preventDefault();
            event.stopPropagation();


            const currentDirection =
                document.documentElement.getAttribute("dir") ||
                "ltr";


            const newDirection =
                currentDirection === "ltr"
                    ? "rtl"
                    : "ltr";


            // Apply direction
            document.documentElement.setAttribute(
                "dir",
                newDirection
            );


            // Save direction
            localStorage.setItem(
                "learnora-direction",
                newDirection
            );


            // Update button text
            updateToggleUI();

        });

    });

}


// ============================================================
// 10. STICKY NAVBAR
// ============================================================

function initializeStickyNavbar() {

    const navbar =
        document.getElementById("navbar");


    if (!navbar) {
        return;
    }


    const handleScroll = () => {

        if (window.scrollY > 50) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    };


    window.addEventListener(
        "scroll",
        handleScroll,
        { passive: true }
    );


    handleScroll();

}


// ============================================================
// 11. SCROLL REVEAL ANIMATION
// ============================================================

function initializeScrollReveal() {

    const revealElements =
        document.querySelectorAll(".reveal");


    if (revealElements.length === 0) {
        return;
    }


    const revealOnScroll = () => {

        const windowHeight =
            window.innerHeight;

        const revealPoint = 100;


        revealElements.forEach(element => {

            const revealTop =
                element.getBoundingClientRect().top;


            if (
                revealTop <
                windowHeight - revealPoint
            ) {

                element.classList.add("active");

            }

        });

    };


    window.addEventListener(
        "scroll",
        revealOnScroll,
        { passive: true }
    );


    revealOnScroll();

}


// ============================================================
// 12. COURSE FILTERING
// ============================================================

function initializeCourseFilters() {

    const filterButtons =
        document.querySelectorAll(".filter-btn");

    const courseCards =
        document.querySelectorAll(".course-card-rich");


    if (
        filterButtons.length === 0 ||
        courseCards.length === 0
    ) {

        return;

    }


    filterButtons.forEach(button => {

        button.addEventListener("click", () => {

            filterButtons.forEach(btn => {

                btn.classList.remove("active");

            });


            button.classList.add("active");


            const filterValue =
                button.getAttribute("data-filter");


            courseCards.forEach(card => {

                const category =
                    card.getAttribute("data-category");


                if (
                    filterValue === "all" ||
                    category === filterValue
                ) {

                    card.style.display = "flex";

                } else {

                    card.style.display = "none";

                }

            });

        });

    });

}


// ============================================================
// 13. FAQ ACCORDION
// ============================================================

function initializeFAQ() {

    const faqQuestions =
        document.querySelectorAll(".faq-question");


    if (faqQuestions.length === 0) {
        return;
    }


    faqQuestions.forEach(question => {

        if (question.dataset.initialized === "true") {
            return;
        }
        question.dataset.initialized = "true";

        question.addEventListener("click", () => {

            const item =
                question.closest(".faq-item");


            if (!item) {
                return;
            }


            const answer =
                item.querySelector(".faq-answer");


            if (!answer) {
                return;
            }
            
            const isActive = item.classList.contains("active");

            // Close all others
            document.querySelectorAll(".faq-item").forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove("active");
                    const otherAnswer = otherItem.querySelector(".faq-answer");
                    if (otherAnswer) {
                        otherAnswer.style.maxHeight = "0";
                    }
                }
            });


            if (!isActive) {
                item.classList.add("active");
                answer.style.maxHeight = answer.scrollHeight + "px";
            } else {
                item.classList.remove("active");
                answer.style.maxHeight = "0";
            }

        });

    });

}


// ============================================================
// 14. CURRICULUM ACCORDION
// ============================================================

function initializeCurriculum() {

    const modules =
        document.querySelectorAll(".module-header");


    if (modules.length === 0) {
        return;
    }


    modules.forEach(module => {

        if (module.dataset.initialized === "true") {
            return;
        }
        module.dataset.initialized = "true";

        module.addEventListener("click", () => {

            const item =
                module.closest(".curriculum-module");


            if (!item) {
                return;
            }


            const content =
                item.querySelector(".module-content");


            if (!content) {
                return;
            }


            item.classList.toggle("active");


            if (item.classList.contains("active")) {

                content.style.maxHeight =
                    content.scrollHeight + "px";

            } else {

                content.style.maxHeight = "0";

            }

        });

    });

}


// ============================================================
// 15. COURSE / SERVICE DETAIL SECTION NAVIGATION
// ============================================================

function initializeCourseSectionNavigation() {

    const sections =
        document.querySelectorAll(".course-section");

    const stickyNavLinks =
        document.querySelectorAll(".course-nav a");


    if (
        sections.length === 0 ||
        stickyNavLinks.length === 0
    ) {

        return;

    }


    // --------------------------------------------------------
    // Scroll Spy
    // --------------------------------------------------------

    const updateScrollSpy = () => {

        let current = "";

        const scrollPosition =
            window.scrollY + 150;


        sections.forEach(section => {

            const sectionTop =
                section.offsetTop;

            const sectionHeight =
                section.clientHeight;


            if (
                scrollPosition >= sectionTop &&
                scrollPosition <
                sectionTop + sectionHeight
            ) {

                current =
                    section.getAttribute("id");

            }

        });


        stickyNavLinks.forEach(link => {

            link.classList.remove("active");


            const href =
                link.getAttribute("href");


            if (
                href &&
                current &&
                href.includes(current)
            ) {

                link.classList.add("active");

            }

        });

    };


    window.addEventListener(
        "scroll",
        updateScrollSpy,
        { passive: true }
    );


    updateScrollSpy();


    // --------------------------------------------------------
    // Smooth section navigation
    // --------------------------------------------------------

    stickyNavLinks.forEach(link => {

        link.addEventListener("click", event => {

            const href =
                link.getAttribute("href");


            // Only handle internal anchor links
            if (
                !href ||
                !href.startsWith("#")
            ) {

                return;

            }


            event.preventDefault();


            const targetId =
                href.substring(1);


            const targetSection =
                document.getElementById(targetId);


            if (!targetSection) {
                return;
            }


            window.scrollTo({

                top:
                    targetSection.offsetTop - 120,

                behavior: "smooth"

            });

        });

    });

}


// ============================================================
// END OF LEARNORA MAIN.JS
// ============================================================