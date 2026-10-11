$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Fix brandmark - replace the malformed version
$content = $content -replace '<a class="brandmark" href="index.html">`n<img alt="KIIIBI" src="kiiibi-logo.jpeg">`n</a><a href="index.html" data-page="index">Home</a>', "<a class=`"brandmark`" href=`"index.html`">`n<img alt=`"KIIIBI`" src=`"kiiibi-logo.jpeg`">`n</a>`n<nav class=`"primary`" id=`"primaryNav`">`n<a href=`"index.html`" data-page=`"index`">Home</a>`n<a href=`"products.html`" data-page=`"products`">Shop</a>`n<a href=`"#notify`" data-page=`"notify`">Get Notified</a>`n<a href=`"contact.html`" data-page=`"contact`">Contact</a>`n</nav>"

Set-Content $path -Value $content
Write-Host "Fixed"