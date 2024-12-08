from itertools import combinations

file = open("day8.txt", "r")
input_string = file.read()
map_list = input_string.split("\n")

#remove the blank line at the end
map_list.pop()

#set up map array
map_arr = []
for line in map_list:
    map_arr.append(list(line))

height = len(map_arr)
width = len(map_arr[0])

#find all antenna frequencies and their positions
ant_pos = []
for y in range(height):
    for x in range(width):
        curr_char = map_arr[y][x]
        if curr_char != ".":
            curr_line = []
            curr_line.append(curr_char)
            curr_line.append(y)
            curr_line.append(x)
            ant_pos.append(curr_line)

#find all unique frequencies
unique_freq = ""
for ant in ant_pos:
    curr_char = ant[0]
    if curr_char not in unique_freq:
        unique_freq = unique_freq + curr_char

#set up antinode array
an_map = []
for y in range(height):
    curr_line = []
    for x in range(width):
        curr_line.append(".")
    an_map.append(curr_line)

#find all antinote positions
for curr_char in unique_freq:
    curr_freq_pos = []
    for curr_pos in ant_pos:
        if curr_pos[0] == curr_char:
            curr_freq_pos.append(curr_pos[1:])

    pos_comb = list(combinations(curr_freq_pos, 2))

    for curr_pos_comb in pos_comb:
        y1 = curr_pos_comb[0][0]
        x1 = curr_pos_comb[0][1]
        y2 = curr_pos_comb[1][0]
        x2 = curr_pos_comb[1][1]

        y_diff = y2 - y1
        x_diff = x2 - x1

        an1_y = y1 - y_diff
        an1_x = x1 - x_diff
        an2_y = y2 + y_diff
        an2_x = x2 + x_diff

        an1_y_test = (an1_y >= 0) and (an1_y < height)
        an1_x_test = (an1_x >= 0) and (an1_x < height)
        an2_y_test = (an2_y >= 0) and (an2_y < height)
        an2_x_test = (an2_x >= 0) and (an2_x < height)

        if an1_y_test and an1_x_test:
            an_map[an1_y][an1_x] = "#"

        if an2_y_test and an2_x_test:
            an_map[an2_y][an2_x] = "#"

total = 0
for y in range(height):
    for x in range(width):
        if an_map[y][x] == "#":
            total += 1

print(total)

#set up antinode array
an_map2 = []
for y in range(height):
    curr_line = []
    for x in range(width):
        curr_line.append(".")
    an_map2.append(curr_line)

#find all antinote positions
for curr_char in unique_freq:
    curr_freq_pos = []
    for curr_pos in ant_pos:
        if curr_pos[0] == curr_char:
            curr_freq_pos.append(curr_pos[1:])

    pos_comb = list(combinations(curr_freq_pos, 2))

    for curr_pos_comb in pos_comb:
        y1 = curr_pos_comb[0][0]
        x1 = curr_pos_comb[0][1]
        y2 = curr_pos_comb[1][0]
        x2 = curr_pos_comb[1][1]

        y_diff = y2 - y1
        x_diff = x2 - x1

        an1_y = y1
        an1_x = x1
        an2_y = y2
        an2_x = x2

        while (an1_y >= 0) and (an1_y < height) and (an1_x >= 0) and (an1_x < height):
            an_map2[an1_y][an1_x] = "#"
            an1_y = an1_y - y_diff
            an1_x = an1_x - x_diff

        while (an2_y >= 0) and (an2_y < height) and (an2_x >= 0) and (an2_x < height):
            an_map2[an2_y][an2_x] = "#"
            an2_y = an2_y + y_diff
            an2_x = an2_x + x_diff         

total2 = 0
for y in range(height):
    for x in range(width):
        if an_map2[y][x] == "#":
            total2 += 1

print(total2)
