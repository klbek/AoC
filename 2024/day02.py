report_list = list()
with open(r'2024\input02.txt', encoding='utf-8') as input_file:
    for line in input_file:
        report = line.strip().split(' ')
        num_report = [int(val) for val in report]
        report_list.append(num_report)

output = 0 # number of safe values

for number_list in report_list:
    difflist = list()
    # for idx in range(len(number_list) - 1):    
    #     result = number_list[idx] - number_list[idx + 1]
    #     difflist.append(result)
    for idx, num in enumerate(number_list[:-1]):    
        result = num - number_list[idx + 1]
        difflist.append(result)
    # print(difflist)

    row = True # safe
    increasing = difflist[0] < 0
    for a in difflist:
        if a == 0:
            row = False
            break
        elif increasing and a < -3:
            row = False
            break
        elif increasing and a > 0:
            row = False
            break
        elif not increasing and a > 3:
            row = False
            break
        elif not increasing and a < 0:
            row = False
            break
    if row:
        output += 1
print(output)






