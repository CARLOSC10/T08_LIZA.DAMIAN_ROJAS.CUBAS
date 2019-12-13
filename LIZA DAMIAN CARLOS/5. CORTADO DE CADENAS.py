#OPERACION CON CORTADO DE CADENAS

print("*EJERCICIO NRO 01")
#CORTADO
#                     10       20        30
#       012345678901234567890123456789012345678
python="HOLA MUNDO DE LA PROGRAMACION EN PYTHON"
#       987654321098765432109876543210987654321
#           -30       -20      -10
print(python[0:4]) #cortado de la palabra HOLA
print(python[17:28]) #cortado de la palabra PROGRAMACION
print(python[33:]) #cortado de la palabra PYTHON
print("")

print("*EJERCICIO NRO 02")
#CORTADO
#                    10       20        30      40
#      012345678901234567890123456789012345678901
frase="LA VIDAD ES UNA PREPARACION PARA EL FUTURO"
#      210987654321098765432109876543210987654321
#     -40    -30      -20      -10
print(frase[36:]) #cortado de la palabra FURURO
print(frase[16:23]) #cortado de la palabra PREPARA
print(frase[:27]) #cortado de la palabra LA VIDA ES UNA PREPARACION
print("")

print("*EJERCICIO NRO 03")
#CORTADO
#                  10       20        30
#    0123456789012345678901234567890123456
uni="UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO"
#    7654321098765432109876543210987654321
#        -30      -20      -10
print(uni[0:11]) #cortado de la palabra UNIVERSIDAD
print(uni[:20]) #cortado de la palabra UNIVERSIDAD NACIONAL
print(uni[:]) #cortado de la palabra UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO
print("")

print("*EJERCICIO NRO 04")
#CORTADO
#                      10       20        30       40
#        012345678901234567890123456789012345678901234567
frase01="CUALQUIER MOMENTO ES PERFECTO PARA APRENDER ALGO"
#        876543210987654321098765432109876543210987654321
#           -40      -30      -20      -10
print(frase01[10:17]) #cortado de la palabra MOMENTO
print(frase01[::-40]) #cortado de la palabra OE
print(frase01[::1]) #cortado de la palabra CUALQUIER MOMENTO ES PERFECTO PARA APRENDER ALGO
print("")

print("*EJERCICIO NRO 05")
#CORTADO
#                     10
#     01234567890123456789
mate="MATEMATICA BASICA II"
#     09876543210987654321
#      -20    -10
print(mate[7:]) #cortado de la palabra ICA BASICA II
print(mate[18:]) #cortado de la palabra II
print(mate[:4:10]) #cortado de la palabra M
print("")

print("*EJERCICIO NRO 06")
#CORTADO
#                       10       20      30
#         01234567890123456789012345678901234567
farmacia="FARMACIA INKA FARMA ESTA EN LAMBAYEQUE"
#         87654321098765432109876543210987654321
#          -30      -20      -10
print(farmacia[0:8]) #cortado de la palabra FARMACIA
print(farmacia[:]) #cortado de la palabra FARMACIA INKA FARMA ESTA EN LAMBAYEQUE
print(farmacia[::-1]) #cortado de la palabra EUQEYABMAL NE ATSE AMRAF AKNI AICAMRAF
print("")

print("*EJERCICIO NRO 07")
#CORTADO
#                     10       20
#        01234567890123456789012345678
frase02="EL APRENDISAJE ES EXPERIENCIA"
#        98765432109876543210987654321
#          -20       -10
print(frase02[::-2]) #cortado de la palabra ACERPES JSDEP E
print(frase02[3:14]) #cortado de la palabra APRENDISAJE
print(frase02[15:17]) #cortado de la palabra ES
print("")

print("*EJERCICIO NRO 08")
#CORTADO
#                      10       20
#        01234567890123456789012345678
frase03="EL TIEMPO TAMBIEN ES RELATIVO"
#        98765432109876543210987654321
#           -20      -10
print(frase03[21:]) #cortado de la palabra RELATIVO
print(frase03[:7:-9]) #cortado de la palabra OST
print(frase03[:]) #cortado de la palabra EL TIEMPO ES TAMBIEN ES RELATIVO
print("")

print("*EJERCICIO NRO 09")
#CORTADO
#                     10       20        30        40        50
#        01234567890123456789012345678901234567890123456789012345678
frase04="LA FELICIDAD CONSISTE EN PODER UNIR EL PRINCIPIO CON EL FIN"
#        98765432109876543210987654321098765432109876543210987654321
#           -50     -40       -30     -20         -10
print(frase04[:8:-45]) #cortado de la palabra NC
print(frase04[::-1]) #cortado de la palabra NIF LE NOC OIPICNIRP LE RINU REDOP NE ETSISNOC DADICILEF AL
print(frase04[:-5]) #cortado de la palabra LA FELICIDAD CONSISTE EN PODER UNIR EL PRINCIPIO CON E
print("")

print("*EJERCICIO NRO 10")
#CORTADO
#                     10       20        30
#      012345678901234567890123456789012345678
curso="INTRODUCCION A LA INGENERIA ELECTRONICA"
#      987654321098765432109876543210987654321
#           -30       -20      -10
print(curso[28:]) #cortado de la palabra ELECTRONICA
print(curso[:]) #cortado de la palabra INTRODUCCION A LA INGENERIA ELECTRONICA
print(curso[:4:-1]) #cortado de la palabra ACINORTCELE AIRENEGNI AL A NOICCUD
print("")

print("*EJERCICIO NRO 11")
#CORTADO
#                     10       20
#       01234567890123456789012345
nombre="CARLOS RONALDO LIZA DAMIAN"
#       65432109876543210987654321
#        -20     -10
print(nombre[0:6]) #cortado de la palabra CARLOS
print(nombre[:8:-8]) #cortado de la palabra NZN
print(nombre[:]) #cortado de la palabra CARLOS RONALDO LIZA DAMIAN
print("")


print("*EJERCICIO NRO 12")
#CORTADO
#                     10       20       30
#       012345678901234567890123456789012345
fisico="ALBERT EINSTEIN FUE UN FISICO ALEMAN"
#       654321098765432109876543210987654321
#        -30      -20      -10
print(fisico[::-2]) #cortado de la palabra NML CSFN U ITNETEL
print(fisico[::-1]) #cortado de la palabra NAMELA OCISIF NU EUF NIETSNIE TREBLA
print(fisico[0:15]) #cortado de la palabra ALBERT EINSTEIN
print("")

print("*EJERCICIO NRO 13")
#CORTADO
#                     10       20        30        40      50
#      012345678901234567890123456789012345678901234567890123
marca="MARCA DE ZAPATIILLAS: ADIDAS, NIKE, REEBOK, PUMAS, CAT"
#      432109876543210987654321098765432109876543210987654321
#        -50     -40       -30      -20       -10
print(marca[22:]) #cortado de la palabra ADIDAS, NIKE, REEBOK, PUMAS, CAT
print(marca[1:8:15]) #cortado de la palabra A
print(marca[:-2]) #cortado de la palabra MARCA DE ZAPATIILLAS: ADIDAS, NIKE, REEBOK, PUMAS, C
print("")

print("*EJERCICIO NRO 14")
#CORTADO
#                     10
#       0123456789012345678
calle= "JUAN FANNING GARCIA"
#       9876543210987654321
#         -10
print(calle[7:8]) #cortado de la palabra N
print(calle[:]) #cortado de la palabra JUAN FANNING GARCIA
print(calle[10::8]) #cortado de la palabra NA
print("")

print("*EJERCICIO NRO 15")
#CORTADO
#                     10       20        30        40       50
#        0123456789012345678901234567890123456789012345678901234
frase05="LA FUERZA Y EL CRECIMIENTO VIENEN A TRAVES DEL ESFUERSO"
#        5432109876543210987654321098765432109876543210987654321
#         -50     -40       -30     -20        -10
print(frase05[:]) #cortado de la palabra LA FUERZA Y EL CRECIMIENTO VIENEN A TRAVES DEL ESFUERSO
print(frase05[8:-17]) #cortado de la palabra A Y EL CRECIMIENTO VIENEN A TR
print(frase05[:-1]) #cortado de la palabra LA FUERZA Y EL CRECIMIENTO VIENEN A TRAVES DEL ESFUERS
print("")
