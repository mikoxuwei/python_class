# cascade/access open data 
import urllib.request as request
import json

# 新的 API URL
scr = 'https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-002150-013'

# 發送請求並讀取資料
with request.urlopen(scr) as response:
    # 讀取並解碼 HTTP 回應內容
    data = json.loads(response.read().decode('utf-8'))  # 將回應內容解析為 JSON

# 提取資料
clist = data['result']['records']  # 根據 API 的結構，提取 "records" 部分

# 將資料寫入檔案
with open('./website_data.txt', 'w', encoding='utf-8') as f:
    for i, record in enumerate(clist):
        # 提取需要的欄位
        website_name = record.get('WEBSITE_NM', '未知')  # 使用 .get() 方法避免 KeyError
        web_url = record.get('WEBURL', '未知')
        
        # 將資料寫入檔案
        f.write(f"網站名稱：{website_name}, 網址：{web_url}\n")

         # 如果是第 2 行到第 11 行，則打印出來
        if 1 <= i < 11:  # 索引 1 對應第 2 行，索引 10 對應第 11 行
            print(f"網站名稱：{website_name}, 網址：{web_url}")

print('done')