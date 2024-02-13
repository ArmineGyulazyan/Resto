class Category:

    def __init__(self,category_name):
        self.category_name = category_name
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def display_items(self):
        print(f'Category: {self.category_name}')
        for item in self.menu_items:
            print(f' {item.name}: {item.ingredients}, {item.price}')
