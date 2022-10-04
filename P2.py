print("#------------#")
inti = int(input('請輸入整數:'))
print(type(ini)) #若輸入整數數值將程式錯誤
print(inti)
inf = float(input('請輸入浮點數:'))
print(type(inf))
print(inf)
inp = eval(input('請輸入數字:')) #將輸入數值自動轉型
print(type(inp)) 
print(inp)
print("#------------#")
x=int(input('Input Int x:'))
y=int(input('Input Int y:'))
if x > y:
    print("x=%d > y=%d" %(x,y))  #""內皆為字串
else :
    print("x=%d <= y=%d" %(x,y))
print("if之後執行")
print("#------------#")
score = eval(input('請輸入成績:'))
if ( 0 <= score  <=100 ):
    if( score == 100) :
        print(score,'滿分')
    elif (score >= 90):
        print(score,'特優')
    elif (score >= 80):
        print(score,'優等')
    elif (score >= 70):
        print(score,'甲上')
    elif (score >= 60):
        print(score,'甲等')
    elif(score < 60):
        print(score,'不及格')
else: #上述條件均不成立則會執行此行指令
    print('成績輸入錯誤')
print("#------------#")
n1 = eval(input('輸入數字1:'))
n2 = eval(input('輸入數字2:'))
n3 = eval(input('輸入數字3:'))
if ( n1 > n2 ):
    if( n2 > n3): 
        pass #
        print("n1 > n2 > n3 : %d > %d > %d " %(n1,n2,n3))
    else :
        print("n1 > n3 > n2 : %d > %d > %d " %(n1,n3,n2))
else: # n1 <n2
    if( n2 < n3):
        print("n3 > n2 > n1 : %d > %d > %d " %(n3,n2,n1))
    else :
        print("n2 > n3 > n1 : %d > %d > %d " %(n2,n3,n1))
