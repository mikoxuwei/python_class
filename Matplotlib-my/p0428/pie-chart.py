# import matplotlib.pyplot as plt
# plt.rc('font', family='Microsoft JhengHei')
# # 繪製一組資料點的圓餅圖，加上百分比標示
# x = [10, 15, 25]
# total = sum(x) # 計算總和
# # labels = [str(100*data/total)+ '%' for data in x]
# # 計算百分比
# plt.pie([10, 15, 25], 
#         # labels=labels,
#         labels=[str(100*x[0]/total)+'%', str(100*x[1]/total)+'%', 
#                 str(100*x[2]/total)+'%',], 
#         labeldistance=0.5) # 標籤距圓心的距離
# plt.legend()
# plt.show()

# 從csv格式的檔案讀取資料，並繪製圓餅圖
import csv
import matplotlib.pyplot as plt
plt.rc('font', family='Microsoft JhengHei')
file = open('Matplotlib-my/p0428/pie-chart-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader) # 讀取標題行 跳過第一行
x = []
labels = []
for row in reader:
    x.append(int(row[1])) # 讀取數值
    labels.append(row[0]) # 讀取標籤

plt.pie(x, 
        labels=labels, 
        labeldistance=0.5) # 標籤距圓心的距離
plt.legend()
plt.title('瀏覽器的市場佔有率分佈圖')
plt.show()
print(x) # 印出每一行資料
print(labels) # 印出每一行資料
file.close()








