file = open('recipes.txt', encoding='utf8')
cookbook = {}

for lines in file.read().splitlines():
    if (lines.isdigit() is not True) and (' | ' not in lines) and (lines != ''):
        cookbook[lines] = []
        curr_recipe = lines
    if ' | ' in lines:
        curr_ingredient = lines.split(' | ')
        curr_ingredient = {'ingredient_name': curr_ingredient[0], 'quantity': curr_ingredient[1], 'measure': curr_ingredient[2]}
        cookbook[curr_recipe].append(curr_ingredient)

print(cookbook)