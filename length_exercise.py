# *se1_7, se8 = (4, 5, 8, 7, 9, 6, 7, 8)
# avg = sum(se1_7)/ len(se1_7)
# print(avg, se8)


records=[('foo', 1,2), ('bar','hello'), ('foo', 3,4)]
def do_foo(x, y) :
    print('foo',x,y)
def do_bar(s) :
    print('bar',s)
for tag, *args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)

line=( 'nobody:*: -2: -2:Unprivileged User:/var/empty:/user/bin/false')
uname, *field, homedtr, sh=line.split(':')
print (uname)
print(field)
print (homedtr)
print(sh)