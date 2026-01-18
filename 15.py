from cmath import inf

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

max_num=max(num1,num2,num3)
print(f"最大的数是{max_num}")



max_number2=-inf
print("max_number2",max_number2)

list=[num1,num2,num3]
for i in list:
    if i>max_number2:
        max_number2=i
print("max_number2",max_number2)



list=[num1,num2,num3]
list.sort(reverse=True)
print(list)