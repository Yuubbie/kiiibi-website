$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Find the exact string to replace
$oldImg = '<img alt="Kweevah Bath Body Naturals" src="data:image/png;base64,'
$idx = $content.IndexOf($oldImg)
if ($idx -ge 0) {
    # Find the closing ">
    $endIdx = $content.IndexOf('">', $idx)
    if ($endIdx -ge 0) {
        $endIdx += 2  # Include the ">
        $toReplace = $content.Substring($idx, $endIdx - $idx)
        $newImg = '<img alt="KIIIBI" src="kiiibi-logo.jpeg">'
        $content = $content.Replace($toReplace, $newImg)
        Set-Content $path -Value $content
        Write-Host "Replaced brandmark image"
    }
} else {
    Write-Host "Could not find brandmark image"
}