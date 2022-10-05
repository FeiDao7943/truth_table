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


class gate_reff:

    def check_input(self, a, b, c, d, num):
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

    def not_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 1)
        if check:
            if a == 0:
                return 1
            if a == 1:
                return 0

    def and_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
        if check:
            for i in (a, b, c, d):
                if i != -1:
                    if i == 0:
                        return 0
                        break
            return 1

    def nand_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
        if check:
            for i in (a, b, c, d):
                if i != -1:
                    if i == 0:
                        return 1
                        break
            return 0

    def or_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
        if check:
            for i in (a, b, c, d):
                if i != -1:
                    if i == 1:
                        return 1
                        break
            return 0

    def nor_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
        if check:
            for i in (a, b, c, d):
                if i != -1:
                    if i == 1:
                        return 0
                        break
            return 1

    def xor_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
        if check:
            std = a
            for i in (a, b, c, d):
                if i != -1:
                    if i != std:
                        return 1
                        break
            return 0

    def xnor_gate(self, a=-1, b=-1, c=-1, d=-1):
        check = self.check_input(a, b, c, d, 2)
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
    cal = gate_reff()
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
        final_result = function_expression(digital1, digital2, digital3, digital4, var_dig, cal)
        print(final_result)


def value_list_cal(gate, dig1, dig2, dig3, dig4, minus1, minus2, minus3, minus4):
    value_list = np.zeros(50)
    value_list[0] = gate(dig1, dig2)
    value_list[1] = gate(minus1, dig2)
    value_list[2] = gate(dig1, minus2)

    value_list[3] = gate(dig1, dig3)
    value_list[4] = gate(minus1, dig3)
    value_list[5] = gate(dig1, minus3)

    value_list[6] = gate(dig1, dig4)
    value_list[7] = gate(minus1, dig4)
    value_list[8] = gate(dig1, minus4)

    value_list[9] = gate(dig2, dig3)
    value_list[10] = gate(minus2, dig3)
    value_list[11] = gate(dig2, minus3)

    value_list[12] = gate(dig2, dig4)
    value_list[13] = gate(minus2, dig4)
    value_list[14] = gate(dig2, minus4)

    value_list[15] = gate(dig3, dig4)
    value_list[16] = gate(minus3, dig4)
    value_list[17] = gate(dig3, minus4)

    value_list[18] = gate(dig1, dig2, dig3)
    value_list[19] = gate(dig1, dig2, minus3)
    value_list[20] = gate(dig1, minus2, dig3)
    value_list[21] = gate(minus1, dig2, dig3)
    value_list[22] = gate(dig1, minus2, minus3)
    value_list[23] = gate(minus1, dig2, minus3)
    value_list[24] = gate(minus1, minus2, dig3)
    value_list[25] = gate(minus1, minus2, minus3)

    value_list[26] = gate(dig1, dig2, dig4)
    value_list[27] = gate(dig1, dig2, minus4)
    value_list[28] = gate(dig1, minus2, dig4)
    value_list[29] = gate(minus1, dig2, dig4)
    value_list[30] = gate(dig1, minus2, minus4)
    value_list[31] = gate(minus1, dig2, minus4)
    value_list[32] = gate(minus1, minus2, dig4)
    value_list[33] = gate(minus1, minus2, minus4)

    value_list[34] = gate(dig1, dig3, dig4)
    value_list[35] = gate(dig1, dig3, minus4)
    value_list[36] = gate(dig1, minus3, dig4)
    value_list[37] = gate(minus1, dig3, dig4)
    value_list[38] = gate(dig1, minus3, minus4)
    value_list[39] = gate(minus1, dig3, minus4)
    value_list[40] = gate(minus1, minus3, dig4)
    value_list[41] = gate(minus1, minus3, minus4)

    value_list[42] = gate(dig2, dig3, dig4)
    value_list[43] = gate(dig2, dig3, minus4)
    value_list[44] = gate(dig2, minus3, dig4)
    value_list[45] = gate(minus2, dig3, dig4)
    value_list[46] = gate(dig2, minus3, minus4)
    value_list[47] = gate(minus2, dig3, minus4)
    value_list[48] = gate(minus2, minus3, dig4)
    value_list[49] = gate(minus2, minus3, minus4)
    return value_list


def function_expression(digi1, digi2, digi3, digi4, var, gate_class):
    if var == 4:
        dig1 = digi1
        dig2 = digi2
        dig3 = digi3
        dig4 = digi4

        minus1 = gate_class.not_gate(dig1)
        minus2 = gate_class.not_gate(dig2)
        minus3 = gate_class.not_gate(dig3)
        minus4 = gate_class.not_gate(dig4)

    if var == 3:
        dig1 = digi2
        dig2 = digi3
        dig3 = digi4
        dig4 = 0

        minus1 = gate_class.not_gate(dig1)
        minus2 = gate_class.not_gate(dig2)
        minus3 = gate_class.not_gate(dig3)
        minus4 = 0

    if var == 2:
        dig1 = digi3
        dig2 = digi4
        dig3 = 0
        dig4 = 0

        minus1 = gate_class.not_gate(dig1)
        minus2 = gate_class.not_gate(dig2)
        minus3 = 0
        minus4 = 0
    list_dig = ['12', '1_2', '12_', '13', '1_3', '13_', '14', '1_4', '14_',
                '23', '2_3', '23_', '24', '2_4', '24_', '34', '3_4', '34_',
                '123', '123_', '12_3', '1_23', '12_3_', '1_23_', '1_2_3', '1_2_3_',
                '124', '124_', '12_4', '1_24', '12_4_', '1_24_', '1_2_4', '1_2_4_',
                '134', '134_', '13_4', '1_34', '13_4_', '1_34_', '1_3_4', '1_3_4_',
                '234', '234_', '23_4', '2_34', '23_4_', '2_34_', '2_3_4', '2_3_4_',
                ]

    for gates_name in ('and', 'or', 'nand', 'nor', 'xor', 'xnor'):
        if gates_name == 'and':
            gate = gate_class.and_gate
        if gates_name == 'or':
            gate = gate_class.and_gate
        if gates_name == 'nand':
            gate = gate_class.and_gate
        if gates_name == 'nor':
            gate = gate_class.and_gate
        if gates_name == 'xor':
            gate = gate_class.and_gate
        if gates_name == 'xnor':
            gate = gate_class.and_gate

        value_list = value_list_cal(gate, dig1, dig2, dig3, dig4,
                                    minus1, minus2, minus3, minus4)
        value_num = 0
        for var_name in list_dig:
            globals()[gates_name + var_name] = int(value_list[value_num])
            value_num += 1

    ''' Enter the expression of tne circuit function
        1.Ignore the red-highlight warning, variables' references produced during the running process
        2.The '_'behind the digit means the 'not'
        3.The digits follow the name of gates should increase gradually
            e.g. "and12_3", but not "and13_2"
        4.Not more than 3 digits behind the name of gate, if beyond
            it is possible to combine with functions of gate
        5.Not nore than 4 variables plug in function of gate, if beyond
            it is possible to combine with functions of gate
        6.Use variable 'f' to return the final output
        7.The variable of function 'main' in rwp 395 means the number of total variables
            remember change the correct number just in 2, 3 or 4 before runing
    '''
    # Expression begin
    tem1 = or_gate(and124, and1_3_4_, and1_34, and12_4_)
    f = or_gate(tem1, and1_2)

    # Ignore the red-highlight warning, variables' references produced during the running process
    # Expression end
    return f


if __name__ == "__main__":
    '''
    The variable of function 'main' in rwp 395 means the number of total variables
        remember change the correct number just in 2, 3 or 4 before runing
    '''
    main(4)
