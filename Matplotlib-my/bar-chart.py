import matplotlib.pyplot as plt
plt.rc('font', family='microsoft yahei')
'''
x軸為數字
x = [3,4,1]
height_= [3,4,1]
'''
plt.bar([3,4,1], [3,4,1])
plt.show()

''''
x軸為字串, 調整寬度和顏色, 加上標示'
'x= ['A','B','C']''
'height_ = [3,4,1]'
'''
plt.bar(['B','A','C'], [8,10,16] , width=0.3, color='red')
plt.show()