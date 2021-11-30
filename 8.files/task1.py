file = open('recipes.txt', encoding='utf8')
cookbook = {}

def get_shop_list_by_dishes(cookbook, dishes, person_count):
    output_ing = {}
    for dish in dishes:
        for ing in cookbook[dish]:
            if ing['ingredient_name'] not in output_ing.keys():
                output_ing[ing['ingredient_name']] = {'measure' : ing['measure'], 'quantity' : ing['quantity'] * person_count}
            else:
                output_ing[ing['ingredient_name']]['quantity'] = output_ing[ing['ingredient_name']]['quantity'] + (ing['quantity'] * person_count)
    return output_ing

for lines in file.read().splitlines():
    if (lines.isdigit() is not True) and (' | ' not in lines) and (lines != ''):
        cookbook[lines] = []
        curr_recipe = lines
    if ' | ' in lines:
        curr_ingredient = lines.split(' | ')
        curr_ingredient = {'ingredient_name': curr_ingredient[0], 'quantity': int(curr_ingredient[1]), 'measure': curr_ingredient[2]}
        cookbook[curr_recipe].append(curr_ingredient)

print(cookbook)

print(get_shop_list_by_dishes(cookbook, ['Запеченный картофель', 'Омлет', 'Борщ'], 10))