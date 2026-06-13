class valoracionCaracter:
    def __init__ (self, letra,valor):
        self.letra = letra
        self.valor = valor

listaCaracteres = [
    valoracionCaracter("a",1),
    valoracionCaracter("b",2),
    valoracionCaracter("c",3),
    valoracionCaracter("d",4),
    valoracionCaracter("e",5),
    valoracionCaracter("f",6),
    valoracionCaracter("g",7),
    valoracionCaracter("h",8),
    valoracionCaracter("i",9),
    valoracionCaracter("j",0),
    valoracionCaracter("k",1),
    valoracionCaracter("l",2),
    valoracionCaracter("m",3),
    valoracionCaracter("n",4),
    valoracionCaracter("o",5),
    valoracionCaracter("p",6),
    valoracionCaracter("q",7),
    valoracionCaracter("r",8),
    valoracionCaracter("s",9),
    valoracionCaracter("t",0),
    valoracionCaracter("u",1),
    valoracionCaracter("v",2),
    valoracionCaracter("w",3),
    valoracionCaracter("x",4),
    valoracionCaracter("y",5),
    valoracionCaracter("z",6)
    ]
    
class Elementos:
    def __init__ (self,nombre,fortaleza,debilidad):
        self._nombre = nombre
        self._fortaleza = fortaleza
        self._debilidad = debilidad
    
    def get_nombre(self):
        return self._nombre
    def get_fortaleza(self):
        return self._fortaleza
    def get_debilidad(self):
        return self._debilidad

Agua = Elementos("Agua","Fuego","Tierra")
Fuego = Elementos("Fuego","Planta","Agua")
Planta = Elementos("Planta","Tierra","Fuego")
Tierra = Elementos("Tierra","Agua","Planta")
Neutral = Elementos("Neutral","","")

class Mago:
    def __init__ (self,ID,nombre,elemento,hpActual,hpMax,fuerza,armadura,velocidad,nivel):
        self._ID = ID
        self._nombre = nombre
        self._elemento = elemento
        self._hpActual = hpActual
        self._hpMax = hpMax
        self._fuerza = fuerza
        self._armadura = armadura
        self._velocidad = velocidad
        self._nivel = nivel

    def get_ID(self):
        return self._ID
    def get_nombre(self):
        return self._nombre
    def get_elemento(self):
        return self._elemento
    def get_hpActual(self):
        return self._hpActual
    def get_hpMax(self):
        return self._hpMax
    def get_fuerza(self):
        return self._fuerza
    def get_armadura(self):
        return self._armadura
    def get_velocidad(self):
        return self._velocidad
    def get_nivel(self):
        return self._nivel
    


    def repartir_Stats(self):
        raise NotImplementedError("funcion repartir no declarada")
    
    def mostrar_Stats(self):
        print(f"{self.get_nombre()} de {self.get_elemento().get_nombre()}:\nHP: {self.get_hpActual()}/{self.get_hpMax()}\nFuerza: {self.get_fuerza()}\nArmadura: {self.get_armadura()}\nVelocidad: {self.get_velocidad()}\nNivel: {self.get_nivel()}")

    def calcular_Daño(self,objetivo):
        daño = self.get_fuerza() - objetivo.get_armadura()
        if daño < 1:
            daño=1
        if objetivo.get_elemento().get_nombre() == self.get_elemento().get_fortaleza():
            daño += (daño*5)//10
        elif objetivo.get_elemento().get_nombre() == self.get_elemento().get_debilidad():
            daño = (daño*5)//10       
        if daño < 1:
           daño=1
        return daño
        
    def recibir_Daño(self,daño):
        self._hpActual -= daño
        if self._hpActual < 0:
            self._hpActual = 0

    def curar(self,curacion):
        self._hpActual += curacion
        if self._hpActual > self._hpMax:
            self._hpActual = self._hpMax
        print(f"recupera {curacion}: vida {self._hpActual}/{self._hpMax}\n")

class Jugador(Mago):

    def repartir_Stats(self):
        puntos = 4
        while puntos > 0:
            eleccion = int(input(f"tienes {puntos} puntos a repartir \n selecciona a que le quieres asignar el siguiente punto\n1-HP\n2-Fuerza\n3-Armadura\n4-Velocidad:\n"))
            if eleccion == 1:
                self._hpMax += 1
                puntos -= 1
            elif eleccion == 2:
                self._fuerza += 1
                puntos -= 1
            elif eleccion == 3:
                self._armadura += 1
                puntos -= 1
            elif eleccion == 4:
                self._velocidad += 1
                puntos -= 1
            else:
                print("Estadistica no existe")

    def subir_Nivel(self):
        self._nivel += 1
        self.repartir_Stats()


class Rival(Mago):

    def repartir_Stats(self):

        puntos = 4 * (self.get_nivel() - (2*(self.get_nivel()//10)))

        while puntos > 4:
            self._hpMax += 1
            self._fuerza += 1
            self._armadura += 1
            self._velocidad += 1
            puntos -= 4
        while puntos > 0:
            self._velocidad +=1
            puntos -= 1
        self._hpActual = self._hpMax


class Jefe(Mago):

    def repartir_Stats(self):
            
        puntos = 4 * self._nivel

        while puntos > 8:
            self._hpMax += 1
            self._fuerza += 1
            self._armadura += 1
            self._velocidad += 1
            puntos -= 4
        while puntos > 0:
            self._hpMax += 1
            self._velocidad +=1
            puntos -= 2
        self._hpActual = self._hpMax

def nombrar_Jugador():
    nombre_Usuario = input("Ingrese el nombre del usuario ")
    idJugador = 0
    
    for i in nombre_Usuario:
        for j in listaCaracteres:
            if i.lower() == j.letra:
                idJugador += j.valor
    if idJugador < 1:
        idJugador = 713
    
    elemento_Jugador = "error"
    while elemento_Jugador == "error":
        elemento_Jugador = int(input("selecciona un elemento de la lista: \n1-Agua\n2-Fuego\n3-Planta\n4-Tierra\n5-Neutral\n:"))
        if elemento_Jugador == 1:
            elemento_Jugador = Agua
        elif elemento_Jugador == 2:
            elemento_Jugador = Fuego
        elif elemento_Jugador == 3:
            elemento_Jugador = Planta
        elif elemento_Jugador == 4:
            elemento_Jugador = Tierra
        elif elemento_Jugador == 5:
            elemento_Jugador = Neutral
        else:
            print("Elemento no existe")
            elemento_Jugador = "error"

    player1 = Jugador(idJugador,nombre_Usuario,elemento_Jugador,20,20,8,8,8,0)
       
    return player1

def enfrentamiento(mago1,mago2):
    turno = 1

    if mago1.get_velocidad() > mago2.get_velocidad():
        primero = mago1
        segundo = mago2
    else:
        primero = mago2
        segundo = mago1
         
    while primero.get_hpActual() > 0 and segundo.get_hpActual() > 0:
        print(f"turno {turno}")
        daño = primero.calcular_Daño(segundo)
        segundo.recibir_Daño(daño)
        print(f"el mago {primero.get_nombre()} ataco y causo {daño} a mago {segundo.get_nombre()}")
        daño = segundo.calcular_Daño(primero)
        if segundo.get_hpActual() > 0:
            primero.recibir_Daño(daño)
            print(f"el mago {segundo.get_nombre()} ataco y causo {daño} a mago {primero.get_nombre()}")
        print(f"{mago1.get_nombre()}: {mago1.get_hpActual()}/{mago1.get_hpMax()}           |      {mago2.get_nombre()}: {mago2.get_hpActual()}/{mago2.get_hpMax()}")
        print(f"{"▓"*mago1.get_hpActual()}{"░"* (mago1.get_hpMax()-mago1.get_hpActual())}   |   {"░"* (mago2.get_hpMax()-mago2.get_hpActual())}{"▓"*mago2.get_hpActual()}")
        input()
        turno += 1

    if primero.get_hpActual() > segundo.get_hpActual():
        print(f"EL Mago {primero.get_nombre()} derroto a {segundo.get_nombre()}")
        ganador = primero
    else:
        print(f"EL Mago {segundo.get_nombre()} derroto a {primero.get_nombre()}")
        ganador = segundo
    
    if ganador == mago1:
        mago1.subir_Nivel()
        mago1.curar((mago1.get_hpMax() * 3) // 10)
    
        
    mago1.mostrar_Stats()

class Generadores:
    def __init__ (self,estado):
        self._estado = estado
        
    def aleatorio(self): 
        self._estado = (self._estado * 120295 + 713) % (240214)
        return self._estado

def raiz_digital(numero):
    while numero >= 10:
        suma = 0
        for i in str(numero):
            suma += int(i)
        numero = suma
    return numero

# class Mapa:
#     def __init__ (self,semilla,posicion_Actual, siguiente0, siguiente1,valor_Camino):
#         self._semilla = semilla
#         self._posicion_Actual = posicion_Actual
#         self._siguiente0 = siguiente0
#         self._siguiente1 = siguiente1
#         self._valor_Camino = valor_Camino

#     camino=[]


#     def get_semilla(self):
#         return self._semilla
#     def get_posicion_Actual(self):
#         return self._posicion_Actual
#     def get_siguiente0(self):
#         return self._siguiente0
#     def get_siguiente1(self):
#         return self._siguiente1
#     def get_valor_Camino(self):
#         return self._valor_Camino

#     def generar_Semilla(self,idJugador):
#         verificador = 0
#         for i in str(idJugador):
#             verificador += int(i)
#         self._semilla = verificador
        

#     def generar_posicion_Actual(self):
#         avanzar = input("que camino quieres tomar? \n0-arriba\n1-abajo\n:")
#         self._camino.append(avanzar)
#         self._posicion_Actual += avanzar

#     def generar_Siguientes(self):
#         if self.validar_vs_Jefe() == True:
#             self._siguiente0 = "Jefe"
#             self._siguiente1 = "Jefe"
#         else:
#             self.generar_siguiente_no_Jefe()
#         return self._siguiente0,self._siguiente1

#     def  generar_siguiente_no_Jefe(self):
#         v1 = (self._semilla * len(self._camino)* self.generar_valor_Camino() ) + 1
#         for i in str(v1):
#             v1 += int(i)
#         v1 =v1 % 10
#         if v1 <= 5:
#             self._siguiente1= "Rival"
#         elif v1 <= 7:
#             self._siguiente1= "Cofre"
#         else:
#             self._siguiente1= "Curacion"
#         v2 = (self._semilla * len(self._camino)* self.generar_valor_Camino() ) + 2
#         for i in str(v2):
#             v2 += int(i)
#         v2 =v2 % 10
#         if v2 < 5:
#             self._siguiente0= "Rival"
#         elif v2 < 7:
#             self._siguiente0= "Cofre"
#         else:
#             self._siguiente0= "Curacion"
#         return self._siguiente0,self._siguiente1
        
#     def generar_valor_Camino(self):
#         valor = 0
#         for i in self._camino:
#             valor += int(i)
#         self._valor_Camino = valor

#     def validar_vs_Jefe(self):
#         if (len(self._camino)+1) % 10 == 0:
#             return True
#         else:
#             return False
        





listaRivales = [
    Rival("00","Sortilego",Agua,24,24,3,4,4,0),
    Rival("01","Debugorio",Agua,24,24,3,4,4,0),
    Rival("02","Hexomante",Fuego,18,18,8,4,5,0),
    Rival("03","Algoritus",Planta,22,22,4,6,3,0),
    Rival("04","Binarcano",Tierra,26,26,3,5,1,0),
    Rival("05","Stackomante",Neutral,20,20,5,5,5,0),
    Rival("06","Recursio",Agua,17,17,6,3,9,0),
    Rival("07","Kernelius",Fuego,15,15,10,4,6,0),
    Rival("08","Overflorius",Planta,19,19,4,8,4,0),
    Rival("09","Crashelio",Tierra,21,21,5,7,2,0),
    Rival("10","Punterius",Agua,30,30,1,2,2,0),
    Rival("11","Hexagoro",Fuego,16,16,11,3,5,0),
    Rival("12","Alquimia",Planta,18,18,6,5,6,0),
    Rival("13","Oraclon",Tierra,23,23,4,7,1,0),
    Rival("14","Trucanor",Agua,20,20,7,2,6,0),
    Rival("15","Nigrombo",Fuego,17,17,9,5,4,0),
    Rival("16","Musgorio",Planta,25,25,3,6,1,0),
    Rival("17","Pedrurio",Tierra,28,28,2,5,0,0),
    Rival("18","Cubistar",Agua,14,14,7,4,10,0),
    Rival("19","Esotron",Fuego,20,20,6,4,5,0)
]

listaJefes =[
    Jefe("0","Nullizador",Neutral,28,28,2,4,1,0),
    Jefe("1","Hexecutor",Fuego,16,16,10,4,5,0),
    Jefe("2","Rootmancer",Tierra,22,22,6,6,1,0),
    Jefe("3","CarlosTenebris",Neutral,25,25,7,2,1,0),
    Jefe("4","Bytemaster",Agua,18,18,5,3,9,0),
    Jefe("5","Compilator",Planta,24,24,4,5,2,0),
    Jefe("6","Daemonus",Fuego,19,19,7,4,5,0),
    Jefe("7","Fatalerror",Neutral,20,20,8,3,4,0),
    Jefe("8","CeszarW",Fuego,17,17,7,5,6,0),
    Jefe("9","CarluxSanguis",Neutral,26,26,6,2,1,0),
]










# jefe_Actual = listaJefes[8]
# player1 = nombrar_Jugador()
# #rival1.repartir_Stats()
# jefe_Actual.repartir_Stats()
# player1.mostrar_Stats()
# #rival1.mostrar_Stats()
# jefe_Actual.mostrar_Stats()
# enfrentamiento(player1,jefe_Actual)

for n in range(1, 1001):
    if raiz_digital(n) != 1 + (n - 1) % 9:
        print(f"DIFIERE en {n}")
print("prueba terminada")