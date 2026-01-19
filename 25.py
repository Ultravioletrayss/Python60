def judgement_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        return True




def print_primes(start, end):
    for i in range(start, end+1):
        if judgement_prime(i):
            print(i, end=' ')


if __name__ == '__main__':
    print_primes(1, 100)
