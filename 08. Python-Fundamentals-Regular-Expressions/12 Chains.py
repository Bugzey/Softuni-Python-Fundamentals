#   Get a url with an alphabet-shift cypher hidden between <p> tags
import re
def de_cypher(string):
    chars = [ord(char) for char in string]
    chars = list(enumerate(chars))
    ref_a = ord('a')
    ref_n = ord('n')
    ref_z = ord('z')
    ref_diff = ref_n - ref_a
    char_range = range(ref_a, ref_z + 1)

    result = []
    for char in chars:
        cur_index = char[0]
        cur_char = char[1]

        if cur_char not in char_range:
            result.append(string[cur_index])
        elif cur_char in range(ref_a, ref_n):
            cur_result = chr(cur_char + ref_diff)
            result.append(cur_result)
        elif cur_char in range(ref_n, ref_z + 1):
            cur_result = chr(cur_char - ref_diff)
            result.append(cur_result)
        else:
            raise ValueError('Something happened.')

    result = ''.join(result)
    return(result)

lines = []

pattern_ptags = re.compile(r'<p>(?P<value>[^<>]+)<\/p>')
pattern_odd_chars = re.compile(r'[^a-z0-9]+')

user_input = input()
match_iter = re.finditer(pattern_ptags, user_input)

for match in match_iter:
    cur_match = match.group('value')
    result = re.sub(pattern_odd_chars, ' ', cur_match)
    lines.append(result)

result = [de_cypher(line) for line in lines]
print(*result, sep = '')
