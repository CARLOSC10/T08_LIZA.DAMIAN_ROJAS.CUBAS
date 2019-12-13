#CORTADO(SLICE) DE CADENAS
#                 10                 20         30        40       50         60        70        80       90        100       110       #indices positivos
#       01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567  #indices positivos
cadena="ALGUNOS ESCRITORES PERUANOS: MARIO VARGAS LLOSA, CESAR VALLEJO, ABRAHAN ALDELOMAR, JULIO RAMON RIBEYRO, ENRIQUE LOPEZ DE ALBUJAR"
#       87654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321   #indices negativos
#             -120      -110      -100       -90       -80       -70       -60       -50       -40       -30       -20       -10           #indices negativos


#EJERCICIO 1
print("EJERCICIO 1")
cortado=cadena[0:3]                  #cortado de la cadena  entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [0:3], es:"+cortado)

print("")
#EJERCICIO 2
print("EJERCICIO 2")
cortado=cadena[0:9]               #cortado de la cadena  entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [0:9], es:"+cortado)

print("")
#EJERCICIO 3
print("EJERCICIO 3")
cortado=cadena[0:110]         #cortado de la cadena  entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [0:110], es:"+cortado)

print("")
#EJERCICIO 4
print("EJERCICIO 4")
cortado=cadena[:]        #cortado de la cadena  entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [:], es:"+cortado)

print("")
#EJERCICIO 5
print("EJERCICIO 5")
cortado=cadena[::]     #cortado de la cadena  entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [::], es:"+cortado)

print("")
#EJERCICIO 6
print("EJERCICIO 6")
cortado=cadena[50:70]     #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [50:70], es:"+cortado)


print("")
#EJERCICIO 7
print("EJERCICIO 7")
cortado=cadena[70:120]          #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [70:120], es:"+cortado)

print("")
#EJERCICIO 8
print("EJERCICIO 8")
cortado=cadena[::-1]     #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [::-1], es:"+cortado)

print("")
#EJERCICIO 9
print("EJERCICIO 9")
cortado=cadena[::-3]      #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [::-33], es:"+cortado)

print("")
#EJERCICIO 10
print("EJERCICIO 10")
cortado=cadena[10:24:-1]    #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [10:24:-1], es:"+cortado)

print("")
#EJERCICIO 11
print("EJERCICIO 11")
cortado=cadena[52:100:-1]       #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [52:100:-1], es:"+cortado)

print("")
#EJERCICIO 12
print("EJERCICIO 12")
cortado=cadena[:5:-1]       #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [:5:-1], es:"+cortado)

print("")
#EJERCICIO 13
print("EJERCICIO 13")
cortado=cadena[2:22]            #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [2:22], es:"+cortado)

print("")
#EJERCICIO 14
print("EJERCICIO 14")
cortado=cadena[-2:-4:-1]              #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [-2:-4:-1], es:"+cortado)

print("")
#EJERCICIO 15
print("EJERCICIO 15")
cortado=cadena[30:117]              #cortado de la cadena entre las dimensiones dadas
print("la subcadena obtenida entre las dimensiones [30:117], es:"+cortado)
