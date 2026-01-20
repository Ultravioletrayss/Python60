def count_even_number(start,end,list):
    for i in range(start,end+1):
        if i % 2 == 0:
            list.append(i)
    return list


list=[]
if __name__ == '__main__':
    print(count_even_number(1,10,list))