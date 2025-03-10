# 載入內建的sys模組並取得資訊
# import sys
# # import sys as s
# # # Print Python version
# # print("Python version:", sys.version)

# # Print platform information
# print("Platform:", sys.platform)

# # Print maxsize information
# print(sys.maxsize)

# # Print path information
# print("Path:", sys.path)

# 建立 geometry 模組載入使用
# import python_basic.modules.geometry as geometry
# result = geometry.distance(1, 1, 5, 5)
# print(result)

# result1 = geometry.slope(1, 2, 5, 6)
# print(result1)

# 調整搜尋模組的路徑
import sys
# sys.path.append("modules")
print(sys.path) # 印出模組的搜尋路徑
print('-------------------')
import modules.geometry as geometry
result = geometry.distance(1, 1, 5, 5)
print(result)