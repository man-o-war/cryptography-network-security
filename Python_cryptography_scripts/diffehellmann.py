import random
import hashlib

g = 9
p = 1001

a = random.randint(5, 10)
b = random.randint(10, 20)

A = (g ** a) % p
B = (g ** b) % p

print('g: ', g, ' (a shared value), n: ', p, ' (a prime number)')
print('\nAlice calculates:')
print('a (Alice random): ', a)
print('Alice value (A): ', A, ' (g^a) mod p')
print('\nBob calculates:')
print('b (Bob random): ', b)
print('Bob value (B): ', B, ' (g^b) mod p')
print('\nAlice calculates:')
keyA = (B ** a) % p
print('Key: ', keyA, ' (B^a) mod p')
result = hashlib.sha256(str(keyA).encode())
print('Key: ',result.hexdigest())
print('\nBob calculates:')
keyB = (A ** b) % p
print('Key: ', keyB, ' (A^b) mod p')
result = hashlib.sha256(str(keyB).encode())
print('Key: ',result.hexdigest())
