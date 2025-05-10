# 載入 Selenium 套件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"
# 建立 Driver 物件實體, 用程式操作 Chrome 瀏覽器
driver = webdriver.Chrome(options=options)
# 連線到PTT股票版
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# 取得網頁的 HTML 原始碼
# html = driver.page_source
# print(html)

### 上課程式
# tags = driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 為 title 的所有標籤
# # print(tags) # 印出所有標籤
# for tag in tags:
#     # 取得每個標籤的文字內容
#     title = tag.text
#     print(title) #, link 印出標題和連結網址
# links = driver.find_elements(By.LINK_TEXT, "‹ 上頁") # 搜尋連結文字為 ‹ 上頁 的所有標籤
# if links:
#     links[0].click() # 點擊第一個連結

# # 再取一頁
# tags = driver.find_elements(By.CLASS_NAME, "title") # 搜尋 class 為 title 的所有標籤
# for tag in tags:
#     # 取得每個標籤的文字內容
#     title = tag.text
#     print(title) #, link 印出標題和連結網址
# driver.close()

### 自己練習
# 定義要抓取的頁數
num_pages = 2  # 抓取 2 頁的資料

for _ in range(num_pages):
    # 抓取當前頁面的標題
    tags = driver.find_elements(By.CLASS_NAME, "title")  # 搜尋 class 為 title 的所有標籤
    for tag in tags:
        title = tag.text.strip()  # 取得每個標籤的文字內容
        if title:  # 避免空白標題
            print(title)

    # 點擊「‹ 上頁」按鈕，進入上一頁
    links = driver.find_elements(By.LINK_TEXT, "‹ 上頁")  # 搜尋連結文字為 ‹ 上頁 的所有標籤
    if links:
        links[0].click()  # 點擊第一個連結
    else:
        print("找不到 ‹ 上頁 按鈕，結束爬取")
        break  # 如果找不到「‹ 上頁」，結束迴圈

driver.close()