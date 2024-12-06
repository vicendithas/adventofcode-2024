file = open("day5.txt", "r")
input_string = file.read()
[rules_string, updates_string] = input_string.split("\n\n")

rules_list = rules_string.split("\n")
updates_list = updates_string.split("\n")

#remove the blank line at the end
updates_list.pop()

#set up rules arrays
rules_arr = []
for rule in rules_list:
    curr_rule = rule.split("|")
    rules_arr.append(list(map(int,curr_rule)))

#set up updates array
updates_arr = []
for update in updates_list:
    curr_update = update.split(",")
    updates_arr.append(list(map(int,curr_update)))

def rules_sort(pages):
    #base case
    if len(pages) <= 1: return pages

    #general case
    index = len(pages) // 2
    middle_val = pages[index]
    left = []
    right = []

    for i in range(len(pages)):
        curr_val = pages[i]
        if curr_val != middle_val:
            for rule in rules_arr:
                if (curr_val in rule) and (middle_val in rule):
                    if rule[0] == middle_val:
                        right.append(curr_val)
                    else:
                        left.append(curr_val)

    output = []
    output.extend(rules_sort(left))
    output.extend([middle_val])
    output.extend(rules_sort(right))

    return output        

total = 0
total2 = 0
for update in updates_arr:
    update_ord = rules_sort(update)

    index = len(update) // 2
    if update == update_ord:
        total += update[index]
    else:
        total2 += update_ord[index]

print(total)
print(total2)
