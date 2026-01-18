input=int(input("请输入一个数"))
if input%4==0 and input%100!=0 or input%400==0:
    print("闰年")
else:
    print("平年")