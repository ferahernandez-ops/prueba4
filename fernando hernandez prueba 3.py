pacientes = []

def mostrar_menu():
    print("\n=======MENU PRINCIPAL==========")
    print("1.agregue al paciente")
    print("2.busque al paciente")
    print("3.elimine al paciente")
    print("4.actualizar estado")
    print("5.mostrar al paciente")
    print("6.salir")
    print("\n================================")

def leer_opcion():
    while True:
        try:
            opcion =int(input("ingrese una de las opciones (1/6): "))

            if 1 <= opcion <=6:
                return opcion
            else:
                print("ERRO: debe ingresar una opcion valida.")

        except ValueError:
            print("ERROR: debe ingresar un numero valido")


def validar_nombre(nombre):
    return nombre.strip() !=""

def validar_edad(edad):
    return edad > 0

def validar_temperatura(temperatura):
    return 35.0 <= temperatura <= 42.0


def agregar_pacientes(lista):
    nombre=input("ingrese nombre del paciente: ")
    if not validar_nombre(nombre):
        print("ERROR: el nombre no debe estar vacio.")
        return
    
    try:
        edad = int(input("ingrese la edad del paciente: "))

        if not validar_edad(edad):
            print("ERROR: la edad debe ser mayor a cero.")
            return
    except ValueError:
        print("ERROR: la edad debe ser un numero entero.")
        return
    try:
        temperatura = float(input("ingrese la temperatura del paciente"))
        if not validar_temperatura(temperatura):
            print("ERRRO: La temperaura debe estar entre 35.0 y 42.0.")
            return
        
    except ValueError:
        print("ERROR: la temperatura debe ser un numero decimal.")
        return
    
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "temperatura": temperatura,
        "atendido": False
        }
    
    lista.append(paciente)

    print("paciente agregado correctamente")

def buscar_paciente(lista, nombre_buscar):
        for i in range(len(lista)):
            if lista[i]["nombre"]== nombre_buscar:
                return i
            
        return -1
    
def actualizar_estado(lista):
        for paciente in lista:
            if paciente["temperatura"] <= 37.0:
                paciente["atendido"] = True
            else:
                paciente["atendido"] = False

    
def mostrar_paciente(lista):
        
        actualizar_estado(lista)
        print("\n=== LISTA DE PACIENTES ===")

        if len(lista) == 0:
            print("no hay pacientes registrados")
            return
        for paciente in lista:

            print(f"nombre: {paciente['nombre']}")
            print(f"edad: {paciente['edad']}")
            print(f"temperatura: {paciente['temperatura']}")

            if paciente["atendido"]:
                print("estado: ATENDIDO")

            else:
                print("estado: REQUIERE ATENCION")

            print("*********************************************")
while True:
    mostrar_menu()
    opcion= leer_opcion()

    if opcion == 1:
        agregar_pacientes(pacientes)

    elif opcion == 2:
        nombre= input("nombre del paciente a buscar: ")
        posicion = buscar_paciente(pacientes, nombre)
        if posicion != -1:

            paciente = pacientes[posicion]
            print(f"paciente encontrado en posicion {posicion}")

            print(f"nombre: {paciente['nombre']}")
            print(f"edad: {paciente['edad']}")
            print(f"temperatura: {paciente['temperatura']}")
            print(f"Atendido: {paciente['atendido']}")
        else:
            print("paciente no encontrado.")

    elif opcion == 3:
        nombre = input("ingrese el nombre del paciente a eliminar: ")

        posicion = buscar_paciente(pacientes, nombre)

        if posicion !=-1:
            pacientes.pop(posicion)

            print("paciente eliminado correctamente.")

        else:
            print(f" el paciente '{nombre}' no se encuentra registrado")
    

    elif opcion == 4:

        actualizar_estado(pacientes)

        print("estado del paciente actualizado correctamente.")

    elif opcion == 5:
        mostrar_paciente(pacientes)

    elif opcion == 6:

        print(" GRACIAS por usar nuestro sistema vuelva pronto")
        break