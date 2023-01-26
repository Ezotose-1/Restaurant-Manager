#! /usr/bin/env python3

from utils import header, clear, menu, Empty

from stocks import Stocks
from menu import Menu
from order import Order

class Quit(Empty):
    def run():
        return False


def main():
    res = True
    while res:
        clear()
        header("RESTAURANT LIPSUM", '15 rue des Ecoles', '08360 GIVET')
        print()
        d = {
            "Gestion des commandes": Order,
            "Gestion des stocks": Stocks,
            "Gestion du menu": Menu,
            "Quitter": Quit,
        }
        obj = menu(d)
        if not obj:
            obj = Quit

        try:
            res = obj.run()
        except KeyboardInterrupt:
            pass
    clear()
    return True


if __name__ == "__main__":
    main()