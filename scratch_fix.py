import os

files = [r'c:\Users\vigas\Desktop\learnora\service.html', r'c:\Users\vigas\Desktop\learnora\service-detail.html']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('class="section padding-block"', 'class="section-padding"')
    content = content.replace('class="section padding-block text-center"', 'class="section-padding text-center"')
    content = content.replace('class="section padding-block bg-light"', 'class="section-padding bg-light"')
    
    content = content.replace('class="course-section padding-block"', 'class="course-section section-padding"')
    content = content.replace('class="course-section padding-block bg-light"', 'class="course-section section-padding bg-light"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Done')
