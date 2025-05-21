# 載入 Selenium 套件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 載入 Chrome Driver
chrome_driver_path = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"


# 建立 Chrome 的設定選項
options = Options()
options.add_argument("--headless")  # 啟用無頭模式(不顯示瀏覽器)
service = Service(executable_path = chrome_driver_path)

# 啟動 Chrome 瀏覽器 webdriver
driver = webdriver.Chrome(service=service, options=options)

# 開啟 webflow 的 Geospace Template 頁面
url = "https://webflow.com/made-in-webflow/website/Geospace-Template"
driver.get(url)

# 等待網頁載入
time.sleep(5)  # 等待 5 秒，確保網頁完全載入

#定義要擷取的文字的 HTML 標籤類型
tags = ['h1', 'h2', 'h3', 'p', 'button']  # 可以根據需要添加更多標籤
text_labels = [] # 儲存擷取的文字

# 逐一擷取各種標籤的文字
for tag in tags:
    elements = driver.find_elements(By.TAG_NAME, tag)  # 根據標籤名稱擷取元素
    for element in elements:
        text = element.text.strip()  # 擷取文字並去除前後空白
        if text:  # 確保文字不為空
            text_labels.append(text)  # 將文字加入列表

# 印出擷取的文字
for label in text_labels:
    print(label)

# 關閉瀏覽器
driver.quit()