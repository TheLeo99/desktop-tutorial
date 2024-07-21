calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    string_upper = string.upper()
    for item in list_to_search:
        if string_upper == item.upper():
            return True
    return False


print(string_info('Semantica'))
print(string_info('Shestoff'))
print(is_contains('pink', ['Pink', 'Floyd', 'oLD']))
print(is_contains('car', ['Carbon', 'Scarlet']))
print(calls)
