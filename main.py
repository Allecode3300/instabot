import db_manage as _db
import vista as _vista
import app_insta as _app

from instagrapi import Client

opc = 1
usuarios  = []

while opc != "0":
    opc = _vista.menu_inicial()

    if opc == "1":
        _app.seeusers()
    
    elif opc == "2":
        _app.adduser()
    elif opc == "3":
        _app.seepersonalusers()
    elif opc == "4":
        _app.addpersonaluser()

    elif opc == "5":
        usr = _app.login()
        if usr != None:
            pass
            #usuarios.append(usr)
        
        _vista.menu_login()
        opc = _vista.readln()
        if opc == 1:
            medias = usr.hashtag_medias_top("weed", 20)
            for media in medias:
                usr.user_follow(media.user.pk)
                print(f"Usuario seguido {media.user.username}")
            
    elif opc == "6":
        opc = _vista.menu_secundario()
        if opc == "0":
            opc = "1"
        elif opc == "1":
            _app.rmuser()
            
