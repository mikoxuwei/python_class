import matplotlib.pyplot as plt
plt.rc('font', family='microsoft yahei')
'''
一組資料點
(1, 2), (2, 4), (3, 6)
'''
# plt.plot([1, 2, 3], [2, 4, 6])
# plt.show()
'''
兩組資料點
    第一組(1, 2), (2, 4), (3, 6)
    第二組(1, 1), (2, 2), (3, 3)
'''
plt.plot([1, 2, 3], [[2, 1], [4, 2], [6, 3]], label=['第一組', '第二組']) # 設定每一組標籤
plt.legend() # 顯示圖例
plt.xlabel('X軸的說明') # 設定X軸標籤
plt.ylabel('Y軸的說明') # 設定Y軸標籤
plt.show()  