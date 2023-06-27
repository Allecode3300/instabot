import os

def clrscr():
    os.system("clear")



def menu_inicial():
    
    names = ["Salir", "Ver usuarios", "Añadir usuario", "Ver usuarios personales", "Añadir usuario personal", "Más"]
    
    print("-"*39)
    for i in range(len(names)):
        print("|{:<3} : {:>30}|".format(i, names[i]))
    opcion = input("Elige una opcin: ")
    clrscr()
    return opcion

def line():
    print("-"*39)

def printinf(msg):
    if len(msg) < 36:
        print("|{:<37}|".format(msg))

def readln(msg = ""):
    res = input("|" + msg + ": ")
    return res