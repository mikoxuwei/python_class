from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
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
    print("🔍  開啟 templatemonster 商品頁面...")
    driver.get("https://www.templatemonster.com/wordpress-themes/clean-amp-clear-free-home-cleaning-wordpress-theme-385925.html") # 載入 Medium 首頁

    # print("⌛ 等待頁面內容載入中...")
    # # 等待頁面至少有一個<article>標籤出現(文章容器)
    # WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((By.TAG_NAME, "article"))
    # )

    time.sleep(3)  # 再多等幾秒，確保 JavaScript AJAX 載入完成

    print("📰  抓取到的文章標題:")

    # 抓取所有文章內的標題元素(h1-h3)
    for tag in ["h1", "h2", "h3"]:
        headers = driver.find_elements(By.TAG_NAME, tag)
        for h in headers:
            text = h.text.strip()
            if text:
                print(f"{tag.upper()} → {text}")

except Exception as e:
    print("❌  發生例外錯誤:\n", str(e))
finally:
    # 等待使用者關閉瀏覽器
    input("👁️   按 Enter 鍵關閉瀏覽器...")
    driver.quit()  # 關閉瀏覽器