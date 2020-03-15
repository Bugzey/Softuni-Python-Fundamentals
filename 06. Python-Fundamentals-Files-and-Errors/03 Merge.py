#   Merge two files
file_1 = open('Resources/03. Merge Files/FileOne.txt', 'r').read().split('\n')
file_2 = open('Resources/03. Merge Files/FileTwo.txt', 'r').read().split('\n')

out_file = file_1 + file_2

open('output/03.txt', 'w').write('\n'.join(out_file))
