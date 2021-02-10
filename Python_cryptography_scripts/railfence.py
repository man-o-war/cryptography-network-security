def print_fence(fence):
    for rail in range(len(fence)):
        print(''.join(fence[rail]))


def encrypt_fence(pl, rails, offset=0, debug=False):
    dr = 0
    cip = ''

    # offset
    pl = '#' * offset + pl

    length = len(pl)
    fence = [['#'] * length for _ in range(rails)]

    # build fence
    rail = 0
    for x in range(length):
        fence[rail][x] = pl[x]
        if rail >= rails - 1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    # print fence
    if debug:
        print_fence(fence)

    # read fence
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cip += fence[rail][x]
    return cip


def decrypt_fence(cip, rails, offset=0, debug=False):
    pl = ''

    # offset
    if offset:
        t = encrypt_fence('o' * offset + 'x' * len(cip), rails)
        for i in range(len(t)):
            if t[i] == 'o':
                cip = cip[:i] + '#' + cip[i:]

    length = len(cip)
    fence = [['#'] * length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails - 1))
        x = rail
        while x < length and i < length:
            fence[rail][x] = cip[i]
            if p:
                x += 2 * (rails - rail - 1)
            else:
                x += 2 * rail
            if (rail != 0) and (rail != (rails - 1)):
                p = not p
            i += 1

    # print fence
    if debug:
        print_fence(fence)

    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                pl += fence[rail][i]
    return pl


plain = input('Input Message for encryption ')
print('Message: ', plain, '\n')
r = int(input('Input number of rails '))
plain = plain.replace(' ', '')
plain = plain.upper()
cipher = encrypt_fence(plain, r)
print('Encrypting... \nCipher: ', cipher, '\n')
plain2 = decrypt_fence(cipher, r)
print('Decrypting... \nPlain Text Obtained: ', plain2)
