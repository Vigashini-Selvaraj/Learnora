import os
import re

file_path = r'c:\Users\vigas\Desktop\learnora\service.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Learn More links in the Service overview section
# They are grouped under `<div class="service-nav-item">`
links = [
    'service-detail-tutoring.html',
    'service-detail-batch.html',
    'service-detail-exam.html',
    'service-detail-material.html',
    'service-detail-assessment.html',
    'service-detail-guidance.html'
]

# We need to replace occurrences of `href="service-detail.html"` with the above links in order.
# Find all occurrences
parts = content.split('href="service-detail.html"')
if len(parts) > len(links):
    new_content = parts[0]
    for i in range(len(links)):
        new_content += f'href="{links[i]}"' + parts[i+1]
    # Append the rest if there are more
    for i in range(len(links)+1, len(parts)):
        new_content += 'href="service-detail.html"' + parts[i]
    content = new_content
elif len(parts) - 1 == len(links):
    new_content = parts[0]
    for i in range(len(links)):
        new_content += f'href="{links[i]}"' + parts[i+1]
    content = new_content

# Update "Explore Service" in the Featured Service section (it's the 7th one)
# Wait, let's just make it point to service-detail-tutoring.html
content = content.replace('href="service-detail.html"', 'href="service-detail-tutoring.html"')

# 2. Fix the CTA alignment at the bottom of the page
old_cta_buttons = '''<div class="hero-buttons justify-center">
                <a href="#contact" class="btn btn-secondary" style="background-color: var(--secondary-yellow); color: var(--main-text); border:none;">Talk to Us</a>
                <a href="courses.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.3); color: var(--white);">Explore Courses</a>
            </div>'''
new_cta_buttons = '''<div class="hero-buttons" style="justify-content: center; align-items: center; display: flex;">
                <a href="contact.html" class="btn btn-secondary" style="background-color: var(--secondary-yellow); color: var(--main-text); border:none;">Talk to Us</a>
                <a href="courses.html" class="btn btn-outline" style="border-color: rgba(255,255,255,0.3); color: var(--white);">Explore Courses</a>
            </div>'''
content = content.replace(old_cta_buttons, new_cta_buttons)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated service.html")
