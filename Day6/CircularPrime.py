# Method -1 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    s = str(n)
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i])
        if not is_prime(rotated):
            return False
    return True

print("2-digit Circular Prime Numbers:")
for num in range(10, 100):
    if is_circular_prime(num):
        print(num, end=' ')


# Method 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def rotate_2digit(num):

    tens = num // 10
    units = num % 10
    rotated = units * 10 + tens
    return rotated

def is_circular_prime_2digit(n):
    if not is_prime(n):
        return False
    rotated = rotate_2digit(n)
    return is_prime(rotated)


print("2-digit Circular Primes (No string conversion):")
for i in range(10, 100):
    if is_circular_prime_2digit(i):
        print(i, end=' ')
