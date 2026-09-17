import os

services = [
    {
        'file': 'service-detail-tutoring.html',
        'hero_img_missing': False,
        'about_img': 'images/service_about_tutoring.jpg'
    },
    {
        'file': 'service-detail-batch.html',
        'hero_img_missing': False,
        'about_img': 'images/service_about_tutoring.jpg'
    },
    {
        'file': 'service-detail-exam.html',
        'hero_img_missing': True,
        'old_hero': 'images/hero_img2.jpg',
        'new_hero': 'assets/images/hero_exam.jpg',
        'about_img': 'assets/images/courses_hero.jpg'
    },
    {
        'file': 'service-detail-material.html',
        'hero_img_missing': True,
        'old_hero': 'images/blog_img1.jpg',
        'new_hero': 'images/blog_study_env.jpg',
        'about_img': 'images/icon_study_materials.jpg'
    },
    {
        'file': 'service-detail-assessment.html',
        'hero_img_missing': True,
        'old_hero': 'images/blog_img2.jpg',
        'new_hero': 'assets/images/environment.jpg',
        'about_img': 'assets/images/student_karan.jpg'
    },
    {
        'file': 'service-detail-guidance.html',
        'hero_img_missing': True,
        'old_hero': 'images/about_vision.jpg',
        'new_hero': 'images/blog_online_learning.jpg',
        'about_img': 'assets/images/student_arjun.jpg'
    }
]

for s in services:
    path = os.path.join(r'c:\Users\vigas\Desktop\learnora', s['file'])
    if not os.path.exists(path): continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Fix hero images if missing
    if s['hero_img_missing']:
        content = content.replace(s['old_hero'], s['new_hero'])
        
    # 2. Fix 'About this Service' side image for the specific services
    if s['file'] != 'service-detail-tutoring.html' and s['file'] != 'service-detail-batch.html':
        content = content.replace('images/service_about_tutoring.jpg', s['about_img'])
        
    # 3. Add purple theme to Hero section ("Book a Session" area)
    # The hero section is: <section class="hero reveal bg-light" style="padding: 100px 0 60px;">
    # Let's replace 'bg-light' with a custom purple gradient and make text white if needed, 
    # but the simplest is just adding a light purple background.
    old_hero_tag = '<section class="hero reveal bg-light" style="padding: 100px 0 60px;">'
    new_hero_tag = '<section class="hero reveal" style="padding: 100px 0 60px; background: linear-gradient(135deg, rgba(91,58,140,0.05) 0%, rgba(91,58,140,0.15) 100%); border-bottom: 1px solid rgba(91,58,140,0.1);">'
    content = content.replace(old_hero_tag, new_hero_tag)
    
    # 4. Add purple theme to "About this Service" section
    # The about section is: <section id="overview" class="course-section section-padding">
    old_about_tag = '<section id="overview" class="course-section section-padding">'
    new_about_tag = '<section id="overview" class="course-section section-padding" style="background: rgba(91,58,140,0.03); border-radius: 40px; margin: 40px 20px;">'
    content = content.replace(old_about_tag, new_about_tag)
    
    # Actually, margin: 40px 20px breaks the full width sometimes. Let's just use background color.
    new_about_tag = '<section id="overview" class="course-section section-padding" style="background-color: rgba(91,58,140,0.04);">'
    content = content.replace(old_about_tag, new_about_tag)
    
    # Also fix 'service-detail.html' base template if needed, but not strictly necessary since the user only looks at the specific ones now.
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates applied to all specific service detail pages.")
