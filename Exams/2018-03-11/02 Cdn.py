#   Add lectures to local vide storage servers
import re

pattern_time = re.compile(r'(\d+)h(\d{0,2})m')

lectures = []
server = []

while True:
    user_input = input()
    if 'scrape' in user_input.lower():
        break

    user_input = user_input.split(';')
    if len(user_input) != 4:
        continue

    user_input = list(map(lambda x: x.split(':'), user_input))

    if user_input is None:
        continue

    cur_lecture = {key: value for key, value in user_input}

    match_duration = re.match(pattern_time, cur_lecture['duration']) 
    cur_duration = {
        'hour': int(match_duration.group(1)),
        'minute': int(match_duration.group(2))
    }
    cur_lecture['duration'] = cur_duration

    if len(server) == 0:
        cur_server = {
            'hour': cur_duration['hour'],
            'minute': cur_duration['minute']
        }
        cur_lecture['server'] = 1
        server.append(cur_server)
    else:
        cur_server = server[-1]

        new_minutes = (cur_server['minute'] + cur_duration['minute']) % 60
        new_hours = cur_server['hour'] + cur_duration['hour'] + (cur_server['minute'] + cur_duration['minute']) // 60

        if new_hours > 10 or (new_hours == 10 and new_minutes > 0):
            cur_server = {
                'hour': cur_duration['hour'],
                'minute': cur_duration['minute']
            }
            server.append(cur_server)
        else:
            server[-1]['hour'] = new_hours
            server[-1]['minute'] = new_minutes
    
    cur_lecture['server'] = len(server)
    lectures.append(cur_lecture)

command, arg1, arg2 = user_input.split(' ')[0:3]
scrape = filter(lambda x: x[arg1] == arg2, lectures)

total_minutes = 0
total_hours = 0

for lecture in list(scrape):
    total_hours += lecture['duration']['hour'] + (total_minutes + lecture['duration']['minute']) // 60
    total_minutes = (total_minutes + lecture['duration']['minute']) % 60
    url = f"https://streamcdn{lecture['server']}.softuni.bg/course={lecture['course']}&lecture={lecture['lecture']}&trainer={lecture['trainer']}"
    print(url)

total_minutes_str = f'0{str(total_minutes)}' if total_minutes < 10 else str(total_minutes)
total_hours_str = f'0{str(total_hours)}' if total_hours < 10 else str(total_hours)

result = f'total duration: {total_hours_str}:{total_minutes_str}:00'
print(result)

