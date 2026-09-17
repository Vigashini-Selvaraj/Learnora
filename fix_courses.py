import os

courses = [
    {
        'file': 'course-detail-math.html',
        'title': 'Mathematics Mastery',
        'grade': 'Grade 10',
        'h1': 'Mathematics <span>Mastery</span>'
    },
    {
        'file': 'course-detail-science.html',
        'title': 'Science Exploration',
        'grade': 'Grades 6-8',
        'h1': 'Science <span>Exploration</span>'
    },
    {
        'file': 'course-detail-physics.html',
        'title': 'Advanced Physics',
        'grade': 'Grade 12',
        'h1': 'Advanced <span>Physics</span>'
    },
    {
        'file': 'course-detail-exam.html',
        'title': 'Intensive Board Revision',
        'grade': 'All Grades',
        'h1': 'Intensive Board <span>Revision</span>'
    }
]

template_path = r'c:\Users\vigas\Desktop\learnora\course-detail.html'
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

for c in courses:
    content = template
    # Title
    content = content.replace('<title>Grade 10 Mathematics Mastery - Learnora</title>', f'<title>{c["grade"]} {c["title"]} - Learnora</title>')
    
    # H1
    content = content.replace('Mathematics <span>Mastery</span>', c['h1'])
    
    # Badge
    content = content.replace('<span class="badge-primary">Grade 10</span>', f'<span class="badge-primary">{c["grade"]}</span>')
    
    # Breadcrumb/others
    content = content.replace('Mathematics Mastery', c['title'])
    
    file_path = os.path.join(r'c:\Users\vigas\Desktop\learnora', c['file'])
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
