# 實體物件的建立與使用- 上篇
# https://www.youtube.com/watch?v=Lr5N2r1rmtM
# 類別的兩種用法 1.類別與類別屬性 2.類別與實體物件、實體屬性

# 實體物件
# 透過類別建立   先定義類別，再透過類別建立實體物件

# 建立 -> 使用   要先建立實體物件，然後才能使用實體屬性

# 建立實體
# 基本語法
#class 類別名稱:   
    #定義初始化函式:
    #def__init__(self):  # 固定初始化函式定義是 兩個底線init兩個底線():
        #透過操作 self 來定義實體屬性
# 建立實體物件，放入變數 obj 中
#obj=類別名稱() # 呼叫初始化函式

# 程式範例
# class Point:
    # def __init__(self):
    #     self.x=3     #self.屬性的名稱=資料放進去
    #     self.y=4
# 建立實體物件
# 此實體物件包含 x 和 y 兩個實體屬性
# p=Point()

# 程式範例
#class Point:
    #def __init__(self,x,y):        # 除了放self之外  還可以放參數
        #self.x=x
        #self.y=y
# 建立實體物件
# 建立時，可直接傳入參數資料
#p=Point(1,5)      # 對應位置， 1 會放到 x , 5 會放到 y 

# 使用實體
# 基本語法
#實體物件.實體屬性名稱

# 程式範例
#class Point:
    #def __init__(self,x,y):
        #self.x=x
        #self.y=y
# 建立實體物件，並取得實體屬性資料
#p=Point(1,5)
#print(p.x+p.y)

#----------------------------

# Point 實體物件的設計: 平面座標上的點
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
# 建立第一個實體物件
p1=Point(3,4)
print(p1.x,p1.y)
# 建立第二個實體物件
p2=Point(5,6)
print(p2.x,p2.y)


# FullName 實體物件的設計: 分開紀錄姓、名資料的全名

class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=FullName("C.W.","Peng")
print(name1.first,name1.last)

name2=FullName("W.M.","Lai")
print(name2.first,name2.last)