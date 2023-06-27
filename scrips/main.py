import db_manage as _db
import vista as _vista

opc = 1

while opc != "0":
    opc = _vista.menu_inicial()

    if opc == "1":
        users = _db.seeusers()
        _vista.line()
        for usr in users:
            _vista.printinf(usr[1])
    
    elif opc == "2":
        _vista.line()
        _vista.printinf("Cual es el nikname del usuario")
        _db.newuser(_vista.readln())
    
    elif opc == "3":
        _vista.line()
        _vista.printinf("")
    

    

