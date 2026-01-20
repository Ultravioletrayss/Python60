list1=[3,5,7,9,11,13,15,17,19]
list2=[7,9,11]


def list_sub(list1,list2):
    list3=[]
    for i in list1:
        if i not in list2:
            list3.append(i)
    return list3
if __name__ == '__main__':
    list3=list_sub(list1,list2)
    print(list3)