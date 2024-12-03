file = open("day2.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")
valid_count = 0
valid_count_damp = 0

def isValid(report):
    # set up a copy of the reports where the levels are sorted increasing
    report_inc = report.copy()
    report_inc.sort(reverse=False)
    # set up a copy of the reports where the levels are sorted decreasing
    report_dec = report.copy()
    report_dec.sort(reverse=True)
    
    valid = True
    # checking for valid gaps between consecutive levels
    for j in range(1, len(report)):
        curr_level = report[j]
        prev_level = report[j-1]

        curr_diff = abs(curr_level - prev_level)
        valid = valid and (curr_diff >= 1)
        valid = valid and (curr_diff <= 3)

    # checking for increasing/decreasing (comparing to sorted copies)
    inc_test = (report == report_inc)
    dec_test = (report == report_dec)

    valid = valid and (inc_test or dec_test)

    return valid

def isValidDamp(report):
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)

        if isValid(new_report):
            return True

    return False

# set up the reports (inc converting to integers)
report_list = []
for curr_item in input_list:
    curr_report = curr_item.split(" ")

    curr_report_int = []
    for curr_level in curr_report:
        curr_report_int.append(int(curr_level))
        
    report_list.append(curr_report_int)

for curr_report in report_list:
    if isValid(curr_report):
        valid_count += 1
        valid_count_damp += 1
    elif isValidDamp(curr_report):
        valid_count_damp += 1

print(valid_count)
print(valid_count_damp)
