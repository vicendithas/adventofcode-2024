file = open("day7.txt", "r")
input_string = file.read()
equ_list = input_string.split("\n")

#remove the blank line at the end
equ_list.pop()

#set up equation array
equ_arr = []

for line in equ_list:
    curr_equ = []
    line_list = line.split(": ")
    result = int(line_list[0])
    curr_equ.append(result)

    oper_str = line_list[1].split(" ")
    for oper in oper_str:
        curr_equ.append(int(oper))

    equ_arr.append(curr_equ)

def toBase(num, base, digits):
    num_str = ""
    for i in range(digits):
        num_str = str(num%base) + num_str
        num = num//base
    return num_str

total = 0
for curr_equ in equ_arr:
    target_result = curr_equ[0]
    curr_operands = curr_equ[1:]
    num_operands = len(curr_operands)

    #set up all iterations of operations represented in binary
    #0-add, 1-multiply
    operations = range(2**(num_operands-1))

    for co in operations:
        curr_result = curr_operands[0]
        co_bin = toBase(co, 2, num_operands-1)

        for i in range(1, num_operands):
            if co_bin[i-1] == "0":
                curr_result += curr_operands[i]
            elif co_bin[i-1] == "1":
                curr_result *= curr_operands[i]
            else:
                print("This shoudln't be possible")

        if curr_result == target_result:
            total += target_result
            break

print(total)

total2 = 0
for curr_equ in equ_arr:
    target_result = curr_equ[0]
    curr_operands = curr_equ[1:]
    num_operands = len(curr_operands)

    #set up all iterations of operations represented in binary
    #0-add, 1-multiply, 2-concatenation
    operations = range(3**(num_operands-1))

    for co in operations:
        curr_result = curr_operands[0]
        co_bin = toBase(co, 3, num_operands-1)

        for i in range(1, num_operands):
            if co_bin[i-1] == "0":
                curr_result += curr_operands[i]
            elif co_bin[i-1] == "1":
                curr_result *= curr_operands[i]
            elif co_bin[i-1] == "2":
                curr_result = int(str(curr_result) + str(curr_operands[i]))
            else:
                print("This shoudln't be possible")

        if curr_result == target_result:
            total2 += target_result
            break

print(total2)
