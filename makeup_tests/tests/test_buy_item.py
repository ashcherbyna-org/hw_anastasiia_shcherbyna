
def test_buy_item(dashboard, item):
    dashboard.select_category("Парфюмерия")
    dashboard.select_sub_category('Вся парфюмерия')
    dashboard.choose_item("Versace Man Eau Fraiche")
    item.add_item_basket()
    item.close_pop_up()
    basket_value = item.get_basket_value()

    assert basket_value == "(1)"





