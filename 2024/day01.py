left_list = list()
right_list = list()

with open(r'2024\input01.txt', encoding='utf-8') as input_file:
    file = input_file.readlines()
    for line in file:
        sep_line = line.strip().split('   ')
        left_list.append(sep_line[0])
        right_list.append(sep_line[1])

left_list.sort()
right_list.sort()

distance_list = list()
for i in range(len(left_list)):
    distance = abs(int(left_list[i]) - int(right_list[i]))
    distance_list.append(distance)
   

sum_distance = sum(distance_list)
print(sum_distance)