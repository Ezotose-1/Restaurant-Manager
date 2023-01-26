from utils import header, clear, table, menu, Empty

from pathlib import Path
import json


class Stocks(Empty):

    def __init__(self) -> None:
        p = Path(__file__).parent.joinpath('data/stocks.json')
        if not p.exists():
            print(f"Error on file loading. Please check {str(p)}")
            exit(1)
        self.path = p


    def load(self):
        """ Load the json data file and print an table """
        with open(self.path) as f:
            data = json.load(f)
        table(data)
        return data


    def __remove(self):
        """ Remove an element from the stock """
        clear()
        header('RESTAURANT LIPSUM', 'RETIRER DU STOCK')
        data = self.load()
        if not data:
            return False
        options = {}
        for k in data.keys():
            options[k] = k
        id = menu(options)
        if id is False:
            return True

        data.pop(id)

        with open(self.path, "w") as f:
            f.write(json.dumps(data, indent=4))
        return True


    def __add(self):
        """ And an element in the stock """
        clear()
        header('RESTAURANT LIPSUM', 'AJOUTER AU STOCK')
        data = self.load()
        if not data:
            return False
        name = input("Nom de l'élément : ")
        quantity = input("Quantité : ")
        if not quantity.isdigit():
            return False

        data[name] = int(quantity)
        with open(self.path, "w") as f:
            f.write(json.dumps(data, indent=4))
        return True


    def update(self):
        """ Update a product in the stocks """
        clear()
        header('RESTAURANT LIPSUM', 'METTRE A JOUR STOCK')
        data = self.load()
        if not data:
            return False

        options = {}
        for k in data.keys():
            options[k] = k

        id = menu(options)
        if id is False:
            return True

        quantity = input(f"Quantité de {id.lower()} : ")
        if not quantity.isdigit():
            return False

        data[id] = int(quantity)

        with open(self.path, "w") as f:
            f.write(json.dumps(data, indent=4))
        return True


    def manage(self):
        """ Main frame of stocks management """
        res = True
        while res:
            clear()
            header('RESTAURANT LIPSUM', 'GESTIONS DES STOCKS')
            r = self.load()
            if not r:
                return False

            options = {
                'Mettre à jour le stock': self.update,
                'Ajouter un élément dans le stock': self.__add,
                'Retirer un élément du stock': self.__remove,
                'Quitter': lambda: False
            }
            f = menu(options)
            if not f:
                continue
            res = f()
        return True

    def run():
        s = Stocks()
        return s.manage()



if (__name__ == "__main__"):
    Stocks.run()
