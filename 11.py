# 计算1到10中所有偶数的和
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

# 遍历数组，累加偶数
for n in numbers:
    if n % 2 == 0:
        total += n

# 输出结果
print(total)