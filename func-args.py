# function data setup
def power(base, exp):
    print(base**exp)
power(3, 2) # function execution


def avg(*ns):
    sum=0 # 要算平均數，先算出總和
    for n in ns:
        sum+=n # 在這一個迴圈中把資料一個一個加進去
    print(sum/len(ns)) #然後再把總合除以列表長度  # 因為 ns 是一個列表，所以我們用操作列表的 len 來算出 ns 這個列表有幾個資料
avg(3, 4)  # 算出 3 跟 4 的平均數。
avg(4, 5, 100) 