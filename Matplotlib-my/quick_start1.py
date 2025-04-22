# 從 csv 格式的檔案中讀取資料，並繪製折線圖
import csv
import matplotlib.pyplot as plt
plt.rc('font', family='microsoft yahei')
file = open('Matplotlib-my\phone.csv', 'r', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)  # 讀取標題列
print('標題', header)
x= [] # 預期[2010, 2011, 2012]
y= [] # 預期[[40000, 30000], [42000, 60000], [45000, 50000]]
for row in reader:
    print('每列資料', row)
    x.append(int(row[0]))  
    y.append([int(row[1]), int(row[2])])
    plt.plot(x, y, label=header[1:3]) # 設定每一組標籤
    plt.legend() # 顯示圖例
    plt.xlabel(header[0]) # 設定X軸標籤
    plt.ylabel('銷售') # 設定Y軸標籤
    plt.show() # 顯示圖形
file.close()