# Read the file
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\products.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the product-grid section to replace
start_marker = '<div class="product-grid">'
end_marker = '</div>\n</div>\n</section>'

# Find the first occurrence of product-grid after the section-head
start_idx = content.find(start_marker, content.find('<section class="products"'))
if start_idx == -1:
    print("Could not find start marker")
    exit(1)

# Find the closing </div> of product-grid by counting divs
search_start = start_idx + len(start_marker)
div_count = 1
pos = search_start
while pos < len(content) and div_count > 0:
    next_open = content.find('<div', pos)
    next_close = content.find('</div>', pos)
    if next_close == -1 or (next_open != -1 and next_open < next_close):
        div_count += 1
        pos = next_open + 4
    else:
        div_count -= 1
        if div_count == 0:
            end_product_grid = next_close + 6  # include </div>
            break
        pos = next_close + 6

if div_count != 0:
    print("Could not find matching closing div for product-grid")
    exit(1)

print(f"Found product-grid from {start_idx} to {end_product_grid}")

# New content
new_product_grid = '''<div class="product-grid">
<div class="product-card" data-idx="0" data-title="Kiiibi Cleanse" data-tag="Black Cream Wash" data-desc="Crafted in Nigeria with plantain peel ash, palm kernel oil, shea butter, and nourishing botanicals. Our Black Cream Wash creates a rich, creamy lather that cleanses thoroughly without leaving skin dry or stripped. Skin feels clean, comfortable, and refreshed after every wash." data-placeholder="0" data-benefits="Creamy lather|Clean, comfortable skin|Refreshed after every wash" data-ingredients="Plantain peel ash, palm kernel oil, shea butter, nourishing botanicals" data-sizes="200g \u00b7 250g" data-wa="https://wa.me/2348129711772?text=Hi%20KIIIBI!%20I%27d%20love%20to%20order%20Kiiibi%20Cleanse%20%F0%9F%98%8A">
<div class="thumb"><img alt="Kiiibi Cleanse Black Cream Wash" src="kiiibi-cleanse.jpeg"></div>
<p class="tag">Black Cream Wash</p>
<h3>Kiiibi Cleanse</h3>
<p class="desc">Crafted in Nigeria with plantain peel ash, palm kernel oil, shea butter, and nourishing botanicals. Our Black Cream Wash creates a rich, creamy lather that cleanses thoroughly without leaving skin dry or stripped. Skin feels clean, comfortable, and refreshed after every wash.</p>
<div class="meta">
  <span class="size">200g <span class="limited-tag">\u20a611,300</span> \u00b7 250g <span class="limited-tag">\u20a612,650</span></span>
  <span class="price">From \u20a611,300</span>
</div>
<a class="order" href="https://wa.me/2348129711772?text=Hi%20KIIIBI!%20I%27d%20love%20to%20order%20Kiiibi%20Cleanse%20%F0%9F%98%8A">Order on WhatsApp</a>
<button class="read-more" type="button">Read More</button>
</div>
</div>'''

# Replace
new_content = content[:start_idx] + new_product_grid + content[end_product_grid:]

# Write back
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\products.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Replacement done successfully!")