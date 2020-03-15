#   Calculate the size of all non-folders in a folder
import os
input_folder = 'Resources/07. Folder Size/'
file_structure = os.walk(input_folder)
folder_list = {folder[0] : folder[2]  for folder in file_structure}

file_list = []
for folder in folder_list:
    for file in folder_list[folder]:
        file_list.append(folder + '/' + file)

#print(*file_list, sep = '\n')

file_sizes = [os.stat(file).st_size for file in file_list]
result = sum(file_sizes) / 1024
print(result)
open('output/07 Folder size.txt', 'w').write(str(result))
