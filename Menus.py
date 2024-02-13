import abc


class Menu(abc.ABC):
    def __init__(self,type_name):
        self.type_name = type_name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    @abc.abstractmethod
    def display_menu(self):
        ...


class Appetizers(Menu):

    def display_menu(self):
        print(f'Appetizers: {self.type_name}')
        for category in self.categories:
            category.display_items()


class MainCourse(Menu):

    def display_menu(self):
        print(f'Main Course: {self.type_name}')
        for category in self.categories:
            category.display_items()


class Desserts(Menu):

    def display_menu(self):
        print(f'Desserts: {self.type_name}')
        for category in self.categories:
            category.display_items()


class Drinks(Menu):

    def display_menu(self):
        print(f'Drinks: {self.type_name}')
        for category in self.categories:
            category.display_items()