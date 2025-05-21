# 載入 Selenium 套件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os, time

# 載入 Chrome Driver
chrome_driver_path = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"

# 建立 Chrome 的設定選項
options = Options()
options.add_argument("--headless")  # 啟用無頭模式(不顯示瀏覽器)
service = Service(executable_path = chrome_driver_path)

# 啟動 Chrome 瀏覽器 webdriver
driver = webdriver.Chrome(service=service, options=options)

# 開啟 webflow 的 Geospace Template 頁面
# url = "https://webflow.com/made-in-webflow/website/Geospace-Template"
# url = "https://www.awwwards.com/sites/who-is-guilty#google_vignettw"
url = "https://artelagunaprize.com/edition-2025/?gad_source=5&gclid=EAIaIQobChMI4aO5hfyfjQMViVnCBR0eKBQfEAEYASAAEgK4zPD_BwE"
driver.get(url)

# 等待網頁載入
time.sleep(5)  # 等待 5 秒，確保網頁完全載入

#定義要擷取的文字的 HTML 標籤類型
heading_tags = ['h1', 'h2', 'h3']  # 可以根據需要添加更多標籤
data = [] # 儲存結束的清單

# 逐一擷取各種標籤的文字
for tag in heading_tags:
    headings = driver.find_elements(By.TAG_NAME, tag)  # 根據標籤名稱擷取元素
    for heading in headings:
        heading_text = heading.text.strip()  # 擷取文字並去除前後空白
        if heading_text:  # 確保文字不為空
            # 嘗試取得heading所在父元素中的內文段落
            try:
                parent = heading.find_element(By.XPATH, "./..")  # 往上一層找
                paragraphs = parent.find_elements(By.TAG_NAME, "p")  # 再父層內找p
                paragraph_texts = [p.text.strip() for p in paragraphs if p.text.strip()]  # 擷取段落文字
                data.append((heading_text, paragraph_texts))  # 將段落文字加入列表
            except:
                data.append((heading_text, [])) # 沒有內文也加入
        

# 印出擷取的文字
print("擷取到的標題文字: \n")
for title, paragraphs in data:
    print(f"標題: {title}")
    if paragraphs:
        for para in paragraphs:
            print(f"    -內文:{para}")
    else:
        print("    - 內文: 無")
    print()

# 關閉瀏覽器
driver.quit()


# # 開啟 Webflow 的 Geospace Template 頁面
# url = "https://artelagunaprize.com/edition-2025/?gad_source=5&gclid=EAIaIQobChMI4aO5hfyfjQMViVnCBR0eKBQfEAEYASAAEgK4zPD_BwE"
# driver.get(url)

# # 等待幾秒鐘讓網頁內容完全載入 ( 可視網路速度調整時間 )
# time.sleep(5)

# # 定義要擷取文字的 HTML 標籤類型
# heading_tags = ['h1', 'h2', 'h3']
# data = []  # 用來儲存所有擷取到的文字標籤

# # 逐一擷取各級標題文字
# for tag in heading_tags:
#     headings = driver.find_elements(By.TAG_NAME, tag)  # 取得該標籤的所有元素
#     for heading in headings:
#         heading_text = heading.text.strip()  # 去除前後空白
#         if heading_text:   # 若文字不為空，加入清單中
#             # 嘗試取得 heading 所在富元素中的內文段落
#             try:
#                 parent = heading.find_element(By.XPATH, './..')  # 往上一層找
#                 paragraphs = parent.find_elements(By.TAG_NAME,'p')  # 再複層內找 p 標籤
#                 paragraph_texts = [p.text.strip() for p in paragraphs if p.text.strip()]
#                 data.append((heading_text, paragraph_texts))
#             except:
#                 data.append((heading_text, []))  # 沒有內文也加入
    
# # 將所有擷取到的文字列印出來
# print('📄 擷取結果如下: \n')
# for title, paragraphs in data:
#     print(f"🔹 標題:{title}")
#     if paragraphs:
#         for para in paragraphs:
#             print(f"    -內文:{para}")
#     else:
#         print("    -內文:無")
#     print()
# # 關閉瀏覽器
# driver.quit()