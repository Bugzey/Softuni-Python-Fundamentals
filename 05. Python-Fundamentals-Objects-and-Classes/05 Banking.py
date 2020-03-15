#   Enter banking info and then print in a specific order
class Account:
    def __init__(self, *tokens):
        self.bank, self.name, self.balance = tokens
        self.balance = float(self.balance)

    def __str__(self):
        result = self.name + ' -> ' + f'{self.balance:.2f}' + ' (' + self.bank + ')'
        return(result)

    def __gt__(self, other):
        greater_balance = self.balance > other.balance
        shorter_bank = len(self.bank) < len(other.bank)

        result = shorter_bank if not greater_balance else greater_balance
        return(result)

user_list = []

while True:
    user_input = input().split(' | ')
    if user_input[0] == 'end':
        break
    
    cur_user = Account(*user_input)
    user_list.append(cur_user)

result = sorted(user_list, reverse = True)
print(*result, sep = "\n")
