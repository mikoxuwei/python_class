# 在 geometry 模組中定義幾何運算功能

# 計算 2 點距離
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# 計算 2 點間直線斜率
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)