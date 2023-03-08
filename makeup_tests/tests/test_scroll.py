def test_scroll_page(dashboard):
    dashboard.select_category("Парфюмерия")
    dashboard.select_sub_category('Вся парфюмерия')
    dashboard.scroll()

