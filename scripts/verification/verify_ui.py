import os
import re
from playwright.sync_api import sync_playwright

def verify_ui_improvements():
    # Use a real chapter file
    cwd = os.getcwd()

    # Target directory for temp file must be deep to match ../../../ logic
    target_dir = os.path.join(cwd, "Đạo/Chương_Truyện/Góc_Nhìn_Chính")
    chapter_filename = "Chương_00001_Dấu_Hiệu_Tai_Ương.md"
    chapter_path = os.path.join(target_dir, chapter_filename)

    # Read markdown content
    with open(chapter_path, "r", encoding="utf-8") as f:
        content = f.read()

    # The content contains minimal navigation placeholder and scripts.
    # We will simulate how it is rendered in a browser.

    # We need to wrap this in HTML structure for the browser to execute scripts properly.
    temp_html_path = os.path.join(target_dir, "temp_test_chapter.html")

    # Simple HTML wrapper
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Test UI Chapter</title>
    </head>
    <body class="chapter-page">
        <div class="chapter-content">
            {content}
        </div>
    </body>
    </html>
    """

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Created temp file at {temp_html_path}")

    # Use 'chrome' or 'chromium' depending on what is installed
    with sync_playwright() as p:
        # Launch browser. Headless=True for CI/remote environments
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the file using file:// protocol
        file_url = f"file://{os.path.abspath(temp_html_path)}"
        print(f"Loading {file_url}")

        page.goto(file_url)

        try:
            # Wait for navigation scripts to run and inject content
            # navigation.js creates #chapter-navigation and fills it
            # It also injects CSS link into head

            # 1. Check for CSS injection
            print("Checking for CSS injection...")
            # Wait for link element
            page.wait_for_selector('link[href*="style.css"]', state="attached", timeout=5000)
            print("CSS link injected.")

            # 2. Check for Progress Bar
            print("Checking for Progress Bar...")
            page.wait_for_selector('#progress-bar', state="attached", timeout=5000)
            print("Progress bar injected.")

            # 3. Check for Navigation UI
            print("Checking for Navigation UI...")
            page.wait_for_selector('.nav-bar', state="visible", timeout=5000)
            print("Navigation UI visible.")

            # 4. Check for Audio Player
            print("Checking for Audio Player...")
            page.wait_for_selector('.audio-player', state="visible", timeout=5000)
            print("Audio Player visible.")

            # Take Screenshot for visual verification
            screenshot_dir = os.path.join(cwd, "scripts/verification")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, "ui_verified.png")
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        except Exception as e:
            print(f"Verification failed: {e}")
            page.screenshot(path=os.path.join(cwd, "scripts/verification/ui_failure.png"), full_page=True)

        finally:
            browser.close()
            # Clean up
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)
                print("Cleaned up temp file.")

if __name__ == "__main__":
    verify_ui_improvements()
