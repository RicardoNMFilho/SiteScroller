import os # Biblioteca para interagir com o sistema operacional
import asyncio # Biblioteca para trabalhar com eventos de tempo e tarefas assíncronas
from playwright.async_api import async_playwright # Biblioteca para automatizar navegadores web

OUTPUT_DIR = 'frames'
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Cria o diretório "output" se não existir

async def scroll_and_capture(url: str):
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 720})
        page = await context.new_page()

        await page.goto(url)
        await asyncio.sleep(1)

        scroll_height = await page.evaluate("() => document.body.scrollHeight")
        current_scroll = 0
        frame = 0

        while current_scroll < scroll_height:
            screenshot_path = os.path.join(OUTPUT_DIR, f"frame_{frame:04d}.png")
            await page.screenshot(path=screenshot_path)

            current_scroll += 50
            await page.evaluate(f"window.scrollTo(0, {current_scroll})")
            await asyncio.sleep(0.05)

            frame += 1

        await browser.close()
        print(f"✅ Capturadas {frame} imagens em '{OUTPUT_DIR}'")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python main.py <URL>")
        exit(1)

    url = sys.argv[1]
    asyncio.run(scroll_and_capture(url))
