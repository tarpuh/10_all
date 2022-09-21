def smart_search(*spis, func):
    if type(spis[0]) == int:
        return tuple(list(filter(func, list(map(int, spis)))))
    return tuple(list(filter(lambda x: x.capitalize() == x, spis)))


print(smart_search(1, 2, 3, 5, 12, func=lambda x: x % 2))

print(smart_search('The', 'quick', 'brown', 'Fox', 'jumps', 'over', 'the', 'Lazy', 'Dog', func=lambda x: x))
