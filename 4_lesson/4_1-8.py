def car(l):
    return (l[0])


def cdr(l):
    return (l[1:])


def cons(x, l):
    l.insert(0, x)
    return (l)


def null(l):
    return (l == [])


def begin(l):
    return (l[:len(l) - 1])


def last(l):
    return (l[len(l) - 1])


def atom(l):
    if (type(l) == type(1) or type(l) == type('a') or type(l) == type(1.5)):
        return True
    else:
        return False


def list_begin(L):
    if null(cdr(L)):
        return []
    else:
        return cons(car(L), list_begin(cdr(L)))


def list_len(L):
    if null(L):
        return 0
    else:
        return 1 + list_len(cdr(L))


def list_reverse(L):
    if null(L):
        return []
    else:
        return cons(last(L), list_reverse(begin(L)))


def count_atoms(L):
    if null(L):
        return 0
    elif atom(car(L)):
        return 1 + count_atoms(cdr(L))
    else:
        return count_atoms(cdr(L))


def only_atoms(L):
    if null(L):
        return []
    elif atom(car(L)):
        return cons(car(L), only_atoms(cdr(L)))
    else:
        return only_atoms(cdr(L))


def into_sort(x, L):
    if null(L):
        return [x]
    elif x <= car(L):
        return cons(x, L)
    else:
        return cons(car(L), into_sort(x, cdr(L)))


def list_sort(L):
    if null(L):
        return []
    else:
        return into_sort(car(L), list_sort(cdr(L)))


def list_merge(L, R):
    if null(L):
        return R
    elif null(cdr(L)):
        return into_sort(car(L), list_sort(R))
    else:
        return list_merge(cdr(L), into_sort(car(L), list_sort(R)))


L = [1, 2, 5, 4]
R = [1, 2, 3, 4]
print(list_merge(L, R))