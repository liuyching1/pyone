#預設編碼 部分版本不支援需自行定義
#coding:UTF-8 

##資料型態
#####################

#字串的定義
x = 'Hello'
y = ", world!"
z = 'aaa,"eee"'
q = '''python 
       hello '''

#容器(Container Type)

#列表list :以[]建構
#有順序,可更改內容
[3,4,5]

#Tuple    :以()建構
# 有順序, 不可更改
("Hi","Python")

a = (1,2,3,4,5) 
b = [a,b,c,5,9]
Error!
# a,b,c 變數處理, 需先定義, 否則會Error

c =('xyz')
b= ['a','b',c,5,9]   #變數C有定義OK

#集合Set  :以{}建構
x = {1,2,3,4}
type(x)
set

#字典Dictionary {key:val} 建構
y = {'a': 123,'b': 456}
type(y)
dict

y['a']
123

x = {4,3,2,1} #對照33行
x == x
True

input() #回傳字串型態
int(input()) #轉成int型態
eval((input()) #轉成數值型 (*)
x= eval(input('這是提示文字'))
