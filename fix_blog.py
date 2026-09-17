import os

file_path = r'c:\Users\vigas\Desktop\learnora\blog.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hero background
# We'll just replace the class string to inject inline styles
hero_search = '<section class="blog-section-hero">'
hero_replace = '<section class="blog-section-hero" style="background-color: var(--primary-purple); color: var(--white); padding: 120px 0 160px;">'
content = content.replace(hero_search, hero_replace)
# Change the subtitle color if it's there
content = content.replace('<span class="blog-eyebrow">', '<span class="blog-eyebrow" style="color: rgba(255,255,255,0.8);">')
content = content.replace('<p class="blog-hero-desc">', '<p class="blog-hero-desc" style="color: rgba(255,255,255,0.9);">')

# 2. Article 5: Preparing for Technical Interviews
# It currently uses images/author_david_chen.jpg for the cover
# Find the article block
art5_idx = content.find('Preparing for Technical Interviews')
if art5_idx != -1:
    # search backwards for the cover image
    img_idx = content.rfind('<img src="images/author_david_chen.jpg"', 0, art5_idx)
    if img_idx != -1:
        content = content[:img_idx] + '<img src="images/blog_tech_interview.jpg"' + content[img_idx + 41:]

# 3. Article 6: Online Learning Strategies
art6_idx = content.find('Online Learning Strategies')
if art6_idx != -1:
    img_idx = content.rfind('<img src="images/author_david_chen.jpg"', 0, art6_idx)
    if img_idx != -1:
        content = content[:img_idx] + '<img src="images/blog_online_learning.jpg"' + content[img_idx + 41:]

# 4. Article 7: Skills Every Student Should Develop
art7_idx = content.find('Skills Every Student Should Develop')
if art7_idx != -1:
    img_idx = content.rfind('<img src="images/featured_tutoring.jpg"', 0, art7_idx)
    if img_idx != -1:
        content = content[:img_idx] + '<img src="assets/images/courses_hero.jpg"' + content[img_idx + 40:]

# 5. Trending Now: Top 5 Productivity Apps
app_idx = content.find('Top 5 Productivity Apps')
if app_idx != -1:
    img_idx = content.rfind('<img src="images/environment.jpg"', 0, app_idx)
    if img_idx != -1:
        content = content[:img_idx] + '<img src="assets/images/environment.jpg"' + content[img_idx + 33:]

# 6. Final CTA Buttons
btn_html_old = '''<div class="cta-actions">
                    <a href="courses.html" class="primary-btn-style cta-btn">Explore Courses</a>
                    <a href="service.html" class="secondary-btn-style cta-btn">Our Services</a>
                </div>'''
btn_html_new = '''<div class="cta-actions" style="display: flex; justify-content: center; gap: 15px; margin-top: 30px;">
                    <a href="courses.html" class="btn btn-primary" style="background-color: var(--primary-purple); color: white; border: none; padding: 12px 28px;">Explore Courses</a>
                    <a href="service.html" class="btn btn-outline" style="border-color: var(--primary-purple); color: var(--primary-purple); padding: 12px 28px;">Our Services</a>
                </div>'''
content = content.replace(btn_html_old, btn_html_new)

# Add a little negative margin to the featured section to create the overlap effect since hero is now dark
feat_search = '<section class="blog-section-featured">'
feat_replace = '<section class="blog-section-featured" style="margin-top: -80px; position: relative; z-index: 10;">'
content = content.replace(feat_search, feat_replace)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Blog page updated!")
