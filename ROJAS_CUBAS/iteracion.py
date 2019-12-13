#ITERACIÓN DE CADENAS

#ejercicio 1
print("EJERCICIO 1")
cadena="LENGUAJE C++"
#ITERAR LA CADENA
for letra in cadena:
    print(letra)
#fin_for

print("")
#ejercicio 2
print("EJERCICIO 2")
cadena="COMPUTADORAS Y LAPTOS"
#ITERAR LA CADENA Y CONTAR LA CANTIDA DE CARACTERES QUE TIENE
contador=0
for letra in cadena:
    contador +=1
#fin_for
print("la cantidad de caracteres que tiene la cadena \"COMPUTADORAS Y LAPTOS\", ES:"+str(contador))

print("")
#ejercicio 3
print("EJERCICIO 3")
cadena="concatenacion. comparacion... iteracion,;"
#ITERAR LA CADENA Y CONTAR LA CANTIDAD DE SIMBOLOS "." ,QUE TIENE LA CADENA
cont=0
for letra in cadena:
    if(letra=="."):
        cont+=1
    #fin_if
#fin_for
print("la cantidad de simbolos \".\", que tiene la cadena \"concatenacion. comparacion... iteracion,;\", es:"+str(cont))

print("")
#ejercicio 4
print("EJERCICIO 4")
cadena="hola $$$$$como es $ tas bien$"
#ITERAR LA CADENA Y contar la cantidad de simbolos "$" tiene
contador=0
for letra in cadena:
    if(letra=="$"):
        contador=contador+1
    #fin_if
#fin_for
print("la cantidad de simbolos \"$\" ,que tiene la cadena \"hola $$$$$como es $ tas bien$\", es:"+str(contador))


print("")
#ejercicio 5
print("EJERCICIO 5")
cadena="#########,,ncbvh,.-.,/////w//d/ex"
#ITERAR LA CADENA Y contar la cantidad de simbolos "#" y "/" que tiene
contador1=0
contador2=0
for letra in cadena:
    if(letra=="#"):
        contador1=contador1+1
    #fin_if
    if(letra=="/"):
        contador2=contador2+1
    #fin_if
#fin_for
print("la cantidad de simbolos \"#\" y \"/\"  ,que tiene la cadena \"#########,,ncbvh,.-.,/////w//d/ex\", son respectivamente:"+str(contador1)+","+str(contador2))

print("")
#ejercicio 6
print("EJERCICIO 6")
cadena1="123Qx*19"
cadena2="123QX*19"
#ITERAR LAS CADENAS Y VERIFICAR SI ES EL CODIGO DEL AULA VIRTUAL("123Qx*19)
msg1,msg2="",""
#iterar cadena1
for letra in cadena1:
    if(letra=="x"):
        msg1="VERDADERO"
    #fin_if
#fin_for

#iterar cadena2
for letra in cadena2:
    if(letra=="X"):
        msg2="FALSO"
    #fin_if
#fin_for

print("el primer codigo es correcto?:"+msg1)
print("el segundo codigo es correcto?:"+msg2)

print("")
#ejercicio 7
print("EJERCICIO 7")
cadena="PROGRAMACION I"
#iterar y luego convertir a minisculas la cadena dada
for letra in cadena:
    print(letra.lower())
#fin_for

print("")
#ejercicio 8
print("EJERCICIO 8")
cadena="                    "
#iterar y contar la cantidad de espacios que tiene
contar=0
for letra in cadena:
    if(letra==" "):
        contar+=1
    #fin_if
#fin_for
print("la cantidad de espacios que tiene la cadena \"                    \" ,es:"+str(contar))

print("")
print("EJERCICIO 9")
#ejercicio 9
cadena="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAJAJAJ"
contar1=0
contar2=0
#iterar contar la cantidad de letras "a" y "A"
for letra in cadena:
    if(letra=="a"):
        contar1+=1
    #fin_if
    if(letra=="A"):
        contar2+=1
    #fin_if
#fin_for
print("la cantidad de letras a y A  que tiene la cadena \"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaAAAAAAAAAAAAJAJAJ\" ,es respectivamente:"+str(contar1)+","+str(contar2))

print("")
#ejercicio 10
print("EJERCICIO 10")
cadena="aeiouadsahgsabhchbavcc duriiodaee"
#iterar y contar la cantidad de vocales que hay en la cadena dada
cant_vocales=0
for letra in cadena:
    if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="iou"):
        cant_vocales+=1
    #fin_if
#fin_for
print("la cantidad de vocales que tiene la cadena \"aeiouadsahgsabhchbavcc duriiodaee\" ,es:"+str(cant_vocales))
