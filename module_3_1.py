calls = 0

def count_calls():
    global calls
    return (calls)
def string_info(string):
    global calls
    calls = calls + 1
    return(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    global calls
    calls = calls + 1
    for n in range(0, len(list_to_search)):
        if list_to_search[n].lower() == string.lower():
            result = True
        else:
            result = False
    return(result)




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)