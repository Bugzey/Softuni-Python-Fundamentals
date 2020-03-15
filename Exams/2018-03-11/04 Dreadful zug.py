#   Implement a discount card and ticketing system
class Card:
    def __init__(self,first_name, last_name, number):
        self.number = number
        self.first_name, self.last_name = first_name, last_name
        self.is_valid = sum([int(digit) for digit in number]) % 7 == 0

class Ticket:
    def __init__(self, first_name, last_name, destination, card = None):
        self.first_name, self.last_name = first_name, last_name
        self.destination, self.card = destination, card

        raw_price = sum([ord(letter) for letter in destination]) / 100

        if card is not None:
            discount = 0.5 if card.is_valid else 0
        else:
            discount = 0

        self.price = raw_price * (1 - discount)

    def __str__(self):
        if self.card is not None:
            line2 = f' (using card {str(self.card.number)})'
        else:
            line2 = ''
        result = f'--{self.destination}: {self.price:.2f}lv' + line2
        return(result)

cards = {} 
passengers = {}

n_cards = int(input())
for index in range(n_cards):
    first_name, last_name, number = input().split(' ')
    cards[number] = Card(first_name, last_name, number)

while True:
    user_input = input()
    if user_input == 'time to leave!':
        break

    command, first_name, last_name, destination, number = user_input.split(' ')

    if number not in cards.keys():
        cur_card = Card(first_name, last_name, number)
        if not cur_card.is_valid:
            cur_card = None
            print(f'card {number} is not valid!')
        else:
            cards[number] = cur_card
            print(f'issuing card {number}')

    else:
        cur_card = cards[number]
        card_is_foreign = first_name != cur_card.first_name or last_name != cur_card.last_name

        if card_is_foreign:
            print(f'card {number} already exists for another passenger!')
            cur_card = None

    cur_ticket = Ticket(first_name, last_name, destination, cur_card)

    cur_passenger = f'{first_name} {last_name}'

    if cur_passenger not in passengers.keys():
        passengers[cur_passenger] = [cur_ticket]
    else:
        passengers[cur_passenger].append(cur_ticket)

passenger_sums = [(name, sum([ticket.price for ticket in tickets])) for name, tickets in passengers.items()]
passenger_sums.sort(key = lambda x: -x[1])

for passenger in passenger_sums:
    cur_passenger = passenger[0]
    total_sum = passenger[1]

    tickets = [(ticket.price, str(ticket)) for ticket in passengers[cur_passenger]]
    tickets.sort(key = lambda x: -x[0])

    print(f'{cur_passenger}:')
    print(*[ticket[1] for ticket in tickets], sep = '\n')
    print(f'total: {total_sum:.2f}lv')
