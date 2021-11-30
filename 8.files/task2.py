files_list = ['1.txt', '2.txt', '3.txt']
files_dict = {}

for files in files_list:
    with open(files, encoding='utf8') as file:
        files_dict[len(file.read().splitlines())] = files

files_len = []
files_len = list(files_dict.keys())
files_len.sort()

with open('output.txt', 'w', encoding='utf8') as file_w:
    file_w.flush()
    file_w.mode = 'a'
    for length in files_len:
        with open(files_dict[length], encoding='utf8') as file_r:
            output = files_dict[length] + f"\n{length}\n" + file_r.read() + '\n'
            file_w.write(output)