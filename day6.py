import copy

file = open("day6.txt", "r")
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

#initialize starting position and direction
#0-up, 1-down, 2-left, 3-right
start_x = -1
start_y = -1
start_direction = -1
curr_x = -1
curr_y = -1
direction = -1

for y in range(height):
    for x in range(width):
        if map_arr[y][x] == "^":
            start_x = x
            start_y = y
            start_direction = 0
            curr_x = x
            curr_y = y
            direction = 0
        elif map_arr[y][x] == "v":
            start_x = x
            start_y = y
            start_direction = 1
            curr_x = x
            curr_y = y
            direction = 1
        elif map_arr[y][x] == "<":
            start_x = x
            start_y = y
            start_direction = 2
            curr_x = x
            curr_y = y
            direction = 2
        elif map_arr[y][x] == ">":
            start_x = x
            start_y = y
            start_direction = 3
            curr_x = x
            curr_y = y
            direction = 3

map_arr1 = copy.deepcopy(map_arr)
travel = True
while travel:
    #up
    if direction == 0:
        if curr_y == 0:
            travel = False
            map_arr1[curr_y][curr_x] = "X"
        elif map_arr1[curr_y - 1][curr_x] == "#":
            direction = 3
        else:
            map_arr1[curr_y][curr_x] = "X"
            curr_y -= 1
            map_arr1[curr_y][curr_x] = "^"
            
    #down
    elif direction == 1:
        if curr_y == height - 1:
            travel = False
            map_arr1[curr_y][curr_x] = "X"
        elif map_arr1[curr_y + 1][curr_x] == "#":
            direction = 2
        else:
            map_arr1[curr_y][curr_x] = "X"
            curr_y += 1
            map_arr1[curr_y][curr_x] = "v"

    #left
    elif direction == 2:
        if curr_x == 0:
            travel = False
            map_arr1[curr_y][curr_x] = "X"
        elif map_arr1[curr_y][curr_x - 1] == "#":
            direction = 0
        else:
            map_arr1[curr_y][curr_x] = "X"
            curr_x -= 1
            map_arr1[curr_y][curr_x] = "<"

    #right
    elif direction == 3:
        if curr_x == width - 1:
            travel = False
            map_arr1[curr_y][curr_x] = "X"
        elif map_arr1[curr_y][curr_x + 1] == "#":
            direction = 1
        else:
            map_arr1[curr_y][curr_x] = "X"
            curr_x += 1
            map_arr1[curr_y][curr_x] = ">"

total = 0
visited = []
for y in range(height):
    for x in range(width):
        if map_arr1[y][x] == "X":
            total += 1

            obst = [y, x]
            if (obst not in visited) and (obst != [start_y, start_x]):
                visited.append(obst)

print(total)

total2 = 0
for obst in visited:
    curr_x = start_x
    curr_y = start_y
    direction = start_direction
    
    #copy original map and place new obstacle
    map_arr2 = copy.deepcopy(map_arr)
    map_arr2[obst[0]][obst[1]] = "#"

    #set up visited counter for each square
    visit_count = []
    for y in range(height):
        curr_line = []
        for x in range(width):
            curr_line.append(0)
        visit_count.append(curr_line)

    travel = True
    loop = False
    while travel and not loop:
        #up
        if direction == 0:
            if curr_y == 0:
                travel = False
                map_arr2[curr_y][curr_x] = "X"
            elif map_arr2[curr_y - 1][curr_x] == "#":
                direction = 3
            else:
                map_arr2[curr_y][curr_x] = "X"
                visit_count[curr_y][curr_x] += 1
                if visit_count[curr_y][curr_x] >= 5:
                    loop = True
                curr_y -= 1
                map_arr2[curr_y][curr_x] = "^"
                
        #down
        elif direction == 1:
            if curr_y == height - 1:
                travel = False
                map_arr2[curr_y][curr_x] = "X"
            elif map_arr2[curr_y + 1][curr_x] == "#":
                direction = 2
            else:
                map_arr2[curr_y][curr_x] = "X"
                visit_count[curr_y][curr_x] += 1
                if visit_count[curr_y][curr_x] >= 5:
                    loop = True
                curr_y += 1
                map_arr2[curr_y][curr_x] = "v"

        #left
        elif direction == 2:
            if curr_x == 0:
                travel = False
                map_arr2[curr_y][curr_x] = "X"
            elif map_arr2[curr_y][curr_x - 1] == "#":
                direction = 0
            else:
                map_arr2[curr_y][curr_x] = "X"
                visit_count[curr_y][curr_x] += 1
                if visit_count[curr_y][curr_x] >= 5:
                    loop = True
                curr_x -= 1
                map_arr2[curr_y][curr_x] = "<"

        #right
        elif direction == 3:
            if curr_x == width - 1:
                travel = False
                map_arr2[curr_y][curr_x] = "X"
            elif map_arr2[curr_y][curr_x + 1] == "#":
                direction = 1
            else:
                map_arr2[curr_y][curr_x] = "X"
                visit_count[curr_y][curr_x] += 1
                if visit_count[curr_y][curr_x] >= 5:
                    loop = True
                curr_x += 1
                map_arr2[curr_y][curr_x] = ">"

    if loop:
        total2 += 1

print(total2)
