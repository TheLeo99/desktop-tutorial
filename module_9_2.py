first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string) for string in first_strings if len(string) >= 5]

second_result = [(f_s, s_s) for f_s in first_strings for s_s in second_strings if len(f_s) == len(s_s)]

third_result = {x : len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)