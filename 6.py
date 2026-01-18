# 计算猴子吃桃问题
initial = 1

# 逆向计算每天剩余桃子数量
for i in range(1, 10):
    initial = (initial + 1) * 2

# 输出最初桃子数量
print(initial)