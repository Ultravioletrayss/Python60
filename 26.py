def calculation_sum_squares(number):
    total = 0
    for i in range(1,number+1):
        total+= i**2
    return total

if __name__== '__main__':
    print(calculation_sum_squares(2))