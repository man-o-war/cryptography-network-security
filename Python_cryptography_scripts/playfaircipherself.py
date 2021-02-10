import string


def matrix(k):
    mat = []
    for e in k.upper():
        if e not in mat:
            mat.append(e)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for e in alphabet:
        if e not in mat:
            mat.append(e)
    matrix_group = []
    for e in range(5):
        matrix_group.append('')
    matrix_group[0] = mat[0:5]
    matrix_group[1] = mat[5:10]
    matrix_group[2] = mat[10:15]
    matrix_group[3] = mat[15:20]
    matrix_group[4] = mat[20:25]
    return matrix_group


def message_to_digraphs(message_original):
    digraphs = []
    s = message_original
    s = "".join((char for char in s if char not in string.punctuation))
    s = s.replace(' ', '')
    s = s.upper()
    if len(s) % 2 == 1:
        s = s + 'X'
    for i in range(0, len(s), 2):
        di = [s[i]]
        if s[i + 1] == s[i]:
            di.append('X')
        else:
            di.append(s[i + 1])
        digraphs.append(di)
    return digraphs


def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j
    return x, y


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


def encrypt(message):
    message = message_to_digraphs(message)
    key_matrix = matrix(key)
    cipher = []
    for e in message:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    st_cipher = convert(cipher)
    return st_cipher


def cipher_to_digraphs(cipher):
    i = 0
    new = []
    for x in range(len(cipher) // 2):
        new.append(cipher[i:i + 2])
        i = i + 2
    return new


def decrypt(cipher):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = matrix(key)
    plaintext = []
    for e in cipher:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            plaintext.append(key_matrix[p1][q1 - 1])
            plaintext.append(key_matrix[p1][q2 - 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            plaintext.append(key_matrix[p1 - 1][q1])
            plaintext.append(key_matrix[p2 - 1][q2])
        else:
            plaintext.append(key_matrix[p1][q2])
            plaintext.append(key_matrix[p2][q1])
    for unused in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")
    output = ""
    for e in plaintext:
        output += e
    return output.lower()


print("Playfair Cipher")
order = int(input("Choose :\n1,Encrypting \n2,Decrypting\n"))
if order == 1:
    key = input("Please input the key : ")
    msg = input("Please input the message : ")
    print("Encrypting: \n" + "Message: " + msg)
    print("Cipher: ")
    print(encrypt(msg))
elif order == 2:
    key = input("Please input the key : ")
    cip = input("Please input the cipher text: ")
    print("\nDecrypting: \n" + "Cipher: " + cip)
    print("Plaintext:")
    print(decrypt(cip))
else:
    print("Error")
