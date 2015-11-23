import re

filename = 'regex_sum_202320.txt'
text = open(filename).read()
numbers = re.findall('[0-9]+', text)
total = sum(int(n) for n in numbers)

print total