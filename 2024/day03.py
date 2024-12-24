import re

with open('2024/input03.txt', 'r', encoding='utf-8') as input_file:
    file = input_file.read()

result_list = list()

regex_pattern = 'mul\(\d{1,5},\d{1,5}\)'
regex_list = re.findall(regex_pattern, string=file)

for regex in regex_list:
    regex = regex.replace('mul(', '').replace(')', '').split(',')
    result = int(regex[0]) * int(regex[1])
    result_list.append(result)
    
print(sum(result_list))