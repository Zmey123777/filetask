import os

#Код к заданиям №1, №2
def parse_ingredient(ingredient_line):
    parts = [part.strip() for part in ingredient_line.split('|')]
    ingredient_name = parts[0]
    quantity = int(parts[1])
    measure = parts[2]

    return {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients_list = cook_book[dish]
            for ingredient in ingredients_list:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list

file_path = os.path.join(os.getcwd(), 'recipes.txt')
cook_book = {}
with open(file_path, 'r', encoding='utf-8') as f:
    current_recipe_name = None
    current_ingredients = []
    for line in f:
        stripped_line = line.strip()
        if stripped_line:
            if current_recipe_name is None:
                current_recipe_name = stripped_line
            else:
                try:
                    ingredients_qty = int(stripped_line)
                    current_ingredients = []
                except ValueError:
                    ingredient_details = parse_ingredient(stripped_line)
                    current_ingredients.append(ingredient_details)
                    if len(current_ingredients) == ingredients_qty:
                        cook_book[current_recipe_name] = current_ingredients
                        current_recipe_name = None
                        current_ingredients = []
result_dict = dict()
result_dict['cook_book'] = cook_book
print(result_dict)
dishes_for_guests = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(dishes_for_guests)

#Код к заданию №3

file_names = ['1.txt', '2.txt', '3.txt']
def prepare_file_info(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            file_info = f"{file_name}\n{num_lines}\n"
            content = ''.join(lines)
            return file_info, content
    except FileNotFoundError:
        raise FileNotFoundError(f'Файл не найден: {file_path}')

files_info = []
for file_name in file_names:
    file_info, content = prepare_file_info(file_name)
    files_info.append((file_info, content))
files_info.sort(key=lambda x: int(x[0].split('\n')[1]))
result_file_path = os.path.join(os.getcwd(), 'result.txt')
try:
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        for file_info, content in files_info:
            result_file.write(file_info)
            result_file.write(content)
except FileNotFoundError:
        raise FileNotFoundError(f'Файл не найден: {result_file_path}')
    
print(f"Файл записан: {result_file_path}")