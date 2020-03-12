import questions

qa = questions.get_question()
a = tuple(qa[1])
aa = [""] * len(a)
q = qa[0]
print(q + "\n" + str(len(aa)) + " букв\n")


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
    letter = input("Введите букву: ").lower()
    if aa.count(letter) != 0:
        print("Такая буква уже есть")
        continue
    ind = entry_indices(letter)
    if len(ind) > 0:
        fill_word(ind)
    else:
        print("Неверная буква!")
print("\nПоздравляем! Вы угадали слово!")
