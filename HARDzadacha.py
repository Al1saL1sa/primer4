if __name__ == '__main__':
    s = input("Введите текст: ").split(" ")
    print(s)
    z = []
    l = []
    m = []

    for i in s:
        if i[0] == i[-1]:
            z.append(i)
    print("Начинается и оканчивается на одну и ту же букву:", z)

    for x in s:
        if x.count('e') == 3:
            l.append(x)
    print("Содержит ровно три буквы e:", l)

    for y in s:
        if y.count("o"):
            m.append(y)
    print("Содержит хотя бы одну букву o:", m)