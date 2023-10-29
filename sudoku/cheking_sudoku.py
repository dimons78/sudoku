
# Проверка по горизонтали
def cheking_hor(sud):
    key_hor = 0

    for i in range(9):
        hor_sum = 0
        set_hor = set()

        for j in range(9):
            hor_sum += sud[i][j]
            set_hor.add(sud[i][j])

        if hor_sum == 45 and len(set_hor) == 9:
            key_hor += 1
        else:
            break

    if key_hor == 9:
        return True
    else:
        return False


# Проверка по вертикали
def cheking_ver(sud):
    key_ver = 0

    for j in range(9):
        ver_sum = 0
        set_ver = set()

        for i in range(9):
            ver_sum += sud[i][j]
            set_ver.add(sud[i][j])

        if ver_sum == 45 and len(set_ver) == 9:
            key_ver += 1
        else:
            break

    if key_ver == 9:
        return True
    else:
        return False


# Проверка по квадратам 3*3
def cheking_sq(sud):
    key_sq = 0

    for i_sq in range(3):
        sq_sum = 0
        set_sq = set()

        for i in range(3):
            for j in range(i_sq*3, i_sq*3 + 3):
                sq_sum += sud[i][j]
                set_sq.add(sud[i][j])

        if sq_sum == 45 and len(set_sq) == 9:
            key_sq += 1
        else:
            return False

    for i_sq in range(3):
        sq_sum = 0
        set_sq = set()

        for i in range(3, 6):
            for j in range(i_sq*3, i_sq*3 + 3):
                sq_sum += sud[i][j]
                set_sq.add(sud[i][j])
        if sq_sum == 45 and len(set_sq) == 9:
            key_sq += 1
        else:
            return False

    for i_sq in range(3):
        sq_sum = 0
        set_sq = set()

        for i in range(6, 9):
            for j in range(i_sq*3, i_sq*3 + 3):
                sq_sum += sud[i][j]
                set_sq.add(sud[i][j])

        if sq_sum == 45 and len(set_sq) == 9:
            key_sq += 1
        else:
            return False

    if key_sq == 9:
        return True
    else:
        return False


# Печать Судоку
def out_sud(sud):
    for i in range(9):
        print(sud[i])



# Проверка с учетом предыдущих строк
def cheking_new(elem, set_1, set_2, set_3, set_4 = set()):
    if elem not in set_1 | set_2 | set_3 | set_4:
        return True
    else:
        return False

