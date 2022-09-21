a = input()
eng = 'qwertyuiopasdfghjklzxcvnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбю'
dict = {'car': 'машина', 'cat': 'кошка', 'hat': 'шляпа', 'umbrella': 'зонт', 'computer': 'компьютер'}
if a[0].lower() in eng:
    print(dict[a.lower()])
elif a[0].lower() in rus:
    for elem in dict.items():
        if elem[1] == a.lower():
            print(elem[0])