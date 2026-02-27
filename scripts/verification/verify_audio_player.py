import os
from playwright.sync_api import sync_playwright

def verify_audio_player():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Read the markdown file content
        cwd = os.getcwd()
        md_path = os.path.join(cwd, "Đạo/Chương_Truyện/Góc_Nhìn_Chính/Chương_00001_Dấu_Hiệu_Tai_Ương.md")

        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Create a temporary HTML file
        # We wrap it in a basic body to ensure the browser treats it as HTML
        # Note: The markdown text will just appear as unformatted text, but the HTML tags
        # for navigation will be rendered by the browser.
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <body>
        {content}
        </body>
        </html>
        """

        temp_html_path = os.path.join(cwd, "scripts/verification/temp_chapter.html")
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Load the temporary HTML file
        page.goto(f"file://{temp_html_path}")

        # Wait for the audio player container to be visible
        try:
            # We look for the ID we added
            selector = "#chapter-navigation"
            page.wait_for_selector(selector, timeout=5000)

            # Take a screenshot of the navigation and audio player area
            element = page.locator(selector)
            screenshot_path = os.path.join(cwd, "scripts/verification/audio_player.png")
            element.screenshot(path=screenshot_path)

            print(f"Verification successful. Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Verification failed: {e}")
            # Take a full page screenshot for debugging
            page.screenshot(path="scripts/verification/debug_full_page.png")

        finally:
            browser.close()
            # Clean up
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)

if __name__ == "__main__":
    verify_audio_player()
