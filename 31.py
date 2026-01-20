def switch(num1,num2):
    num3=0
    num3=num1
    num1=num2
    return num1,num3
if __name__ == '__main__':
    num1=int(input("请输入第一个数字："))
    num2=int(input("请输入第二个数字："))
    num1,num2=switch(num1,num2)
    print("交换后的第一个数字是：",num1)
    print("交换后的第二个数字是：",num2)