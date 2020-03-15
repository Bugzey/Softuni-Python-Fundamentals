#   Sum the ascii codes of a string
user_input = input()
count_which = input()

def is_what_we_seek(letter):
    if count_which == 'LOWERCASE': 
        result = str.islower(letter)
    elif count_which == 'UPPERCASE':
        result = str.isupper(letter)
    return(result)

ascii_codes = sum([ord(letter) for letter in user_input if is_what_we_seek(letter)])
print(f'The total sum is: {ascii_codes}')

