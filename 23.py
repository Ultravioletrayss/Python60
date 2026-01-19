def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

total = 1
def factorial2(n,total):
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            total*=i
        return total
number=int(input("请输入一个正整数："))
print(factorial(number))



print(factorial2(number,total))