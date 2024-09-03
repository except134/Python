first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
third_result = {s: len(s) for s in first_strings + second_strings if not len(s)%2}

third_result[0] = 0
print(third_result)

print(first_result)
print(second_result)
print(third_result)
