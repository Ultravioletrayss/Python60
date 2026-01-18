# 查找水仙花数（三位数，各位立方和等于原数）
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            # 检查是否为水仙花数
            if i**3 + j**3 + k**3 == 100*i + 10*j + k:
                print(i, j, k)
