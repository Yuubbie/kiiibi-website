$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Use a simpler approach - replace the specific duplicate block
$oldBlock = '</nav>
<a href="products.html" data-page="products">Shop</a>
<a href="ritual.html" data-page="ritual">Our Ritual</a>
<a href="about.html" data-page="about">About</a>
<a href="lifestyle.html" data-page="lifestyle">Lifestyle</a>
<a href="contact.html" data-page="contact">Contact</a>
</nav>
<div class="nav-actions">'

$newBlock = '</nav>
<div class="nav-actions">'

$content = $content.Replace($oldBlock, $newBlock)

Set-Content $path -Value $content
Write-Host "Done"