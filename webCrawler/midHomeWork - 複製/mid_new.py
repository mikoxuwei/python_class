# cascade/access open data 
import urllib.request as request
import json
import ssl

# 建立一個不驗證 SSL 憑證的上下文
ssl._create_default_https_context = ssl._create_unverified_context

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
        website_name = record.get('WEBSITE_NM', '未知')  # 提取網站名稱
        web_url = record.get('WEBURL', '未知')  # 提取網站網址
        case_count = record.get('CNT', '未知')  # 提取發生件數

        # 將資料寫入檔案
        f.write(f"網站名稱：{website_name}, 網址：{web_url}, 案件次數：{case_count}\n")

        # 嘗試將案件次數轉換為整數
        try:
            cc = int(case_count)  # 將案件次數轉換為整數
            if cc > 10: # 如果案件次數大於 10，則 print 出來
                print(f"網站名稱：{website_name}, 網址：{web_url}, 案件次數：{case_count}\n")
        except ValueError:
            # print(f"無效的案件次數：{case_count}，無法轉換為整數")
            cc = 0

print('done')