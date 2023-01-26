from utils import header, clear, tableMenu, menu, Empty

from pathlib import Path
import json

class Menu(Empty):

    def __init__(self) -> None:
        p = Path(__file__).parent.joinpath('data/menu.json')
        if not p.exists():
            print(f"Error on file loading. Please check {str(p)}")
            exit(1)
        self.path = p


    def load(self, doPrint=True):
        """ Load the json data file and print an table """
        with open(self.path) as f:
            data = json.load(f)
        
        if doPrint:
            tableMenu(data)
        return data

    
    def __add(self):
        """ And an element in the menu """
        clear()
        header('RESTAURANT LIPSUM', 'AJOUTER AU MENU')
        data = self.load()
        if not data:
            return False
        name = input("Nom de l'élément : ")
        categ = input("Catégorie (Entrée, Plat, Dessert, Boisson) : ").lower()
        if ("entree" in categ):
            categ = "ENTREE"
        elif ("plat" in categ):
            categ = "PLAT PRINCIPAL"
        elif ("dessert" in categ):
            categ = "DESSERT"
        elif ("boisson" in categ):
            categ = "BOISSON"
        else:
            categ = categ.upper()
        price = input("Prix : ")
        if not price.isdigit() or categ == "" or price == "":
            return False

        price = int(price)
        data[name.upper()] = {"Category": categ, "Prix": price}
        with open(self.path, "w") as f:
            f.write(json.dumps(data, indent=4))
        return True


    def __remove(self):
        """ Remove an element from the menu """
        clear()
        header('RESTAURANT LIPSUM', 'RETIRER DU MENU')
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

    def manage(self):
        """ Main frame of menu management """
        res = True
        while res:
            clear()
            header('RESTAURANT LIPSUM', 'GESTIONS DU MENU')
            r = self.load()
            if not r:
                return False

            options = {
                'Ajouter un élément': self.__add,
                'Retirer un élément': self.__remove,
                'Quitter': lambda: False
            }
            f = menu(options)
            if not f:
                continue
            res = f()
        return True

    def run():
        m = Menu()
        return m.manage()

if (__name__ == "__main__"):
    Menu.run()