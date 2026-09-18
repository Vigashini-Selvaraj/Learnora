import os

faq_html_path = r'c:\Users\vigas\Desktop\learnora\faq.html'
standalone_css_path = r'c:\Users\vigas\Desktop\learnora\css\standalone.css'

# 1. Update faq.html
with open(faq_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the sections
old_sections = '''            <div class="standalone-section">
                <h3>1. How do I enroll in a course?</h3>
                <p>You can enroll in any course by navigating to the Courses page, selecting your desired course, and clicking the "Enroll Now" button. You will be guided through our secure checkout process.</p>
            </div>
            <div class="standalone-section">
                <h3>2. Can I switch from a Monthly to a Yearly plan?</h3>
                <p>Yes, you can upgrade your plan at any time through your account dashboard. Any remaining balance on your monthly plan will be prorated towards your new yearly subscription.</p>
            </div>
            <div class="standalone-section">
                <h3>3. Do you offer refunds?</h3>
                <p>We offer a 14-day money-back guarantee for all our premium courses. If you are not satisfied with the content or tutoring quality within the first 14 days, you can request a full refund via our Contact page.</p>
            </div>
            <div class="standalone-section">
                <h3>4. How does 1-on-1 tutoring work?</h3>
                <p>If you are subscribed to our Elite plan, you receive 4 hours of dedicated 1-on-1 tutoring per month. You can schedule these sessions directly with our expert educators through the built-in calendar in your dashboard.</p>
            </div>'''

new_sections = '''            <div class="faq-container">
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>1. How do I enroll in a course?</h3>
                        <i class="fa-solid fa-chevron-down toggle-icon"></i>
                    </div>
                    <div class="faq-answer">
                        <p>You can enroll in any course by navigating to the Courses page, selecting your desired course, and clicking the "Enroll Now" button. You will be guided through our secure checkout process.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>2. Can I switch from a Monthly to a Yearly plan?</h3>
                        <i class="fa-solid fa-chevron-down toggle-icon"></i>
                    </div>
                    <div class="faq-answer">
                        <p>Yes, you can upgrade your plan at any time through your account dashboard. Any remaining balance on your monthly plan will be prorated towards your new yearly subscription.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>3. Do you offer refunds?</h3>
                        <i class="fa-solid fa-chevron-down toggle-icon"></i>
                    </div>
                    <div class="faq-answer">
                        <p>We offer a 14-day money-back guarantee for all our premium courses. If you are not satisfied with the content or tutoring quality within the first 14 days, you can request a full refund via our Contact page.</p>
                    </div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-question">
                        <h3>4. How does 1-on-1 tutoring work?</h3>
                        <i class="fa-solid fa-chevron-down toggle-icon"></i>
                    </div>
                    <div class="faq-answer">
                        <p>If you are subscribed to our Elite plan, you receive 4 hours of dedicated 1-on-1 tutoring per month. You can schedule these sessions directly with our expert educators through the built-in calendar in your dashboard.</p>
                    </div>
                </div>
            </div>'''

html_content = html_content.replace(old_sections, new_sections)

# Add script at the bottom
script_tag = '''
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const faqItems = document.querySelectorAll('.faq-item');
            faqItems.forEach(item => {
                const question = item.querySelector('.faq-question');
                question.addEventListener('click', () => {
                    // Close others (optional, but good UX)
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item) {
                            otherItem.classList.remove('active');
                            otherItem.querySelector('.faq-answer').style.maxHeight = null;
                        }
                    });
                    
                    // Toggle current
                    item.classList.toggle('active');
                    const answer = item.querySelector('.faq-answer');
                    if (item.classList.contains('active')) {
                        answer.style.maxHeight = answer.scrollHeight + "px";
                    } else {
                        answer.style.maxHeight = null;
                    }
                });
            });
        });
    </script>
'''

if "<script src=\"js/main.js\"></script>" in html_content:
    html_content = html_content.replace("<script src=\"js/main.js\"></script>", "<script src=\"js/main.js\"></script>\n" + script_tag)

with open(faq_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# 2. Update standalone.css
with open(standalone_css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

faq_css = '''
/* FAQ Accordion Styles */
.faq-container {
    margin-top: 30px;
}

.faq-item {
    margin-bottom: 16px;
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
}

.faq-item.active {
    border-color: var(--primary-purple);
    box-shadow: var(--shadow-md);
}

.faq-question {
    padding: 20px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    background: var(--card-bg);
}

.faq-question h3 {
    margin: 0;
    font-size: 1.15rem;
    color: var(--main-text);
    font-weight: 600;
}

.faq-question .toggle-icon {
    color: var(--secondary-text);
    transition: transform 0.3s ease;
}

.faq-item.active .faq-question .toggle-icon {
    transform: rotate(180deg);
    color: var(--primary-purple);
}

.faq-item.active .faq-question h3 {
    color: var(--primary-purple);
}

.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out, padding 0.3s ease-out;
    padding: 0 24px;
}

.faq-item.active .faq-answer {
    padding: 0 24px 20px 24px;
}

.faq-answer p {
    margin: 0;
    color: var(--secondary-text);
    line-height: 1.6;
}
'''

with open(standalone_css_path, 'w', encoding='utf-8') as f:
    f.write(css_content + '\n' + faq_css)

print("FAQ accordion implemented.")
