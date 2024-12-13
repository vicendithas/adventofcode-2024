file = open("day11.txt", "r")
input_string = file.read()
stone_list = input_string.split("\n")

#remove the blank line at the end
stone_arr_str = stone_list[0].split(" ")

def addToDict(my_dict, key, amount):
    if key in my_dict:
        my_dict[key] += amount
    else:
        my_dict[key] = amount

#create a dictionary of each stone value (key) and how many there are (value)
stone_dict = {}
for stone in stone_arr_str:
    value = int(stone)
    addToDict(stone_dict, value, 1)

for blink in range(75):
    new_stone_dict = {}
    for stone in stone_dict:
        if stone == 0:
            addToDict(new_stone_dict, 1, stone_dict[stone])
        elif len(str(stone))%2 == 0:
            stone_str = str(stone)
            mid = len(stone_str)//2
            left = int(stone_str[:mid])
            right = int(stone_str[mid:])
            addToDict(new_stone_dict, left, stone_dict[stone])
            addToDict(new_stone_dict, right, stone_dict[stone])
        else:
            addToDict(new_stone_dict, stone*2024, stone_dict[stone])

    stone_dict = new_stone_dict

    if blink == 24:
        total = 0
        for stone in stone_dict.keys():
            total += stone_dict[stone]
        print(total)

total2 = 0
for stone in stone_dict.keys():
    total2 += stone_dict[stone]

print(total2)
