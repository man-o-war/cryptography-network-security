def modInverse(a, m):
    g = gcd(a, m)

    if (g != 1):
        return 1

    else:
        # If a and m are relatively prime,
        # then modulo inverse is a^(m-2) mode m
        return power(a, m - 2, m)


# To compute x^y under modulo m
def power(x, y, m):
    if (y == 0):
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m

    if (y % 2 == 0):
        return p
    else:
        return ((x * p) % m)


# Function to return gcd of a and b
def gcd(a, b):
    if (a == 0):
        return b

    return gcd(b % a, a)

n = int(input())
l = [1]
for i in range(1,n):
    if modInverse(i,n) != 1:
        l.append(modInverse(i,n))
    else:
        continue
l.sort()
k = set(l)

z = k.__len__()
print(z)