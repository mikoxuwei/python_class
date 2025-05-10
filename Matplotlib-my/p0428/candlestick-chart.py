import matplotlib.pyplot as plt
plt.rc('font', family='Microsoft JhengHei')
'''
範例資料:
日期, 開盤價, 最高價, 最低價, 收盤價
11/01, 95, 80, 100, 75
11/02, 82, 75, 83, 65
11/03, 73, 85, 90, 70
'''
# 根據範例資料，繪製 K 線圖
plt.bar('11/01', 15, bottom=80, color='green', width=0.5)  # 11/01
plt.bar('11/01', 25, bottom=75, color='green', width=0.1)  # 11/01
plt.bar('11/02', 7, bottom=75, color='green', width=0.5)  # 11/02
plt.bar('11/02', 18, bottom=65, color='green', width=0.1)  # 11/02
plt.bar('11/03', 12, bottom=73, color='red', width=0.5)  # 11/03
plt.bar('11/03', 20, bottom=70, color='red', width=0.1)  # 11/03
plt.show()

# import matplotlib.dates as mdates
# from matplotlib.patches import Rectangle
# import datetime
# # 範例數據 (日期, 開盤價, 最高價, 最低價, 收盤價)
# data = [
#     ("2023-04-20", 100, 110, 95, 105),
#     ("2023-04-21", 105, 115, 100, 110),
#     ("2023-04-22", 110, 120, 105, 115),
#     ("2023-04-23", 115, 125, 110, 120),
#     ("2023-04-24", 120, 130, 115, 125),
# ]

# # 將日期轉換為 datetime 格式
# dates = [datetime.datetime.strptime(d[0], "%Y-%m-%d") for d in data]
# opens = [d[1] for d in data]
# highs = [d[2] for d in data]
# lows = [d[3] for d in data]
# closes = [d[4] for d in data]

# # 繪製 K 線圖
# fig, ax = plt.subplots()

# for i in range(len(data)):
#     color = 'green' if closes[i] >= opens[i] else 'red'
#     # 畫出影線
#     ax.plot([dates[i], dates[i]], [lows[i], highs[i]], color=color, linewidth=1)
#     # 畫出實體
#     rect = Rectangle(
#         (mdates.date2num(dates[i]) - 0.2, min(opens[i], closes[i])),
#         0.4,
#         abs(opens[i] - closes[i]),
#         color=color
#     )
#     ax.add_patch(rect)

# # 設定日期格式
# ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
# ax.xaxis.set_major_locator(mdates.DayLocator())
# plt.xticks(rotation=45)
# plt.title("K-line Chart")
# plt.xlabel("Date")
# plt.ylabel("Price")
# plt.grid()

# plt.show()