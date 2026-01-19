while True:
    number = input("Enter a number: ")
    times = int(input("Enter how many times to add it: "))

    total = 0
    for i in range(1, times + 1):
        term = int(number * i)
        total += term

    print(total)



