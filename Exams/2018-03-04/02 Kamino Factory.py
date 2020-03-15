#   Regex fun
import re
pattern = re.compile(r'(1+)')
sequences = []

line_length = int(input())

while True:
    line = input()
    if line == 'Clone them!':
        break

    to_match = line.replace('!', '')
    match_iter = re.finditer(pattern, to_match)
    
    cur_max_subsequence = 0
    cur_min_index = 0
    cur_sum = sum([int(letter) for letter in to_match])
    out_line = line.replace('!', ' ')
    cur_index = len(sequences) + 1

    for match in match_iter:
        cur_seq_len = len(match.group())
        if cur_seq_len > cur_max_subsequence:
            cur_max_subsequence = cur_seq_len
            cur_min_index = match.start()
    
    #result = {'index' : cur_index, 'sequence' : out_line, 'max_subsequence' : cur_max_subsequence, 'min_index' : cur_min_index, 'sum' : cur_sum}
    result = (cur_index, out_line, cur_max_subsequence, cur_min_index, cur_sum)
    sequences.append(result)

#sequences.sort(key = lambda x: (-x['max_subsequence'], x['min_index'], -x['sum']))
sequences.sort(key = lambda x: (-x[2], x[3], -x[4]))
result = sequences[0]

#line1 = f"Best DNA sample {result['index']} with sum: {result['sum']}."
#line2 = f"{result['sequence']}"
line1 = f"Best DNA sample {result[0]} with sum: {result[4]}."
line2 = f"{result[2]}"

print(line1)
print(line2)
