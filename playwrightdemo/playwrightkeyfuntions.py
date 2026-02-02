from playwright.async_api import async_playwright
import asyncio

async def playwright_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Launch browser with UI
        page = await browser.new_page()

        # Navigate to website
        await page.goto("https://google.com")

        # Print page title
        print(await page.title())

        # Wait for 5 seconds
        await page.wait_for_timeout(5000)

        # Close browser
        await browser.close()

if __name__ == "__main__":
    asyncio.run(playwright_function())

# New code 

from playwright.async_api import async_playwright
import asyncio

async def playwright_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Go to DuckDuckGo
        await page.goto("https://duckduckgo.com")

        # Wait for search box and type query
        await page.wait_for_selector("input[name='q']")
        await page.fill("input[name='q']", "South Africa vs Australia score")
        await page.keyboard.press("Enter")

        # Wait for results and click first link
        await page.wait_for_selector("a.result__a")
        first_result = await page.query_selector("a.result__a")
        if first_result:
            await first_result.click()
            print("✅ Clicked first result")

        await page.wait_for_timeout(5000)
        await browser.close()

if __name__ == "__main__":
    asyncio.run(playwright_function())