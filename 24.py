
def calculate_radius():
    radius=float(input("请输入圆的半径："))
    area=3.14*radius*radius
    print("圆的面积为：",round(area,2))

def calculate_radius2():
    radius = float(input("请输入圆的半径："))
    area = 3.14 * radius * radius
    print(f"圆的面积为： {area:.2f}")


if __name__ == "__main__":
    calculate_radius()
    calculate_radius2()