def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, (list, tuple, set)):
            sum_ += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                if isinstance(key, (int, str)):
                    sum_ += len(str(key)) if isinstance(key, str) else key
                if isinstance(value, (int, str)):
                    sum_ += len(str(value)) if isinstance(value, str) else value
                elif isinstance(value, (list, tuple, set, dict)):
                    sum_ += calculate_structure_sum(value)
    return sum_


data_structure = [
[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
