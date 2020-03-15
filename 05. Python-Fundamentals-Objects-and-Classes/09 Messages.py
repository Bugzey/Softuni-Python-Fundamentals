#   Users, messages and message history
class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.message_history = []

    def receive_message(self, message):
        if type(message) != Message:
            raise ValueError("Message not of class Message.")
        self.message_history.append(message)

class Message:
    def __init__(self, sender, content):
        self.sender, self.content = sender, content

    def print_message(self, position = 'left'):
        if position == 'left':
            result = self.sender + ': ' + self.content
        elif position == 'right':
            result = self.content + ' :' +  self.sender
        else:
            result = 'wtf, man?'
        return(result)

def print_history(*users):
    user1_messages = users[0].message_history
    user2_messages = users[1].message_history
    length_messages = max(len(user1_messages), len(user2_messages))
    for message_index in range(length_messages):
        if message_index < len(user1_messages):
            print(user1_messages[message_index].print_message(position = 'left'))
        if message_index < len(user2_messages):
            print(user2_messages[message_index].print_message(position = 'right'))

user_db = {}

while True:
    user_input = input().split()
    if user_input[0] == 'exit':
        user_input = input().split()
        user1 = user_db[user_input[1]]
        user2 = user_db[user_input[0]]
        print_history(user1, user2)
        break

    if user_input[0] == 'register':
        new_user = User(user_name = user_input[1])
        user_db[new_user.user_name] = new_user
        continue

    user_sender = user_input[0]
    user_recipient = user_input[2]
    message_content = ' '.join(user_input[3:])

    cur_message = Message(sender = user_sender, content = message_content)

    try:
        user_db[user_recipient].receive_message(cur_message)
    except KeyError:
        continue
