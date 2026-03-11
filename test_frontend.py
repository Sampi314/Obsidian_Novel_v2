from playwright.sync_api import sync_playwright

def test_chapter_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to one of the newly generated HTML files
        page.goto("file:///app/Đạo HTML/Chương_Truyện/Góc_Nhìn_Chính/Chương_00125_Băng_Uyên_Sụp_Đổ.html")

        # Take a screenshot
        page.screenshot(path="chapter125.png", full_page=True)

        # Navigate to the second newly generated HTML file
        page.goto("file:///app/Đạo HTML/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm/Chương_00119_Nuốt_Chửng_Ma_Châu.html")

        # Take a screenshot
        page.screenshot(path="chapter119.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_chapter_generation()
