def count_ingredients_price(ingredients_list):
    ingredients_price = 0

    for i in ingredients_list:
        ingredients_price = ingredients_price + i.price

    return ingredients_price

def get_ingredients_names(ingredients):
    ingredients_list = []

    for i in ingredients:
        ingredients_list.append(f'= {str(i.get_type()).lower()} {i.get_name()} =')
        
    return ingredients_list
