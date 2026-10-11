import re
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the base64 image with the new image reference - use a broader regex
content = re.sub(
    r'<img alt="KIIIBI Original Pure Shea Butter, 500g jar" src="data:image/jpeg;base64,[^"]*">',
    '<img alt="Kiiibi Cleanse Black Cream Wash 250g jar" src="kiiibi-cleanse.jpeg">',
    content
)

with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')