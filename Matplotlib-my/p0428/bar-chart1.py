# 從csv格式的檔案讀取資料, 並畫出長條圖
import csv
import matplotlib.pyplot as plt
plt.rc('font', family='microsoft yahei')
file = open(r'Matplotlib-my\bar-chart-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader) # 讀取標題
print('標頭', header)
x = []
height = []
for row in reader:
    # print(row) # 印出每一列資料
    x.append(row[0])
    height.append(int(row[1]))
    # print('x', x)
    # print('height', height)
    plt.bar(x, height, width = 0.6, color='green')
    plt.xlabel(header[0]) # 設定X軸標籤
    plt.ylabel(header[1]) # 設定Y軸標籤
plt.show() # 顯示圖形
file.close()