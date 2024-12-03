file = open("day1.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")
curr_total = 0
simil_score = 0

left_list = []
right_list = []

for i in range(len(input_list)):
    curr_item = input_list[i].split(",")
    left_list.append(int(curr_item[0]))
    right_list.append(int(curr_item[1]))

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    curr_total += abs(left_list[i] - right_list[i])
    simil_score += left_list[i] * right_list.count(left_list[i])

print(curr_total)
print(simil_score)
