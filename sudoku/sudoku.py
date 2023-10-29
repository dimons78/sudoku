from tqdm import tqdm
from cheking_sudoku import cheking_hor, cheking_ver, cheking_sq, out_sud, cheking_new
from list_combination import get_list_comb, cheking_list_chek

import itertools
import datetime
import locale


locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

if __name__ == '__main__':

    start = datetime.datetime.now()

    # Необходимо заполнить ячеек: 25 а это: 30.864197530864196 %
    # sud_in = [
    #         '596820017',
    #         '024901350',
    #         '810070906',
    #         '247006509',
    #         '900248763',
    #         '030795041',
    #         '070682135',
    #         '102350804',
    #         '305017690'
    # ]

    #  Необходимо заполнить ячеек: 28 а это: 34.5679012345679 %
    # Уровень 1
    # sud_in = [
    #     '079630405',
    #     '543271900',
    #     '602509107',
    #     '000006572',
    #     '450782010',
    #     '027153800',
    #     '805020641',
    #     '291360058',
    #     '704015200'
    # ]

    # Уровень 2  3сек.
    # Необходимо заполнить ячеек: 34 а это: 41.97530864197531 %
    # sud_in = [
    #     '790001405',
    #     '381050076',
    #     '400607310',
    #     '009542830',
    #     '240790000',
    #     '075300920',
    #     '007804002',
    #     '564003790',
    #     '120905043'
    # ]

    # Уровень 2
    # 3 сек
    # Необходимо заполнить ячеек: 40 а это: 49.382716049382715 %
    # sud_in = [
    #     '800900456',
    #     '450700123',
    #     '010005000',
    #     '002090500',
    #     '063000942',
    #     '790052031',
    #     '001408070',
    #     '205073098',
    #     '670500300'
    # ]

    # Уровень 3
    #  2 сек.
    # Необходимо заполнить ячеек: 45 а это: 55.55555555555556 %
    # sud_in = [
    #     '713200400',
    #     '000694071',
    #     '004071008',
    #     '200405000',
    #     '037800064',
    #     '900700800',
    #     '025000643',
    #     '006000905',
    #     '080030200'
    # ]

    # Уровень 4
    # 1.4 сек
    # sud_in = [
    #     '800904567',
    #     '400067830',
    #     '000000000',
    #     '000600100',
    #     '100002040',
    #     '030009000',
    #     '060023701',
    #     '004080056',
    #     '712000004'
    # ]

    # Уровень 4 с поворотом на 90 град.
    # Необходимо заполнить ячеек: 50 а это: 61.72839506172839 %
    # 0,7 сек
    # sud_in = [
    #     '700010048',
    #     '106300000',
    #     '240000000',
    #     '000006009',
    #     '082000060',
    #     '003920074',
    #     '007001085',
    #     '050040036',
    #     '461000007'
    # ]

    # Уровень 5
    # Необходимо заполнить ячеек: 59 а это: 72.8395061728395 %
    #  1,1 сек.
    # sud_in = [
    #     '000930070',
    #     '080000010',
    #     '450002000',
    #     '000400000',
    #     '000078001',
    #     '000000630',
    #     '003800200',
    #     '000009000',
    #     '000005846'
    # ]

    # Уровень 6
    # Необходимо заполнить ячеек: 56 а это: 69.1358024691358 %
    #  4.8 сек.
    # sud_in = [
    #     '700000100',
    #     '100004300',
    #     '046100080',
    #     '050010842',
    #     '000003000',
    #     '008050000',
    #     '000040605',
    #     '000906000',
    #     '020300007'
    # ]


    # 12 сек
    # Необходимо заполнить ячеек: 48 а это: 59.25925925925926 %
    # sud_in = [
    #         '960070000',
    #         '105006090',
    #         '703200010',
    #         '004080750',
    #         '500060008',
    #         '039010600',
    #         '090007302',
    #         '010800405',
    #         '000020079'
    # ]

    # 6 сек
    # Необходимо заполнить ячеек: 46 а это: 56.79012345679013 %
    # sud_in = [
    #         '060904507',
    #         '005000400',
    #         '001805009',
    #         '400521000',
    #         '058070910',
    #         '000698004',
    #         '200307100',
    #         '004000200',
    #         '503206090'
    # ]

    # Необходимо заполнить ячеек: 57 а это: 70.37037037037037 %
    # 7,6 сек.
    # sud_in = [
    #         '000009502',
    #         '000704300',
    #         '060000000',
    #         '020056009',
    #         '500000008',
    #         '400810050',
    #         '000000030',
    #         '001302000',
    #         '804100000'
    # ]


    # Уровень 6
    # Необходимо заполнить ячеек: 57 а это: 70.37 %
    #  27.7 сек.
    # sud_in = [
    #         '000708600',
    #         '000000000',
    #         '050001093',
    #         '500000040',
    #         '020087000',
    #         '810300006',
    #         '900040008',
    #         '006000030',
    #         '003900050'
    # ]

    # Уровень 5
    # Необходимо заполнить ячеек: 59 а это: 72.8395061728395 %
    #  8,9 сек
    # sud_in = [
    #         '000001070',
    #         '000070005',
    #         '280000904',
    #         '005010600',
    #         '000000003',
    #         '034000000',
    #         '109700000',
    #         '800000500',
    #         '000064002'
    # ]
    # Уровень 5
    # с поворотом на 180 град.
    sud_in = [
            '200460000',
            '005000008',
            '000007901',
            '000000430',
            '300000000',
            '006010500',
            '409000082',
            '500070000',
            '070100000'
    ]

    # Уровень 4
    # Необходимо заполнить ячеек: 50 а это: 61 %
    #  8,9 сек
    # sud_in = [
    #         '204085900',
    #         '000020034',
    #         '010300580',
    #         '002093000',
    #         '071400009',
    #         '508006100',
    #         '087000001',
    #         '000000260',
    #         '000609300'
    # ]




    n_comb = 1

    # Основной список Судоку
    sud = []
    # Вспомогательный проверочный список
    sud_chek = []
    num_zero = 0

    # Занесение строк
    for i in range(9):
        str_ = (sud_in[i])

        # строка в список
        list_ = list(map(int,str_))

        # Заносим проверочный список (0 - пусто, 1- есть цифра в дано и менять НЕЛЬЗЯ!)
        list_chek = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            if list_[j] != 0:
                list_chek[j] = 1
            else:
                num_zero += 1

        # Заносим лист судоку и проверочный лист
        sud.append(list_)
        sud_chek.append(list_chek)

    print('Необходимо заполнить ячеек:',  num_zero, ", а это:", int(num_zero*100/81),'%')

    # создание вертикальных сетов (1-9):
    set_ver_1 = set()
    set_ver_2 = set()
    set_ver_3 = set()
    set_ver_4 = set()
    set_ver_5 = set()
    set_ver_6 = set()
    set_ver_7 = set()
    set_ver_8 = set()
    set_ver_9 = set()

    for j in range(9):
        for i in range(9):
            if j == 0:
                set_ver_1.add(sud[i][0])
            if j == 1:
                set_ver_2.add(sud[i][1])
            if j == 2:
                set_ver_3.add(sud[i][2])
            if j == 3:
                set_ver_4.add(sud[i][3])
            if j == 4:
                set_ver_5.add(sud[i][4])
            if j == 5:
                set_ver_6.add(sud[i][5])
            if j == 6:
                set_ver_7.add(sud[i][6])
            if j == 7:
                set_ver_8.add(sud[i][7])
            if j == 8:
                set_ver_9.add(sud[i][8])

    # создание списка вертик. сетов
    list_set_ver = [
        set_ver_1,
        set_ver_2,
        set_ver_3,
        set_ver_4,
        set_ver_5,
        set_ver_6,
        set_ver_7,
        set_ver_8,
        set_ver_9
    ]

    # создание квадрантных сетов (1-9):
    set_sq_1 = {sud[0][0], sud[0][1], sud[0][2], sud[1][0], sud[1][1], sud[1][2], sud[2][0], sud[2][1], sud[2][2]}
    set_sq_2 = {sud[0][3], sud[0][4], sud[0][5], sud[1][3], sud[1][4], sud[1][5], sud[2][3], sud[2][4], sud[2][5]}
    set_sq_3 = {sud[0][6], sud[0][7], sud[0][8], sud[1][6], sud[1][7], sud[1][8], sud[2][6], sud[2][7], sud[2][8]}

    set_sq_4 = {sud[3][0], sud[3][1], sud[3][2], sud[4][0], sud[4][1], sud[4][2], sud[5][0], sud[5][1], sud[5][2]}
    set_sq_5 = {sud[3][3], sud[3][4], sud[3][5], sud[4][3], sud[4][4], sud[4][5], sud[5][3], sud[5][4], sud[5][5]}
    set_sq_6 = {sud[3][6], sud[3][7], sud[3][8], sud[4][6], sud[4][7], sud[4][8], sud[5][6], sud[5][7], sud[5][8]}

    set_sq_7 = {sud[6][0], sud[6][1], sud[6][2], sud[7][0], sud[7][1], sud[7][2], sud[8][0], sud[8][1], sud[8][2]}
    set_sq_8 = {sud[6][3], sud[6][4], sud[6][5], sud[7][3], sud[7][4], sud[7][5], sud[8][3], sud[8][4], sud[8][5]}
    set_sq_9 = {sud[6][6], sud[6][7], sud[6][8], sud[7][6], sud[7][7], sud[7][8], sud[8][6], sud[8][7], sud[8][8]}

    # создание списка квадрантных сетов
    list_set_sq = [
        set_sq_1,
        set_sq_2,
        set_sq_3,
        set_sq_4,
        set_sq_5,
        set_sq_6,
        set_sq_7,
        set_sq_8,
        set_sq_9
    ]

    # создание списков i-той строки с нулями
    list_1 = list(map(int, sud_in[0]))
    list_2 = list(map(int, sud_in[1]))
    list_3 = list(map(int, sud_in[2]))
    list_4 = list(map(int, sud_in[3]))
    list_5 = list(map(int, sud_in[4]))
    list_6 = list(map(int, sud_in[5]))
    list_7 = list(map(int, sud_in[6]))
    list_8 = list(map(int, sud_in[7]))
    list_9 = list(map(int, sud_in[8]))

    # создание списка из возможных сочетаний
    for i in range(9):

        str_ = (sud_in[i])
        # '800900456'

        # создание списка i-той строки с нулями
        list_ = list(map(int, str_))
        # [0, 0, 0, 0, 5, 6, 0, 1, 0]

        # создание МАКС списка из возможных сочетаний для строки
        list_comb_max = get_list_comb(str_)
        # [(2, 3, 4, 7, 8, 9), (2, 3, 4, 7, 9, 8), (2, 3, 4, 8, 7, 9),...


        # создание списка из возможных сочетаний для строки 1
        if i == 0:
            list_comb_1 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_1, set_sq_2, set_sq_3)
            len_1 = len(list_comb_1)
            n_comb *= len_1

        # создание списка из возможных сочетаний для строки 2
        if i == 1:
            list_comb_2 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_1, set_sq_2, set_sq_3)
            len_2 = len(list_comb_2)
            n_comb *= len_2

        # создание списка из возможных сочетаний для строки 3
        if i == 2:
            list_comb_3 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_1, set_sq_2, set_sq_3)
            len_3 = len(list_comb_3)
            n_comb *= len_3

        # создание списка из возможных сочетаний для строки 4
        if i == 3:
            list_comb_4 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_4, set_sq_5, set_sq_6)
            len_4 = len(list_comb_4)
            n_comb *= len_4

        if i == 4:
            list_comb_5 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_4, set_sq_5, set_sq_6)
            len_5 = len(list_comb_5)
            n_comb *= len_5

        if i == 5:
            list_comb_6 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_4, set_sq_5, set_sq_6)
            len_6 = len(list_comb_6)
            n_comb *= len_6

        if i == 6:
            list_comb_7 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_7, set_sq_8, set_sq_9)
            len_7 = len(list_comb_7)
            n_comb *= len_7

        if i == 7:
            list_comb_8 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_7, set_sq_8, set_sq_9)
            len_8 = len(list_comb_8)
            n_comb *= len_8

        if i == 8:
            list_comb_9 = cheking_list_chek(list_comb_max, str_, list_, list_set_ver, set_sq_7, set_sq_8, set_sq_9)
            len_9 = len(list_comb_9)
            n_comb *= len_9


    # Пробуем варианты (9 основных циклов по строкам)
    key = 0
    num = 0

    # --------------------------------------------------------------------
    # Строка 1
    for i_1 in tqdm(list_comb_1):

        # Создание доп. вертик. строки 1:
        set_ver_new_1 = set()
        set_ver_new_2 = set()
        set_ver_new_3 = set()
        set_ver_new_4 = set()
        set_ver_new_5 = set()
        set_ver_new_6 = set()
        set_ver_new_7 = set()
        set_ver_new_8 = set()
        set_ver_new_9 = set()

        # Создание доп. квадр. строки 1:
        set_sq_new_1 = set()
        set_sq_new_2 = set()
        set_sq_new_3 = set()

        el_i1 = 0
        for j_1 in range(9):
            if sud_chek[0][j_1] == 0:
                sud[0][j_1] = i_1[el_i1]
                el_i1 += 1

        list_1 = sud[0]

        # Занесение доп. верт. строки 1:
        set_ver_new_1.add(list_1[0])
        set_ver_new_2.add(list_1[1])
        set_ver_new_3.add(list_1[2])
        set_ver_new_4.add(list_1[3])
        set_ver_new_5.add(list_1[4])
        set_ver_new_6.add(list_1[5])
        set_ver_new_7.add(list_1[6])
        set_ver_new_8.add(list_1[7])
        set_ver_new_9.add(list_1[8])

        # Занесение доп. квадр. строки 1:
        set_sq_new_1.add(list_1[0])
        set_sq_new_1.add(list_1[1])
        set_sq_new_1.add(list_1[2])

        set_sq_new_2.add(list_1[3])
        set_sq_new_2.add(list_1[4])
        set_sq_new_2.add(list_1[5])

        set_sq_new_3.add(list_1[6])
        set_sq_new_3.add(list_1[7])
        set_sq_new_3.add(list_1[8])

        # --------------------------------------------------------------------
        # Строка 2
        for i_2 in (list_comb_2):

            # Создание доп. вертик. строки 2:
            set_ver_new_2_1 = set()
            set_ver_new_2_2 = set()
            set_ver_new_2_3 = set()
            set_ver_new_2_4 = set()
            set_ver_new_2_5 = set()
            set_ver_new_2_6 = set()
            set_ver_new_2_7 = set()
            set_ver_new_2_8 = set()
            set_ver_new_2_9 = set()

            # Создание доп. квадр. строки 2:
            set_sq_new_2_1 = set()
            set_sq_new_2_2 = set()
            set_sq_new_2_3 = set()

            el_i2 = 0
            for j_2 in range(9):
                if sud_chek[1][j_2] == 0:
                    sud[1][j_2] = i_2[el_i2]
                    el_i2 += 1

            list_2 = sud[1]

            count_chek = 0
            for j in range(9):
                # проверка, что числа нет в вертикали и квадранте + доп.
                if j == 0 and sud_chek[1][0] == 0:
                    if cheking_new(list_2[j], set_ver_1, set_sq_1, set_ver_new_1, set_sq_new_1):
                        count_chek += 1
                    else:
                        break

                if j == 1 and sud_chek[1][1] == 0:
                    if cheking_new(list_2[j], set_ver_2, set_sq_1, set_ver_new_2, set_sq_new_1):
                        count_chek += 1
                    else:
                        break

                if j == 2 and sud_chek[1][2] == 0:
                    if cheking_new(list_2[j], set_ver_3, set_sq_1, set_ver_new_3, set_sq_new_1):
                        count_chek += 1
                    else:
                        break

                if j == 3 and sud_chek[1][3] == 0:
                    if cheking_new(list_2[j], set_ver_4, set_sq_2, set_ver_new_4, set_sq_new_2):
                        count_chek += 1
                    else:
                        break

                if j == 4 and sud_chek[1][4] == 0:
                    if cheking_new(list_2[j], set_ver_5, set_sq_2, set_ver_new_5, set_sq_new_2):
                        count_chek += 1
                    else:
                        break

                if j == 5 and sud_chek[1][5] == 0:
                    if cheking_new(list_2[j], set_ver_6, set_sq_2, set_ver_new_6, set_sq_new_2):
                        count_chek += 1
                    else:
                        break

                if j == 6 and sud_chek[1][6] == 0:
                    if cheking_new(list_2[j], set_ver_7, set_sq_3, set_ver_new_7, set_sq_new_3):
                        count_chek += 1
                    else:
                        break

                if j == 7 and sud_chek[1][7] == 0:
                    if cheking_new(list_2[j], set_ver_8, set_sq_3, set_ver_new_8, set_sq_new_3):
                        count_chek += 1
                    else:
                        break

                if j == 8 and sud_chek[1][8] == 0:
                    if cheking_new(list_2[j], set_ver_9, set_sq_3, set_ver_new_9, set_sq_new_3):
                        count_chek += 1
                    else:
                        break

            # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
            # то строка возможна (переходим к след. строке):
            if count_chek != el_i2:
                continue

            # Занесение доп. верт. строки 2:
            set_ver_new_2_1.add(list_2[0])
            set_ver_new_2_2.add(list_2[1])
            set_ver_new_2_3.add(list_2[2])
            set_ver_new_2_4.add(list_2[3])
            set_ver_new_2_5.add(list_2[4])
            set_ver_new_2_6.add(list_2[5])
            set_ver_new_2_7.add(list_2[6])
            set_ver_new_2_8.add(list_2[7])
            set_ver_new_2_9.add(list_2[8])

            # Занесение доп. квадр. строки 2:
            set_sq_new_2_1.add(list_2[0])
            set_sq_new_2_1.add(list_2[1])
            set_sq_new_2_1.add(list_2[2])

            set_sq_new_2_2.add(list_2[3])
            set_sq_new_2_2.add(list_2[4])
            set_sq_new_2_2.add(list_2[5])

            set_sq_new_2_3.add(list_2[6])
            set_sq_new_2_3.add(list_2[7])
            set_sq_new_2_3.add(list_2[8])

            # --------------------------------------------------------------------
            # Строка 3

            for i_3 in (list_comb_3):
                # Создание доп. вертик. строки 3:
                set_ver_new_3_1 = set()
                set_ver_new_3_2 = set()
                set_ver_new_3_3 = set()
                set_ver_new_3_4 = set()
                set_ver_new_3_5 = set()
                set_ver_new_3_6 = set()
                set_ver_new_3_7 = set()
                set_ver_new_3_8 = set()
                set_ver_new_3_9 = set()

                el_i3 = 0
                for j_3 in range(9):
                    if sud_chek[2][j_3] == 0:
                        sud[2][j_3] = i_3[el_i3]
                        el_i3 += 1

                list_3 = sud[2]

                # Объединяем СЕТЫ
                set_ver_new_2_1.update(set_ver_new_1)
                set_ver_new_2_2.update(set_ver_new_2)
                set_ver_new_2_3.update(set_ver_new_3)
                set_ver_new_2_4.update(set_ver_new_4)
                set_ver_new_2_5.update(set_ver_new_5)
                set_ver_new_2_6.update(set_ver_new_6)
                set_ver_new_2_7.update(set_ver_new_7)
                set_ver_new_2_8.update(set_ver_new_8)
                set_ver_new_2_9.update(set_ver_new_9)

                set_sq_new_2_1.update(set_sq_new_1)
                set_sq_new_2_2.update(set_sq_new_2)
                set_sq_new_2_3.update(set_sq_new_3)

                count_chek = 0
                for j in range(9):
                    # проверка, что числа нет в вертикали и квадранте + доп.
                    if j == 0 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_1, set_sq_1, set_ver_new_2_1, set_sq_new_2_1):
                            count_chek += 1
                        else:
                            break

                    if j == 1 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_2, set_sq_1, set_ver_new_2_2, set_sq_new_2_1):
                            count_chek += 1
                        else:
                            break

                    if j == 2 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_3, set_sq_1, set_ver_new_2_3, set_sq_new_2_1):
                            count_chek += 1
                        else:
                            break

                    if j == 3 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_4, set_sq_2, set_ver_new_2_4, set_sq_new_2_2):
                            count_chek += 1
                        else:
                            break

                    if j == 4 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_5, set_sq_2, set_ver_new_2_5, set_sq_new_2_2):
                            count_chek += 1
                        else:
                            break

                    if j == 5 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_6, set_sq_2, set_ver_new_2_6, set_sq_new_2_2):
                            count_chek += 1
                        else:
                            break

                    if j == 6 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_7, set_sq_3, set_ver_new_2_7, set_sq_new_2_3):
                            count_chek += 1
                        else:
                            break

                    if j == 7 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_8, set_sq_3, set_ver_new_2_8, set_sq_new_2_3):
                            count_chek += 1
                        else:
                            break

                    if j == 8 and sud_chek[2][j] == 0:
                        if cheking_new(list_3[j], set_ver_9, set_sq_3, set_ver_new_2_9, set_sq_new_2_3):
                            count_chek += 1
                        else:
                            break

                # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                # то строка возможна (переходим к след. строке):
                if count_chek != el_i3:
                    continue

                # Занесение доп. верт. строки 3:
                set_ver_new_3_1.add(list_3[0])
                set_ver_new_3_2.add(list_3[1])
                set_ver_new_3_3.add(list_3[2])
                set_ver_new_3_4.add(list_3[3])
                set_ver_new_3_5.add(list_3[4])
                set_ver_new_3_6.add(list_3[5])
                set_ver_new_3_7.add(list_3[6])
                set_ver_new_3_8.add(list_3[7])
                set_ver_new_3_9.add(list_3[8])

                # --------------------------------------------------------------------
                # Строка 4

                for i_4 in (list_comb_4):
                    # Создание 4 доп. вертик. строки 4:
                    set_ver_new_4_1 = set()
                    set_ver_new_4_2 = set()
                    set_ver_new_4_3 = set()
                    set_ver_new_4_4 = set()
                    set_ver_new_4_5 = set()
                    set_ver_new_4_6 = set()
                    set_ver_new_4_7 = set()
                    set_ver_new_4_8 = set()
                    set_ver_new_4_9 = set()

                    # Создание доп. квадр. строки 4:
                    set_sq_new_4 = set()
                    set_sq_new_5 = set()
                    set_sq_new_6 = set()

                    el_i4 = 0
                    for j_4 in range(9):
                        if sud_chek[3][j_4] == 0:
                            sud[3][j_4] = i_4[el_i4]
                            el_i4 += 1

                    list_4 = sud[3]

                    # Объединяем СЕТЫ
                    set_ver_new_3_1.update(set_ver_new_2_1)
                    set_ver_new_3_2.update(set_ver_new_2_2)
                    set_ver_new_3_3.update(set_ver_new_2_3)
                    set_ver_new_3_4.update(set_ver_new_2_4)
                    set_ver_new_3_5.update(set_ver_new_2_5)
                    set_ver_new_3_6.update(set_ver_new_2_6)
                    set_ver_new_3_7.update(set_ver_new_2_7)
                    set_ver_new_3_8.update(set_ver_new_2_8)
                    set_ver_new_3_9.update(set_ver_new_2_9)

                    count_chek = 0
                    for j in range(9):
                        # проверка, что числа нет в вертикали и квадранте + доп.

                        if j == 0 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_1, set_sq_4, set_ver_new_3_1):
                                count_chek += 1
                            else:
                                break

                        if j == 1 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_2, set_sq_4, set_ver_new_3_2):
                                count_chek += 1
                            else:
                                break

                        if j == 2 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_3, set_sq_4, set_ver_new_3_3):
                                count_chek += 1
                            else:
                                break

                        if j == 3 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_4, set_sq_5, set_ver_new_3_4):
                                count_chek += 1
                            else:
                                break

                        if j == 4 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_5, set_sq_5, set_ver_new_3_5):
                                count_chek += 1
                            else:
                                break

                        if j == 5 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_6, set_sq_5, set_ver_new_3_6):
                                count_chek += 1
                            else:
                                break

                        if j == 6 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_7, set_sq_6, set_ver_new_3_7):
                                count_chek += 1
                            else:
                                break

                        if j == 7 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_8, set_sq_6, set_ver_new_3_8):
                                count_chek += 1
                            else:
                                break

                        if j == 8 and sud_chek[3][j] == 0:
                            if cheking_new(list_4[j], set_ver_9, set_sq_6, set_ver_new_3_9):
                                count_chek += 1
                            else:
                                break

                    # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                    # то строка возможна (переходим к след. строке):
                    if count_chek != el_i4:
                        continue

                    # Занесение доп. верт. строки 4:
                    set_ver_new_4_1.add(list_4[0])
                    set_ver_new_4_2.add(list_4[1])
                    set_ver_new_4_3.add(list_4[2])
                    set_ver_new_4_4.add(list_4[3])
                    set_ver_new_4_5.add(list_4[4])
                    set_ver_new_4_6.add(list_4[5])
                    set_ver_new_4_7.add(list_4[6])
                    set_ver_new_4_8.add(list_4[7])
                    set_ver_new_4_9.add(list_4[8])

                    # Занесение доп. квадр. строки 4:
                    set_sq_new_4.add(list_4[0])
                    set_sq_new_4.add(list_4[1])
                    set_sq_new_4.add(list_4[2])

                    set_sq_new_5.add(list_4[3])
                    set_sq_new_5.add(list_4[4])
                    set_sq_new_5.add(list_4[5])

                    set_sq_new_6.add(list_4[6])
                    set_sq_new_6.add(list_4[7])
                    set_sq_new_6.add(list_4[8])

                    # --------------------------------------------------------------------
                    # Строка 5
                    for i_5 in (list_comb_5):
                        # Создание 2 доп. вертик. строки 5:
                        set_ver_new_5_1 = set()
                        set_ver_new_5_2 = set()
                        set_ver_new_5_3 = set()
                        set_ver_new_5_4 = set()
                        set_ver_new_5_5 = set()
                        set_ver_new_5_6 = set()
                        set_ver_new_5_7 = set()
                        set_ver_new_5_8 = set()
                        set_ver_new_5_9 = set()

                        # Создание 2 доп. квадр. строки 5:
                        set_sq_new_2_4 = set()
                        set_sq_new_2_5 = set()
                        set_sq_new_2_6 = set()

                        el_i5 = 0
                        for j_5 in range(9):
                            if sud_chek[4][j_5] == 0:
                                sud[4][j_5] = i_5[el_i5]
                                el_i5 += 1

                        list_5 = sud[4]

                        # Объединяем СЕТЫ
                        set_ver_new_4_1.update(set_ver_new_3_1)
                        set_ver_new_4_2.update(set_ver_new_3_2)
                        set_ver_new_4_3.update(set_ver_new_3_3)
                        set_ver_new_4_4.update(set_ver_new_3_4)
                        set_ver_new_4_5.update(set_ver_new_3_5)
                        set_ver_new_4_6.update(set_ver_new_3_6)
                        set_ver_new_4_7.update(set_ver_new_3_7)
                        set_ver_new_4_8.update(set_ver_new_3_8)
                        set_ver_new_4_9.update(set_ver_new_3_9)

                        count_chek = 0
                        for j in range(9):
                            # проверка, что числа нет в вертикали и квадранте + доп.
                            if j == 0 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_1, set_sq_4, set_ver_new_4_1,
                                               set_sq_new_4):
                                    count_chek += 1
                                else:
                                    break

                            if j == 1 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_2, set_sq_4, set_ver_new_4_2,
                                               set_sq_new_4):
                                    count_chek += 1
                                else:
                                    break

                            if j == 2 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_3, set_sq_4, set_ver_new_4_3,
                                               set_sq_new_4):
                                    count_chek += 1
                                else:
                                    break

                            if j == 3 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_4, set_sq_5, set_ver_new_4_4,
                                               set_sq_new_5):
                                    count_chek += 1
                                else:
                                    break

                            if j == 4 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_5, set_sq_5, set_ver_new_4_5,
                                               set_sq_new_5):
                                    count_chek += 1
                                else:
                                    break

                            if j == 5 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_6, set_sq_5, set_ver_new_4_6,
                                               set_sq_new_5):
                                    count_chek += 1
                                else:
                                    break

                            if j == 6 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_7, set_sq_6, set_ver_new_4_7,
                                               set_sq_new_6):
                                    count_chek += 1
                                else:
                                    break

                            if j == 7 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_8, set_sq_6, set_ver_new_4_8,
                                               set_sq_new_6):
                                    count_chek += 1
                                else:
                                    break

                            if j == 8 and sud_chek[4][j] == 0:
                                if cheking_new(list_5[j], set_ver_9, set_sq_6, set_ver_new_4_9,
                                               set_sq_new_6):
                                    count_chek += 1
                                else:
                                    break

                        # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                        # то строка возможна (переходим к след. строке):
                        if count_chek != el_i5:
                            continue

                        # Занесение доп. верт. строки 5:
                        set_ver_new_5_1.add(list_5[0])
                        set_ver_new_5_2.add(list_5[1])
                        set_ver_new_5_3.add(list_5[2])
                        set_ver_new_5_4.add(list_5[3])
                        set_ver_new_5_5.add(list_5[4])
                        set_ver_new_5_6.add(list_5[5])
                        set_ver_new_5_7.add(list_5[6])
                        set_ver_new_5_8.add(list_5[7])
                        set_ver_new_5_9.add(list_5[8])

                        # Занесение доп. квадр. строки 5:
                        set_sq_new_2_4.add(list_5[0])
                        set_sq_new_2_4.add(list_5[1])
                        set_sq_new_2_4.add(list_5[2])

                        set_sq_new_2_5.add(list_5[3])
                        set_sq_new_2_5.add(list_5[4])
                        set_sq_new_2_5.add(list_5[5])

                        set_sq_new_2_6.add(list_5[6])
                        set_sq_new_2_6.add(list_5[7])
                        set_sq_new_2_6.add(list_5[8])

                        # --------------------------------------------------------------------
                        # Строка 6
                        for i_6 in (list_comb_6):
                            # Создание доп. вертик. строки 6:
                            set_ver_new_6_1 = set()
                            set_ver_new_6_2 = set()
                            set_ver_new_6_3 = set()
                            set_ver_new_6_4 = set()
                            set_ver_new_6_5 = set()
                            set_ver_new_6_6 = set()
                            set_ver_new_6_7 = set()
                            set_ver_new_6_8 = set()
                            set_ver_new_6_9 = set()

                            el_i6 = 0
                            for j_6 in range(9):
                                if sud_chek[5][j_6] == 0:
                                    sud[5][j_6] = i_6[el_i6]
                                    el_i6 += 1

                            list_6 = sud[5]

                            # Объединяем СЕТЫ
                            set_ver_new_5_1.update(set_ver_new_4_1)
                            set_ver_new_5_2.update(set_ver_new_4_2)
                            set_ver_new_5_3.update(set_ver_new_4_3)
                            set_ver_new_5_4.update(set_ver_new_4_4)
                            set_ver_new_5_5.update(set_ver_new_4_5)
                            set_ver_new_5_6.update(set_ver_new_4_6)
                            set_ver_new_5_7.update(set_ver_new_4_7)
                            set_ver_new_5_8.update(set_ver_new_4_8)
                            set_ver_new_5_9.update(set_ver_new_4_9)

                            set_sq_new_2_4.update(set_sq_new_4)
                            set_sq_new_2_5.update(set_sq_new_5)
                            set_sq_new_2_6.update(set_sq_new_6)

                            count_chek = 0
                            for j in range(9):
                                # проверка, что числа нет в вертикали и квадранте + доп.
                                if j == 0 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_1, set_sq_4, set_ver_new_5_1,
                                                   set_sq_new_2_4):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 1 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_2, set_sq_4, set_ver_new_5_2,
                                                   set_sq_new_2_4):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 2 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_3, set_sq_4, set_ver_new_5_3,
                                                   set_sq_new_2_4):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 3 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_4, set_sq_5, set_ver_new_5_4,
                                                   set_sq_new_2_5):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 4 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_5, set_sq_5, set_ver_new_5_5,
                                                   set_sq_new_2_5):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 5 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_6, set_sq_5, set_ver_new_5_6,
                                                   set_sq_new_2_5):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 6 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_7, set_sq_6, set_ver_new_5_7,
                                                   set_sq_new_2_6):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 7 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_8, set_sq_6, set_ver_new_5_8,
                                                   set_sq_new_2_6):
                                        count_chek += 1
                                    else:
                                        break

                                if j == 8 and sud_chek[5][j] == 0:
                                    if cheking_new(list_6[j], set_ver_9, set_sq_6, set_ver_new_5_9,
                                                   set_sq_new_2_6):
                                        count_chek += 1
                                    else:
                                        break

                            # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                            # то строка возможна (переходим к след. строке):
                            if count_chek != el_i6:
                                continue

                            # Занесение доп. верт. строки 6:
                            set_ver_new_6_1.add(list_6[0])
                            set_ver_new_6_2.add(list_6[1])
                            set_ver_new_6_3.add(list_6[2])
                            set_ver_new_6_4.add(list_6[3])
                            set_ver_new_6_5.add(list_6[4])
                            set_ver_new_6_6.add(list_6[5])
                            set_ver_new_6_7.add(list_6[6])
                            set_ver_new_6_8.add(list_6[7])
                            set_ver_new_6_9.add(list_6[8])

                            # --------------------------------------------------------------------
                            # Строка 7
                            for i_7 in (list_comb_7):
                                # Создание  доп. вертик. строки 7:
                                set_ver_new_7_1 = set()
                                set_ver_new_7_2 = set()
                                set_ver_new_7_3 = set()
                                set_ver_new_7_4 = set()
                                set_ver_new_7_5 = set()
                                set_ver_new_7_6 = set()
                                set_ver_new_7_7 = set()
                                set_ver_new_7_8 = set()
                                set_ver_new_7_9 = set()

                                # Создание доп. квадр.:
                                set_sq_new_7 = set()
                                set_sq_new_8 = set()
                                set_sq_new_9 = set()

                                el_i7 = 0
                                for j_7 in range(9):
                                    if sud_chek[6][j_7] == 0:
                                        sud[6][j_7] = i_7[el_i7]
                                        el_i7 += 1

                                list_7 = sud[6]

                                # Объединяем СЕТЫ
                                set_ver_new_6_1.update(set_ver_new_5_1)
                                set_ver_new_6_2.update(set_ver_new_5_2)
                                set_ver_new_6_3.update(set_ver_new_5_3)
                                set_ver_new_6_4.update(set_ver_new_5_4)
                                set_ver_new_6_5.update(set_ver_new_5_5)
                                set_ver_new_6_6.update(set_ver_new_5_6)
                                set_ver_new_6_7.update(set_ver_new_5_7)
                                set_ver_new_6_8.update(set_ver_new_5_8)
                                set_ver_new_6_9.update(set_ver_new_5_9)

                                count_chek = 0
                                for j in range(9):
                                    # проверка, что числа нет в вертикали и квадранте + доп.
                                    if j == 0 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_1, set_sq_7, set_ver_new_6_1):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 1 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_2, set_sq_7, set_ver_new_6_2):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 2 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_3, set_sq_7, set_ver_new_6_3):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 3 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_4, set_sq_8, set_ver_new_6_4):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 4 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_5, set_sq_8, set_ver_new_6_5):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 5 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_6, set_sq_8, set_ver_new_6_6):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 6 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_7, set_sq_9, set_ver_new_6_7):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 7 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_8, set_sq_9, set_ver_new_6_8):
                                            count_chek += 1
                                        else:
                                            break

                                    if j == 8 and sud_chek[6][j] == 0:
                                        if cheking_new(list_7[j], set_ver_9, set_sq_9, set_ver_new_6_9):
                                            count_chek += 1
                                        else:
                                            break

                                # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                                # то строка возможна (переходим к след. строке):
                                if count_chek != el_i7:
                                    continue

                                # Занесение доп. верт. строки 7:
                                set_ver_new_7_1.add(list_7[0])
                                set_ver_new_7_2.add(list_7[1])
                                set_ver_new_7_3.add(list_7[2])
                                set_ver_new_7_4.add(list_7[3])
                                set_ver_new_7_5.add(list_7[4])
                                set_ver_new_7_6.add(list_7[5])
                                set_ver_new_7_7.add(list_7[6])
                                set_ver_new_7_8.add(list_7[7])
                                set_ver_new_7_9.add(list_7[8])

                                # Занесение доп. квадр. :
                                set_sq_new_7.add(list_7[0])
                                set_sq_new_7.add(list_7[1])
                                set_sq_new_7.add(list_7[2])

                                set_sq_new_8.add(list_7[3])
                                set_sq_new_8.add(list_7[4])
                                set_sq_new_8.add(list_7[5])

                                set_sq_new_9.add(list_7[6])
                                set_sq_new_9.add(list_7[7])
                                set_sq_new_9.add(list_7[8])

                                # --------------------------------------------------------------------
                                # Строка 8
                                for i_8 in (list_comb_8):

                                    # Создание доп. вертик. строки 8:
                                    set_ver_new_8_1 = set()
                                    set_ver_new_8_2 = set()
                                    set_ver_new_8_3 = set()
                                    set_ver_new_8_4 = set()
                                    set_ver_new_8_5 = set()
                                    set_ver_new_8_6 = set()
                                    set_ver_new_8_7 = set()
                                    set_ver_new_8_8 = set()
                                    set_ver_new_8_9 = set()

                                    # Создание доп. квадр. :
                                    set_sq_new_2_7 = set()
                                    set_sq_new_2_8 = set()
                                    set_sq_new_2_9 = set()

                                    el_i8 = 0
                                    for j_8 in range(9):
                                        if sud_chek[7][j_8] == 0:
                                            sud[7][j_8] = i_8[el_i8]
                                            el_i8 += 1

                                    list_8 = sud[7]

                                    # Объединяем СЕТЫ
                                    set_ver_new_7_1.update(set_ver_new_6_1)
                                    set_ver_new_7_2.update(set_ver_new_6_2)
                                    set_ver_new_7_3.update(set_ver_new_6_3)
                                    set_ver_new_7_4.update(set_ver_new_6_4)
                                    set_ver_new_7_5.update(set_ver_new_6_5)
                                    set_ver_new_7_6.update(set_ver_new_6_6)
                                    set_ver_new_7_7.update(set_ver_new_6_7)
                                    set_ver_new_7_8.update(set_ver_new_6_8)
                                    set_ver_new_7_9.update(set_ver_new_6_9)

                                    count_chek = 0
                                    for j in range(9):
                                        # проверка, что числа нет в вертикали и квадранте + доп.
                                        if j == 0 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_1, set_sq_7, set_ver_new_7_1,
                                                           set_sq_new_7):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 1 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_2, set_sq_7, set_ver_new_7_2,
                                                           set_sq_new_7):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 2 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_3, set_sq_7, set_ver_new_7_3,
                                                           set_sq_new_7):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 3 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_4, set_sq_8, set_ver_new_7_4,
                                                           set_sq_new_8):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 4 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_5, set_sq_8, set_ver_new_7_5,
                                                           set_sq_new_8):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 5 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_6, set_sq_8, set_ver_new_7_6,
                                                           set_sq_new_8):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 6 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_7, set_sq_9, set_ver_new_7_7,
                                                           set_sq_new_9):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 7 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_8, set_sq_9, set_ver_new_7_8,
                                                           set_sq_new_9):
                                                count_chek += 1
                                            else:
                                                break

                                        if j == 8 and sud_chek[7][j] == 0:
                                            if cheking_new(list_8[j], set_ver_9, set_sq_9, set_ver_new_7_9,
                                                           set_sq_new_9):
                                                count_chek += 1
                                            else:
                                                break

                                    # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                                    # то строка возможна (переходим к след. строке):
                                    if count_chek != el_i8:
                                        continue

                                    # Занесение доп. верт. строки 8:
                                    set_ver_new_8_1.add(list_8[0])
                                    set_ver_new_8_2.add(list_8[1])
                                    set_ver_new_8_3.add(list_8[2])
                                    set_ver_new_8_4.add(list_8[3])
                                    set_ver_new_8_5.add(list_8[4])
                                    set_ver_new_8_6.add(list_8[5])
                                    set_ver_new_8_7.add(list_8[6])
                                    set_ver_new_8_8.add(list_8[7])
                                    set_ver_new_8_9.add(list_8[8])

                                    # Занесение доп. квадр. строки 8:
                                    set_sq_new_2_7.add(list_8[0])
                                    set_sq_new_2_7.add(list_8[1])
                                    set_sq_new_2_7.add(list_8[2])

                                    set_sq_new_2_8.add(list_8[3])
                                    set_sq_new_2_8.add(list_8[4])
                                    set_sq_new_2_8.add(list_8[5])

                                    set_sq_new_2_9.add(list_8[6])
                                    set_sq_new_2_9.add(list_8[7])
                                    set_sq_new_2_9.add(list_8[8])

                                    # --------------------------------------------------------------------
                                    # Строка 9
                                    for i_9 in (list_comb_9):

                                        el_i9 = 0
                                        for j_9 in range(9):
                                            if sud_chek[8][j_9] == 0:
                                                sud[8][j_9] = i_9[el_i9]
                                                el_i9 += 1

                                        list_9 = sud[8]

                                        # Объединяем СЕТЫ
                                        set_ver_new_8_1.update(set_ver_new_7_1)
                                        set_ver_new_8_2.update(set_ver_new_7_2)
                                        set_ver_new_8_3.update(set_ver_new_7_3)
                                        set_ver_new_8_4.update(set_ver_new_7_4)
                                        set_ver_new_8_5.update(set_ver_new_7_5)
                                        set_ver_new_8_6.update(set_ver_new_7_6)
                                        set_ver_new_8_7.update(set_ver_new_7_7)
                                        set_ver_new_8_8.update(set_ver_new_7_8)
                                        set_ver_new_8_9.update(set_ver_new_7_9)

                                        set_sq_new_2_7.update(set_sq_new_7)
                                        set_sq_new_2_8.update(set_sq_new_8)
                                        set_sq_new_2_9.update(set_sq_new_9)

                                        count_chek = 0
                                        for j in range(9):
                                            # проверка, что числа нет в вертикали и квадранте + доп.
                                            if j == 0 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_1, set_sq_7, set_ver_new_8_1,
                                                               set_sq_new_2_7):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 1 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_2, set_sq_7, set_ver_new_8_2,
                                                               set_sq_new_2_7):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 2 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_3, set_sq_7, set_ver_new_8_3,
                                                               set_sq_new_2_7):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 3 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_4, set_sq_8, set_ver_new_8_4,
                                                               set_sq_new_2_8):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 4 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_5, set_sq_8, set_ver_new_8_5,
                                                               set_sq_new_2_8):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 5 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_6, set_sq_8, set_ver_new_8_6,
                                                               set_sq_new_2_8):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 6 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_7, set_sq_9, set_ver_new_8_7,
                                                               set_sq_new_2_9):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 7 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_8, set_sq_9, set_ver_new_8_8,
                                                               set_sq_new_2_9):
                                                    count_chek += 1
                                                else:
                                                    break

                                            if j == 8 and sud_chek[8][j] == 0:
                                                if cheking_new(list_9[j], set_ver_9, set_sq_9, set_ver_new_8_9,
                                                               set_sq_new_2_9):
                                                    count_chek += 1
                                                else:
                                                    break

                                        # если всех 9 чисел нет в 9 вертикалях и 3 квадрантах с учетом предыдущих строк,
                                        # то строка возможна (переходим к след. строке):
                                        if count_chek != el_i9:
                                            continue

                                        # Количество перебраных вариантов:
                                        num += 1

                                        # проверка внутри 9-го цикла, если ОК, то ключ = 1
                                        if cheking_hor(sud):
                                            if cheking_ver(sud):
                                                if cheking_sq(sud):
                                                    key = 1

                                        # ключ = 1, то выход
                                        if key == 1:
                                            break
                                    if key == 1:
                                        break
                                if key == 1:
                                    break
                            if key == 1:
                                break
                        if key == 1:
                            break
                    if key == 1:
                        break
                if key == 1:
                    break
            if key == 1:
                break
        if key == 1:
            break

    # Печать Судоку
    if key == 1:
        out_sud(sud)
    else:
        print("Решение не найдено.")

    end = datetime.datetime.now()
    print('Затрачено времени: ', end - start)
