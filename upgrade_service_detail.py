import os
import re

file_path = r'c:\Users\vigas\Desktop\learnora\service-detail.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

styles_to_inject = '''
    <style>
        .premium-card {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.4);
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.05);
            border-radius: 20px;
            padding: 40px;
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s;
        }
        .premium-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(31, 38, 135, 0.12);
        }
        
        .roadmap-container {
            display: flex;
            flex-direction: column;
            gap: 40px;
            position: relative;
            margin-top: 50px;
        }
        .roadmap-container::before {
            content: '';
            position: absolute;
            left: 50%;
            top: 0;
            bottom: 0;
            width: 2px;
            background: var(--primary-purple);
            transform: translateX(-50%);
            opacity: 0.2;
        }
        .roadmap-step {
            display: flex;
            align-items: center;
            width: 100%;
            justify-content: space-between;
        }
        .roadmap-step:nth-child(even) {
            flex-direction: row-reverse;
        }
        .roadmap-content {
            width: 45%;
            background: var(--white);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.06);
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
            border: 1px solid var(--border-color);
        }
        .roadmap-content:hover {
            transform: scale(1.03);
            box-shadow: 0 12px 30px rgba(0,0,0,0.1);
        }
        .roadmap-number {
            width: 50px;
            height: 50px;
            background: var(--primary-purple);
            color: var(--white);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 1.5rem;
            font-weight: bold;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            box-shadow: 0 0 0 8px rgba(91, 58, 140, 0.1);
            z-index: 2;
        }
        .roadmap-step:nth-child(odd) .roadmap-number {
            right: -83px;
        }
        .roadmap-step:nth-child(even) .roadmap-number {
            left: -83px;
        }
        
        @media(max-width: 768px) {
            .roadmap-container::before { left: 25px; }
            .roadmap-step { flex-direction: column; align-items: flex-end; }
            .roadmap-step:nth-child(even) { flex-direction: column; align-items: flex-end; }
            .roadmap-content { width: calc(100% - 60px); }
            .roadmap-step:nth-child(odd) .roadmap-number,
            .roadmap-step:nth-child(even) .roadmap-number {
                left: -60px;
                right: auto;
            }
        }
        
        .included-item {
            transition: transform 0.3s;
        }
        .included-item:hover {
            transform: translateY(-5px);
        }
    </style>
</head>'''

content = content.replace('</head>', styles_to_inject)

# Update the Benefits section to use premium-card
content = content.replace('class="subject-card" style="padding: 40px 30px; text-align: center; border-radius: 20px; transition: transform 0.3s; box-shadow: var(--shadow-sm);"', 'class="premium-card" style="text-align: center;"')

# Replace the old Process section grid with the interactive roadmap
old_process_pattern = re.compile(r'<div class="service-steps-grid reveal" style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(220px, 1fr\)\); gap: 30px; margin-top: 50px;">.*?</div>\s*</div>\s*</section>', re.DOTALL)

new_roadmap_html = '''<div class="roadmap-container reveal">
                <div class="roadmap-step">
                    <div class="roadmap-content">
                        <div class="roadmap-number">1</div>
                        <h4 style="margin-bottom: 12px; font-size: 1.25rem;">Initial Assessment</h4>
                        <p style="color: var(--secondary-text); font-size: 0.95rem; line-height: 1.6; margin:0;">We evaluate your child's current academic standing, identify learning gaps, and define clear milestones.</p>
                    </div>
                    <div style="width: 45%;"></div>
                </div>
                
                <div class="roadmap-step">
                    <div class="roadmap-content">
                        <div class="roadmap-number">2</div>
                        <h4 style="margin-bottom: 12px; font-size: 1.25rem;">Expert Matching</h4>
                        <p style="color: var(--secondary-text); font-size: 0.95rem; line-height: 1.6; margin:0;">We thoughtfully pair your child with an expert tutor whose teaching style matches their unique learning style.</p>
                    </div>
                    <div style="width: 45%;"></div>
                </div>

                <div class="roadmap-step">
                    <div class="roadmap-content">
                        <div class="roadmap-number">3</div>
                        <h4 style="margin-bottom: 12px; font-size: 1.25rem;">Custom Learning Plan</h4>
                        <p style="color: var(--secondary-text); font-size: 0.95rem; line-height: 1.6; margin:0;">A tailored curriculum is designed specifically for your child, focusing intensely on the goals you wish to achieve.</p>
                    </div>
                    <div style="width: 45%;"></div>
                </div>

                <div class="roadmap-step">
                    <div class="roadmap-content">
                        <div class="roadmap-number">4</div>
                        <h4 style="margin-bottom: 12px; font-size: 1.25rem;">Ongoing Support</h4>
                        <p style="color: var(--secondary-text); font-size: 0.95rem; line-height: 1.6; margin:0;">Regular classes commence with dynamic feedback and monthly progress reports sent directly to parents.</p>
                    </div>
                    <div style="width: 45%;"></div>
                </div>
            </div>
        </div>
    </section>'''

content = re.sub(old_process_pattern, new_roadmap_html, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated service-detail.html with premium styling.")
