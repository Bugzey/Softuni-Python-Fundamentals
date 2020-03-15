#   Count fish and their characteristics
import re

class Fish:
    def __init__(self, image, head, body, tail):
        self.image = image
        if head == '\'':
            self.status = 'Awake'
        elif head == '-':
            self.status = 'Asleep'
        elif head == 'x':
            self.status = 'Dead'

        self.body = len(body) * 2
        self.tail = len(tail) * 2

        self.tail_type = 'Long' if self.tail > 5*2 else 'Medium' if self.tail > 1*2 else 'Short' if self.tail == 1*2 else 'None'
        self.body_type = 'Long' if self.body > 10*2 else 'Medium' if self.body > 5*2 else 'Short'

    def __str__(self):
        line1 = self.image
        line2 = f'  Tail type: {self.tail_type}' + (f' ({self.tail} cm)' if self.tail_type != 'None' else '')
        line3 = f'  Body type: {self.body_type} ({self.body} cm)'
        line4 = f'  Status: {self.status}'
        result = '\n'.join([line1, line2, line3, line4])
        return(result)
        

pattern_fish = re.compile(r'(?P<tail>>*)<(?P<body>\(+)(?P<head>[\'-x])>')
fish_list = []


user_input = input()
match_fish = re.finditer(pattern_fish, user_input)

for match in match_fish:
    fish_image = match.group()
    fish_head = match.group('head')
    fish_body = match.group('body')
    fish_tail = match.group('tail')
    cur_fish = Fish(fish_image, fish_head, fish_body, fish_tail)
    fish_list.append(cur_fish)

if len(fish_list) == 0:
    print('No fish found.')
else:
    for nr in range(len(fish_list)):
        fish_nr = str(nr + 1)
        cur_fish = str(fish_list[nr])
        result = f'Fish {fish_nr}: {cur_fish}'
        print(result)
