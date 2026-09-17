import os

base_file = r'c:\Users\vigas\Desktop\learnora\service-detail.html'
with open(base_file, 'r', encoding='utf-8') as f:
    template = f.read()

services = [
    {
        'file': 'service-detail-tutoring.html',
        'title': 'Personalized Tutoring',
        'desc': "Individual guidance designed around each student's learning pace, strengths, and areas for improvement. Our flagship 1-on-1 support.",
        'img': 'images/featured_tutoring.jpg'
    },
    {
        'file': 'service-detail-batch.html',
        'title': 'Small Batch Classes',
        'desc': 'Focused group learning with individual attention in an interactive environment. Ideal for collaborative peer learning.',
        'img': 'images/service_hero.jpg'
    },
    {
        'file': 'service-detail-exam.html',
        'title': 'Exam Preparation',
        'desc': 'Structured revision, mock tests, and exam-focused practice designed to build unshakeable confidence and maximize scores.',
        'img': 'images/hero_img2.jpg'
    },
    {
        'file': 'service-detail-material.html',
        'title': 'Study Material Support',
        'desc': 'Curated notes, detailed worksheets, and comprehensive revision resources created by top educators.',
        'img': 'images/blog_img1.jpg'
    },
    {
        'file': 'service-detail-assessment.html',
        'title': 'Progress Assessment',
        'desc': 'Regular mock tests, detailed performance tracking, and actionable feedback loops to guarantee steady improvement.',
        'img': 'images/blog_img2.jpg'
    },
    {
        'file': 'service-detail-guidance.html',
        'title': 'Academic Guidance',
        'desc': 'Helping students identify strengths, overcome challenges, and map out effective long-term learning goals.',
        'img': 'images/about_vision.jpg'
    }
]

for s in services:
    content = template
    # Replace the Hero Title
    content = content.replace('<h1 class="hero-title">Personalized Tutoring</h1>', f'<h1 class="hero-title">{s["title"]}</h1>')
    # Replace Title tag
    content = content.replace('<title>Service Detail | Learnora</title>', f'<title>{s["title"]} | Learnora Services</title>')
    # Replace description
    old_desc = "Individual guidance designed around each student's learning pace, strengths, and areas for improvement. Our flagship 1-on-1 support."
    content = content.replace(old_desc, s["desc"])
    # Replace Image
    content = content.replace('images/featured_tutoring.jpg', s["img"])
    
    file_path = os.path.join(r'c:\Users\vigas\Desktop\learnora', s['file'])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated all 6 specific service pages.")
