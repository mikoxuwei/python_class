# 集合的運算
S1 = {3, 4, 5}
print(7 in S1)

S1 = {3, 4, 5}
S2 = {4, 5, 6, 7}
S3 = S1 & S2 # 交集: 取2個集合中相同的資料
print(S3)

S1 = {3, 4, 5}
S2 = {4, 5, 6, 7}
S3 = S1 | S2 # 聯集: 取2個集合中所有的資料但是不重複
print(S3)

S1 = {3, 4, 5}
S2 = {4, 5, 6, 7}
S3 = S1 - S2 # 差集: 從 S1 中減去 和 S2 重複的資料
print(S3)

S1 = {3, 4, 5}
S2 = {4, 5, 6, 7}
S3 = S1 ^ S2 # 差集: 從 S1 中減去 和 S2 重複的資料
print(S3)

# 字典的運算
dic = {"apple": "蘋果", "bug":"蟲"}
print(dic)

dic = {x:x*2 for x in [3, 4, 5]}
print(dic)