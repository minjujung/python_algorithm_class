shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    orders_set = set(orders)
    possible_menus = menus_set & orders_set
    for i in range(len(orders)):
        if orders[i] not in possible_menus:
            return False
    else:
        return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)

