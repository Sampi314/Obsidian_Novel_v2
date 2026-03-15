import pytest
from playwright.sync_api import Page, expect
import urllib.parse
import time

def test_chapter_navigation(page: Page):
    page.on("console", lambda msg: print(f"Browser console: {msg.text}"))

    file_path = "Đạo/Chương_Truyện/Nam_Cương/Góc_Nhìn_Lâm_Phong/Chương_00089_Huyết_Trận_Chặn_Đường.md"
    encoded_path = urllib.parse.quote(file_path)
    url = f"http://localhost:8000/reader.html?file={encoded_path}"

    page.goto(url)

    # Check title
    page.wait_for_selector("#content h1")
    title = page.locator("#content h1").inner_text()
    assert "Chương 89" in title

    # Wait for the navigation bar to be generated
    page.wait_for_selector("#chapter-navigation .nav-bar")

    # Check next chapter button
    next_button = page.locator("#next-chapter-link")
    expect(next_button).to_be_visible()

    # Navigate to next chapter
    next_button.click()
    page.wait_for_selector("#content h1")

    # Wait for the navigation bar to be generated on the new page
    page.wait_for_selector("#chapter-navigation .nav-bar")

    # Check title of next chapter
    title = page.locator("#content h1").inner_text()
    print(f"Title found on next page: {title}")
    assert "Chương 90" in title
