import numpy as np


def check_input(a, b, c, d, num):
    count = 0
    for i in (a, b, c, d):
        if i != -1:
            count += 1
    if num != 1:
        if count < num:
            print("Too less value!")
            exit()
    if num == 1:
        if count > num:
            print("Too much value!")
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
        print("Too much value!")
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


def main(var_dig):
    if var_dig < 2:
        print('Too less digital!')
        exit()
    if var_dig > 4:
        print('Too much digital!')
        exit()
    print("truth table:")
    space_holder = '       '
    if var_dig == 4:
        print(space_holder, 'a  b  c  d  |  f')
        print(space_holder, "------------|---")
    if var_dig == 3:
        print(space_holder, 'b  c  d  |  f')
        print(space_holder, "---------|---")
    if var_dig == 2:
        print(space_holder, 'c  d  |  f')
        print(space_holder, "------|---")
    var = var_dig
    max_num = pow(2, var)
    for i in range(max_num):
        digital1, digital2, digital3, digital4 = binary(i)
        if var_dig == 4:
            print(space_holder,
                  str(int(digital1)), '', str(int(digital2)), '',
                  str(int(digital3)), '', str(int(digital4)), '',
                  end=' |  ')
        if var_dig == 3:
            print(space_holder,
                  str(int(digital2)), '',
                  str(int(digital3)), '', str(int(digital4)), '',
                  end=' |  ')
        if var_dig == 2:
            print(space_holder,
                  str(int(digital3)), '', str(int(digital4)), '',
                  end=' |  ')
        final_result = function_expression(digital1, digital2,
                                           digital3, digital4,
                                           var_dig)
        print(final_result)


def function_expression(digi1, digi2, digi3, digi4, var):
    if var == 4:
        dig1 = digi1
        dig2 = digi2
        dig3 = digi3
        dig4 = digi4

        minus1 = not_gate(dig1)
        minus2 = not_gate(dig2)
        minus3 = not_gate(dig3)
        minus4 = not_gate(dig4)

    if var == 3:
        dig1 = digi2
        dig2 = digi3
        dig3 = digi4

        minus1 = not_gate(dig1)
        minus2 = not_gate(dig2)
        minus3 = not_gate(dig3)

    if var == 2:
        dig1 = digi3
        dig2 = digi4

        minus1 = not_gate(dig1)
        minus2 = not_gate(dig2)


    # enter the expression of tne circuit function

    tem1 = and_gate(dig1, dig2, dig4)
    tem2 = and_gate(minus1, minus2, minus3)
    tem3 = and_gate(minus1, dig2)
    tem4 = and_gate(minus1, dig3, dig4)
    tem5 = and_gate(dig1, minus2, minus4)

    tem6 = or_gate(tem1, tem2, tem3, tem4)
    f = or_gate(tem6, tem5)
    # --------------------------------------------

    return f


if __name__ == "__main__":
    main(4)

