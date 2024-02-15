import flask
import Objects

app = flask.Flask(__name__)


@app.route('/')
def menu():
    return flask.render_template('menu.html',menus=Objects.menus)


@app.route('/category/<category_type>')
def categories(category_type):
    menu_typee = None
    for i in Objects.menus:
        if i.type_name.lower() == category_type.lower():
            menu_typee = i
            break

    if menu_typee:
        return flask.render_template('categories.html',category_type=category_type,menu_typee=menu_typee)


@app.route('/category/<category_type>/<specific_dishes>')
def category(category_type,specific_dishes):
    specific_dish_changed = specific_dishes.lower()
    specifics = []
    for mnu in Objects.menus:
        if mnu.type_name.lower() == category_type.lower():
            for ctg in mnu.categories:
                if ctg.category_name.lower()==specific_dish_changed:
                    for dish in ctg.menu_items:
                        specifics.append(dish)

    if specifics:
        return flask.render_template('category.html',specific_dishes=specific_dishes,specifics=specifics)


if __name__ == '__main__':
    app.run(debug=True)