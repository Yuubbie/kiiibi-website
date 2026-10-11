import re
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the exact image tag
match = re.search(r'<img alt="KIIIBI Original Pure Shea Butter, 500g jar" src="data:image/jpeg;base64,[^"]+">', content)
if match:
    print('Found!')
    print(repr(match.group()[:200]))
else:
    print('Not found with exact pattern')
    # Try without the quotes being escaped
    match2 = re.search(r'<img alt=\'KIIIBI Original Pure Shea Butter, 500g jar\' src=[^>]+>', content)
    if match2:
        print('Found with single quotes:', repr(match2.group()[:200]))
    else:
        # Try finding any img tag with base64
        match3 = re.search(r'<img[^>]*base64[^>]*>', content)
        if match3:
            print('Found any base64 img:', repr(match3.group()[:200]))
        else:
            print('No base64 img found')
            # Print a portion around hero-visual
            idx = content.find('hero-visual')
            if idx > 0:
                print('Context around hero-visual:')
                print(repr(content[idx:idx+500]))