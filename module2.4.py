numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime = []
not_prime = []

for num in numbers:
    is_prime = True
    if num == 1:
        continue

    elif num == 2:
        prime.append(num)

    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime == False:
            not_prime.append(num)
        else:
            prime.append(num)

print(prime, not_prime, sep='\n')