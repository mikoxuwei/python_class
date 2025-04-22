# cascade/access open data
import urllib.request as request
import json
scr = 'https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire'
with request.urlopen(scr) as response:
    # 讀取並解碼 HTTP 回應內容
    data = json.loads(response.read().decode('utf-8'))  # 將回應內容解析為 JSON
# 印出 JSON 資料
# print(data)

# list company names
clist = data['result']['results']
# for company in clist:
#     name = company['公司名稱']
#     # address = company['地址']
#     # phone = company['電話']
#     print(name)  # , address, phone)
with open('./company.txt', 'w', encoding='utf-8') as f:
    for company in clist:
        name = company['公司名稱']
        # address = company['地址']
        # phone = company['電話']
        f.write(name + '\n')  # , address, phone)
print('done')