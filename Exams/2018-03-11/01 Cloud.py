#   Calculate cloud storage cash requirements
from math import ceil

price = {
    'server': 2, # usd/hour
    'data': 0.5, # usd/hour
    'host': 10 # usd/month
}
capacity = {
    'server': 50, # users
    'data': 500 # megabytes
}

budget = float(input())
users = int(input())
data = int(input()) # gigabytes
hosts = int(input())
uptime = float(input())

cost_user = ceil(users / capacity['server']) * price['server'] * 24 * 30
cost_data = ceil(data * 1000 / capacity['data']) * price['data'] * 24 * 30
cost_hosts = hosts * price['host']

cost_all = (cost_user + cost_data + cost_hosts) * uptime / 100

if budget >= cost_all:
    leftover = budget - cost_all
    result = f'Clouds Ahoy! Monthly cost: ${cost_all:.2f} (${leftover:.2f} leftover)'
else:
    more = cost_all - budget
    result = f'Stay Grounded! Monthly cost: ${cost_all:.2f} (Need ${more:.2f} more)'

print(result)
