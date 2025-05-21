import asyncio
from playwright.sync_api import sync_playwright

# 設定 Chrome Driver 的執行檔路徑
CHROME_DRIVER_PATH = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"

# 檢查 Chrome Driver 是否存在
if not os.path.isfile(CHROME_DRIVER_PATH):
    raise FileNotFoundError("X 找不到指定的 Chromedriver 路徑")# f"Chrome Driver not found at {CHROME_DRIVER_PATH}"

# 用 Playwright 啟動瀏覽器並抓取Medium首頁
def crawl_medium_titles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True 代表無頭模式
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},  # 設定瀏覽器視窗大小
            ignore_default_args=["--enable-automation"],  # 忽略自動化標記
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"  # 模擬正常用戶的 User-Agent
        )
        page = context.new_page()

        try:
            print("開啟 Medium 首頁...")
            page.goto("https://medium.com/", timeout=30000)  # 設定載入超時時間為30秒

            print("等待頁面內容載入中...")
            page.wait_for_selector("article h2", timeout = 15000)  # 等待至少一個<article>標籤出現

            headers = page.query_selector_all("article h2")
            print("抓取到的文章標題:")
            found = False
            for h in headers:
                title = h.inner_text().strip()
                if title:
                    print("．", title)
                    found = True
            if not found:
                print("X 沒有找到任何文章標題，可能是 JavaScript 渲染或網站封鎖了機器人")
                html_dump = page.content()
                with open("medium_page_dump.html", "w", encoding="utf-8") as f:
                    f.write(html_dump)
                print("√ 已將頁面 HTML 儲存到 'medium_page_dump.html'。")
        except Exception as e:
            print("X 發生例外錯誤:\n", str(e))  
        finally:
            # 等待使用者關閉瀏覽器
            input("按 Enter 鍵關閉瀏覽器...")
            context.close()

if __name__ == "__main__":
    crawl_medium_titles()
    # asyncio/.run(crawl_medium_titles())  # 如果使用 async/await，則需要這行