students=[
    {
        "sno":101,
        "sname":"Mike",
        "sgrade":88
    },
    {
        "sno":102,
        "sname":"Jhon",
        "sgrade":90
    },
    {
        "sno":103,
        "sname":"Mike",
        "sgrade":80
    },
    {
        "sno":104,
        "sname":"Mike",
        "sgrade":100
    }

]
students_sort=sorted(students,key=lambda x:x["sgrade"])
print(students_sort)
students.sort(key=lambda x:x["sgrade"],reverse=True)
print(students)

def my_sort(x):
    return x["sgrade"]
students.sort(key=my_sort,reverse=True)