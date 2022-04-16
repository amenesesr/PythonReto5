'''
El director del Programa de Ingeniería de Sistemas de la Universidad El Bosque, a raíz de la
participación en un proyecto muy especial con el MinTic, requiere poder generar una agenda
con los datos de nombre y apellido, número de cédula y el número celular de todos los
beneficiarios del proyecto, para poder hacerles algún seguimiento en su proceso de formación.
Dicha agenda deberá ser almacenada en un archivo de texto en el directorio activo con el
nombre agenda.txt. Cada beneficiario ocupará tres líneas en el archivo, una por cada campo
(nombre y apellido, cedula, celular). Por ejemplo, el beneficiario José Castro con cédula
18145321 y celular 3091234567 y la beneficiaria Sofía Vergara con cédula 52120318 y celular
3109876543, quedarían así en el archivo:

José Castro
18145321
3091234567
Sofía Vergara
52120318
3109876543

El director del Programa de Ingeniería de Sistemas le ha solicitado a usted como programador,
que le desarrolle un programa en lenguaje Python que le permita:

• Crear el archivo agenda.txt leyendo los datos desde el teclado (por lo menos 10
beneficiarios). AUN NO

• Buscar en el archivo agenda.txt el número celular de un beneficiario, dados su nombre
y apellido. AUN NO

• Añadir un nuevo beneficiario en la agenda.txt, al final del archivo. No debe haber otro
beneficiario con la misma cédula. YA

• Borrar un beneficiario de la agenda.txt dado su número de cédula. YA

• Buscar, añadir y borrar un beneficiario deberán ser funciones, que serán llamadas
dentro del programa principal. YA

• Mostrar en consola el listado completo de los beneficiarios del archivo agenda.txt. YA

• Mostrar en consola el listado de los beneficiarios cuyo nombre empieza por una letra
determinada. YA

• Presentar un menú con las diferentes opciones solicitadas para que el usuario pueda
decidir qué proceso desea realizar. YA

Autor: Alejandro Meneses R
Fecha: 30/05/2021
'''

lista = []
listadef = []
opcion = int(0)

def crear_archivo():
    archivo = open("agenda.txt","a")
    archivo.close()

def cargar_datos():

    archivo = open("agenda.txt","r")
    linea = archivo.readline()

    i = int (0)
    if linea:
        while linea:
            if linea [-1] == "\n":
                linea = linea[:-1]
                lista.append([i])
                lista[i] = (linea)
            linea = archivo.readline()
            i += 1
    archivo.close()

    a = 0
    x = 0
    for i in range(len(lista)):
        listadef.append([])
        for x in range(3):
            if a == len(lista):
                break
            listadef[i].append(lista[a])
            a +=1
        if a == len(lista):
                break
    listadef.sort()

def grabar_archivo():
    archivo = open('agenda.txt','w')
    for dato in listadef:
        archivo.write('{:<1}\n{:<1}\n{:<1}\n'.format(dato[0],dato[1],dato[2]))
    archivo.close()

def ingresar():
    i = int(0)
    x = int(0)
    nombre_temp = " "
    print('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓                                                                      ▓')
    print('   █  I N G R E S O  D E  B E N E F I C I A R I O S  A  L A  A G E N D A  █')
    print('   ▓                                                                      ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    nombre_temp = capturacadena("\t\t\tDigite el nombre completo del beneficiario: ")
    novacio = nombre_temp.isspace()
    nonumeros = nombre_temp.isalpha()
    nombre_temp = nombre_temp.title()
    cedula_temp = capturaentero("\n\t\t\tDigite la cedula del beneficiario: ")
    celular_temp = capturaentero("\n\t\t\tDigite el celular del beneficiario: ")
    for i in range(len(listadef)):
        if str(cedula_temp) == str(listadef[i][1]) :
            return pausa('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n   ▒                                                                      ▒\n   ▓                E L  B E N E F I C I A R I O  {:<15}         ▓\n   █                                                                      █\n   ▓                        Y A  E X I S T E                              ▓\n   ▒                                                                      ▒\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n\t\t\t\t\tPresione ENTER para continuar...'.format(cedula_temp))
    x = len(listadef)
    listadef.append([])
    listadef[x].append(nombre_temp)
    listadef[x].append(cedula_temp)
    listadef[x].append(celular_temp)
    print('\n\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓                E L  B E N E F I C I A R I O  {:<15}         ▓'.format(cedula_temp))
    print('   █                                                                      █')
    print('   ▓           H A  S I D O  R E G I S T R A D O  C O N  E X I T O        ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    listadef.sort()
    grabar_archivo()
    pausa("\t\t\t\t\tPresione ENTER para continuar...")

def borrar():
    i = 0
    centinela = int(0)
    indice = int(0)
    print('\n\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓                                                                      ▓')
    print('   █     B O R R A R  B E N E F I C I A R I O S  D E  L A  A G E N D A    █')
    print('   ▓                                                                      ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    cedula_temp = capturaentero ("           Digite la cedula del beneficiario que desea eleminar: ")
    print('\t══════════════════════════════════════════════════════════════════════')
    for dato in listadef:
        if str(cedula_temp) == str(listadef[i][1]):
            print('\n\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
            print('   ▒                                                                      ▒')
            print('   ▓                E L  B E N E F I C I A R I O  {:<15}         ▓'.format(dato[1]))
            print('   █                                                                      █')
            print('   ▓               H A  S I D O  B O R R A D O  C O N  E X I T O          ▓')
            print('   ▒                                                                      ▒')
            print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n')
            print("\t\tNOMBRE  : ",dato[0])
            print("\t\tCEDULA  : ",dato[1])
            print("\t\tCELULAR : ",dato[2])
            indice = listadef.index(dato)
            listadef.pop(indice)
            print('\t────────────────────────────────────────────────────────────────────────')
            pausa("\t\t\t\t\tPresione ENTER para continuar...")
            break
        else:
            centinela += 1
            if centinela == (len(listadef)):
                print("\t\tNO EXISTE UN BENEFICIARIO CON CEDULA {:<15}".format(cedula_temp).center(75))
                print('\t══════════════════════════════════════════════════════════════════════')
                pausa("\t\t\t\t\tPresione ENTER para continuar...")
                break
        i += 1
    grabar_archivo()

def buscar_letra():
    i = int(0)
    x = int(0)
    centinela = int(0)
    print('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓             B U S Q U E D A  D E  B E N E F I C I A R I O S          ▓')
    print('   █                                                                      █')
    print('   ▓        P O R  L A  P R I M E R A  L E T R A  D E L  N O M B R E      ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    letra = capturacadena('\t\tDigite la primera letra del nombre para realizar la búsqueda: ')
    letra = letra.upper()
    print('\n\n\t════════════════════════════════════════════════════════════════════════════════')
    print('\tBENEFICIARIOS QUE SU NOMBRE EMPIEZA CON LA LETRA {:<1}'.format(letra).center(80))

    for dato in listadef:
        if letra not in str(dato[0]):
            centinela += 1
        else:
            break
        if centinela == len(listadef):
            print('\t────────────────────────────────────────────────────────────────────────────────')
            print("\tNO HAY BENEFICIARIOS QUE EMPIECEN CON LA LETRA {:<1}".format(letra).center(80))
            break

    for i in range(len(listadef)):
        if letra == str(listadef[i][0][0]):
                print('\t────────────────────────────────────────────────────────────────────────────────')
                print('\t\tNOMBRE  : ',listadef[i][0])
                print('\t\tCEDULA  : ',listadef[i][1])
                print('\t\tCELULAR : ',listadef[i][2])
                x += 1
    print('\t════════════════════════════════════════════════════════════════════════════════')
    print("\tCANTIDAD TOTAL DE BENEFICIARIOS {:<15} ".format(x).center(95))
    print('\t════════════════════════════════════════════════════════════════════════════════')
    pausa("\t\t\t\t\t\tPresione ENTER para continuar...")

def buscar_cedula():
    i = int(0)
    centinela = int(0)
    print('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓            B U S Q U E D A  D E  B E N E F I C I A R I O S           ▓')
    print('   █                                                                      █')
    print('   ▓                          P O R  C E D U L A                          ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    cedula_temp = capturaentero('\t\tDigite la cedula del beneficiario para realizar la búsqueda: ')
    print("")
    print('DATOS DEL BENEFICIARIO CON CEDULA {:<15}'.format(cedula_temp).center(85))
    for i in range(len(listadef)):
        if str(cedula_temp) == listadef[i][1]:
            print('\t══════════════════════════════════════════════════════════════════════')
            print('\t\tNOMBRE  : ',listadef[i][0])
            print('\t\tCEDULA  : ',listadef[i][1])
            print('\t\tCELULAR : ',listadef[i][2])
            print('\t══════════════════════════════════════════════════════════════════════')
            break
        else:
            centinela += 1
            if centinela == (len(listadef)):
                print('══════════════════════════════════════════════════════════════════════')
                print("NO EXISTE UN BENEFICIARIO CON CEDULA {:<15}".format(cedula_temp).center(85))
                print('══════════════════════════════════════════════════════════════════════')
    pausa("\t\t\t\t\tPresione ENTER para continuar...")

def buscar_celular():
    i = int(0)
    x = int(0)
    centinela = int(0)
    print('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓              B U S Q U E D A  D E  C E L U L A R  P O R              ▓')
    print('   █                                                                      █')
    print('   ▓                   N O M B R E  C O M P L E T O                       ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    nombre = capturacadena('\tPor favor digite el nombre del beneficiario para realizar la búsqueda: ')
    nombre = nombre.title()
    print('\n\n\t══════════════════════════════════════════════════════════════════════')
    print('\tCELULAR DEL BENEFICIARIO {:<1}'.format(nombre).center(70).upper())

    for i in range(len(listadef)):
        if str(nombre) == listadef[i][0]:
            print('\t══════════════════════════════════════════════════════════════════════')
            print('\t\tNOMBRE  : ',listadef[i][0])
            print('\t\tCELULAR : ',listadef[i][2])
            print('\t══════════════════════════════════════════════════════════════════════')
            break
        else:
            centinela += 1
            if centinela == (len(listadef)):
                print('\t══════════════════════════════════════════════════════════════════════')
                print("NO EXISTE UN BENEFICIARIO CON EL NOMBRE {:<15}".format(nombre).center(85))
                print('\t══════════════════════════════════════════════════════════════════════')
    pausa("\t\t\t\t\tPresione ENTER para continuar...")

def buscar_por_nombre():
    i = int(0)
    x = int(0)
    centinela = int(0)
    print('\n\n   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('   ▒                                                                      ▒')
    print('   ▓         B U S Q U E D A  D E  D A T O S  C O M P L E T O S           ▓')
    print('   █                                                                      █')
    print('   ▓                P O R  N O M B R E  C O M P L E T O                   ▓')
    print('   ▒                                                                      ▒')
    print('   ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░\n\n')
    nombre = capturacadena('\tPor favor digite el nombre del beneficiario para realizar la búsqueda: ')
    nombre = nombre.title()
    print('\n\n\t══════════════════════════════════════════════════════════════════════')
    print('\tDATOS DEL BENEFICIARIO {:<1}'.format(nombre).center(70).upper())

    for i in range(len(listadef)):
        if str(nombre) == listadef[i][0]:
            print('\t══════════════════════════════════════════════════════════════════════')
            print('\t\tNOMBRE  : ',listadef[i][0])
            print('\t\tCEDULA  : ',listadef[i][1])
            print('\t\tCELULAR : ',listadef[i][2])
            print('\t══════════════════════════════════════════════════════════════════════')
            break
        else:
            centinela += 1
            if centinela == (len(listadef)):
                print('\t══════════════════════════════════════════════════════════════════════')
                print("NO EXISTE UN BENEFICIARIO CON EL NOMBRE {:<15}".format(nombre).center(85))
                print('\t══════════════════════════════════════════════════════════════════════')
    pausa("\t\t\t\t\tPresione ENTER para continuar...")

def ver_lista():
    print('\n\n\t══════════════════════════════════════════════════════════════════════')
    print('\tLISTA COMPLETA DE BENEFICIARIOS EL BOSQUE'.center(70))
    print('\t══════════════════════════════════════════════════════════════════════')
    for dato in listadef:
        print('\t\tNOMBRE  : {:<1}\n\t\tCEDULA  : {:<1}\n\t\tCELULAR : {:<1}'.format(dato[0],dato[1],dato[2]))
        print('\t──────────────────────────────────────────────────────────────────────')
    print("\tCANTIDAD TOTAL DE BENEFICIARIOS {:<15} ".format(len(listadef)).center(85))
    print('\t══════════════════════════════════════════════════════════════════════')
    pausa("\t\t\t\t\tPresione ENTER para continuar...")

def errormenu():
        print('\n\n\n   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
        print('   ░                                                             ░')
        print('   ▒        ░ ░ ▒ ▒ ▓ ▓ █ █   E R R O R !  █ █ ▓ ▓ ▒ ▒ ░ ░       ▒')
        print('   ▓                                                             ▓')
        print('   █                        LA OPCION {:<5}                      █'.format(opcion))
        print('   █                                                             █')
        print('   ▓                  NO SE ENCUENTRA EN EL MENU                 ▓')
        print('   ▒                                                             ▒')
        print('   ░                                                             ░')
        print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░\n\n')
        pausa("\t\t\t\t\tPresione ENTER para continuar...")

def fin():
        print('\n\n   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░')
        print('   ░                                                             ░')
        print('   ▒   ░ ░ ▒ ▒ ▓ ▓ █ █  H A S T A   L U E G O  █ █ ▓ ▓ ▒ ▒ ░ ░   ▒')
        print('   ▓                                                             ▓')
        print('   █                 Usted ha salido del sistema...              █')
        print('   ▓                                                             ▓')
        print('   ▒   ░▒▓█ S U  S E S I O N  H A  S I D O  G R A B A D A █▓▒░   ▒')
        print('   ░                                                             ░')
        print('   ░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████████████▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░\n\n')
        grabar_archivo()
        pausa("\t\t\t\t\tPresione ENTER para continuar...")

def menu():
    print('                                                      ')
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓███ ▒ █ ▒ ████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')
    print('   ▒                ░ ▒ ▓ █ █ ▓ ▒ ░                  ▒')
    print('   ▓ ░ ▒ ▓ █ AGENDA BENEFICIARIOS EL BOSQUE █ ▓ ▒ ░  ▓')
    print('   ▒                ░ ▒ ▓ █ █ ▓ ▒ ░                  ▒')
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓████ ▒ █ ▒ ████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')
    print('   ░                                                 ░')
    print('   ░  ☺ INGRESAR BENEFICIARIO               OPCION 1 ░')
    print('   ▒  ☻ BORRAR BENEFICIARIO POR CEDULA      OPCION 2 ▒')
    print('   ▓  ☺ LISTA DE BENEFICIARIOS POR LETRA    OPCION 3 ▓')
    print('   █  ☻ BUSCAR BENEFICIARIO POR CEDULA      OPCION 4 █')
    print('   █  ☺ BUSCAR CELULAR POR NOMBRE COMPLETO  OPCION 5 █')
    print('   █  ☻ BUSCAR DATOS COMPLETOS POR NOMBRE   OPCION 6 █')
    print('   █  ☺ VER TODA LA LISTA DE BENEFICIARIOS  OPCION 7 █')
    print('   █                                                 █')
    print('   ▓  ────────────────────────────────────────────── ▓')
    print('   ▒                                                 ▒')
    print('   ░            S A L I R   O P C I O N   0          ░')
    print('   ░                                                 ░')
    print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓████ ▒ █ ▒ ████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')

def capturaentero (mensaje):
    while True:
        try:
            num = int(input(mensaje))
            break
        except:
            error("\n\tEL DATO INGRESADO DEBE SER NUMERICO, por favor digite nuevamente: \n")
    return num

def capturacadena(mensaje):
    centinela = int(0)
    while True:
        try:
            cadena = str(input(mensaje))
            while True:
                for i in range (len(cadena)):
                    if (cadena[i].isdecimal() == True) or (cadena.isspace() == True) or (len(cadena) == 0):
                        cadena = ""
                        centinela = 0
                        i = 0
                        cadena = input("\n\tCAMPO VACIO O CONTIENE NUMEROS, por favor digite nuevamente: ")
                        break
                    else:
                        centinela += 1
                if (centinela == len(cadena)) and (len(cadena) == 0):
                    centinela = 0
                    cadena = input("\n\tCAMPO VACIO O CONTIENE NUMEROS, por favor digite nuevamente: ")
                elif centinela == (len(cadena)):
                    break
            break
        except:
            error("\n\tCAMPO VACIO O CONTIENE NUMEROS, por favor digite nuevamente: ")
            pass
    return cadena

def pausa(mensaje):
    while True:
        try:
            tecla = input(mensaje)
            break
        except:
            pass

def error(mensaje):
    print (mensaje)

crear_archivo()
cargar_datos()

while True:
        menu()
        print('   ░                                                 ░')
        opcion = capturaentero("\t\t\t\tPor favor digite una opcion: ")
        print('   ░                                                 ░')
        print('   ░░░░░░▒▒▒▒▒▒▓▓▓▓▓████ █ █ █ ████▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░')
        if opcion == 1:
            ingresar()
        elif opcion == 2:
            borrar()
        elif opcion == 3:
            buscar_letra()
        elif opcion == 4:
            buscar_cedula()
        elif opcion == 5:
            buscar_celular()
        elif opcion == 6:
            buscar_por_nombre()
        elif opcion == 7:
            ver_lista()
        elif opcion == 0:
            fin()
            break
        else:
            errormenu()