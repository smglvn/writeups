from nclib import netcat

PASSWD = 59784015375233083673486266

connection = netcat.Netcat(('phc1.sdc.tf', 1337))

stack = [(PASSWD, [])]

while len(stack) != 0:
    passwd_hash, possible_chars = stack.pop()
    if passwd_hash == 0:
        password = b'\n'
        for char in possible_chars:
            password = chr(char).encode() + password
        connection.send(password)
        print(password)
        print(connection.recv(1024))
        break
    if passwd_hash < 0:
        continue

    mod = passwd_hash % 31
    for x in range(1, 5):
        possible_last_char = mod + x * 31
        new_passwd_hash = (passwd_hash - possible_last_char) // 31
        new_possible_chars = possible_chars.copy()
        new_possible_chars.append(possible_last_char)
        stack.append((new_passwd_hash, new_possible_chars))
