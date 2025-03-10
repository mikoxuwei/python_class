# 有序可變動列表 List

# 1
grades = [12, 60, 15, 70, 90]
grades[0] = 55 # 放到列表中的第一個位置
print(grades[1:4])

# 2
grades = [12, 60, 15, 70, 90]
grades[1:4] = [] # 連續刪除2-4的資料
grades = grades + [12, 33] 
print(grades)

# 3
length = len(grades)
print(length)
print(grades)

# 有序不可變動 Tuple
data = (3, 4, 5)
## data [0] = 5 # 不可變動所以會出錯誤訊息
print(data[0:2])