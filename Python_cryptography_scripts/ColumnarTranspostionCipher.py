import string


def generate_enc_matrix(message, r, c):
    message = msg_processing(message, c)
    mat = []
    for i in range(0, r):
        tm = []
        for j in range(0, c):
            tm.append('')
        mat.append(tm)
    count = 0
    for i in range(0, r):
        for j in range(0, c):
            mat[i][j] = message[count]
            count += 1
    return mat


def msg_processing(message, c):
    message = "".join((char for char in message if char not in string.punctuation))
    message = message.replace(' ', '')
    message = message.upper()
    if len(message) % c != 0:
        for i in range(len(message) % c):
            message += 'X'
    return message


def encrypt(message, r, c):
    mat = generate_enc_matrix(message, r, c)
    s = ''
    for i in range(0, c):
        for j in range(0, r):
            s += mat[j][i]
    return s


def generate_dec_mat(message, r, c):
    mat = []
    for i in range(0, r):
        tm = []
        for j in range(0, c):
            tm.append('')
        mat.append(tm)
    count = 0
    for i in range(0, c):
        for j in range(0, r):
            mat[j][i] = message[count]
            count += 1
    return mat


def decrypt(message, r, c):
    mat = generate_dec_mat(message, r, c)
    s = ''
    for i in range(0, r):
        for j in range(0, c):
            s += mat[i][j]
    return s


msg = input("Input text: ")
row = int(input("Input no of rows: "))
col = int(input("Input no of columns: "))
ch = input("What do you want to do?\n1.Encryption\n2.Decryption\n")
if ch == '1':
    print("Encrypted text: ", encrypt(msg, row, col))
elif ch == '2':
    print("Decrypted text: ", decrypt(msg, row, col))
else:
    print("Wrong choice")
