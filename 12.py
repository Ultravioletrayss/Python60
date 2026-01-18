
people={"张三":18,"王五":20,"赵六":19}
max_age=max(people.values())

max_name=""
for name,age in people.items():
    if age>=max_age:
        max_name=name
        max_age=age
print(f"最大的年龄是{max_age},对应的名字是{max_name}")