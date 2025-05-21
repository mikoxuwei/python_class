import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 載入 Chrome Driver
chrome_driver_path = r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe"
# 設定 ChromeDriver 服務
service = Service(chrome_driver_path)
# 設定 Chrome 瀏覽器選項
options = Options()
options.add_argument('--headless')  # 無頭模式
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=service, options=options)
# 設定要爬取的網址
driver.get('https://www.olympedia.org/statistics/medal/country')
time.sleep(2)  # 等待網頁加載完成

# 找到年份和性別下拉選單
year_select = driver.find_element(By.ID,'edition_select')
gender_select = driver.find_element(By.ID,'athlete_gender')

# 取得所有選項
year_options = year_select.find_elements(By.TAG_NAME, 'option')
gender_options = gender_select.find_elements(By.TAG_NAME, 'option')

usa_lst = []

# 依序選取性別和年份
for gender in gender_options[1:]: # 跳過第一個選項
    gender.click()
    gender_val = gender.get_attribute('text')

    for year in year_options[2:]: # 從 1900s 開始，跳過前兩個選項
        year.click()
        year_val = year.get_attribute('text')

        # 等待網頁加載完成
        time.sleep(1)
        the_soup = BeautifulSoup(driver.page_source, 'html.parser')

        try:
            # 找到USA的資料列(超連結)
            head = the_soup.find(href=re.compile('USA'))
            medal_values = head.find_all_next('td', limit=5)
            val_lst = [td.get_text(strip=True) for td in medal_values[1:]]
            # 跳過旗幟欄位
        except Exception as e:
            val_lst = ['0' for _ in range(4)] # 沒資料時預設為0

        val_lst.append(year_val)
        val_lst.append(gender_val)
        usa_lst.append(val_lst)

# 關閉瀏覽器
driver.quit()

# 儲存資料到 CSV 檔案
with open('output.csv', 'w', newline='', encoding='utf-8') as output_f:
    output_writer = csv.writer(output_f)
    # 寫入標題
    output_writer.writerow(['金牌', '銀牌', '銅牌', '年份', '性別'])
    # 寫入資料
    for row in usa_lst:
        output_writer.writerow(row)

# 印出結果
print("爬蟲完成，結果已儲存為 output.csv")
