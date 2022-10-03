import numpy as np


def check_input(a, b, c, d, num):
    count = 0
    for i in (a, b, c, d):
        if i != -1:
            count += 1
    if num != 1:
        if count < num:
            print("too less value!")
            exit()
    if num == 1:
        if count > num:
            print("too much value!")
            exit()
    return 1


def not_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 1)
    if check:
        if a == 0:
            return 1
        if a == 1:
            return 0


def and_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        for i in (a, b, c, d):
            if i != -1:
                if i == 0:
                    return 0
                    break
        return 1


def nand_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        for i in (a, b, c, d):
            if i != -1:
                if i == 0:
                    return 1
                    break
        return 0


def or_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        for i in (a, b, c, d):
            if i != -1:
                if i == 1:
                    return 1
                    break
        return 0


def nor_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        for i in (a, b, c, d):
            if i != -1:
                if i == 1:
                    return 0
                    break
        return 1


def xor_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        std = a
        for i in (a, b, c, d):
            if i != -1:
                if i != std:
                    return 1
                    break
        return 0


def xnor_gate(a=-1, b=-1, c=-1, d=-1):
    check = check_input(a, b, c, d, 2)
    if check:
        std = a
        for i in (a, b, c, d):
            if i != -1:
                if i != std:
                    return 0
                    break
        return 1


def binary(nums):
    nums += 1
    if nums > 16:
        print("too much value!")
        exit()
    bin_list = np.zeros(4)
    for number in range(nums):
        for digits in range(5):
            if not number:
                break
            bin_list[3 - digits] = int(number % 2)
            number = (number - (number % 2)) / 2
        # print(bin_list)
    return bin_list[0], bin_list[1], bin_list[2], bin_list[3]


if __name__ == "__main__":
    print("truth table:")
    space_holder = '       '
    print(space_holder, 'a  b  c  d  |  f')
    print(space_holder, "------------|---")
    vir = 4
    max_num = pow(2, vir)
    for i in range(max_num):
        dig1, dig2, dig3, dig4 = binary(i)
        print(space_holder,
              str(int(dig1)), '', str(int(dig2)), '',
              str(int(dig3)), '', str(int(dig4)), '',
              end=' |  ')

        # 输入对应的逻辑电路
        # -------------------------------------------

        tem1 = not_gate(dig1)

        tem2 = nand_gate(tem1, dig2)
        tem3 = xnor_gate(dig3, dig4)

        f = or_gate(tem2, tem3)

        # -------------------------------------------
        print(f)
