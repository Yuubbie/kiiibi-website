import re
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the img tag in hero section
match = re.search(r'<img[^>]*alt=[^>]*500g[^>]*>', content)
if match:
    print('Found:', match.group()[:200])
else:
    print('Not found with that pattern')

# Try finding the hero-visual section
match2 = re.search(r'<div class="hero-visual">.*?</div>\s*</div>\s*</section>', content, re.DOTALL)
if match2:
    print('Hero visual section found')
    # Print the img tag within it
    img_match = re.search(r'<img[^>]*>', match2.group())
    if img_match:
        print('Image tag:', img_match.group()[:300])