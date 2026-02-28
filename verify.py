from playwright.sync_api import sync_playwright

def verify_app():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        try:
            # Go to app
            page.goto("http://localhost:4173/Obsidian_Novel_v2/")
            page.wait_for_timeout(1000)

            # Click on Wiki tab
            page.get_by_text("Wiki").click()
            page.wait_for_timeout(1000)

            # Click on Lâm Phong in the sidebar
            page.get_by_role("button", name="Lâm Phong 🐉").click()
            page.wait_for_timeout(2000) # wait for fetch

            page.screenshot(path="verify_wiki.png", full_page=True)

        finally:
            browser.close()

if __name__ == "__main__":
    verify_app()
