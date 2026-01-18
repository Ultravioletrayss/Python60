# 统计输入字符串中各类字符的数量
s = input("Please enter some number")
print(s, type(s))

number1 = 0  # 字母计数器
number2 = 0  # 空格计数器
number3 = 0  # 数字计数器
number4 = 0  # 特殊字符计数器

# 遍历字符串中的每个字符
for t in s:
    if t.isalpha():
        print(t, "is Alpha")
    elif t.isspace():
        print(t, "is space")
    elif t.isdigit():
        print(t, "is digit")
    else:
        print(t, "is special")
