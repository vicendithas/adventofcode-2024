import re

file = open("day3.txt", "r")
input_string = file.read()

regex = r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"
mul_list = ["".join(x) for x in re.findall(regex, input_string)]

total = 0
total_alt = 0
enabled = True
for mul_item in mul_list:
    if mul_item == "do()":
        enabled = True
    elif mul_item == "don't()":
        enabled = False
    else:
        mul_item2 = mul_item.strip("mul()")
        mul_item3 = mul_item2.split(",")
        curr_mul = int(mul_item3[0]) * int(mul_item3[1])
        total += curr_mul

        if enabled:
            total_alt += curr_mul

print(total)
print(total_alt)
