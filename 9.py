# 数字列表排序操作示例
list_nums = [20, 50, 10, 40, 30]

# 升序排序
list_nums.sort(key=None, reverse=False)  # ASC
print(list_nums)

# 降序排序
list_nums.sort(key=None, reverse=True)  # DESC
print(list_nums)

# 反转列表
list_nums.reverse()

# 排序（升序）
list_nums.sort()

# 创建排序副本
list2 = sorted(list_nums)
