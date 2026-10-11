$path = 'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\lifestyle.html'
$content = Get-Content $path -Raw

# Normalize line endings
$content = $content.Replace("`r`n", "`n").Replace("`r", "`n")

# Remove everything from the second <a href="products.html" after </nav> up to and including the second </nav>
$idx = $content.IndexOf('</nav>')
if ($idx -ge 0) {
    $idx2 = $content.IndexOf('</nav>', $idx + 6)
    if ($idx2 -ge 0) {
        # Find the <div class="nav-actions"> after the second </nav>
        $idx3 = $content.IndexOf('<div class="nav-actions">', $idx2)
        if ($idx3 -ge 0) {
            # Remove from after first </nav> to before <div class="nav-actions">
            $before = $content.Substring(0, $idx + 6)  # Include first </nav>
            $after = $content.Substring($idx3)
            $content = $before + "`n" + $after
        }
    }
}

Set-Content $path -Value $content
Write-Host "Done"