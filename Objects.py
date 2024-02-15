import Menus
import Categories
import MenuItem

appetizers = Menus.Appetizers('Appetizers')
main_course = Menus.MainCourse('Main Course')
desserts = Menus.Desserts('Desserts')
drinks = Menus.Drinks('Drinks')

salads = Categories.Category('Salads')
dips = Categories.Category('Dips')
pizzas = Categories.Category('Pizzas')
diet_dessert = Categories.Category('Dietetic')
non_diet_dessert = Categories.Category('Non Dietetic')
with_alcohol = Categories.Category('Alcoholic Drinks')
non_alcohol = Categories.Category('Non Alcoholic Drinks')

appetizers.add_category(salads)
appetizers.add_category(dips)
main_course.add_category(pizzas)
desserts.add_category(diet_dessert)
desserts.add_category(non_diet_dessert)
drinks.add_category(with_alcohol)
drinks.add_category(non_alcohol)

caesar_salad = MenuItem.MenuItem('Caesar Salad', 'Lettuce,Cheese,Dressing',2000)
hummus = MenuItem.MenuItem('Hummus', 'Pea, Olive oil',3000)
margarita = MenuItem.MenuItem('Margarita', 'Tomato, Olive oil, Cheese',2100)
cheesecake = MenuItem.MenuItem('Cheesecake', 'Crust,Cream Cheese',3100)
brownies = MenuItem.MenuItem('Brownies', 'Chocolate chips, Flour, Cacao',3200)
aperol = MenuItem.MenuItem('Aperol', 'Aperol,Orange',2500)
citrus_lemonade = MenuItem.MenuItem('Citrus Lemonade', 'Orange,Lime,Mint',2300)
berry_lemonade = MenuItem.MenuItem('Berry Lemonade', 'Strawberry,Raspberry,Mint',2400)

salads.add_item(caesar_salad)
dips.add_item(hummus)
pizzas.add_item(margarita)
diet_dessert.add_item(cheesecake)
non_diet_dessert.add_item(brownies)
with_alcohol.add_item(aperol)
non_alcohol.add_item(citrus_lemonade)
non_alcohol.add_item(berry_lemonade)


menus = [appetizers,main_course,desserts,drinks]
