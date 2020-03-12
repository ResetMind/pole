import questions

q = questions.question
print(q)
a = tuple(questions.answer)
print(a)
aa = [""] * len(a)


def entry_indices(s):
    indices = []
    for i in range(len(a)):
        if s == a[i]:
            indices.append(i)
    return indices


def fill_word(indices):
    global aa
    for i in range(len(indices)):
        aa[indices[i]] = a[indices[i]]
    print(aa)


while tuple(aa) != a:
    letter = str(input("Введите букву: "))
    ind = entry_indices(letter)
    if len(ind) > 0:
        fill_word(ind)
    else:
        print("Неверная буква!")
print("Поздравляем! Вы угадали слово")