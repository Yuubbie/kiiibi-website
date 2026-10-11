$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Fix the brandmark - add missing </a>
$content = $content -replace '<a class="brandmark" href="index.html">\s*<img alt="KIIIBI" src="kiiibi-logo.jpeg">\s*(?=<a href="index.html")', '<a class="brandmark" href="index.html">`n<img alt="KIIIBI" src="kiiibi-logo.jpeg">`n</a>'

# Replace nav links with 4 links: Home, Shop, Get Notified, Contact
$oldNav = '<nav class="primary" id="primaryNav">\s*<a href="index.html" data-page="index">Home</a>\s*<a href="products.html" data-page="products">Shop</a>\s*<a href="ritual.html" data-page="ritual">Our Ritual</a>\s*<a href="about.html" data-page="about">About</a>\s*<a href="lifestyle.html" data-page="lifestyle">Lifestyle</a>\s*<a href="contact.html" data-page="contact">Contact</a>\s*</nav>'
$newNav = '<nav class="primary" id="primaryNav">`n<a href="index.html" data-page="index">Home</a>`n<a href="products.html" data-page="products">Shop</a>`n<a href="#notify" data-page="notify">Get Notified</a>`n<a href="contact.html" data-page="contact">Contact</a>`n</nav>'

$content = $content -replace $oldNav, $newNav

Set-Content $path -Value $content
Write-Host "Fixed brandmark and nav links"