import asyncio
from pyppeteer import launch


async def html_parse(html):
    from bs4 import BeautifulSoup

    print("htm解析")
    soup = BeautifulSoup(html, 'html.parser')


async def main():
    # ブラウザ起動
    # 初回はChroniumのダウンロードが実施される
    print("ブラウザ起動")
    browser = await launch(headless=False, args=["--no-sandbox"])

    # 新規タブ追加
    print("新規タブ追加")
    page = await browser.newPage()

    # ウィンドウサイズ設定
    await page.setViewport({"width": 1280, "height": 1696})

    # サイトを開く
    print("ウェブサイトを開く")
    await page.goto("https://www.google.co.jp/advanced_image_search")

    await page.type('#xX4UFf', '請求書')

    # スクリーンショット取得
    print("スクリーンショット1を保存")
    await page.screenshot({"path": "./sceeenshot1.png"})

    await asyncio.wait([
        page.click('input[value="詳細検索"]'),
        page.waitForNavigation(),
    ])

    print("スクリーンショット2を保存")
    await page.screenshot({"path": "./sceeenshot2.png"})

    # ブラウザ停止
    await browser.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())