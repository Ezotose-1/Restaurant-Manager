from os import system

try:
    from simple_term_menu import TerminalMenu
except ModuleNotFoundError:
    print("Cannot found module simple_term_menu.")
    print("Please use ``pip install simple_term_menu``")
    exit(1)


class Empty():
    def run():
        return True


def clear():
    _ = system('clear||cls')


def header(*args) -> bool:
    """ Pretty print a header """
    l = len(max(args, key=len))
    s = f'''{(l+8) * "-"}\n'''
    for sub in args:
        s += f'--  {sub.center(l)}  --\n'
    s += f'''{(l+8) * "-"}'''
    print(s)
    return True


def menu(func : dict):
    """
    From a dictionnary build a menu and return the value
    
    :param func: Dictionnary { label: value }
    :return: Selected value
    """
    options = list(func.keys())

    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index is None:
        return False

    selected = options[menu_entry_index]
    return func.get(selected)



def table(stocks: dict):
    def intLen(i):
        return len(str(i))
    print()
    lk, vl = len(max(stocks.keys(), key=len)), intLen(max(stocks.values(), key=intLen))
    vl = max(vl, len('Quantité'))
    s = f'''{(lk + vl + 12) * "-"}\n'''
    s += f'| Id | {"Stocks".center(lk)} | Quantité |\n'
    s += f'''{(lk + vl + 12) * "-"}\n'''
    
    i = 1
    for k, v in stocks.items():
        s += f'| {str(i).zfill(2)} | {str(k).ljust(lk)} | {str(v).center(vl)} |\n'
        i+=1
    
    s += f'''{(lk + vl + 12) * "-"}\n'''
    print(s)


def tableMenu(menu: dict):
    print()
    plat_len = len(max(menu.keys(), key=len))
    cate_len = 0
    prix_len = len("Prix")
    for info in menu.values():
        cate_len = max(cate_len, len(info.get('Category')))

    line = "-" * (plat_len + cate_len + prix_len + 2 + 3 + 3 + 2) + "\n"
    s = line
    s += f'| {"Plat".center(plat_len)} | {"Catégorie".center(cate_len)} | {"Prix".center(prix_len)} |\n'
    s += line

    for k, v in menu.items():
        s += f'| {str(k).ljust(plat_len)} | {v.get("Category").ljust(cate_len)} | {str(v.get("Prix")).center(prix_len)} |\n'
    s += line

    print(s)
    


def tableOrder(orders: dict):
    print()