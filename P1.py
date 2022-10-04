#CTRL +/ 快速註解

print("#------------# (資料型態)")
#檢視a的資料型態
a= 0
print(type (a))

a = (1,2,3,4,5)
print(type (a))
print(a)
print("#------------#")
#字串
x = 'Hello'
y = ", world!"
z = 'aaa,"eee"'
q = '''python 
       hello '''
h = 'Hello python'
#取得字串長度
print(len(h))
#印出index=6的值
print(h[6])
#印出字元p的index
print(h.index('p'))
#印出序列h的0-12字元,每2位元顯示一次
print(h[0:12:2])
print("#------------#")
#檢查pyth是否在h序列之中
if 'pyth' in h:
    print(True)
else:
    print(False)
print("#------------#")
#多變數宣告
int1=int2=int3=100
str01,int01 = 'Hello',1234
#將 x,y值互換
x=10;y=20; x,y = y,x
print(x)

num=[1,2,3]
print(num)
num=[4,5,6]
print(num)
print("#------------# ")
i,j,k = 4,5,0.5
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i**j)
print(i//j)
print(i%j)
print(i**k)
print(i==k)
print("#-----------#")
inum = 3456
#利用運算子拆解每一字元
print(inum//1000)
print((inum%1000)//100)
print((inum%100)//10)
print(inum%10)
print("#------------#")
#算術運算子
A='ABCD'
B=A + 'DEFG'
C=A*2
print(B)
print(C)
print("#------------#")
#關係運算子 回傳 Bool
a,b,c = 5,7,9
print(a == b)
print(a > b)
print(a < b)
print(a != b)
print(a >= b)
print(a <= b)
print(a < c > b)
a**=2  # a = a**2
print(a)
print("#------------#")
list1 = [1, 2, 3, 'apple']
#將一樣的值賦予到兩個不同的變數上面
list2 = [1, 2, 3, 'apple']
print(list1 == list2) # 測試list1 跟list2 的值是否相等 True
print(list1 is list2) # 測試list1 跟list2 的指向目標物件是否為同一個 False
list1 = list2 # 將list1 指向list2 所指向的物件
print(list1 == list2) # True
print(list1 is list2) # True
print("#------------#")
#is 檢查物件是否相同
x,y = 156,156
print(x == y)
print(x is y)
print("#------------#")
tuple1 = (1, 2, '3', '4', [1, 2])
list1 = [5, 6, '7', '8']
dict1 = {9 : 'b', 0 : 'd'}
set1 = {'x', 'y', 'z'}
strg1 = 'abcdefghijklmn'
print('b' in dict1, 9 in dict1) #False True print('x' in set1, 10 in set1) #True False
print('z' in strg1, 'c' in strg1) #False True
print("#------------#")
# a and b  
# a or b   
a, b = 0, (10, 11)  
print(a or b)  
print(a and b)  
print(not a)  
print((not a)and b) 
print("#------------#") 

