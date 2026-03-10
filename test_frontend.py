from playwright.sync_api import sync_playwright

def test_chapter_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to one of the newly generated HTML files
        page.goto("file:///app/Đạo HTML/Chương_Truyện/Góc_Nhìn_Chính/Chương_00111_Dấu_Vết_Tại_Vạn_Yêu_Thành.html")

        # Take a screenshot
        page.screenshot(path="screenshot_111.png", full_page=True)

        # Navigate to the second newly generated HTML file
        page.goto("file:///app/Đạo HTML/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm/Chương_00105_Tam_Vương_Nội_Chiến.html")

        # Take a screenshot
        page.screenshot(path="screenshot_105.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_chapter_generation()
