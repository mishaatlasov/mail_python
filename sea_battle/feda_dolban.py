gr_numb = int(input())
a = []
a_summ = 0
grades_updt_count = 0

for i in range(gr_numb):
    a.append(int(input()))


def count_summ(list):
    a_summ = 0
    for i in range(gr_numb):
        a_summ += list[i]
    return a_summ

if count_summ(a) / gr_numb >= 4:
    print("Всё в порядке, Федя!")
    exit()


def check_min_ball(grades_updt_count):
    if count_summ(a) / gr_numb >= 4:
        print(grades_updt_count)
        print(a)
        exit()
    else:
        grades_updt_count += 1
        a[a.index(min(a))] = 5
        check_min_ball((grades_updt_count))


check_min_ball(grades_updt_count)