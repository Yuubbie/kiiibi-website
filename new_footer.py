with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the footer section
start = content.find('<footer>')
end = content.find('</footer>') + 8

old_footer = content[start:end]

new_footer = '''<footer>
<div class="wrap">
<div class="footer-grid">
<div class="footer-brand">
<img class="footer-logo" src="kiiibi-logo.jpeg" alt="KIIIBI">
<p>KIIIBI is the body care line of Kweevah Bath Body Naturals. Nature meets Refinement. Made in Nigeria.</p>
<div class="footer-social">
<a aria-label="Instagram" href="https://instagram.com/kiiibi1"><svg fill="none" stroke-width="1.6" viewbox="0 0 24 24"><rect height="18" rx="5" width="18" x="3" y="3"></rect><circle cx="12" cy="12" r="4"></circle><circle cx="17.5" cy="6.5" fill="currentColor" r="0.8" stroke="none"></circle></svg></a>
<a aria-label="WhatsApp" href="https://wa.me/2348129711772"><svg fill="none" stroke-width="1.6" viewbox="0 0 24 24"><path d="M4 20l1.4-4.2A8 8 0 1 1 9 19L4 20z"></path></svg></a>
</div>
</div>
<div class="footer-col">
<h5>Shop</h5>
<ul>
<li><a href="products.html">Kiiibi Cleanse</a></li>
</ul>
</div>
<div class="footer-col">
<h5>Company</h5>
<ul>
<li><a href="about.html">Our Story</a></li>
<li><a href="ritual.html">Our Ritual</a></li>
<li><a href="contact.html">Contact</a></li>
</ul>
</div>
<div class="footer-col">
<h5>Stay in Touch</h5>
<p>contactkiiibi@kiiibi.com</p>
<p>+234 812 971 1772</p>
<p>www.kiiibi.com</p>
<p>@kiiibi1</p>
</div>
</div>
<div class="footer-bottom">
<span>© 2026 Kweevah Bath Body Naturals. All rights reserved.</span>
<span>Made in Nigeria, always.</span>
<a class="credit-link" href="https://wa.me/2347032352158?text=Hi%20Yubbie%2C%20I%20saw%20the%20KIIIBI%20website%20and%20I%27d%20like%20to%20talk%20about%20a%20website%20too" target="_blank" rel="noopener">Built by Yubbie Pen & Pixel</a>
</div>
</div>
</footer>'''

content = content[:start] + new_footer + content[end:]

with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Footer updated successfully!')