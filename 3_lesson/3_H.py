def fact_generator():
    m = 1
    i = 1
    while True:
        m *= i
        i += 1
        yield m

