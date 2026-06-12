class valoracionCaracter():
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
    


class Mago:
    def __init__ (self,ID,nombre,elemento,hpActual,hpMax,fuerza,armadura,velocidad,nivel):
        self.ID = ID
        self.nombre = nombre
        self.elemento = elemento
        self.hpActual = hpActual
        self.hpMax = hpMax
        self.fuerza = fuerza
        self.armadura = armadura
        self.velocidad = velocidad
        self.nivel = nivel

    def repartir_Stats(self):
        raise NotImplementedError("funcion repartir no declarada")
    
    def mostrar_Stats(self):
        print(f"{self.nombre}:\nHP: {self.hpActual}/{self.hpMax}\nFuerza: {self.fuerza}\nArmadura: {self.armadura}\nVelocidad: {self.velocidad}\nNivel: {self.nivel}")


class Jugador(Mago):

    def repartir_Stats(self):
        puntos = 4
        while puntos > 0:
                eleccion = int(input(f"tienes {puntos} puntos a repartir \n selecciona a que le quieres asignar el siguiente punto\n1-HP\n2-Fuerza\n3-Armadura\n4-Velocidad:\n"))
                if eleccion == 1:
                    self.hpMax += 1
                    puntos -= 1
                elif eleccion == 2:
                    self.fuerza += 1
                    puntos -= 1
                elif eleccion == 3:
                    self.armadura += 1
                    puntos -= 1
                elif eleccion == 4:
                    self.velocidad += 1
                    puntos -= 1
                else:
                    print("Estadistica no existe")

    def subir_Nivel(self):
        self.nivel += 1
        self.repartir_Stats()


class Rival(Mago):

    def repartir_Stats(self):

        puntos = 4 * (self.nivel - (2*(self.nivel//10)))

        while puntos > 4:
            self.hpMax += 1
            self.fuerza += 1
            self.armadura += 1
            self.velocidad += 1
            puntos -= 4
        while puntos > 0:
            self.velocidad +=1
            puntos -= 1
        self.hpActual = self.hpMax        

class Jefe(Mago):

    def repartir_Stats(self):
            
        puntos = 4 * self.nivel 

        while puntos > 8:
            self.hpMax += 1
            self.fuerza += 1
            self.armadura += 1
            self.velocidad += 1
            puntos -= 4
        while puntos > 0:
            self.hpMax += 1
            self.velocidad +=1
            puntos -= 2
        self.hpActual = self.hpMax

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
            elemento_Jugador = "Agua"
        elif elemento_Jugador == 2:
            elemento_Jugador = "Fuego"
        elif elemento_Jugador == 3:
            elemento_Jugador = "Planta"
        elif elemento_Jugador == 4:
            elemento_Jugador = "Tierra"
        elif elemento_Jugador == 5:
            elemento_Jugador = "Neutral"
        else:
            print("Elemento no existe")
            elemento_Jugador = "error"

    player1 = Jugador(idJugador,nombre_Usuario,elemento_Jugador,20,20,5,5,5,0)
       
    return player1

def enfrentamiento(mago1,mago2):
    if mago1.velocidad > mago2.velocidad:
        primero = mago1
        segundo = mago2
    else:
        primero = mago2
        segundo = mago1
         
    while primero.hpActual > 0 and segundo.hpActual > 0:
        daño =  primero.fuerza - segundo.armadura
        if daño < 1:
            daño = 1
        segundo.hpActual -= daño
        print(f"el mago {primero.nombre} ataco y causo {daño} a mago {segundo.nombre}\nvida {primero.nombre} {primero.hpActual}/ {segundo.hpActual} {segundo.nombre}")
        daño =  segundo.fuerza - primero.armadura
        if daño < 1:
            daño = 1
        if segundo.hpActual > 0:
            primero.hpActual -= daño 
            print(f"el mago {segundo.nombre} ataco y causo {daño} a mago {primero.nombre}\nvida {primero.nombre} {primero.hpActual}/ {segundo.hpActual} {segundo.nombre}")
        print(f"{mago1.nombre}: {mago1.hpActual}/{mago1.hpMax}   ---   {mago2.nombre}: {mago2.hpActual}/{mago2.hpMax}")
        input()

    if primero.hpActual > segundo.hpActual:
        print(f"EL MAGO {primero.nombre} derroto a {segundo.nombre}")
        ganador = primero
    else:
        print(f"EL MAGO {segundo.nombre} derroto a {primero.nombre}")
        ganador = segundo
    
    if ganador == mago1:
        mago1.subir_Nivel()
        mago1.hpActual += ((mago1.hpMax * 3)//10)
    if mago1.hpActual > mago1.hpMax:
        mago1.hpActual = mago1.hpMax
        
    mago1.mostrar_Stats()





player1 = nombrar_Jugador()
player1.subir_Nivel()
rival1 = Rival(1,"rival1","Agua",20,20,5,5,5,1)
jefe1 = Jefe(1,"jefeprueba","Neutral",20,20,5,5,5,10)
rival1.repartir_Stats()
jefe1.repartir_Stats()
player1.mostrar_Stats()
rival1.mostrar_Stats()
jefe1.mostrar_Stats()

enfrentamiento(player1,rival1)