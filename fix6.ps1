$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Remove the duplicate nav section (lines 666-671 in the current output)
$content = $content -replace "`n<a href=`"products.html`" data-page=`"products`">Shop</a>`n<a href=`"ritual.html`" data-page=`"ritual`">Our Ritual</a>`n<a href=`"about.html`" data-page=`"about`">About</a>`n<a href=`"lifestyle.html`" data-page=`"lifestyle`">Lifestyle</a>`n<a href=`"contact.html`" data-page=`"contact`">Contact</a>`n</nav>`n<div class=`"nav-actions`">", "`n<div class=`"nav-actions`">"

Set-Content $path -Value $content
Write-Host "Removed duplicate nav"