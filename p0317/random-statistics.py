# random module
import random
# random choice
data = random.choice([1, 5, 6, 10, 20])
print(data)

# random shuffle
# randomly change the number position of the list
x = [1, 2, 3, 4, 5]
random.shuffle(x)
print(x)

# random sample
data = random.sample([1, 5, 6, 10, 20], 3)
print(data)

data = random.random() # random float: 0.0 <= x < 1.0
data = random.uniform(60, 100) # random float: 60 <= x < 100
print(data)

data = random.randint(1, 10) # random integer: 1 <= x <= 10
print(data)

# 平均值是100，標準差是10的常態分佈
data = random.normalvariate(100, 10) # random float: mean=0, standard deviation=1
print(data)

import statistics as stat
data = [1, 2, 3, 4, 5]
print(stat.mean(data)) # 平均值
print(stat.median(data)) # 中位數
print(stat.stdev(data)) # 標準差
print(stat.variance(data)) # 變異數