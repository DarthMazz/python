import asyncio
from pyppeteer import launch
import time
import random
import urllib
import os


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

    time.sleep(5+random.randrange(10))
    await page.type('#xX4UFf', '請求書')

    # スクリーンショット取得
    print("スクリーンショット1を保存")
    await page.screenshot({"path": "./sceeenshot1.png"})

    time.sleep(5+random.randrange(10))
    await asyncio.wait([
        page.click('input[value="詳細検索"]'),
        page.waitForNavigation(),
    ])

    print("スクリーンショット2を保存")
    await page.screenshot({"path": "./sceeenshot2.png"})

    time.sleep(5+random.randrange(10))
    a_images = await page.JJ('a[class="wXeWr islib nfEiy"]')
    await asyncio.wait([
        a_images[0].click(),
        page.waitForNavigation(),
    ])

    print("スクリーンショット3を保存")
    await page.screenshot({"path": "./sceeenshot3.png"})
    time.sleep(5+random.randrange(10))
    image = await page.JJ('img[class="n3VNCb"]')
    src = await image[0].getProperty('src')
    targetUrl = await src.jsonValue()
    download_file_name = os.path.basename(urllib.parse.urlparse(targetUrl).path)
    viewSource = await page.goto(targetUrl)
    time.sleep(5+random.randrange(10))
    image_buffer = await viewSource.buffer()
    with open(f'./{download_file_name}', 'wb') as f:
        f.write(image_buffer)

    # ブラウザ停止
    await browser.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())