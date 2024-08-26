def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
            
        return num

    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 2, 2)
print(result)

result = sum_three(2, 9, 4)
print(result)

result = sum_three(1, 3, 3)
print(result)
