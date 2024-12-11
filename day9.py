file = open("day9.txt", "r")
input_string = file.read()
disk_list = input_string.split("\n")

#remove the blank line at the end
disk_map = disk_list[0]

#set up maps of disk with IDs (one for each part)
disk_map_list = []
disk_map_list2 = []
curr_id = 0
isFile = True
for i in range(len(disk_map)):
    value = int(disk_map[i])

    if isFile:
        for j in range(value):
            disk_map_list.append(curr_id)
            disk_map_list2.append(curr_id)
        curr_id += 1
        isFile = False
    else:
        for j in range(value):
            disk_map_list.append(".")
            disk_map_list2.append(".")
        isFile = True

#move file blocks from the end to the beginning
left = 0
right = len(disk_map_list) - 1

while left < right:
    #find next empty space from the start
    while (disk_map_list[left] != ".") and (left < right):
        left += 1

    #find next file block from the end
    while (disk_map_list[right] == ".") and (left < right):
        right -= 1

    if left < right:
        #print("Replacing index", left, "value", disk_map_list[left], "with index", right, "value", disk_map_list[right])
        disk_map_list[left] = disk_map_list[right]
        disk_map_list[right] = "."

#calculate the checksum
total = 0
for i in range(len(disk_map_list)):
    if disk_map_list[i] != ".":
        total += (i * disk_map_list[i])

print(total)

#find the highest ID in the file
high_id = -1
for value in disk_map_list2:
    if (value != ".") and (value > high_id):
        high_id = value

#move whole files from the end to the beginning (only moving files once)
for curr_id in range(high_id, -1, -1):
    #find position of file on the disk
    file_index = disk_map_list2.index(curr_id)

    #find length of the file
    temp_index = file_index
    file_len = 0
    while (temp_index < len(disk_map_list2)) and (disk_map_list2[temp_index] == curr_id):
        file_len += 1
        temp_index += 1

    #find free space big enough (if it exists)
    found = False
    temp_index = disk_map_list2.index(".")
    free_index = -1
    while (temp_index < file_index) and (not found):
        #find the next free space
        while (temp_index < file_index) and (disk_map_list2[temp_index] != "."):
            temp_index += 1

        #get the length of the free space
        free_len = 0
        while (temp_index < file_index) and (disk_map_list2[temp_index] == "."):
            free_len += 1
            temp_index += 1

        #check if the free space is long enough
        if (free_len >= file_len):
            found = True
            free_index = temp_index - free_len

    #move the file if free space was found
    if found:
        #put the file in the free space area and clear out the old file location
        for i in range(file_len):
            disk_map_list2[free_index + i] = curr_id
            disk_map_list2[file_index + i] = "."

#calculate the checksum
total2 = 0
for i in range(len(disk_map_list2)):
    if disk_map_list2[i] != ".":
        total2 += (i * disk_map_list2[i])

print(total2)
