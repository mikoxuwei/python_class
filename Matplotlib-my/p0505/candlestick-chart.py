# # 從csv格式檔案載入資料，並繪製 K 線圖
# import matplotlib.pyplot as plt
# import csv
# plt.rc('font', family='microsoft yahei')
# file = open(r'Matplotlib-my\p0505\candlestick-chart-data.csv', encoding='utf-8')
# reader = csv.reader(file)
# header = next(reader) # 讀取標題
# print(header)
# for row in reader:
#     date, time, ap = row[0].split(' ')
#     hour, minute, second = time.split(':')
#     open_price = float(row[2])
#     close_price = float(row[5])
#     highest = float(row[3])
#     lowest = float(row[4])
#     # 決定陰線、陽線
#     color = 'green' if close_price >= open_price else 'red'
#     # 畫出影線
#     plt.plot([time, time], [lowest, highest], color=color, linewidth=1)
#     # 畫出實體
#     plt.bar(time, abs(open_price - close_price), 
#             bottom = min(open_price, close_price), 
#             color=color, width=0.5)
# plt.xlabel('時間') # 設定X軸標籤
# plt.ylabel('價格') # 設定Y軸標籤
# plt.title('6/10/2023 的股價走勢') # 設定標題
# plt.show() # 顯示圖形
# file.close()
# 從csv格式檔案載入資料，並繪製 K 線圖


# 從csv格式檔案載入資料，並繪製 K 線圖
import matplotlib.pyplot as plt
import csv
import matplotlib.dates as mdates
from datetime import datetime
from dateutil.parser import parse

plt.rc('font', family='microsoft yahei')

# 打開 CSV 檔案
file = open(r'Matplotlib-my\p0505\candlestick-chart-data.csv', encoding='utf-8')
reader = csv.reader(file)
header = next(reader)  # 讀取標題
print(header)

# 儲存時間和價格資料
times = []
open_prices = []
close_prices = []
highs = []
lows = []

# 讀取資料
for row in reader:
    date, time, ap = row[0].split(' ')
    full_time = parse(f"{date} {time}")  # 自動解析日期和時間
    times.append(full_time)
    open_prices.append(float(row[2]))
    close_prices.append(float(row[5]))
    highs.append(float(row[3]))
    lows.append(float(row[4]))

# 繪製 K 線圖
for i in range(len(times)):
    color = 'green' if close_prices[i] >= open_prices[i] else 'red'
    # 畫出影線
    plt.plot([times[i], times[i]], [lows[i], highs[i]], color=color, linewidth=1)
    # 畫出實體
    plt.bar(times[i], abs(open_prices[i] - close_prices[i]),
            bottom=min(open_prices[i], close_prices[i]),
            color=color, width=0.0005)  # 調整寬度以適應時間軸

# 設定 X 軸格式
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # 顯示小時和分鐘
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))  # 每 5 分鐘顯示一個刻度

# 設定標籤和標題
plt.xlabel('時間')  # 設定 X 軸標籤
plt.ylabel('價格')  # 設定 Y 軸標籤
plt.title('6/10/2023 的股價走勢')  # 設定標題

# 自動調整 X 軸標籤的顯示
plt.gcf().autofmt_xdate()

# 顯示圖形
plt.show()

# 關閉檔案
file.close()