#   Parse the dude's travelling time
#   input1: time of departure
#   input2: nr. of steps
#   input3: time per step

import datetime

start_time = datetime.datetime.strptime(input(), '%H:%M:%S')
steps = int(input())
time_per_step = int(input())

total_seconds = (time_per_step * steps) % (24*60*60)
travel_time = datetime.timedelta(seconds = total_seconds)
end_time = start_time + travel_time

result = datetime.datetime.strftime(end_time, '%H:%M:%S')

print(f'Time Arrival: {result}')
