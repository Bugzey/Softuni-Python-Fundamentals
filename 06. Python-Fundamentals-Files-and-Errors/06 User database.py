#   Users and logins
from hashlib import sha256
class User:
    def __init__(self, username, password = None, password_hash = None):
        if password == None and password_hash == None:
            raise ValueError('Error password or password_hash must be given.')
        self.username = username
        if password_hash == None:
            self.password_hash = sha256(password.encode()).hexdigest()
        else:
            self.password_hash = password_hash

    def login(self, new_password):
        new_password = sha256(new_password.encode()).hexdigest()
        if new_password == self.password_hash:
            return True
        else:
            return False

    def save_to_disk(self, file = 'output/06 Users.txt'):
        file_line = self.username + ' ' + self.password_hash + '\n'
        open(file, 'a').write(file_line)

def write_db_file():
    for user in user_list.values():
        user.save_to_disk()

user_list = {}
logged_in_user = ''
db_file = 'output/06 Users.txt'
try:
    old_users = open(db_file, 'r').read().split('\n')
    old_users = [user for user in old_users if user != '']
    for line in old_users:
        user, password_hash = line.split(' ')
        user_list[user] = User(user, password_hash = password_hash)

except FileNotFoundError:
    pass

while True:
    user_input = input().split(' ')

    if user_input[0] == 'exit':
        write_db_file()
        break

    if user_input[0] == 'register':
        user, password, repeat_password = user_input[1:]
        if user in user_list.keys():
            print('The given username already exists.')
        elif password == repeat_password:
            cur_user = User(user, password)
            user_list[user] = cur_user
        else:
            print('The password you entered is incorrect.')

        continue

    if user_input[0] == 'login':
        if logged_in_user != '':
            print('There is already a logged in user.')
        else:
            user, password = user_input[1:]
            try:
                login_success = user_list[user].login(password)
            except KeyError:
                print('There is no user with the given username.')
                continue

            if login_success:
                logged_in_user = user
            else:
                print('The password you entered is incorrect.')
        continue

    if user_input[0] == 'logout':
        if logged_in_user != '':
            logged_in_user = ''
        else:
            print('There is no currently logged in user.')
        continue

