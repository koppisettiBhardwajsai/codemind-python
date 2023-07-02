def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime(number):
    if is_prime(number):
        return number

    lower_prime = number - 1
    while not is_prime(lower_prime):
        lower_prime -= 1

    upper_prime = number + 1
    while not is_prime(upper_prime):
        upper_prime += 1

    if abs(number - lower_prime) <= abs(number - upper_prime):
        return lower_prime
    else:
        return upper_prime
m=int(input())
for i in range(m):
    num =int(input())
    result = nearest_prime(num)
    print(result)
