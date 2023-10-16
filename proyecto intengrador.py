#Proyecto Integrador
#Buscaminas
#🟩
#🚩
#1️⃣
#2️⃣
#1 nivel 7x7, minas=7

#como se ve el tablero
h1 = ["1","⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
h2 = ["2","⬜️","⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
h3 = ["3","⬜️️","⬜️️","⬜️️","️⬜️","️⬜️","️⬜️","️⬜️"]
h4 = ["4","⬜️","⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
h5 = ["5","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]
h6 = ["6","⬜️","⬜️","️⬜️","️⬜️","️⬜️","️⬜️","️⬜️"]
h7 = ["7","⬜️️","⬜️️","⬜️️","⬜️️","⬜️️","️⬜️","️⬜️"]

#nivel 1 tablero inicial
cc = "    1   2   3   4   5   6   7"
h1 = ["1 ", "⬜️", "⬜️", " ⬜", " ⬜", " ⬜", " 1️⃣", "🟩"]
h2 = ["2 ", "⬜️", "⬜️", " 2️⃣", " 2️⃣", " 2️⃣", " 1️⃣", "🟩"]
h3 = ["3 ", "⬜️", "⬜️", " 1️⃣", " 🟩", " 1️⃣", " 1️⃣", "1️⃣"]
h4 = ["4 ", "⬜️", "2️⃣", " 1️⃣", " 🟩", " 1️⃣", " ⬜", "⬜"]
h5 = ["5 ", "⬜️", "1️⃣", " 🟩", " 🟩", " 1️⃣", " 1️⃣", "1️⃣"]
h6 = ["6 ", "⬜️", "1️⃣", " 1️⃣", " 🟩", " 🟩", " 🟩", "🟩"]
h7 = ["7 ", "⬜️", "⬜️", " 1️⃣", " 🟩", " 🟩", " 🟩", "🟩"]

#hoja de respuestas nivel 1
cc = "  1 2 3 4 5 6 7"
hr1 = ["1 ", "🚩", "1️⃣", " 1️⃣", " 🚩", " 🚩", " 1️⃣", "🟩"]
hr2 = ["2 ", "2️⃣", "2️⃣", " 2️⃣", " 2️⃣", " 2️⃣", " 1️⃣", "🟩"]
hr3 = ["3 ", "2️⃣", "🚩", " 1️⃣", " 🟩", " 1️⃣", " 1️⃣", "1️⃣"]
hr4 = ["4 ", "🚩", "2️⃣", " 1️⃣", " 🟩", " 1️⃣", " 🚩", "1️⃣"]
hr5 = ["5 ", "1️⃣", "1️⃣", " 🟩", " 🟩", " 1️⃣", " 1️⃣", "1️⃣"]
hr6 = ["6 ", "1️⃣", "1️⃣", " 1️⃣", " 🟩", " 🟩", " 🟩", "🟩"]
hr7 = ["7 ", "1️⃣", "🚩", " 1️⃣", " 🟩", " 🟩", " 🟩", "🟩"]

resp = [cc, hr1, hr2, hr3, hr4, hr5, hr6, hr7]
mapa1 = [cc, h1,h2, h3, h4, h5, h6, h7]

while True:
    com = int(input("Ingresa un '0' para comenzar: ")) #inicio del programa
    if com == 0:
        break


if com == 0:
    print("1er nivel, 🚩7")
    for fila in mapa1:
      print(" ".join(fila))
    vidas = 3
    x = 0

    while x < 9: #numero de movimientos especificos
        horizontal = int(input("Ingresa la fila: "))  # Conversión a entero
        vertical = int(input("Ingresa la columna: "))  # Conversión a entero

        if resp[horizontal][vertical] == "🚩" or resp[horizontal][vertical] == " 🚩" : #si usuario cae en mina
            x-=1
            vidas -= 1  #resta de vidas
            print("¡Has encontrado una mina! Te quedan", vidas, "vidas.") #imprimir vidas restantes
            mapa1[horizontal][vertical] = resp[horizontal][vertical]
            if vidas == 0:
                mapa1[horizontal][vertical] = resp[horizontal][vertical]
                print("Perdiste") #se acabo nivel 1
                break
        else:
            mapa1[horizontal][vertical] = resp[horizontal][vertical]

        for fila in mapa1:
          print(" ".join(fila))

        x += 1
    print("Terminó el primer nivel")
#2 nivel 7x7, minas=10

#nivel 2 tablero inicial
cc = "    1   2   3   4   5   6   7"
hj1 = ["1", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
hj2 = ["2", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
hj3 = ["3", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
hj4 = ["4", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
hj5 = ["5", "1️⃣", "3️⃣", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
hj6 = ["6", "🟩", "1️⃣", "1️⃣", "2️⃣", "⬜️", "2️⃣", "1️⃣"]
hj7 = ["7", "🟩", "🟩", "🟩", "1️⃣", "⬜️", "1️⃣", "🟩"]


#nivel 2 hoja de respuestas
cc = " 1 2 3 4 5 6 7"
hr1 = ["1", "1️⃣", "1️⃣", "2️⃣", "🚩", "2️⃣", "2️⃣", "2️⃣"]
hr2 = ["2", "1️⃣", "🚩", "2️⃣", "1️⃣", "2️⃣", "🚩", "🚩"]
hr3 = ["3", "1️⃣", "2️⃣", "2️⃣", "1️⃣", "2️⃣", "3️⃣", "3️⃣"]
hr4 = ["4", "1️⃣", "3️⃣", "🚩", "2️⃣", "1️⃣", "🚩", "2️⃣"]
hr5 = ["5", "🚩", "3️⃣", "🚩", "3️⃣", "2️⃣", "3️⃣", "🚩"]
hr6 = ["6", "1️⃣", "2️⃣", "1️⃣", "2️⃣", "🚩", "2️⃣", "1️⃣"]
hr7 = ["7", "🟩", "🟩", "🟩", "1️⃣", "1️⃣", "1️⃣", "🟩"]

resp = [cc, hr1, hr2, hr3, hr4, hr5, hr6, hr7]
mapa1 = [cc, hj1, hj2, hj3, hj4, hj5, hj6, hj7]


if com == 0:
    print("2er nivel, 🚩10")
    for fila in mapa1:
      print(" ".join(fila))
    vidas = 3
    x = 0
    while x < 25: #numero de intentos
        horizontal = int(input("Ingresa la fila: "))  # Conversión a entero
        vertical = int(input("Ingresa la columna: "))  # Conversión a entero

        if resp[horizontal][vertical] == "🚩" or resp[horizontal][vertical] == " 🚩" :
            x-=1
            vidas -= 1   #resta de vidas
            print("¡Has encontrado una mina! Te quedan", vidas, "vidas.") #imprimir numero de vidas restantes
            mapa1[horizontal][vertical] = resp[horizontal][vertical]
            if vidas == 0:
                mapa1[horizontal][vertical] = resp[horizontal][vertical]
                print("Perdiste") #se acaban vidas
                break
        else:
            mapa1[horizontal][vertical] = resp[horizontal][vertical]

        for fila in mapa1:
          print(" ".join(fila))

        x += 1
    print("Completaste el segundo nivel")

#3 nivel 7x7, minas=13

#nivel 3 tablero inicial
cc = " 1 2 3 4 5 6 7"
h1 = ["1", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
h2 = ["2", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
h3 = ["3", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
h4 = ["4", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
h5 = ["5", "1️⃣", "3️⃣", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
h6 = ["6", "🟩", "1️⃣", "1️⃣", "2️⃣", "⬜️", "⬜️", "⬜️"]
h7 = ["7", "🟩", "🟩", "🟩", "1️⃣", "⬜️", "⬜️", "⬜️"]


#nivel 3 hoja de respuestas
cc = " 1 2 3 4 5 6 7"
hr1 = ["1", "1️⃣", "🚩", "2️⃣", "1️⃣", "🚩", "2️⃣", "🚩"]
hr2 = ["2", "1️⃣", "1️⃣", "2️⃣", "🚩", "3️⃣", "4️⃣", "3️⃣"]
hr3 = ["3", "1️⃣", "2️⃣", "2️⃣", "3️⃣", "🚩", "2️⃣", "🚩"]
hr4 = ["4", "🚩", "3️⃣", "🚩", "3️⃣", "2️⃣", "3️⃣", "2️⃣"]
hr5 = ["5", "1️⃣", "3️⃣", "🚩", "2️⃣", "1️⃣", "🚩", "2️⃣"]
hr6 = ["6", "🟩", "1️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "🚩"]
hr7 = ["7", "🟩", "🟩", "🟩", "1️⃣", "🚩", "🚩", "2️⃣"]

resp = [cc, hr1, hr2, hr3, hr4, hr5, hr6, hr7]
mapa1 = [cc, h1, h2, h3, h4, h5, h6, h7]


if com == 0:
    print("3er nivel, 🚩13")
    for fila in mapa1:
      print(" ".join(fila))
    vidas = 3
    x = 0
    while x < 26: #numero de intentos
        horizontal = int(input("Ingresa la fila: "))  # Conversión a entero
        vertical = int(input("Ingresa la columna: "))  # Conversión a entero

        if resp[horizontal][vertical] == "🚩" or resp[horizontal][vertical] == " 🚩" :
            x-=1
            vidas -= 1 #resta de vidas
            print("¡Has encontrado una mina! Te quedan", vidas, "vidas.")
            mapa1[horizontal][vertical] = resp[horizontal][vertical]
            if vidas == 0:
                mapa1[horizontal][vertical] = resp[horizontal][vertical]
                print("Perdiste")
                break
        else:
            mapa1[horizontal][vertical] = resp[horizontal][vertical]

        for fila in mapa1:
          print(" ".join(fila))

        x += 1
    print("Acabaste todos, felicidades")

  
  






