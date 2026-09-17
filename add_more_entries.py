import re

with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add extra Tutors
tutors_replacement = """                        <div class="action-btns" style="justify-content: center;">
                            <button class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;">View Profile</button>
                            <button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.85rem;">Schedule</button>
                        </div>
                    </div>
                    
                    <!-- Tutor Card -->
                    <div class="profile-card">
                        <img src="https://ui-avatars.com/api/?name=Michael+Chen&background=10B981&color=fff" alt="Michael Chen" class="profile-img">
                        <h4 class="profile-name">Michael Chen</h4>
                        <div class="profile-role">Physics Expert</div>
                        <div class="profile-meta">
                            <div class="meta-box">
                                <strong>6 Yrs</strong>
                                <span>Experience</span>
                            </div>
                            <div class="meta-box">
                                <strong>2</strong>
                                <span>Active Batches</span>
                            </div>
                        </div>
                        <div style="margin-bottom: 20px;">
                            <span class="status-badge purple">Grades 10-12</span>
                            <span class="status-badge success">Available</span>
                        </div>
                        <div class="action-btns" style="justify-content: center;">
                            <button class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;">View Profile</button>
                            <button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.85rem;">Schedule</button>
                        </div>
                    </div>

                    <!-- Tutor Card -->
                    <div class="profile-card">
                        <img src="https://ui-avatars.com/api/?name=Sarah+Connor&background=F4B942&color=fff" alt="Sarah Connor" class="profile-img">
                        <h4 class="profile-name">Sarah Connor</h4>
                        <div class="profile-role">English Teacher</div>
                        <div class="profile-meta">
                            <div class="meta-box">
                                <strong>4 Yrs</strong>
                                <span>Experience</span>
                            </div>
                            <div class="meta-box">
                                <strong>3</strong>
                                <span>Active Batches</span>
                            </div>
                        </div>
                        <div style="margin-bottom: 20px;">
                            <span class="status-badge purple">Grades 8-12</span>
                            <span class="status-badge success">Available</span>
                        </div>
                        <div class="action-btns" style="justify-content: center;">
                            <button class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;">View Profile</button>
                            <button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.85rem;">Schedule</button>
                        </div>
                    </div>"""
if 'Michael Chen' not in html:
    html = re.sub(r'                        <div class="action-btns" style="justify-content: center;">\s*<button class="btn btn-secondary" style="padding: 8px 16px; font-size: 0.85rem;">View Profile</button>\s*<button class="btn btn-outline" style="padding: 8px 16px; font-size: 0.85rem;">Schedule</button>\s*</div>\s*</div>\s*</div>\s*</section>', tutors_replacement + '\n                </div>\n            </section>', html, flags=re.DOTALL)

with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(html)
