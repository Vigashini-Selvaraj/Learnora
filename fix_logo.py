import os

css_path = r'c:\Users\vigas\Desktop\learnora\css\style.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

logo_css = '''
/* Logo Subtitle Styling */
.logo-subtitle {
  font-size: 0.6rem;
  color: var(--primary-purple);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-top: 2px;
  transition: color 0.2s ease;
}

[data-theme="dark"] .logo-subtitle {
  color: #b59ee0; /* Lighter purple for dark mode contrast */
}
'''

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content + '\n' + logo_css)

print("Logo subtitle CSS added to style.css")
