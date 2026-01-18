list=[21,33,57,88,95,100,120,123]
input=int(input("请输入一个数"))




for i in range(len(list)):
    if input<list[i]:
        list.insert(i,input)
        break
    else:
        list.append(input)

print(list)
