# 学生信息列表，包含学号、姓名和成绩
students = [
    {
        "sno": 101,
        "sname": "Mike",
        "sgrade": 88
    },
    {
        "sno": 102,
        "sname": "Jhon",
        "sgrade": 90
    },
    {
        "sno": 103,
        "sname": "Mike",
        "sgrade": 80
    },
    {
        "sno": 104,
        "sname": "Mike",
        "sgrade": 100
    }

]

# 按成绩升序排序并打印
students_sort = sorted(students, key=lambda x: x["sgrade"])
print(students_sort)

# 按成绩降序排序并打印
students.sort(key=lambda x: x["sgrade"], reverse=True)
print(students)


def my_sort(x):
    """自定义排序函数，根据成绩排序"""
    return x["sgrade"]


# 使用自定义函数按成绩降序排序
students.sort(key=my_sort, reverse=True)
