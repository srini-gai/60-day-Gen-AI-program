import asyncio
from playwright.async_api import async_playwright

async def playwright_function():
    async with async_playwright() as p:
        # Path to Microsoft Edge executable (adjust if different on your system)
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

        # Launch Edge
        browser = await p.chromium.launch(
            headless=False,
            executable_path=edge_path
        )
        page = await browser.new_page()

        # Navigate to TradingView chart page
        await page.goto("https://www.tradingview.com/chart/")

        # Collect metadata
        metadata = {}

        # Page title
        metadata["title"] = await page.title()

        # Meta description
        try:
            description = await page.locator("meta[name='description']").get_attribute("content")
            metadata["description"] = description
        except:
            metadata["description"] = None

        # Meta keywords
        try:
            keywords = await page.locator("meta[name='keywords']").get_attribute("content")
            metadata["keywords"] = keywords
        except:
            metadata["keywords"] = None

        # OpenGraph tags
        og_tags = await page.locator("meta[property^='og:']").all()
        for tag in og_tags:
            prop = await tag.get_attribute("property")
            content = await tag.get_attribute("content")
            metadata[prop] = content

        # Twitter card tags
        twitter_tags = await page.locator("meta[name^='twitter:']").all()
        for tag in twitter_tags:
            name = await tag.get_attribute("name")
            content = await tag.get_attribute("content")
            metadata[name] = content

        # Export metadata to text file
        with open("tradingview_metadata.txt", "w", encoding="utf-8") as f:
            for key, value in metadata.items():
                f.write(f"{key}: {value}\n")

        print("✅ Metadata exported to tradingview_metadata.txt")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(playwright_function())