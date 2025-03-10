# 儲存檔案
# file = open('data.txt', 'w', 'utf-8') # 建立/開啟檔案

# file.write('Hello, Python\n Fine Thank you') # 寫入資料
# file.close() # 關閉檔案
path = "./python_basic/p0310/backup_dic/"
# 儲存檔案到 geometry 資料夾
# with open('.\geometry\data.txt', 'w', encoding='utf-8') as file: # 建立/開啟檔案
#     file.write('台南大學\n明天放假') # 寫入資料
with open(path + "data.txt", 'w', encoding='utf-8') as file: # 建立/開啟檔案
    file.write('5\n3\n2\n7') # 寫入資料
# 關閉檔案 (with statement will automatically close the file)

# 讀取檔案從 geometry 資料夾
with open(path + "data.txt", 'r', encoding='utf-8') as file: # 開啟檔案
    data = file.read() # 讀取檔案
print(data) # 輸出讀取的資料

# 讀取檔案
# 把檔案中的數字資料取出來計算總和
sum = 0
with open(path + "data.txt", 'r', encoding='utf-8') as file: # 開啟檔案
    for line in file: # 逐行讀取檔案
        sum += int(line) # 累加數字
print('sum is', sum) # 輸出總和
# 關閉檔案 (with statement will automatically close the file)

# 使用 JSON 格式讀取、複寫檔案
import json
with open(path + "config.json", 'r', encoding='utf-8') as file1: # 開啟檔案
    data = json.load(file1) # 讀取 JSON 資料
print("name :", data["name"]) # 輸出讀取的資料
print("version :", data["version"]) # 輸出讀取的資料
data["name"] = "Smith" # 修改讀取的資料
with open(path + "config.json", 'w', encoding='utf-8') as file2: # 開啟檔案
    json.dump(data, file2) # 寫入 JSON 資料