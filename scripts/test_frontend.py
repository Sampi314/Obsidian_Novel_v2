from playwright.sync_api import sync_playwright
import os

def test_chapter_generation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to one of the newly generated markdown files via reader.html
        page.goto(f"file://{os.getcwd()}/reader.html?file=%C4%90%E1%BA%A1o/Ch%C6%B0%C6%A1ng_Truy%E1%BB%87n/G%C3%B3c_Nh%C3%ACn_L%C3%A2m_Phong/Ch%C6%B0%C6%A1ng_00006_Th%E1%BB%8B_Tr%E1%BA%A5n_V%C3%B9ng_Bi%C3%AAn.md")
        page.wait_for_selector("#content")

        # Take a screenshot
        page.screenshot(path="chapter_06_lam_phong.png", full_page=True)

        # Navigate to the second newly generated markdown file via reader.html
        page.goto(f"file://{os.getcwd()}/reader.html?file=%C4%90%E1%BA%A1o/Ch%C6%B0%C6%A1ng_Truy%E1%BB%87n/G%C3%B3c_Nh%C3%ACn_L%C3%A2m_Phong/Ch%C6%B0%C6%A1ng_00007_%C4%90%C6%B0%E1%BB%9Dng_V%C3%A0o_Nam_C%C6%B0%C6%A1ng.md")
        page.wait_for_selector("#content")

        # Take a screenshot
        page.screenshot(path="chapter_07_lam_phong.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    test_chapter_generation()
