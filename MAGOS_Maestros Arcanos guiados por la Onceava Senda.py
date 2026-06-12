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
    def __init__ (self,ID,nombre,elemento,hp,fuerza,armadura,velocidad,nivel):
        self.ID = ID
        self.nombre = nombre
        self.elemento = elemento
        self.hp = hp
        self.fuerza = fuerza
        self.armadura = armadura
        self.velocidad = velocidad
        self.nivel = nivel

    def repartir_Stats(self):
        raise NotImplementedError("variable repartir no declarada")
    
    def mostrar_Stats(self):
        print(f"HP: {self.hp}\nFuerza: {self.fuerza}\nArmadura: {self.armadura}\nVelocidad: {self.velocidad}\nNivel: {self.nivel}")


class Jugador(Mago):

    def repartir_Stats(self):
        puntos = 4
        while puntos != 0:
                eleccion = int(input(f"tienes {puntos} puntos a repartir \n selecciona a que le quieres asignar el siguiente punto\n1-HP\n2-Fuerza\n3-Armadura\n4-Velocidad:\n"))
                if eleccion == 1:
                    self.hp += 1
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


class Rival(Mago):

    def repartir_Stats(self):

        puntos = 4 * (self.nivel - (2*(self.nivel//10)))

        while puntos > 4:
            self.hp += 1
            self.fuerza += 1
            self.armadura += 1
            self.velocidad += 1
            puntos -= 4
        while puntos > 0:
            self.velocidad +=1
            puntos -= 1
            
        

class Jefe(Mago):

    def repartir_Stats(self):
            
        puntos = 4 * self.nivel 

        while puntos > 8:
            self.hp += 1
            self.fuerza += 1
            self.armadura += 1
            self.velocidad += 1
            puntos -= 4
        while puntos > 0:
            self.hp += 1
            self.velocidad +=1
            puntos -= 2

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

    player1 = Jugador(idJugador,nombre_Usuario,elemento_Jugador,20,5,5,5,0)
       
    return player1


player1 = nombrar_Jugador()
player1.nivel = 1
player1.repartir_Stats()
rival1 = Rival(1,"prueba1","Agua",20,5,5,5,2)
jefe1 = Jefe(1,"jefeprueba","Neutral",20,5,5,5,10)
rival1.repartir_Stats()
jefe1.repartir_Stats()
player1.mostrar_Stats()
rival1.mostrar_Stats()
jefe1.mostrar_Stats()