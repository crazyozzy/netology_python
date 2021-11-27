ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

set_list = set()

for sets in ids.values():
       # set_list.append(set(sets))
       set_list = set_list | set(sets)

print(list(set_list))