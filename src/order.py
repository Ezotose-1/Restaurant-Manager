from utils import header, clear, tableOrder, menu, Empty

from menu import Menu

from datetime import datetime, timedelta
from pathlib import Path
import json

class Order(Empty):

    def __init__(self) -> None:
        p = Path(__file__).parent.joinpath('data/orders.json')
        if not p.exists():
            print(f"Error on file loading. Please check {str(p)}")
            exit(1)
        self.path = p


    def load(self):
        """ Load the json data file and print an table """
        with open(self.path) as f:
            data = json.load(f)
        tableOrder(data)
        return data

    
    def __addOrder(self):
        clear()
        header('RESTAURANT LIPSUM', 'PRENDRE UNE COMMANDE')
        data = self.load()

        newOrder = {}
        newOrder["Name"] = input("Nom de la commande : ")
        newOrder["Day"] = datetime.now().timestamp()
        dish = {}
        totalPrice = 0

        m = Menu()
        menuData = m.load(doPrint=False)
        if not menuData:
            return False

        options = {}
        for k in menuData.keys():
            options[k] = k
        options["-- ANNULER --"] = False
        options["   VALIDER "] = True
        res = True
        while res:
            id = menu(options)
            if id is True:
                res = False
                continue
            if id is False:
                return True

            count = input("Combien ? ")
            if not count.isdigit:
                continue
            price = menuData[id].get("Prix")
            totalPrice += int(count) * price
            dish[id] = { "QUANTITY": int(count), "PRICE": price }
        
        newOrder['Price'] = totalPrice
        newOrder['Dish'] = dish

        idPointer = int(data.get('idPointer')) + 1
        data['idPointer'] = idPointer
        data.get('Orders')[f'{idPointer}'] = newOrder
        with open(self.path, "w") as f:
            f.write(json.dumps(data, indent=4))
        return True


    def __lastCommands(self):
        clear()
        header('RESTAURANT LIPSUM', 'HISTORIQUE DES COMMANDES')
        data = self.load()
        orders = data.get('Orders', {})
        
        startIndex = len(orders.items()) - 10 if len(orders.items()) > 10 else 0
        index = -1
        for _, order in orders.items():
            index += 1
            if (index < startIndex):
                continue
            print(f"{order.get('Name')} {datetime.fromtimestamp(order.get('Day')).strftime('%d/%m/%Y')} {order.get('Price')}€")
            for k, v in order.get('Dish').items():
                print(f"   {v.get('QUANTITY')} {k}")
            print()
        input("> ")
        return True


    def __report(self):
        clear()
        header('RESTAURANT LIPSUM', 'HISTORIQUE DES COMMANDES')
        orders = self.load().get('Orders', {})

        totalCount, totalPrice = 0, 0
        weekCount, weekPrice = 0, 0

        for _, order in orders.items():
            day = datetime.fromtimestamp(order.get('Day'))
            price = int(order.get('Price'))
            totalPrice += price
            totalCount += 1
            if day + timedelta(days=7) > datetime.now():
                weekCount += 1
                weekPrice += price
        print(f'''    Nombre total de commandes : {totalCount}
    Revenus total : {totalPrice}€

    Nombre de commandes ces 7 derniers jours : {weekCount}
    Revenus ces 7 derniers jours: {weekPrice}€''')
        input("> ")
        return True


    def manage(self):
        """ Main frame of menu management """
        res = True
        while res:
            clear()
            header('RESTAURANT LIPSUM', 'GESTIONS DES COMMANDES')
            r = self.load()
            if not r:
                return False

            options = {
                'Prendre une nouvelle commande': self.__addOrder,
                'Voir les 10 dernières commandes': self.__lastCommands,
                'Rapport des commandes': self.__report,
                'Quitter': lambda: False
            }
                        
            f = menu(options)
            if not f:
                continue
            res = f()
        return True

    def run():
        m = Order()
        return m.manage()

if (__name__ == "__main__"):
    Order.run()