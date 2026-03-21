import os
import time
from playwright.sync_api import sync_playwright, expect

def test_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Get the absolute path to relationship.html
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        file_url = f"file://{base_path}/relationship.html"

        # Navigate to the local file
        page.goto(file_url)

        # Wait for the page to load completely and graph to render
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000) # Give D3 some time to settle

        # Search for one of our new characters
        page.fill("#search-box", "Trương Hàn Kiếm")

        # Wait for search results to filter
        page.wait_for_timeout(1000)

        # Create verification directory if it doesn't exist
        os.makedirs("/home/jules/verification", exist_ok=True)

        # Take a screenshot
        page.screenshot(path="/home/jules/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    test_frontend()
