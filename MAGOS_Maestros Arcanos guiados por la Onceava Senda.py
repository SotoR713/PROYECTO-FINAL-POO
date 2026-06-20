class Eventos:
    def __init__(self,nombre,caracter):
        self.nombre = nombre
        self.caracter = caracter

BRival = Eventos("Rival","⚔")
BJefe = Eventos("Jefe","☠")
Curacion = Eventos("Curacion","♥")
Cofre = Eventos("Cofre","[]")
 


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
    
    def calcular_Critico(self,rival):
        raise NotImplementedError("funcion critico no declarada")
    
    def evasion(self,rival):
        raise NotImplementedError("funcion evasion no declarada")
    
    def mostrar_Stats(self):
        print(f"{self.get_nombre()} de {self.get_elemento().get_nombre()}:\nHP: {self.get_hpActual()}/{self.get_hpMax()}\nFuerza: {self.get_fuerza()}\nArmadura: {self.get_armadura()}\nVelocidad: {self.get_velocidad()}\nNivel: {self.get_nivel()}\n")

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

    def curar(self,cantidadCurar):
        self._hpActual += cantidadCurar
        if self._hpActual > self._hpMax:
            self._hpActual = self._hpMax
        print(f"recupera {cantidadCurar}: vida {self._hpActual}/{self._hpMax}\n")


class Jugador(Mago):

    def subir_Nivel(self):
        self._nivel += 1
        self.repartir_Stats()
        self.mostrar_Stats()

    def repartir_Stats(self):
        puntos = 4
        while puntos > 0:
            esValor = False
            while esValor == False:
                eleccion = input(f"tienes {puntos} puntos a repartir \n selecciona a que le quieres asignar el siguiente punto\n1-HP\n2-Fuerza\n3-Armadura\n4-Velocidad:\n")
                esValor = eleccion.isdigit()
            eleccion = int(eleccion)

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


    def calcular_Critico(self,rival,aleato,daño):
        difVel = self._velocidad - rival._velocidad
        if difVel <= 0:
            porcentajeDaño = 0
        else:
            porcentajeDaño = (difVel*100)//rival._velocidad
        
        if porcentajeDaño > 30:
            porcentajeDaño= 30
        elif porcentajeDaño < 0:
            porcentajeDaño = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeDaño:
            daño += (daño*50)//100

        return daño
    
    def evasion(self, rival,aleato):
        difVel = self._velocidad - rival._velocidad
        if difVel <= 0:
            porcentajeEva = 0
        else:
            porcentajeEva = (difVel*100)//rival._velocidad
        
        if porcentajeEva > 20:
            porcentajeEva= 20
        elif porcentajeEva < 0:
            porcentajeEva = 0     

        activacion = aleato
        activacion = activacion % 100

        if activacion <= porcentajeEva:
            esquivar =0
        else:
            esquivar=1
        return esquivar
      
class Rival(Mago):

    def repartir_Stats(self):

        puntos = 4 * (self._nivel - (2*(self._nivel//10)))

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

    def calcular_Critico(self,rival,aleato,daño):

        porcentajeDaño = 10   

        activacion = aleato %100

        if activacion <= porcentajeDaño:
            daño += (daño*50)//100
        return daño
    
    def evasion(self, rival,aleato):

        porcentajeEva = 10   

        activacion = aleato %100

        if activacion <= porcentajeEva:
            esquivar=0
        else: 
            esquivar=1
        
        return esquivar

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
   
    def calcular_Critico(self,rival,aleato,daño):
        porcentajeDaño = 15
      
        activacion = aleato % 100

        if activacion <= porcentajeDaño:
            daño += (daño*50)//100
        return daño
        
    def evasion(self, rival,aleato):
        
        porcentajeEva = 10   

        activacion = aleato %100

        if activacion <= porcentajeEva:
            esquivar=0
        else: 
            esquivar=1
        return esquivar

def nombrar_Jugador():
    nombre_Usuario = input("Ingrese el nombre del usuario ")
    idJugador = "0"
    
    for i in nombre_Usuario:
        for j in listaCaracteres:
            if i.lower() == j.letra:
                idJugador += str(j.valor)
    idJugador=int(idJugador)            
    if idJugador < 1:
        idJugador = 713
    
    elemento_Jugador = "error"
    while elemento_Jugador == "error":
        esValor = False
        while esValor == False:
            elemento_Jugador = input("selecciona un elemento de la lista: \n1-Agua\n2-Fuego\n3-Planta\n4-Tierra\n5-Neutral\n:")
            esValor=elemento_Jugador.isdigit()
        elemento_Jugador=int(elemento_Jugador)
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

    player1.mostrar_Stats()
    print(f"Semilla: {idJugador}")
    return player1

def enfrentamiento(mago1,mago2,generador):
    turno = 1
    print("=============== ⚔  COMBATE  ⚔ ===============")
    mago1.mostrar_Stats()
    print("--------------------- VS ---------------------")
    mago2.mostrar_Stats()
    print("----------------------------------------------")
    input("Presione ENTER para iniciar")

    if mago1.get_velocidad() > mago2.get_velocidad():
        primero = mago1
        segundo = mago2
    else:
        primero = mago2
        segundo = mago1
         
    while primero.get_hpActual() > 0 and segundo.get_hpActual() > 0:
        print(f"turno {turno}")
        daño = primero.calcular_Daño(segundo)
        v1=daño
        daño = (primero.calcular_Critico(segundo,generador.aleatorio(),daño))*(segundo.evasion(primero,generador.aleatorio()))
        v2 = daño
        v3 = v2-v1
        segundo.recibir_Daño(daño)
        if v3 > 0:
            print("¡¡¡CRITICO!!!")
        elif v3<0:
            print(f"El Mago {primero.get_nombre()} ataco, pero {segundo.get_nombre()} esquivo el ataque")
        else:
            print(f"el mago {primero.get_nombre()} ataco y causo {daño} a mago {segundo.get_nombre()}")
        daño = segundo.calcular_Daño(primero)
        v1=daño
        daño = (segundo.calcular_Critico(primero,generador.aleatorio(),daño))*(primero.evasion(segundo,generador.aleatorio()))
        v2=daño
        v3=v2-v1
        if segundo.get_hpActual() > 0:
            primero.recibir_Daño(daño)
            if v3 > 0:
                print("¡¡¡CRITICO!!!")
            elif v3<0:
                print(f"El Mago {segundo.get_nombre()} ataco, pero {primero.get_nombre()} esquivo el ataque")            
            else:
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
    def __init__ (self,dado):
        self._dado = dado
        
    def aleatorio(self):
        self._dado = (self._dado * 120295 + 713) % (240214)
        return self._dado

def crear_Rival(numeroDado,valorPosicion_Actual):
    v1 = numeroDado * valorPosicion_Actual
    v1 = v1 %20

    nivelar = v1 % 10
    if nivelar > 7:
        valorNivel=valorPosicion_Actual-1
    elif nivelar > 4:
        valorNivel=valorPosicion_Actual-2
    else:
        valorNivel=valorPosicion_Actual

    valorPosicion_Actual=valorNivel

    if valorNivel<0:
        valorPosicion_Actual = 0

    asignacionElemento = (numeroDado % 10) // 2
    if asignacionElemento == 0:
        v2 = Agua
    elif asignacionElemento == 1:
        v2 = Fuego
    elif asignacionElemento == 2:
        v2 = Planta
    elif asignacionElemento == 3:
        v2 = Tierra
    else:
        v2 = Neutral

    valores_Rival = listaRivales[v1]
    rival_Actual = Rival(valores_Rival.get_ID(),valores_Rival.get_nombre(),v2,valores_Rival.get_hpActual(),valores_Rival.get_hpMax(),valores_Rival.get_fuerza(),valores_Rival.get_armadura(),valores_Rival.get_velocidad(),valorPosicion_Actual)
    rival_Actual.repartir_Stats()
    return rival_Actual
   
def crear_Jefe(numeroDado,valorPosicion_Actual):
    v1 = numeroDado
    v1 = v1 % 10

    asignacionElemento = (numeroDado % 10) // 2
    if asignacionElemento == 0:
        v2 = Agua
    elif asignacionElemento == 1:
        v2 = Fuego
    elif asignacionElemento == 2:
        v2 = Planta
    elif asignacionElemento == 3:
        v2 = Tierra
    else:
        v2 = Neutral


    valores_Jefe = listaJefes[v1]
    jefe_Actual = Jefe(valores_Jefe.get_ID(),valores_Jefe.get_nombre(),v2,valores_Jefe.get_hpActual(),valores_Jefe.get_hpMax(),valores_Jefe.get_fuerza(),valores_Jefe.get_armadura(),valores_Jefe.get_velocidad(),valorPosicion_Actual)
    jefe_Actual.repartir_Stats()
    return jefe_Actual

def raiz_digital(numero):
    while numero >= 10:
        suma = 0
        for i in str(numero):
            suma += int(i)
        numero = suma
    return numero



class Mapa:
    def __init__ (self,jugador):
        self._jugador = jugador
        self._generador = Generadores((jugador.get_ID()))
        self._posicion = 0
        self._camino = []
        self._historial =["█"]
        self._siguiente0 = BRival
        self._siguiente1 = BRival
        self._caminoHistorico = "█"

    def get_jugador(self):
        return self._jugador
    def get_generador(self):
        return self._generador
    def get_posicion(self):
        return self._posicion
    def get_camino(self):
        return self._camino
    def get_siguiente0(self):
        return self._siguiente0
    def get_siguiente1(self):
        return self._siguiente1
    
        
    def avanzar(self):
        eleccion = ""
        self._caminoHistorico=""
        for i in self._historial:
            self._caminoHistorico += i
        print(f" {" " * len(self._caminoHistorico)}{self.get_siguiente0().caracter}")
        print(self._caminoHistorico)
        print(f" {" " * len(self._caminoHistorico)}{self.get_siguiente1().caracter}")
        while eleccion != "0" and eleccion !="1":
            eleccion = input(f"seleccione a donde avanzar:\n0-{self.get_siguiente0().nombre}\n1-{self.get_siguiente1().nombre}\n")
                    
        self._camino.append(eleccion)
        self._posicion += 1   

        if eleccion == "0":
            return self.get_siguiente0()
        elif eleccion == "1":
            return   self.get_siguiente1()

    def validar_vs_Jefe(self):
        if (len(self._camino)) % 10 == 0:
            return True
        else:
            return False

    def generar_Siguientes(self):
        if self.validar_vs_Jefe() == True:
            self._siguiente0 = BJefe
            self._siguiente1 = BJefe
        else:
            self.generar_siguiente_no_Jefe()
        return self._siguiente0,self._siguiente1

    def  generar_siguiente_no_Jefe(self):
        v1 = (self.get_generador().aleatorio())
        v1=raiz_digital(v1)
        if v1 <= 6:
            self._siguiente1= BRival
        elif v1 <= 8:
            self._siguiente1= Cofre
        else:
            self._siguiente1= Curacion
        v2 = (self.get_generador().aleatorio() )
        v2=raiz_digital(v2)
        if v2 <= 6:
            self._siguiente0= BRival
        elif v2 <= 8:
            self._siguiente0= Cofre
        else:
            self._siguiente0= Curacion
        return self._siguiente0,self._siguiente1

    def resolver_Evento(self, evento):
        if evento == BRival:
            Brival = crear_Rival(self.get_generador().aleatorio(), len(self.get_camino()))
            enfrentamiento(self.get_jugador(), Brival,self.get_generador())
            largo=len(self._historial)-1
            if self._historial[largo] == "[":
                self._historial[largo]="→[⚔]"
            else:    
                self._historial.append("→⚔")
        elif evento == BJefe:
            bjefe = crear_Jefe(self.get_generador().aleatorio(), len(self.get_camino()))
            enfrentamiento(self.get_jugador(), bjefe,self.get_generador())
            self._historial.append( "→☠")
        elif evento == Curacion:
            self.get_jugador().curar(self.get_jugador().get_hpMax()*3//10)
            self._historial.append("→♥")
        elif evento == Cofre:
            v1 = (self.get_generador().aleatorio() * self.get_generador().aleatorio() )// 713
            v1 = raiz_digital(v1)

            if v1 <= 4:
                self.get_jugador().subir_Nivel()
                print("Subiste Nivel")
                self._historial.append("→[↑]")
            elif v1 <= 7:
                vidaCurar=self.get_jugador()._hpMax*3//10
                self.get_jugador().curar(vidaCurar)
                print(f"Recuperaste {vidaCurar} de vida")
                self._historial.append("→[♥]")
            elif v1 <= 8:
                self._historial.append("[")
                self.resolver_Evento(BRival)
                print("BATALLA")
            else:
                vidaDaño=self.get_jugador()._hpMax*1//10
                self.get_jugador().recibir_Daño(vidaDaño)
                print(f"Has perdido {vidaDaño}")
                self._historial.append("→[↓]")

     


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
    Jefe("2","Daemonus",Fuego,19,19,7,4,5,0),
    Jefe("3","ElProfeCaguamo",Tierra,22,22,6,6,1,0),
    Jefe("4","Bytemaster",Agua,18,18,5,3,9,0),
    Jefe("5","Compilator",Planta,24,24,4,5,2,0),
    Jefe("6","Piri",Neutral,25,25,7,2,1,0),
    Jefe("7","Fatalerror",Neutral,20,20,8,3,4,0),
    Jefe("8","CeszarW",Fuego,17,17,7,5,6,0),
    Jefe("9","CarluxSanguis",Neutral,26,26,6,2,1,0),
]

def titulo_Inicio():

    print("███╗   ███╗ █████╗  ██████╗  ██████╗ ███████╗")
    print("████╗ ████║██╔══██╗██╔════╝ ██╔═══██╗██╔════╝")
    print("██╔████╔██║███████║██║  ███╗██║   ██║███████╗")
    print("██║╚██╔╝██║██╔══██║██║   ██║██║   ██║╚════██║")
    print("██║ ╚═╝ ██║██║  ██║╚██████╔╝╚██████╔╝███████║")
    print("╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝")
    print("Maestros Arcanos Guiados por la Onceava Senda")
    print("")
    print("        --Tu nombre define tu senda-")
    print("     -La senda recuerda tus decisiones-")
    print("")

    

def titulo_Final():
    print(            " ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
    print(            "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print(            "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print(            "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print(            "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print(            " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")

















bucle_Juego=0
while bucle_Juego ==0:
    titulo_Inicio()     
    player1 = nombrar_Jugador()
    mapa1 = Mapa(player1)
    while mapa1.get_jugador().get_hpActual() >0:
        print(f"Posición: {mapa1.get_posicion()}")
        mapa1.resolver_Evento(mapa1.avanzar())
        mapa1.generar_Siguientes()
    print("senda: ",mapa1._caminoHistorico)
    print("Has llegado hasta la posicion:",mapa1.get_posicion())
    print("")
    titulo_Final()
    print("")
    input("presion ENTER para reiniciar")