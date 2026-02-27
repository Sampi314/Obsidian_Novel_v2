import os
import time
from playwright.sync_api import sync_playwright

def verify_frontend_changes():
    # Setup paths
    cwd = os.getcwd()
    target_dir = os.path.join(cwd, "Đạo/Chương_Truyện/Góc_Nhìn_Chính")
    chapter_filename = "Chương_00001_Dấu_Hiệu_Tai_Ương.md"
    chapter_path = os.path.join(target_dir, chapter_filename)

    # Read markdown content
    with open(chapter_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Create temp HTML file
    temp_html_path = os.path.join(target_dir, "temp_frontend_test.html")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Frontend Verification</title>
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

    screenshot_path = os.path.join(cwd, "scripts/verification/frontend_verification.png")
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 800, "height": 1200})

        # Load file
        file_url = f"file://{os.path.abspath(temp_html_path)}"
        print(f"Loading {file_url}")
        page.goto(file_url)

        try:
            # Wait for key elements
            print("Waiting for UI elements...")
            page.wait_for_selector("#chapter-navigation", state="visible", timeout=5000)
            page.wait_for_selector("#progress-container", state="attached", timeout=5000)

            # Scroll to trigger progress bar update
            page.evaluate("window.scrollTo(0, document.body.scrollHeight / 3)")
            time.sleep(0.5) # Allow animation

            # Take full page screenshot
            print(f"Taking screenshot to {screenshot_path}")
            page.screenshot(path=screenshot_path, full_page=True)

        except Exception as e:
            print(f"Verification failed: {e}")
        finally:
            browser.close()
            if os.path.exists(temp_html_path):
                os.remove(temp_html_path)

if __name__ == "__main__":
    verify_frontend_changes()
