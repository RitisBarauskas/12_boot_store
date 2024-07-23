MAX_GOODS_PER_PAGE = 10

DATABASE = {
    'category': [
        {'id': 1, 'name': 'Fruit', 'slug': 'fruit', 'description': 'Fruit description'},
        {'id': 2, 'name': 'Vegetable', 'slug': 'vegetable', 'description': 'Vegetable description'},
        {'id': 3, 'name': 'Meat', 'slug': 'meat', 'description': 'Meat description'},
        {'id': 4, 'name': 'Fish', 'slug': 'fish', 'description': 'Fish description'},
        {'id': 5, 'name': 'Milk', 'slug': 'milk', 'description': 'Milk description'},
        {'id': 6, 'name': 'Bread', 'slug': 'bread', 'description': 'Bread description'},
        {'id': 7, 'name': 'Alcohol', 'slug': 'alcohol', 'description': 'Alcohol description'},
    ],
    'goods': [
        {'id': 1, 'name': 'Apple', 'category_id': 1, 'description': 'Apple description'},
        {'id': 2, 'name': 'Banana', 'category_id': 1, 'description': 'Banana description'},
        {'id': 3, 'name': 'Carrot', 'category_id': 2, 'description': 'Carrot description'},
        {'id': 4, 'name': 'Cucumber', 'category_id': 2, 'description': 'Cucumber description'},
        {'id': 5, 'name': 'Pork', 'category_id': 3, 'description': 'Pork description'},
        {'id': 6, 'name': 'Beef', 'category_id': 3, 'description': 'Beef description'},
        {'id': 7, 'name': 'Salmon', 'category_id': 4, 'description': 'Salmon description'},
        {'id': 8, 'name': 'Cod', 'category_id': 4, 'description': 'Cod description'},
        {'id': 9, 'name': 'Cow milk', 'category_id': 5, 'description': 'Cow milk description'},
        {'id': 10, 'name': 'Soy milk', 'category_id': 5, 'description': 'Soy milk description'},
        {'id': 11, 'name': 'White bread', 'category_id': 6, 'description': 'White bread description'},
        {'id': 12, 'name': 'Black bread', 'category_id': 6, 'description': 'Black bread description'},
        {'id': 13, 'name': 'Vodka', 'category_id': 7, 'description': 'Vodka description'},
        {'id': 14, 'name': 'Whiskey', 'category_id': 7, 'description': 'Whiskey description'},
    ]
}