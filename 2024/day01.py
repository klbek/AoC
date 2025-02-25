left_list = list()
right_list = list()

with open(r'2024\input01.txt', encoding='utf-8') as input_file:
    file = input_file.readlines()
    for line in file:
        sep_line = line.strip().split('   ')
        left_list.append(int(sep_line[0]))
        right_list.append(int(sep_line[1]))

left_list.sort()
right_list.sort()

distance_list = list()
similarity_list = list()

for i in range(len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    distance_list.append(distance)

    count = right_list.count(left_list[i])
    result = left_list[i] * count
    similarity_list.append(result)   

print(f'Distance: {sum(distance_list)}')
print(f'Similarity score: {sum(similarity_list)}')

