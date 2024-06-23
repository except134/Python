numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Исходные числа:", numbers)

primes = []
not_primes = []
is_prime = False

for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    
    for j in range(2, i):
        if numbers[i] % j == 0:
            is_prime = False
            break;
    else:
        is_prime = True
        
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print("Простые числа:", primes)
print("Не простые числа:", not_primes)
