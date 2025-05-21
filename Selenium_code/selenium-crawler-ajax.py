from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time

# 設定 Chrome Driver 的執行檔路徑
CHROME_DRIVER_PATH = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"

# 檢查 Chrome Driver 是否存在
if not os.path.isfile(CHROME_DRIVER_PATH):
    raise FileNotFoundError("X 找不到指定的 Chromedriver 路徑")# f"Chrome Driver not found at {CHROME_DRIVER_PATH}"

# 建立 Chrome 瀏覽器設定
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 無頭模式，不顯示瀏覽器視窗
options.add_argument("--disable-gpu") # 禁用 GPU 加速
options.add_argument("--window-size=1920,1080") # 設定瀏覽器視窗大小
options.add_argument("--log-level=3")  # 降低日誌輸出等級，僅顯示錯誤訊息
# 設定瀏覽器使用者代理，模擬正常用戶
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 建立 Chome 驅動程式實例
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

try:
    print("開啟 Medium 首頁...")
    driver.get("https://medium.com/") # 載入 Medium 首頁

    print("等待頁面內容載入中...")
    # 等待頁面至少有一個<article>標籤出現(文章容器)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "article"))
    )

    time.sleep(2)  # 再多等幾秒，確保 JavaScript AJAX 載入完成

    # 抓取所有文章內的標題元素(通常為<h2>標籤)
    headers = driver.find_elements(By.CSS_SELECTOR, "article h2")

    print("抓取到的文章標題:")
    found = False # 用來檢查是否有找到標題
    for h in headers:
        title = h.text.strip()  # 取得標題文字
        if title:  # 確保標題不為空
            print("．", title)
            found = True
    # 如果沒有找到標題，則提示可能是 JS 渲染或被封鎖
    if not found:
        print("X 沒有找到任何文章標題，可能是 JavaScript 渲染或網站封鎖了機器人")
        # 將頁面 HTML 儲存到檔案中以供後續分析
        html_dump = driver.page_source
        with open("medium_page_dump.html", "w", encoding="utf-8") as f:
            f.write(html_dump)
        print("√ 已將頁面 HTML 儲存到 'medium_page_dump.html'。")
except Exception as e:
    print("X 發生例外錯誤:\n", str(e))
finally:
    # 等待使用者關閉瀏覽器
    input("按 Enter 鍵關閉瀏覽器...")
    driver.quit()  # 關閉瀏覽器