def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')
    i = 0
    for string in strings:
        strings_positions[(i, f.tell())] = string
        f.write(string + '\n')
        i += 1
    f.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
