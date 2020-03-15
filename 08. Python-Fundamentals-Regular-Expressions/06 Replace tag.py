#   Replace the <a> html tag
import re
pattern = re.compile(r'<a[ ]?href=\"(?P<url>http[s]?://[a-z]+\.[a-z]+)\">(?P<name>(\w+\s*)+)</a>')

while True:
    user_input = input()
    if user_input == 'end':
        break

    match = re.finditer(pattern, user_input)
    result = user_input

    for instance in match:
        replaced_str = f'[URL href="{instance.group("url")}"]{instance.group("name")}[/URL]'
        result = result.replace(instance.group(), replaced_str)

    print(result)
