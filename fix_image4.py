import re
with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the entire hero-visual div
old_hero_visual = '''<div class="hero-visual">
<div class="frame">
<img alt="KIIIBI Original Pure Shea Butter, 500g jar" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAUEBAQEAwUEBAQGBQUGCA0ICAcHCBALDAkNExAUExIQEhIUFx0ZFBYcFhISGiMaHB4fISEhFBkkJyQgJh0gISD/2wBDAQUGBggHCA8ICA8gFRIVICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICD/wAARCALdBEwDASIAAhEBAxEB/8QAHQAAAQUBAQEBAAAAAAAAAAAAAgEDBAUGAAcICf/EAF0QAAIBAwMCAwQFBwcGCQkGBwECAwAEEQUSIQYxE0FRByJhcRQygZGhFSNCUrHB0QgzYnKCkrMWJENTdeEXNERUY6KywvAlNjdVdIOEk/EYJidFZGVz0jWU06PD/8QAGgEAAwEBAQEAAAAAAAAAAAAAAAECAwQFBv/EADYRAAICAgICAQMDAgUEAgIDAAABAhEDEiExQVETBCJhMnGhBfBCUoGRsRQjQ+HB0TPxYnKS/9oADAMBAAIRAxEAPwD0IURoa7zrxT1jvOjFBXBsUAPClxTatTg7UxAmhI5ozSgDzoADsKaY1II4phxQAGaKgzilU5FIY6OKQ8ikpfKgBO1LmuxzXUAEtFTefspxTzTAUU4KRRS4piFJxQ5pPOuoEdS9q4VxpDFB5pd3FNc5oqACyK6k48qWgBccUuPWk7UuaAOxiuFJmiU80wAZTimmqSaZdeKlghndiiVqbcYpFpWOiSCc0WaZDEUYOTTCgxRihFGKYhMHvRV2aTdQB3eurq6mB2K77a7PpSZoAWkPalzSZoATzpfKkAyaI9qQAHOaQiiPFATzQAh70lFjNcVpDG8miUn41205ogoFAwlpzNAMAUtMkXNEKQDmiAFAHeVcaXFcRTAbLUGctxRsvNJtpAIKMDNIFohQBwXmuNFQtQA33NLS4pMc0hirxTgoAMUucUxB5+6uzQZpVPNAC0uK7FLQAmKSiNATTAXPFJmhLV2aQCmmXp08imWFIaAzzRc4pMc0YFAwRSnAFKBikagQBNCM0WK4CkMJfSnFpteKNc0xDnlXVwpTxTENtwKaJo3PrTdSxpBCloRxzXZoGHSqeaSkpiHQeaLdTQNcWoAPNGDTIOacBoAOupM11MQ53pDSA8V2eKAENCKUmkoAQ0JojSEUgEFdzSgcUJPNAwgRRd6aFHmgDqQ+ldmk+dAjq4CurqAFFKBXUuaYHYxQgmlY0GcUCCzXE0Gc0XlSGd3rvLntQsyoMscVVX2qxwqfeApN0BZmaNeN1cGV/qnNefXfVMMUxBkH31Z6V1FHORh6hTTdEKabo15XFAwwKCC6SZQQacbmtCxuu8qUjAod3NIYmKQijPagagQ21RpPOn3PFRZG4NIYwx70wTzRu3xpgtz3qRmiNdQ5oS3NaAOHtTZJzwKINmuxTEEh9ac3eVM5xRg0AHmizQDmiB4piFzTTmjzTTmkA0Tk0S8U2frU4vakMOiHakFLjigBfKhPeipBTA4DNPKtCop1cUCFApCKUnFJnimAOK7FKTSZoA7NJXE80gNIAxXUgNKDQAhpR3riKTFABV1dSGgDicVwam2PpXKcmgCQKFhSrSsMimBFcZ4pFWnWU5rgtTQ7BI4pMkGnivHamytABqc04KbQU8BTEIeKDNGRQlc0AKKQnFd2oTQAuaIc0GaUGmAXrQ/bS5zSfZQBwPNGDQAUQpAceabI54p3FJQAAHNHjiupeaABIoeaI0negZ1dS4pDxSAINRg0xmjU0APg12abDDFECKYhD3pDRGhxQB2a7PNJik86ADzSedcBRbaAEHNLilVaIjFAA4oDTuKBhQAFEvegNGMZpDHB2rs0OaQnNMQpagY8UhoSaBiZ5owfWm880QNIKHKEgUoNLQIa20vyosDFcB... (line truncated to 2000 chars)
</div>
<div class="float-tag">
<strong>250g</strong>
<span>₦12,650 — Black Cream Wash</span>
</div>
</div>'''

new_hero_visual = '''<div class="hero-visual">
<div class="frame">
<img alt="Kiiibi Cleanse Black Cream Wash 250g jar" src="kiiibi-cleanse.jpeg">
</div>
<div class="float-tag">
<strong>250g</strong>
<span>₦12,650 — Black Cream Wash</span>
</div>
</div>'''

if old_hero_visual in content:
    content = content.replace(old_hero_visual, new_hero_visual)
    print('Replaced via exact match')
else:
    print('Exact match failed, trying regex')
    # Use regex with DOTALL to match across lines
    content = re.sub(
        r'<div class="hero-visual">.*?<div class="float-tag">.*?<strong>250g</strong>.*?</div>\s*</div>',
        new_hero_visual,
        content,
        flags=re.DOTALL
    )
    print('Replaced via regex')

with open(r'C:\Users\HP\AppData\Local\Temp\opencode\kiiibi-website\index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')