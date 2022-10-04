# print("#------------#")
# inf = float(input('請輸入浮點數:'))
# print(type(inf))
# print(inf)
# inp = eval(input('請輸入數字:')) #將自動轉型
# print(type(inp)) 
# print(inp)
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
# print("#------------#")
