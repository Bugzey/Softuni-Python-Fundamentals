#   Group files per extension
import os, shutil
class File:
    def __init__(self, name, path):
        self.name, self.path = name, path
        dots = [index for index, letter in enumerate(name) if letter == '.']
        self.extension = name[dots[-1] + 1:]
    def __str__(self):
        result = self.path + ':' + self.name + ':' + self.extension
        return(result)

in_folder = 'Resources/08. Re-Directory/'
in_files = os.walk(in_folder)
file_list = []

for cur_folder in in_files:
    for cur_file in cur_folder[2]:
        file_list.append(File(cur_file, cur_folder[0]))

result = {}
for cur_file in file_list:
    if cur_file.extension not in result.keys():
        result[cur_file.extension] = []
    result[cur_file.extension].append(cur_file)

try:
    os.mkdir('output/08 Re-directory/')
except FileExistsError:
    pass

for extension in result.keys():
    new_dir = 'output/08 Re-directory/' + extension + 's'
    try:
        os.mkdir(new_dir)
    except FileExistsError:
        pass
    
    for cur_file in result[extension]:
        cur_source = cur_file.path + '/' + cur_file.name
        cur_dest = new_dir + '/'
        shutil.copy2(cur_source, cur_dest)
