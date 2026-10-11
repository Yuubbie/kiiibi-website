import re

with open('C:\\Users\\HP\\AppData\\Local\\Temp\\opencode\\kiiibi-website\\about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the footer section - use a more flexible approach
# Find from <footer> to </footer>
footer_start = content.find('<footer>')
footer_end = content.find('</footer>') + len('</footer>')

if footer_start >= 0 and footer_end > footer_start:
    print(f"Found footer from {footer_start} to {footer_end}")
    old_footer = content[footer_start:footer_end]
    print(f"Old footer length: {len(old_footer)}")
    
    new_footer = '''<footer>
<div class="wrap">
<div class="footer-grid">
<div class="footer-brand">
<img class="footer-logo" src="kiiibi-logo.jpeg" alt="KIIIBI">
<p>KIIIBI is the body care line of Kweevah Bath Body Naturals. Nature meets Refinement. Made in Nigeria.</p>
<p class="footer-tagline">Nature meets Refinement.</p>
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
    
    content = content[:footer_start] + new_footer + content[footer_end:]
    
    with open('C:\\Users\\HP\\AppData\\Local\\Temp\\opencode\\kiiibi-website\\about.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Footer replaced successfully!")
else:
    print("Could not find footer tags")