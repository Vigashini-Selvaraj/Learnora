import os
import re

files = [
    'course-detail-math.html',
    'course-detail-science.html',
    'course-detail-physics.html',
    'course-detail-exam.html'
]

old_math_curriculum = '''                    <!-- Module 1 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 01 &mdash; Algebraic Foundations</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Linear Equations in Two Variables</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Quadratic Equations Basics</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Arithmetic Progressions (AP)</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Polynomials & Factorization</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Module 2 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 02 &mdash; Geometry & Trigonometry</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Introduction to Trigonometry</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Trigonometric Identities</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Triangles & Similarity</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Circles & Tangents</span>
                            </div>
                        </div>
                    </div>'''

science_curriculum = '''                    <!-- Module 1 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 01 &mdash; Physical Sciences</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Motion and Measurement</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Light, Shadows and Reflections</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Electricity and Circuits</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Fun with Magnets</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Module 2 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 02 &mdash; Life Sciences & Chemistry</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Components of Food</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Getting to Know Plants</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Sorting Materials into Groups</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Changes Around Us</span>
                            </div>
                        </div>
                    </div>'''

exam_curriculum = '''                    <!-- Module 1 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 01 &mdash; Core Concept Revision</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Revision</span>
                                <span>High-Yield Topics Review</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Revision</span>
                                <span>Formula and Theorem Recaps</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Practice</span>
                                <span>Solving Important Questions</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Module 2 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 02 &mdash; Mock Tests & Papers</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Mock</span>
                                <span>Full-Length Mock Test 1</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Analysis</span>
                                <span>Mock Test 1 Detailed Review</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Mock</span>
                                <span>Full-Length Mock Test 2</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Analysis</span>
                                <span>Mock Test 2 Detailed Review</span>
                            </div>
                        </div>
                    </div>'''

for filename in files:
    path = os.path.join(r'c:\Users\vigas\Desktop\learnora', filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Curriculum for Science and Exam (Physics already done, Math stays same)
    if filename == 'course-detail-science.html':
        content = content.replace(old_math_curriculum, science_curriculum)
    elif filename == 'course-detail-exam.html':
        content = content.replace(old_math_curriculum, exam_curriculum)

    # 2. Remove View Full Profile link
    content = re.sub(r'<a href="#" style="color: var\(--primary-purple\); font-weight: 600; text-decoration: none;">View Full Profile &rarr;</a>', '', content)
    
    # Also catch other variations if they exist
    content = re.sub(r'<a[^>]*>View Full Profile\s*(?:&rarr;)?</a>', '', content)

    # 3. Remove the entire Course Detail Accordions Logic script tag
    # We will use regex to find the script tag that contains "Course Detail Accordions Logic"
    script_pattern = re.compile(r'<!-- Course Detail Accordions Logic -->\s*<script>.*?</script>', re.DOTALL)
    content = re.sub(script_pattern, '', content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Final changes applied.")
