#   Something about getting lots of commands
import re
pattern_space_around_equal = re.compile(r'(%20|\+)+=|=(%20|\+)+')
pattern_space_other = re.compile(r'(%20|\+)+')
#pattern_kvp = re.compile(r'(^\?)*(?P<key>\b\w+\b)=\s*(?P<value>(http[s]*:\/\/)*[A-Za-z0-9\*\.\-\_\/]+)')
#pattern_kvp = re.compile(r'(^\?$)*(?P<key>\b\w+\b)=\s*(?P<value>(http[s]*:\/\/)*([A-Za-z0-9\*\.\-\_\/]|(?=\1)\ )+)')
pattern_kvp = re.compile(r'(^\?$)*(?P<key>(\w|\ )+)=\s*(?P<value>(http[s]*:\/\/)*([A-Za-z0-9\*\.\-\_\/]|(?=\1)\ )+)')


while True:
    kvps = {}
    user_input = input()
    if user_input == 'END':
        break

    de_whitespaced = re.sub(pattern_space_around_equal, '', user_input)
    de_whitespaced = re.sub(pattern_space_other, ' ', de_whitespaced)
    match_iter = re.finditer(pattern_kvp, de_whitespaced)
    
    for match in match_iter:
        cur_kvp = match.groupdict()
        cur_key = cur_kvp['key']
        cur_value = cur_kvp['value']
        if cur_key not in kvps.keys():
            kvps[cur_key] = [cur_value]
        else:
            kvps[cur_key].append(cur_value)

    result = [f'{key}=[{", ".join(value)}]' for key, value in kvps.items()]
    print(*result, sep='')
