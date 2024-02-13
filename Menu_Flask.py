import flask
import Menus
import Categories
import MenuItem

app = flask.Flask(__name__)

appetizers = Menus.Appetizers('Appetizers')
salads = Categories.Category('Salads')
caesar_salad = MenuItem.MenuItem('CaesarSalad', 'Lettuce,Cheese,dressing',2000)

salads.add_item(caesar_salad)
appetizers.add_category(salads)

appetizers.display_menu()
salads.display_items()

menus = [appetizers]

@app.route('/')
def menu():
    return flask.render_template('menu.html',menus=menus)


@app.route('/category/<category_type>')
def categories(category_type):
    menu_typee = None
    for i in menus:
        if i.type_name.lower() == category_type.lower():
            menu_typee = i
            break

    if menu_typee:
        return flask.render_template('categories.html',category_type=category_type,menu_typee=menu_typee)


@app.route('/category/<category_type>/<specific_dishes>')
def category(category_type,specific_dishes):
    specific_dish_changed = specific_dishes.replace('_', ' ').lower()
    specifics = None
    for i in menus:
        if i.type_name.lower() == category_type.lower():
            for ctg in i.categories:
                for dish in ctg.menu_items:
                    if dish.name.lower().replace(' ', '_') == specific_dish_changed:
                        specifics = [dish]
                        break
                if specifics:
                    break
            if specifics:
                break
    if specifics:
        return flask.render_template('category.html',specific_dishes=specific_dishes,specifics=specifics)
    else:
        return "No specific dish found for the category"


if __name__ == '__main__':
    app.run(debug=True)