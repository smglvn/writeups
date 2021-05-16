#! /usr/bin/env python3
FLAG = 'sdctf{a_v3ry_s3cur3_w4y_t0_st0r3_ur_FLAG}'  # lol

a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)  # its Fibonacci number

b = lambda x: bytes.fromhex(x).decode() # decode from hex

h = print


def d():
    print('Incorrect flag! You need to hack deeper...')
    __import__("sys").exit(1)
    print(FLAG)


def e(f):
    h("Welcome to SDCTF's the first Reverse Engineering challenge.")
    c = get_flag()
    if c[:6] != 'sdctf{':
        d()
    if c[-1] != '}':
        d()
    g = c[6:-1].encode()
    if bytes( (g[i] ^ (a(i) & 0xff) for i in range(len(g))) ) != f:
        d()
    print('Nice job. You got the correct flag!')


def get_flag():
    flag_length = len(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
    dexor_flag = ((a(i) & 0xff) ^ b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4'[i] for i in range(flag_length))
    decode_flag = ''.join(list(map(lambda x: chr(x), dexor_flag)))
    print(decode_flag)
    return 'sdctf{' + decode_flag + '}'


if __name__ == "__main__":
    e(b't2q}*\x7f&n[5V\xb42a\x7f3\xac\x87\xe6\xb4')
else:
    __import__("sys").exit(0)
