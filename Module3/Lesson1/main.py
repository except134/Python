calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    ret = (len(string), string.upper(), string.lower())
    count_calls()
    return ret

def is_contains (string, list_to_search):
    ret = False
    for i in range(len(list_to_search)):
        if string .lower() in list_to_search[i].lower() or list_to_search[i].lower() in string.lower():
            ret = True
            break
    count_calls()
    return ret

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



