def calculate_list(list):
    return sum(list)

if __name__ == '__main__':
    list=[1,2,3,4,5]
    print(calculate_list(list))


    print(f"列表的和为：{calculate_list(list)}")
    print("列表的和为：",calculate_list(list),sep="")