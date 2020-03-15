#   Something, something words with digit N times
import re

pattern_word = re.compile(r'\b\w+\b')
pattern_sentence = re.compile(r'^[A-Z].*[\.\!\?]$')

criteria = list(input())
letter, times = criteria[0], int(criteria[1])
result = []

while True:
    user_input = input()
    if user_input == 'end':
        break

    sentence = re.search(pattern_sentence, user_input)

    if sentence is not None:
        words = re.finditer(pattern_word, sentence.group())
        for word in words:
            cur_word = word.group()
            letter_count = cur_word.count(letter)
            if letter_count == times:
                result.append(cur_word)

print(*result, sep = ', ')
