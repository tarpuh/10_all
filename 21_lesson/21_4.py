import random


def main(n, m):
    L = [generate_password(m) for i in range(n)]
    return L


def generate_password(m):
    password = ''
    s = '23456789qwertyupasdfghjkzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM'
    a1 = random.randint(0, 7)
    a2 = random.randint(8, 31)
    a3 = random.randint(-24, -1)
    password += s[a1]
    password += s[a2]
    password += s[a3]
    while len(password) < m:
        a = random.randint(1, 55)
        if s[a] not in password:
            password += s[a]
    return password


print("Случайный пароль из 7 символов:", generate_password(7))
print("5 случайных паролей длиной 15 символов:")
print(*main(5, 15), sep="\n")
