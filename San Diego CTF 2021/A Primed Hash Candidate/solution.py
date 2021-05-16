from nclib import netcat

PASSWD = 91918419847262345220747548257014204909656105967816548490107654667943676632784144361466466654437911844

connection = netcat.Netcat(('phc2.sdc.tf', 1337))
connection.recvline()


def find_hash(password):
    connection.send(password + b'\n')
    answer = connection.recvline().decode()
    connection.recvline()
    password_hash = answer.split(' ')[-1][:-1]
    return int(password_hash)


def find_secret2_length(temp_hash):
    s2_length = 0
    while temp_hash > 0:
        temp_hash = temp_hash // s3
        s2_length += 1
    return s2_length


def find_data(temp_hash):
    data = []
    while temp_hash != 0:
        mod = temp_hash % s3
        data.insert(0, mod)
        temp_hash = (temp_hash - mod) // s3
    return data


def find_secret1_chars(temp_hash, password):
    s1 = []
    data = find_data(temp_hash)
    data = data[:s2_length + 3]

    for i in range(len(data)):
        x = data[i]
        y = ord(password[i])
        s1.append(x ^ y)
    return s1


def find_password_chars(temp_hash):
    data = find_data(temp_hash)
    result = []
    data = data[:s2_length + 3]
    for i in range(len(data)):
        result.append(data[i] ^ s1[i])
    return result


def form_password(chars):
    password = b''
    for char in chars:
        password += chr(char).encode()
    password += b'\n'
    return password


hash_1 = find_hash(b'')
hash_2 = find_hash(b'my_password' * 10)

for s3 in range(100, 1000):
    print(s3)
    s2_length = find_secret2_length(hash_1)
    s1 = find_secret1_chars(hash_2, 'my_password' * 10)
    password_chars = find_password_chars(PASSWD)

    password = form_password(password_chars)
    connection.send(password)
    res = connection.recvline().decode()
    if 'Wrong' not in res:
        print(res)
        print(connection.recvline())
        break
    connection.recvline()
