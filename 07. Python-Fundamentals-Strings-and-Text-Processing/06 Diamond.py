#   Get garbled string asdf<asdf123>asdf<123dfd>: sum the numbers between <>
user_input = input()

allowed_chars = '1234567890<>'
diamonds = ''.join(filter(lambda l: l in allowed_chars, user_input))

start_index = 0
diamond_carats = []

while start_index < len(diamonds):
    try:
        start_index = diamonds.index('<', start_index)
        end_index = diamonds.index('>', start_index)
        diamond_carats.append(sum([int(letter) for letter in diamonds[start_index + 1:end_index]]))
        start_index = end_index
    except ValueError:
        break
    
if len(diamond_carats) == 0:
    print('Better luck next time')
else:
    print(*[f'Found {carat} carat diamond' for carat in diamond_carats], sep = '\n')
