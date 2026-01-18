# 寻找能被输入奇数整除的最小全9数字
user_input = int(input("please enter odd number:"))

n = 100

# 从1位9开始，逐步增加位数，直到找到能被输入数整除的全9数字
for i in range(1, n):
    n_9 = int('9' * i)
    if n_9 % user_input == 0:
        print(n_9)
        break