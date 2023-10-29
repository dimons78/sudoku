import itertools

def get_list_comb(str_in):
    list_out = []
    list_ = list(map(int,str_in))

    for i in range(9):
        if i + 1 not in list_:
            # создание списка из отсутствующих цифр
            list_out.append(i+1)


    # создание списка из возможных сочетаний
    list_comb = list(itertools.permutations(list_out))
    return list_comb



# проверка проверочного списка без нулей для К-го сочетания
def cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_1, set_2, set_3):

    # создание пустого списка из возможных сочетаний для строки 1
    list_comb = []

    for k_tuple in list_comb_max:

        # создание временного инвертируемого списка для К-го сочетания
        k_list_ = list(k_tuple[::-1])
        # [2, 3, 4, 7, 8, 9] с инвертором

        # создание пустого проверочного списка для К-го сочетания
        list_chek = []

        for j in range(9):

            if list_[j] == 0:
                # заполнение проверочного списка без нулей для К-го сочетания
                list_chek.append(k_list_.pop())
            else:
                list_chek.append(list_[j])
                # [9, 8, 7, 4, 5, 6, 3, 1, 2]

        # проверка проверочного списка без нулей для К-го сочетания
        for j in range(9):
            # проверка, что числа нет в вертикали и квадранте
            count_zero = 0
            count_chek = 0

            if j == 0:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[0] and set_1:
                        count_chek += 1
                    else:
                        break

            if j == 1:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[1] and set_1:
                        count_chek += 1
                    else:
                        break

            if j == 2:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[2] and set_1:
                        count_chek += 1
                    else:
                        break

            if j == 3:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[3] and set_2:
                        count_chek += 1
                    else:
                        break

            if j == 4:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[4] and set_2:
                        count_chek += 1
                    else:
                        break

            if j == 5:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[5] and set_2:
                        count_chek += 1
                    else:
                        break

            if j == 6:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[6] and set_3:
                        count_chek += 1
                    else:
                        break

            if j == 7:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[7] and set_3:
                        count_chek += 1
                    else:
                        break

            if j == 8:
                if list_[j] == 0:
                    count_zero += 1
                    if list_chek[j] not in list_set_ver[8] and set_3:
                        count_chek += 1
                    else:
                        break

        # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах,
        # то строка возможна (добавляем):
        if count_chek == count_zero:
            list_comb.append(k_tuple)

    return list_comb

