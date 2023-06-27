import mariadb
import sys
import random

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="prueba",
        password="1234",
        host="127.0.0.1",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("USE Base_Datos_A")

def CrearCategoria():
    print("Categoria")

def InsertarMedio():
    sigue = True
    #Tabla Prensa
    while(sigue):
        infoPrensa=input("Por favor, ingrese el nombre del medio de prensa, su año de fundación, el continete de origen, el pais, la región y la ciudad. separe los datos con ', ': ")
        infoPrensaArray=infoPrensa.split(", ")
        while (len(infoPrensaArray)!= 6):
            infoPrensa=input("Por favor, siga el formato establecido. ")
            infoPrensaArray=infoPrensa.split(", ")
        print(infoPrensaArray)
        correcto=input("¿La información es correcta?, (Y/n): ")
        if(correcto=="Y" or correcto=="y"):
            sigue=False
    ASCII="ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789"
    IDMedio=""
    for i in range(0,4,1):
        IDMedio+=ASCII[random.randint(0,len(ASCII)-1)]
    #consulta="INSERT INTO Prensa (id, Region, Ciudad, Nombre, Continente, pais, Año_Fundacion) VALUES (%s,%s,%s,%s,%s);"
    try:
        cur.execute("INSERT INTO Prensa (id, Region, Ciudad, Nombre, Continente, pais, Año_Fundacion) VALUES (?, ?, ?, ?, ?, ?, ?)",(IDMedio, infoPrensaArray[4], infoPrensaArray[5], infoPrensaArray[0], infoPrensaArray[2], infoPrensaArray[3], infoPrensaArray[1]))
    except mariadb.Error as e: 
        print(f"Error: {e}")

    #Tabla Redes
    """sigue=True
    while(sigue):
        infoPrensa=input("Por favor, ingrese el nombre del medio de prensa, su año de fundación, el continete de origen, el pais, la región y la ciudad. separe los datos con ', ': ")
        infoPrensaArray=infoPrensa.split(", ")
        while (len(infoPrensaArray)!= 6):
            infoPrensa=input("Por favor, siga el formato establecido. ")
            infoPrensaArray=infoPrensa.split(", ")
        print(infoPrensaArray)
        correcto=input("¿La información es correcta?, (Y/n): ")
        if(correcto=="Y" or correcto=="y"):
            sigue=False
    ASCII="ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789"
    IDMedio=""
    for i in range(0,4,1):
        IDMedio+=ASCII[random.randint(0,len(ASCII)-1)]
    #consulta="INSERT INTO Prensa (id, Region, Ciudad, Nombre, Continente, pais, Año_Fundacion) VALUES (%s,%s,%s,%s,%s);"
    try:
        cur.execute("INSERT INTO Prensa (id, Region, Ciudad, Nombre, Continente, pais, Año_Fundacion) VALUES (?, ?, ?, ?, ?, ?, ?)",(IDMedio, infoPrensaArray[4], infoPrensaArray[5], infoPrensaArray[0], infoPrensaArray[2], infoPrensaArray[3], infoPrensaArray[1]))
    except mariadb.Error as e: 
        print(f"Error: {e}")"""
    #Tabla Fundadores

    #Tabla Ejemplo_N

    conn.commit()
    conn.close()
    print("Medio")

#####################################################################################################
funcionando = True
while(funcionando):
    VarConsulta = 0
    print("¿Qué desea insertar?")
    print("1.- Medio de Prensa /n 2.- Categoría")
    while(VarConsulta != "1" and VarConsulta != "2"):
        VarConsulta=input()
        if (VarConsulta != "1" and VarConsulta != "2"):
            print("Por favor escriba 1 o 2")
    if(VarConsulta=="1"):
        InsertarMedio()
    else:
        CrearCategoria()
    if (input("¿Desea insertar algo más? Y/n: ").lower()=="n"):
        print("  ^__^")
        print(" (oo)\_______")
        print(" (__)\       )\/\\")
        print("     ||----w |")
        print("     ||     ||")
        print("Noh' vimo perro y la ctm")
        dragon = '''
                                / \\  //\\
                |\\___/|      /   \\//  \\\\
                /0  0  \\__  /    //  | \\ \\
                /     /  \\/_/    //   |  \\  \\
                @_^_@'/   \\/_   //    |   \\   \\
                //_^_/     \\/_ //     |    \\    \\
            ( //) |        \\//      |     \\     \\
            ( / /) _|_ /   )  //       |      \\     _\\
        ( // /) '/,_ _ _/  ( ; -.    |    _ _\\.-~        .-~~~^-.
        (( / / )) ,-{        _      `-.|.-~-.           .~         `.
        (( // / ))  '/\\      /                 ~-. _ .-~      .-~^-.  \\
        (( /// ))      `.   {            }                   /      \\  \\
        (( / ))     .----~-.\        \\-'                 .~         \\  `. \\^-.
                    ///.----..>        \\             _ -~             `.  ^-`  ^-_
                    ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                        /.-~
'''
        print(dragon)

        funcionando=False