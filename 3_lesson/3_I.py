def prime_generator():
    i = 2
    while True:
        a = 0
        for x in range(2, int(i ** 0.5) + 1):
            if i % x == 0:
                a += 1
                break
        i += 1
        if a == 0:
            yield i - 1


