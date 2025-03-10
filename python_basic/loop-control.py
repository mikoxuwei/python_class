'''#break 
n = 0
while n < 5:
    if n == 3:
        break
    print(n) # output n in loop
    n += 1
print('the last n: ', n) # output n out of loop


# continue
n = 0
for x in [0, 1, 2, 3]:
    if x % 2 == 0:
        continue
    print(x)
    n += 1
print('there are', n, 'odd number')

# else
sum = 0
for n in range(11):
    sum += n
else:
    print(sum) # output the result of 1 + 2 + 3 + 4... + 10

    #synthesis find the square root of an integral

'''
n = input('please input an integral:')
n = int(n) #transform string into integral
for i in range(n): #i is from 0 to n-1
    if i*i==n:
        print('the square root is ', i)
        break #stop loop
else:
    print('no square root exist')