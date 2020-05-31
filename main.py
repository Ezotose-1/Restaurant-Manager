__author__ = 'PRENOM.NOM'


## Customs Package ##

import os
from os import system, name
import datetime
import sys


## Functions ##


# Cette fonction permet de lire une chaine de caracteres independamment de la version de Python.
def __input(prompt=""):
    if (sys.version_info[0] == 3):
        return input(prompt)
    else:
        return raw_input(prompt)


# Cette fonction prend en entree une liste de string qui formeront le HEADER de chaque menu #
def _headerMain(txt):
    str = "---------------------------------------------------\n"
    for s in txt:
        str += "--------"
        for i in range (0, (36-len(s))//2):
            str +=" "
        str += s
        for i in range (0, (36-len(s))//2):
            str +=" "
        str += "--------\n"
    str += "---------------------------------------------------"
    print(str)


# Cette fonction permet de recupere une des listes de lines des fichiers textes et separe chaque mots
def _tableBuild(list):
    L = []
    for s in list:
        L += s.split(" - ")
    return L

# Cette fonction va convertir un fichier texte menant au storage en liste de couples : (nom, quaitie) #
def _storageToList(path):
    file = open(path, "r")
    L = _tableBuild(file.readlines())
    M = []
    for i in range (0, len(L), 2):
        M.append( (L[i],L[i+1].strip('\n')) )
    return M

# Cette fonction va transformer une liste de (nom, quantite) en nouveau fichier texte storage #
def _listToStorage(path, L):
    file = open(path, "w")
    s = ""
    for i in L:
        s+= i[0] + " - "+ i[1] + "\n"
    file.write(s)

# Cette fonction va convertir un fichier texte menant au menu en une liste de couples : (nom, categorie, prix) #
def _menuToList(path):
    file = open(path, "r")
    L = _tableBuild(file.readlines())
    M = []
    for i in range (0, len(L), 3):
        M.append( (L[i],L[i+1], L[i+2].strip('\n')) )
    return M

# Cette fonction va transformer une liste de (nom, categorie, prix) en nouveau fichier texte menu #
def _listToMenu(path, L):
    file = open(path, "w")
    s = ""
    for i in L:
        s+= i[0] + " - "+ i[1] + " - " + i[2]+ "\n"
    file.write(s)



## --------------- MAIN - MENU ---------------##
def _firstMenu():
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "15 rue des Ecoles", "08360 GIVET"])
    print("MENU PRINCIPALE :\n")
    print("1. PRISE DE COMMANDE")
    print("2. GESTION DES STOCKS")
    print("3. GESTION DU MENU")
    print("4. HISTORIQUE DES COMMANDES")
    print("5. QUITTER\n")
    print("QUE VOULEZ VOUS FAIRE ? (1-5) :")
    entry = __input()
    _ = system("clear||cls")
    if (entry == '1'):
        (path, L) = _orderMenu()
        _orderOption(path, L)
    elif (entry == '2'):
        _stockMenu()
    elif (entry == '3'):
        _menuMenu()
    elif (entry == '4'):
        s = _histoMenu()
        _histoOption(s)
    elif (entry == '5'):
        pass
    else:
        print(entry + " n'est pas une entree valable (1-5)")


## --------------- STOCK - MENU ---------------##
def _stockOptions(path, s):
    print("\n 1. MISE A JOUR DU STOCK               2. AJOUT DE PRODUITS")
    print(" 3. EXPORTER LA LISTE DES PRODUITS     4. SUPPRIMER UN PRODUITS")
    print(" 5. RETOUR AU MENU PRINCIPAL")
    print("QUE VOULEZ VOUS FAIRE ? (1-5)")
    entry = __input()
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "GESTIONS DES STOCKS"])
    if (entry == '1'):
        pass
    elif (entry == '2'):
        print("QUE VOULEZ VOUS AJOUTER ?")
        print("(ex : ''POMME'' )")
        items = __input()
        print("COMBIEN VOULEZ VOUS EN AJOUTER ?")
        count = int(__input())
        _stockAdd(path, items, count)
    elif (entry == '3'):
        print("OU VOULEZ VOUS EXPORTER ?")
        print("(ex : "+path.strip("stocks.txt")+"votrestock.txt )")
        exportPth = __input()
        file = open(exportPth, "wr+")
        file.write(s)
        file.close()
    elif (entry == '4'):
        print(_stockTable())
        print("QUEL PRODUIT VOULEZ VOUS SUPPRIMER ?")
        itemIndx = int(__input())
        print("COMBIEN VOULEZ VOUS EN SUPPRIMER ?")
        count = int(__input())
        _stockRemove(path, itemIndx, int(count))
    elif (entry == '5'):
        _firstMenu()
        return True
    else:
        print(entry + " n'est pas une entree valable (1-5)")
    _stockMenu()


def _stockTable():
    path = os.path.abspath("restaurant.py")
    path = os.path.split(path)[0]+"/stocks.txt"
    file = open(path, "r")
    stocksTxt = file.readlines()
    M = _tableBuild(stocksTxt)
    strTable = "\n\n---------------------------------------------------\n"
    strTable +="|   |  PRODUITS                        | QUANTITE |\n"
    strTable += "---------------------------------------------------\n"
    for i in range (0, len(M), 2):
        strTable +="| "+str(i//2)+" |  "+M[i]
        for j in range (0, 32- len(M[i])):
            strTable += " "
        strTable +="| "+M[i+1].strip('\n')
        for k in range (0, 10- len(M[i+1])):
            strTable += " "
        strTable += "|\n"
    strTable += "---------------------------------------------------\n"
    return strTable


def _stockAdd(path, element, count):    
    L = _storageToList(path)
    isPresent = False
    for i in range (len(L)):
        if (L[i][0] == element):
            isPresent= True
            L[i] = (L[i][0], str(int(L[i][1]) + count))
    if (not isPresent):
        L.append((element, str(count)))
    _listToStorage(path, L)



def _stockRemove(path, index, count):
    L = _storageToList(path)
    if(index < len(L)):
        listEl = L[index]
        if (int(L[index][1]) <= count):
            L.remove(listEl)
            _listToStorage(path, L)
            return True
        else:
            L[index] = (L[index][0], str(int(L[index][1])-count))
    _listToStorage(path, L)


def _stockMenu():
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "GESTIONS DES STOCKS"])
    strTable = _stockTable()
    path = os.path.abspath("restaurant.py")
    path = os.path.split(path)[0]+"/stocks.txt"
    print(strTable)
    _stockOptions(path, strTable)




## --------------- MENU - MENU ---------------##
def _menuMenu():
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "GESTIONS DU MENU"])
    path = os.path.abspath("restaurant.py")
    path = os.path.split(path)[0]+"/menu.txt"
    strTable = _menuTable()
    print(strTable)
    _menuOption(path)


def _menuOption(path):
    print("\n 1. MODIFIER UN PLAT                 2. AJOUTER UN PLAT")
    print(" 3. SUPPRIMER UN PLAT                4. RETOUR AU MENU PRINCIPAL")
    print("QUE VOULEZ VOUS FAIRE ? (1-4)")
    entry = __input()
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "GESTIONS DU MENU"])
    if (entry == '1'):
        print(_menuTable())
        print("QUEL PLAT VOULEZ VOUS MODIFIER ?")
        print("(Mettre son index )")
        platIndex = int(__input())
        print("QUEL EST SON NOUVEAU PRIX ?")
        newprice = int(__input())
        _menuModify(path, platIndex, newprice)
    elif (entry == '2'):
        print("QUEL PLAT VOULEZ VOUS AJOUTER ?")
        print("(ex : ''TARTE AUX POMMES'' )")
        plat = __input()
        print("DE QUEL CATEGORIE EST CE PLAT ?")
        print("(ex : 'DESSERT' / 'ENTREE' / 'PLAT PRINCIPAL' / 'BOISSON' )")
        categorie = __input()
        print("QUEL EST SON PRIX ?")
        prix = int(__input())
        _menuAdd(path, plat, categorie, prix)
    elif (entry == '3'):
        print(_menuTable())
        print("QUEL PLAT VOULEZ VOUS SUPPRIMER ?")
        print("(Mettre son index)")
        platIndx = int(__input())
        _menuRemove(path, platIndx)
    elif (entry == '4'):
        _firstMenu()
        return True
    else:
        print(entry + " n'est pas une entree valable (1-5)")
    _menuMenu()

def _menuTable():
    path = os.path.abspath("restaurant.py")
    path = os.path.split(path)[0]+"/menu.txt"
    menuTxt = _menuToList(path)
    strTable = "\n------------------------------------------------------------\n"
    strTable +="|   | PLAT                       | CATEGORIE         | PRIX |\n"
    strTable += "------------------------------------------------------------\n"
    index = -1
    for i in menuTxt:
        index, plat, categorie, prix = index+1, i[0], i[1], i[2].strip("\n")
        strTable +="| "+ str(index)
        strTable += " " * (2 - len(str(index)))
        strTable +="| "+ plat
        for j in range (0, 27- len(plat)):
            strTable += " "
        strTable +="| "+ categorie
        for k in range (0, 18- len(categorie)):
            strTable += " "
        strTable +="| "+ prix
        for k in range (0, 5- len(prix)):
            strTable += " "
        strTable += "|\n"
    strTable += "-------------------------------------------------------------\n"
    return strTable

def _menuAdd(path, element, categorie, prix):
    L = _menuToList(path)
    isPresent = False
    for i in range (len(L)):
        if (L[i][0] == element):
            isPresent= True
    if (not isPresent):
        L.append((element, categorie, str(prix)))
    _listToMenu(path, L)


def _menuRemove(path, index):
    L = _menuToList(path)
    if (index < len(L)):
        L.remove(L[index])
    _listToMenu(path, L)


def _menuModify(path, index, newprice):
    L = _menuToList(path)
    if (index < len(L)):
        L[index] = (L[index][0], L[index][1], str(newprice))
    _listToMenu(path, L)


## --------------- ORDER - MENU ---------------##
def _orderList():
    path = os.path.abspath("main.py")
    path = os.path.split(path)[0]+"/menu.txt"
    menuTxt = _menuToList(path)
    Entrees, Plats, Desserts, Boissons = [], [], [], []
    for i in menuTxt:
        if (i[1] == "ENTREE"):
            Entrees.append(i)
        elif (i[1] == "PLAT PRINCIPAL"):
            Plats.append(i)
        elif (i[1] == "DESSERT"):
            Desserts.append(i)
        elif (i[1] == "BOISSON"):
            Boissons.append(i)
    plat = Entrees + Plats + Desserts + Boissons
    s = "\nENTREES DISPONIBLES :          PLATS DISPONIBLES : \n\n"
    for i in range ( max(len(Entrees), len(Plats)) ):
        j = 0
        if (i < len(Entrees)):
            s += str(i) + ". "+ Entrees[i][0]
            j = len(Entrees[i][0]) + 3
        s += " " * (29 - j)
        if (i < len(Plats)):
            s += str(i + len(Entrees)) +". "+ Plats[i][0] + "\n"
    
    s += "\nDESSERTS DISPONIBLES :         BOISSONS DISPONIBLES : \n\n"
    for i in range ( max(len(Desserts), len(Boissons)) ):
        j = 0
        if (i < len(Desserts)):
            s += str(i + len(Entrees) + len(Plats)) + ". "+ Desserts[i][0]
            j = len(Desserts[i][0]) + 3
        s += " " * (29 - j)
        if (i < len(Boissons)):
            s += str(i + len(Desserts) + len(Entrees) + len(Plats)) +". "+ Boissons[i][0] + "\n"
    print(s)
    return plat
    


def _orderMenu():
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "PRISE DE COMMANDE"])
    client = __input("NOM DU CLIENT : ")
    plat = _orderList()
    path = os.path.abspath("main.py")
    path = os.path.split(path)[0]+"/orders/"+client+".txt"
    file = open(path, "w")
    file.write("DATE :\n")
    file.close()
    file = open(path, "a")
    file.write("(JOUR - MOIS)\n")
    file.write(str(datetime.datetime.now().day) + " - " + str(datetime.datetime.now().month) + "\n")
    file.write("PRIX TOTAL :\n")
    file.write("0\n")
    file.write("COMMANDE :\n")
    file.write("(PLAT - QUANTITE)\n")
    file.close()
    return (path, plat) 



def _orderOption(path, L):
    print(" 1. SELECTIONNER UN PRODUIT             2. RESUME DE LA COMMANDE")
    print(" 3. ENVOI DE LA COMMANDE A LA CUISINE   4. RETOUR AU MENU PRINCIPAL")
    print("QUE VOULEZ VOUS FAIRE ? (1-4)")
    entry = __input()
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "PRISE DE COMMANDE"])
    _orderList()
    if (entry == '1'):
        print("QUEL PLAT VOULEZ VOUS SELECTIONNER ?")
        i = int(__input())
        print("COMBIEN EN VOULEZ VOUS ?")
        count = int(__input())
        plat = L[i][0]
        _orderAdd(path, plat, count, int(L[i][2]))
        _ = system("clear||cls")
        _orderList()
        _orderOption(path, L)
    elif (entry == '2'):
        _orderResume(path)
        _orderOption(path, L)
    elif (entry  == '3'):
        _firstMenu()
    elif (entry == '4'):
        _firstMenu()


def _orderAdd(path, plat, count, price):
    file = open(path, "a")
    file.write(plat + " - " + str(count) + "\n")
    file.close()
    file = open(path, "r")
    L = file.readlines()
    file.close()
    file = open(path, "w")
    L[4] = str( int(L[4]) + (price * count) ) + "\n"
    file.writelines(L)
    file.close()


# L liste des ligne de la commande #
def _orderToTuples(L):
    (day, month) = ( L[2].split(" - ")[0], L[2].split(" - ")[1].strip("\n") )
    Plats = []
    for i in range (7, len(L)):
        Plats.append( ( L[i].split(" - ")[0], L[i].split(" - ")[1].strip("\n") ) )
    return (day, month, Plats)
    

    
def _orderResume(path):
    file = open(path, "r")
    L = file.readlines()
    (_, _, OrdList) = _orderToTuples(L)
    s = "----------------------------------------------------\n"
    s += "   ETAT DE LA COMMANDE :\n"
    for i in OrdList:
        s += i[0] + " " * (27 - len(i[0])) + " QUANTITE " + i[1] + "\n"
    s += "   PRIX TOTAL :\n"
    s += L[4].strip("\n") + " EURO\n"
    file.close()
    print(s)


## --------------- HISTORIQUE - MENU ---------------##
def _histoMenu():
    _ = system("clear||cls")
    _headerMain(["RESTAURANT LIPSUM", "HISTORIQUE DES COMMANDES"])
    orderL = os.listdir("orders")
    totalOrder, weekOrder, lastOrder = len(orderL), 0, datetime.date(2000, 1, 1)
    totalPrice, weekPrice = 0, 0
    s = "\nNOMBRE TOTAL DE COMMANDES PASSEES : " + str(totalOrder) + "\n"
    path = os.path.abspath("main.py")
    path = os.path.split(path)[0]+"/orders/"
    for i in orderL:
        Thispath = path + str(i)
        file = open(Thispath, "r")
        Lst = file.readlines()
        totalPrice += int(Lst[4].strip("\n"))
        (d, m, L) = _orderToTuples(Lst)
        currentdate = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
        date = datetime.date(2020, int(m), int(d))
        if (date > lastOrder):
            lastOrder = date
        if (currentdate - date) <= datetime.timedelta(7):
            weekPrice += int(Lst[4].strip("\n"))
            weekOrder += 1
    s += "TOTAL PAYE : " + str(totalPrice) + " euro\n"
    s += "\nDERNIERE COMMANDE : " + str(lastOrder.day) + "/" + str(lastOrder.month) + "\n"
    s += "\nCOMMANDE PASSEES CES 7 DERNIERS JOURS : " + str(weekOrder) + "\n"
    s += "TOTAL PAYE CES 7 DERNIERS JOURS : " + str(weekPrice) + " euro\n" 
    print(s)
    return s


def _histoOption(s):
    print(" 1. EXPORTER LE RESUME                  2. RETOUR AU MENU PRINCIPAL")
    print("QUE VOULEZ VOUS FAIRE ? (1-2)")
    entry = __input()
    if (entry == '1'):
        print("OU VOULEZ VOUS L'EXPORTER ?")
        print("(ex : "+os.path.split(os.path.abspath("main.py"))[0] + "/historique.txt )")
        path = __input()
        file = open(path, "wr+")
        file.write(s)
        file.close()
    elif (entry == '2'):
        _firstMenu()

## Main ##

_firstMenu()


# build with Python 3.6.9 #
