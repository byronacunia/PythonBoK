import re
file = "regex_sum_1441846.txt"
try:
    fhandle = open(file)
    print(sum([int(num) for num in re.findall('[0-9]+', fhandle.read())]))
except:
    print(f"The file: {file} do not exist")