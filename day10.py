import dijkstra

file = open("day10.txt", "r")
input_string = file.read()
map_list = input_string.split("\n")

#remove the blank line at the end
map_list.pop()

graph = {}

height = len(map_list)
width = len(map_list[0])

zeros = []
nines = []

for i in range(height * width):
    y = i // width
    x = i % width
    value = int(map_list[y][x])

    graph[i] = {}

    #up
    if (y > 0) and (int(map_list[y-1][x]) == value + 1):
        new_i = (y-1)*width + x
        graph[i][new_i] = 1

    #down
    if (y < height - 1) and (int(map_list[y+1][x]) == value + 1):
        new_i = (y+1)*width + x
        graph[i][new_i] = 1

    #left
    if (x > 0) and (int(map_list[y][x-1]) == value + 1):
        new_i = y*width + x-1
        graph[i][new_i] = 1

    #right
    if (x < width - 1) and (int(map_list[y][x+1]) == value + 1):
        new_i = y*width + x+1
        graph[i][new_i] = 1

    if value == 0:
        zeros.append(i)
    elif value == 9:
        nines.append(i)

total = 0
total2 = 0
for start in zeros:
    for end in nines:
        paths = dijkstra.find_all_paths(graph, start, end)
        if paths != None and len(paths) > 0:
            total += 1
            total2 += len(paths)

print(total)
print(total2)
