num = int(input())
a = num
while num != 1:
    if num % 2 == 0:
        a //= 2
        print(f'{num} / 2 = {a}')
        num = a
    else:
        a *= 3
        print(f'{num} * 3 = {a}', end=' ; ')
        num = a
        a += 1
        print(f'{num} + 1 = {a}', end=' ; ')
        num = a
        a //= 2
        print(f'{num} / 2 = {a}')
        num = a
print('Верно')
