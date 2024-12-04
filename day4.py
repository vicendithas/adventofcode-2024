file = open("day4.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")
xmas_count = 0
xmas_count2 = 0

word_search = []
for item in input_list:
    if item != "":
        curr_list = list(item)
        word_search.append(curr_list)

x_size = len(word_search[0])
y_size = len(word_search)

# XMAS Search
x_min = 3
y_min = 3
x_max = x_size - 3 - 1
y_max = y_size - 3 - 1

for x in range(x_size):
    for y in range(y_size):
        up = (y >= y_min)
        down = (y <= y_max)
        left = (x >= x_min)
        right = (x <= x_max)

        curr_letter = word_search[y][x]

        if curr_letter == "X":
            #up
            if up               and word_search[y-1][ x ] + word_search[y-2][ x ] + word_search[y-3][ x ] == "MAS": xmas_count += 1
            #down
            if down             and word_search[y+1][ x ] + word_search[y+2][ x ] + word_search[y+3][ x ] == "MAS": xmas_count += 1
            #left
            if left             and word_search[ y ][x-1] + word_search[ y ][x-2] + word_search[ y ][x-3] == "MAS": xmas_count += 1
            #right
            if right            and word_search[ y ][x+1] + word_search[ y ][x+2] + word_search[ y ][x+3] == "MAS": xmas_count += 1
            #up-left
            if up and left      and word_search[y-1][x-1] + word_search[y-2][x-2] + word_search[y-3][x-3] == "MAS": xmas_count += 1
            #up-right
            if up and right     and word_search[y-1][x+1] + word_search[y-2][x+2] + word_search[y-3][x+3] == "MAS": xmas_count += 1
            #down-left
            if down and left    and word_search[y+1][x-1] + word_search[y+2][x-2] + word_search[y+3][x-3] == "MAS": xmas_count += 1
            #down-right
            if down and right   and word_search[y+1][x+1] + word_search[y+2][x+2] + word_search[y+3][x+3] == "MAS": xmas_count += 1

print(xmas_count)

# X-MAS Search
x_min = 1
y_min = 1
x_max = x_size - 1 - 1
y_max = y_size - 1 - 1

for x in range(x_size):
    for y in range(y_size):
        up = (y >= y_min)
        down = (y <= y_max)
        left = (x >= x_min)
        right = (x <= x_max)

        curr_letter = word_search[y][x]

        if (curr_letter == "A") and up and down and left and right:
            word1 = word_search[y-1][x-1] + curr_letter + word_search[y+1][x+1]
            word2 = word_search[y+1][x-1] + curr_letter + word_search[y-1][x+1]
            test1 = (word1 == "MAS") or (word1 == "SAM")
            test2 = (word2 == "MAS") or (word2 == "SAM")
            if test1 and test2: xmas_count2 += 1

print(xmas_count2)
