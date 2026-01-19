while True:
    number = int(input("Enter a number: "))
    times = int(input("Enter how many times to add it: "))

    total = 0
    temp = 0

    for _ in range(times):
        temp=temp*10+number
        total=total+ temp
        print(temp)
    print(total)












