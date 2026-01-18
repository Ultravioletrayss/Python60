# 定义人员及其年龄的字典
people = {"张三": 18, "王五": 20, "赵六": 19}

# 获取最大年龄
max_age = max(people.values())

max_name = ""
# 遍历字典，查找具有最大年龄的人
for name, age in people.items():
    if age >= max_age:
        max_name = name
        max_age = age

# 输出最大年龄及对应姓名
print(f"最大的年龄是{max_age},对应的名字是{max_name}")