import matplotlib.pyplot as plt

# 設定自型為window 內建的正黑體， 支援中文顯示
plt.rc('font', family='Microsoft JhengHei')
# 繪製一組資料點的散佈圖，設定樣式
'''
一組資料點
(2, 4),(4, 3), (3, 6)
'''
# plt.scatter([2, 4, 3], [4, 3, 6], color='red', s = 200) #888888
# plt.show()

# 繪製一組資料點的散佈圖，設定樣式
'''
兩組資料點
(2, 4),(4, 3), (3, 6)
(1, 2),(3, 5), (4, 7)
'''
# plt.scatter([2, 4, 3], [4, 3, 6], color='red', s = 200) #888888
# plt.scatter([1, 3, 4], [2, 5, 7], color='blue', s = 200) 
# plt.legend(['紅色', '藍色'], loc='upper left') # 設定圖例
# plt.show()

# # 從 csv 格式的檔案讀取資料，並繪製散佈圖
# import csv
# file = open('Matplotlib-my\p0428\scatter-chart-data.csv', encoding='utf-8')
# reader = csv.reader(file)
# header = next(reader) # 讀取標題行
# for row in reader:
#     print(row) # 印出每一行資料
# file.close()


import csv
file = open('Matplotlib-my\p0428\scatter-chart-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader) # 讀取標題行
data = {
    '男':{'x':[], 'y':[]},
    '女':{'x':[], 'y':[]}
}
for row in reader:
    gender = row[0] # 讀取性別
    data[gender]['x'].append(float(row[1])) # 讀取 x 軸資料
    data[gender]['y'].append(float(row[2])) # 讀取 y 軸資料
    
print(data) # 印出每一行資料
file.close()

import csv
file = open('Matplotlib-my\p0428\scatter-chart-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader) # 讀取標題行
data = {
    '男':{'x':[], 'y':[]},
    '女':{'x':[], 'y':[]}
}
for row in reader:
    gender = row[0] # 讀取性別
    data[gender]['x'].append(float(row[1])) # 讀取 x 軸資料
    data[gender]['y'].append(float(row[2])) # 讀取 y 軸資料
plt.scatter(data['男']['x'], data['男']['y'], color='blue', s = 200)
plt.scatter(data['女']['x'], data['女']['y'], color='red', s = 200)
plt.legend(['男', '女'], loc='upper left') # 設定圖例
plt.show()
file.close()