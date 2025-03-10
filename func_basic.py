'''
#function definition
def multiply():
    print(3 * 4)
# call function
multiply()

#function definition
def multiply(n1, n2):
    print(n1 * n2)
# call function
multiply(3, 4)
multiply(8, 9)

#function definition
def multiply(n1, n2):
    print(n1 * n2)
# call function
value = multiply(3, 4) # return value = none
print(value) # print return value

#function definition
def multiply(n1, n2):
    return(n1 * n2)
# call function
value = multiply(3, 4) + multiply(8, 9) # return value = none
print(value) # print return value
'''
def calculate(x, y):
    sum = 0
    for n in range(x, y+1):
        sum = sum + n
    print(sum)
#主程式
x = int(input('輸入數字: '))
y = int(input('輸入數字: '))
if x<y:
    calculate(x, y)
else:
    print("輸入錯誤")