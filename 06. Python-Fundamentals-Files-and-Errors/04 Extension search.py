#   List some files, get given an extension, show files with extension
import os
file_list_raw = os.walk('Resources/04. Filter-Extensions/')
file_list = [item[2] for item in file_list_raw if len(item[2]) != 0]
if len(file_list) == 1 and type(file_list[0]) == list:
    file_list = file_list.pop()
#print(file_list)

search_extension = input()
search_length = len(search_extension)
result = [item for item in file_list if search_extension in item]
print(*result, sep = "\n")
