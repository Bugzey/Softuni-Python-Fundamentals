#   Set log ins and track successes failures
users = {}
status_options = ['entry', 'login', 'end']
status = 'entry'
history = {
    'success' : 0,
    'failure' : 0
}

def update_user(user, pw):
    users[user] = hash(pw)
    
def login(user, pw):
    messages = {
        'success' : user + ': logged in successfully',
        'fail' : user + ': login failed'
    }
    if user not in users.keys():
        print(messages['fail'])
        history['failure'] += 1
        return(1)

    if users[user] == hash(pw):
        print(messages['success'])
        history['success'] += 1
        return(0)
    else:
        print(messages['fail'])
        history['failure'] += 1
        return(1)
            

def status_report():
    result = 'unsuccessful login attempts: ' + str(history['failure'])
    print(result)

while True:
    user_input = input().split(' -> ')
    if user_input[0] == 'login':
        status = 'login'
        continue
    elif user_input[0] == 'end':
        status = 'end'
        break
    
    user_name = user_input[0]
    user_pw = user_input[1]

    if status == 'entry':
        update_user(user_name, user_pw)
    elif status == 'login':
        login(user_name, user_pw)

status_report()
