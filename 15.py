from cmath import inf

# 输入三个数字
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

# 使用内置函数找出最大值
max_num = max(num1, num2, num3)
print(f"最大的数是{max_num}")

# 方法二：使用循环找出最大值
max_number2 = -inf
print("max_number2", max_number2)

numbers_list = [num1, num2, num3]
for i in numbers_list:
    if i > max_number2:
        max_number2 = i

print("max_number2", max_number2)

# 方法三：使用列表排序
numbers_list2 = [num1, num2, num3]
numbers_list2.sort(reverse=True)
print(numbers_list2)
