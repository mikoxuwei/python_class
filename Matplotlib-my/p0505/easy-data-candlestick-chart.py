# 從csv格式檔案載入資料，並繪製 K 線圖
import matplotlib.pyplot as plt
import csv
plt.rc('font', family='microsoft yahei')
file = open(r'Matplotlib-my\p0505\easy-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader) # 讀取標題
print(header)
for row in reader:
    date = row[0]
    open_price = int(row[1])
    close_price = int(row[2])
    highest = int(row[3])
    lowest = int(row[4])
    # 決定陰線、陽線
    color = 'green' if close_price >= open_price else 'red'
    # 畫出影線
    # plt.bar(date, highest-lowest, bottom=lowest, color=color, width=0.5)
    plt.plot([date, date], [lowest, highest], color=color, linewidth=1)
    # 畫出實體
    plt.bar(date, abs(open_price - close_price), 
            bottom = min(open_price, close_price), 
            color=color, width=0.5)
plt.xlabel('日期') # 設定X軸標籤
plt.ylabel('價格') # 設定Y軸標籤
plt.title('個股的股價走勢') # 設定標題
plt.show() # 顯示圖形
file.close()