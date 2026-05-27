from playwright.sync_api import sync_playwright
import pathlib, time

BASE = pathlib.Path(r"C:\Users\Poins\.gemini\antigravity\scratch\fowler-and-sons")
HTML = BASE / "flier.html"
PDF  = BASE / "Fowler_and_Sons_Flier.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 816, "height": 1056})
    page.goto(HTML.as_uri())
    time.sleep(3)  # let fonts + images load
    page.pdf(
        path=str(PDF),
        width="8.5in",
        height="11in",
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        print_background=True,
    )
    browser.close()

print(f"PDF saved to: {PDF}")
