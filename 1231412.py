calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
   qwe = str(string)
   result = len(qwe), qwe.upper(), qwe.lower()
   count_calls()
   return result

def is_contains (string,list_to_search):
    wasd = str(string)
    zxc = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string.lower():
            result = True
            break
        else:
            result = False
            continue
    return result
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
