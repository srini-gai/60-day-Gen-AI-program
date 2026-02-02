from flask import Flask, jsonify
import asyncio
from playwright.async_api import async_playwright

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask server is running successfully 🚀"


async def run_playwright():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://duckduckgo.com")
        await page.wait_for_selector("input[name='q']")
        await page.fill("input[name='q']", "South Africa vs Australia score")
        await page.keyboard.press("Enter")

        await page.wait_for_selector("a.result__a")
        first_result = await page.query_selector("a.result__a")

        if first_result:
            await first_result.click()

        await page.wait_for_timeout(5000)
        await browser.close()


@app.route("/run-playwright")
def run_script():
    asyncio.run(run_playwright())
    return jsonify({
        "status": "success",
        "message": "Playwright automation completed"
    })


if __name__ == "__main__":
    app.run(debug=True)
