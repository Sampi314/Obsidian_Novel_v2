from playwright.sync_api import sync_playwright
import os

def test_chapter_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to one of the newly generated HTML files
        page.goto(f"file://{os.getcwd()}/Đạo HTML/Chương_Truyện/Góc_Nhìn_Chính/Chương_00128_Hành_Trình_Băng_Ngục.html")

        # Take a screenshot
        page.screenshot(path="chapter_128.png", full_page=True)

        # Navigate to the second newly generated HTML file
        page.goto(f"file://{os.getcwd()}/Đạo HTML/Chương_Truyện/Góc_Nhìn_Lệ_Vô_Tâm/Chương_00122_Bàn_Tiệc_Đẫm_Máu.html")

        # Take a screenshot
        page.screenshot(path="chapter_122.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_chapter_generation()
