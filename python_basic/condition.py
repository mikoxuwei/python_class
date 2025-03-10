# # 判斷式
# x = input("請輸入數字: ")
# x1 = int(x) # 將字串型態轉換成整數
# if x1 > 200:
#     print(x + " > 200")
# elif x1 > 100:
#     print(x + " > 100")
# else:
#     print(x + " <= 100")

n1 = int(input("請輸入數字: "))
n2 = int(input("請輸入數字: "))
op = input("請輸入運算元(+, -, *, /): ")
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)    
else:
    print("不支援運算")