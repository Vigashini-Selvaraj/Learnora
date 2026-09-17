import os
import re

files = [
    'course-detail-math.html',
    'course-detail-science.html',
    'course-detail-physics.html',
    'course-detail-exam.html'
]

old_testimonials = '''                <div class="testi-grid">
                    <div class="testi-card">
                        <div class="testi-rating">⭐⭐⭐⭐⭐</div>
                        <p class="testi-text">"I always feared algebra, but the structured lessons and Ananya Ma'am's patience completely changed my perspective. I scored 95% in my boards!"</p>
                        <div class="testi-author">
                            <strong>Vikram S.</strong>
                            <span>Grade 10</span>
                        </div>
                    </div>
                    <div class="testi-card">
                        <div class="testi-rating">⭐⭐⭐⭐⭐</div>
                        <p class="testi-text">"The weekly tests really kept my son on his toes. I could track his progress perfectly through the dashboard."</p>
                        <div class="testi-author">
                            <strong>Neha G.</strong>
                            <span>Parent</span>
                        </div>
                    </div>
                </div>'''

new_testimonials = '''                <div class="testi-grid">
                    <div class="testi-card">
                        <div class="testi-rating">⭐⭐⭐⭐⭐</div>
                        <p class="testi-text">"Learnora helped me understand math concepts I always struggled with. The tutors are so patient!"</p>
                        <div class="testi-author">
                            <img src="assets/images/student_priya.jpg" alt="Priya Sharma" class="testi-img" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; margin-bottom: 10px;">
                            <strong>Priya Sharma</strong>
                            <span>Grade 10 Student</span>
                        </div>
                    </div>
                    <div class="testi-card">
                        <div class="testi-rating">⭐⭐⭐⭐⭐</div>
                        <p class="testi-text">"Seeing my son's confidence grow has been amazing. The structured batches work perfectly for us."</p>
                        <div class="testi-author">
                            <img src="assets/images/parent_rajiv.jpg" alt="Rajiv Menon" class="testi-img" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; margin-bottom: 10px;">
                            <strong>Rajiv Menon</strong>
                            <span>Parent</span>
                        </div>
                    </div>
                    <div class="testi-card">
                        <div class="testi-rating">⭐⭐⭐⭐⭐</div>
                        <p class="testi-text">"The study materials and regular assessments keep me on track for my board exams. Highly recommend Learnora."</p>
                        <div class="testi-author">
                            <img src="assets/images/student_sneha.jpg" alt="Sneha Patel" class="testi-img" style="width: 50px; height: 50px; border-radius: 50%; object-fit: cover; margin-bottom: 10px;">
                            <strong>Sneha Patel</strong>
                            <span>Grade 12 Student</span>
                        </div>
                    </div>
                </div>'''

old_physics_curriculum = '''                    <!-- Module 1 -->
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
                            <svg class="module-icon" viewBox="0 0 24 24" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><polyline points=\"6 9 12 15 18 9\"></polyline></svg>
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

new_physics_curriculum = '''                    <!-- Module 1 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 01 &mdash; Mechanics</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Kinematics and Dynamics</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Work, Energy and Power</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Rotational Motion</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Gravitation</span>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Module 2 -->
                    <div class="curriculum-module">
                        <div class="module-header">
                            <span>Module 02 &mdash; Electromagnetism & Modern Physics</span>
                            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                        <div class="module-content">
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 1</span>
                                <span>Electrostatics & Capacitance</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 2</span>
                                <span>Current Electricity</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 3</span>
                                <span>Magnetic Effects of Current</span>
                            </div>
                            <div class="lesson-item">
                                <span class="lesson-badge">Lesson 4</span>
                                <span>Dual Nature & Atoms</span>
                            </div>
                        </div>
                    </div>'''

for filename in files:
    path = os.path.join(r'c:\Users\vigas\Desktop\learnora', filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Testimonials
    content = content.replace(old_testimonials, new_testimonials)
    
    # 2. Physics Curriculum
    if filename == 'course-detail-physics.html':
        content = content.replace(old_physics_curriculum, new_physics_curriculum)
        
    # 3. View Full Profile - remove
    content = re.sub(r'<a href="#" class="btn btn-secondary"[^>]*>View Full Profile</a>', '', content)
    
    # 4. Choose Your Plan link
    content = content.replace('href="#pricing"', 'href="pricing.html"')
    
    # 5. Fix Accordion bug
    content = content.replace("header.addEventListener('click', () => {", "header.addEventListener('click', (e) => { e.stopImmediatePropagation();")
    content = content.replace("q.addEventListener('click', () => {", "q.addEventListener('click', (e) => { e.stopImmediatePropagation();")
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
