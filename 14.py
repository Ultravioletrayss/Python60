# 已排序的数字列表
list_nums = [21, 33, 57, 88, 95, 100, 120, 123]

# 用户输入一个数字
user_input = int(input("请输入一个数"))

# 在列表中查找插入位置
for i in range(len(list_nums)):
    if user_input < list_nums[i]:
        list_nums.insert(i, user_input)
        break
else:
    # 如果没有找到合适位置，则添加到末尾
    list_nums.append(user_input)

# 输出最终列表
print(list_nums)
