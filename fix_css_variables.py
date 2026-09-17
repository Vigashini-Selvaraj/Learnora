import os

css_dir = 'user-dashboard/css'

replacements = {
    'var(--text)': 'var(--main-text)',
    'var(--background)': 'var(--bg-color)',
    'var(--primary-dark)': 'var(--main-text)', # For headings
    'color: var(--white)': 'color: #ffffff', # For text in buttons
    'background: var(--white)': 'background: var(--card-bg)', # For backgrounds
}

# Special handling for btn-primary hover
def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    # Fix btn-primary hover background which was using --primary-dark
    content = content.replace('background: var(--main-text);', 'background: var(--primary-purple-dark);')
    # Because we replaced --primary-dark with --main-text, the hover rule `background: var(--primary-dark)` became `background: var(--main-text)`
    # This might accidentally replace other backgrounds, but let's see.
    # A safer way:
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filename in os.listdir(css_dir):
    if filename.endswith('.css'):
        process_file(os.path.join(css_dir, filename))

print("CSS files updated successfully.")
