#OPERACION CON CADENAS CONCATENACION

#EJERCICIO NRO 01
#                     10       20        30      40
#        012345678901234567890123456789012345678901
frase02="LA VIDAD ES UNA PREPARACION PARA EL FUTURO"
#        210987654321098765432109876543210987654321
#       -40    -30      -20      -10
#CONCATENAR
#CARLOS RONALDO
mgs3=(frase02[23]+frase02[6]+frase02[17]+frase02[34]+frase02[41]+frase02[10]) #concatena la palabra CARLOS
msg4=(frase02[17]+frase02[-1]+frase02[26]+frase02[-36]+frase02[34]+frase02[7]+frase02[-1]) #concatena la palabra RONALDO
print(mgs3+" "+msg4) ##imprima la palabra concatenada CARLOS RONALDO


#EJERCICIO NRO 02
#                     10       20        30    40
#      01234567890123456789012345678901234567890
frase="HOLA MUNDO DE LA PROGRAMACION EN PYTHON V"
#      10987654321098765432109876543210987654321
#    -40      -30       -20      -10
#CONCATENAR
#LLEGO NAVIDAD
msg=(frase[2]+frase[2]+frase[12]+frase[-21]+frase[9]) #concatena la palabra LLEGO
msg02=(frase[7]+frase[3]+frase[40]+frase[26]+frase[-33]+frase[3]+frase[-33]) #concatena la palabra NAVIDAD
print(msg+ " " +msg02) #imprima la palabra concatenada LLEGO NAVIDAD


#EJERCICIO NRO 03
#                      10       20        30       40       50
#        012345678901234567890123456789012345678901234567890123
frase03="CUALQUIER MOMENTO ES PERFECTO PARA APRENDER ALGO BUENO"
#        432109876543210987654321098765432109876543210987654321
#         -50      -40      -30      -20      -10
#CONCATENAR
#FRASE DE ALBERT
msg5=(frase03[24]+frase03[23]+frase03[-19]+frase03[19]+frase03[51]) #concatena la palabra FRASE
msg6=(frase03[40]+frase03[41]) #concatena la palabra DE
msg7=(frase03[2]+frase03[3]+frase03[49]+frase03[-13]+frase03[23]+frase03[27]) #concatena la palabra ALBERT
print(msg5+ " "+msg6+" "+msg7) #imprima la palabra concatenada FRASE DE ALBERT


#EJERCICIO NRO 04
#                  10       20        30        40        50
#    01234567890123456789012345678901234567890123456789012345
uni="UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO ESTA EN LAMBAYEQUE"
#    65432109876543210987654321098765432109876543210987654321
#      -50         -40       -30      -20      -10
#CONCATENAR
#EINSTEIN LA VIDA
msg8=(uni[4]+uni[2]+uni[1]+uni[-50]+uni[40]+uni[4]+uni[29]+uni[17]) #concatena la palabra EINSTEIN
msg9=(uni[35]+uni[9]) #concatena la palabra LA
msg10=(uni[3]+uni[2]+uni[10]+uni[18]) #concatena la palabra VIDA
print(msg8+" "+msg9+" "+msg10) #imprima la palabra concatenada EINSTEIN LA VIDA


#EJERCICIO NRO 05
#                         10       20       30          40      50       60     70
#         012345678901234567890123456789012345678901234567890123456789012345678901
farmacia="FARMACIA INKA FARMA ESTA EN LAMBAYEQUE Y ESTAN SORTEANDO UNA MOTO PULSAR"
#         210987654321098765432109876543210987654321098765432109876543210987654321
#         -70     -60      -50        -40       -30      -20      -10
#CONCATENAR
#ES UNA PREPARACION
msg11=(farmacia[25]+farmacia[21]) #concatena la palabra ES
msg12=(farmacia[57]+farmacia[58]+farmacia[59]) #concatena la palabra UNA
msg13=(farmacia[66]+farmacia[16]+farmacia[20]+farmacia[-6]+farmacia[4]+farmacia[71]+farmacia[7]+farmacia[5]+farmacia[6]+farmacia[64]+farmacia[53]) #concatena la palabra PREPARACION
print(msg11+" "+msg12+" "+msg13) #imprima la palabra concatenada ES UNA PREPARACION

#EJERCICIO NRO 06
#                     10       20       30      40
#     012345678901234567890123456789012345678901234
mate="MATEMATICA BASICA II ENSEÑA EL PROFESOR MARLO"
#     543210987654321098765432109876543210987654321
#     -40     -30        -20    -10
#CONCATENAR
#PARA EL
msg14=(mate[31]+mate[9]+mate[31]+mate[1]) #concatena la palabra PARA
msg15=(mate[3]+mate[43]) #concatena la palabra EL
print(msg14+" "+msg15) #imprima la palabra concatenada PARA EL


#EJERCICIO NRO 07
#                     10       20        30        40        50
#      012345678901234567890123456789012345678901234567890123456789
texto="LA FELICIDAD; CONSISTE EN PODER UNIR EL PRINCIPIO CON EL FIN"
#      098765432109876543210987654321098765432109876543210987654321
#    -60      -50     -40       -30       -20     -10
#CONCATENAR
#FUTURO
msg16=(texto[57]+texto[32]+texto[20]+texto[-28]+texto[41]+texto[51]+texto[12]) #concatena la palabra FUTURO,
print(msg16) #imprima la palabra concatenada FUTURO


#EJERCICIO NRO 08
#                     10     20
#        01234567890123456789012345
frase04="ABCDEFGHIJKLMNÑOPQRSTUWXYZ"
#        65432109876543210987654321
#       -20      -10
#CONCATENAR
#Y LA MEJOR PREPARACION
msg17=(frase04[24]) #concatena la palabra Y
msg18=(frase04[11]+frase04[0]) #concatena la palabra LA
msg19=(frase04[12]+frase04[4]+frase04[9]+frase04[15]+frase04[18]) #concatena la palabra MEJOR
msg20=(frase04[16]+frase04[18]+frase04[-22]+frase04[16]+frase04[0]+frase04[18]+frase04[0]+frase04[2]+frase04[-18]+frase04[15]+frase04[-13]) #concatena la palabra PREPARACION
print(msg17+" "+msg18+" "+msg19+" "+msg20) #imprima la palabra concatenada Y LA MEJOR PREPARACION

#EJERCICIO NRO 09
#                      10       20          30        40       50    60
#        0123456789012345678901234567890123456789012345678901234567890
frase05="EL TIEMPO TAMBIEN ES RELATIVO Y NADA PODEMOS SABER DEL FUTURO"
#        1098765432109876543210987654321098765432109876543210987654321
#      -60     -50      -40       -30        -20      -10
#CONCATENAR
#PARA EL FUTURO
msg21=(frase05[37]+frase05[35]+frase05[37]+frase05[35]) #concatena la palabra PARA
msg22=(frase05[-46]+frase05[-8]) #concatena la palabra EL
msg23=(frase05[55]+frase05[-5]+frase05[-4]+frase05[58]+frase05[59]+frase05[-1]) #concatena la palabra FUTURO
print(msg21+" "+msg22+" "+msg23) #imprima la palabra concatenada PARA EL FUTURO

#EJERCICIO NRO 10
#                        10         20        30     40       50
#         0123456789012345678901234567890123456789012345678901234
cadena01="LA FUERZA Y EL CRECIMIENTO VIENEN A TRAVES DEL ESFUERSO"
#         5432109876543210987654321098765432109876543210987654321
#         -50     -40       -30     -20        -10
#CONCATENAR
#ES VIVIR COMO SI
msg24=(cadena01[12]+cadena01[48]) #concatena la palabra ES
msg25=(cadena01[27]+cadena01[28]+cadena01[27]+cadena01[28]+cadena01[-3]) #concatena la palabra VIVIR
msg26=(cadena01[15]+cadena01[25]+cadena01[20]+cadena01[-1]) #concatena la palabra COMO
msg27=(cadena01[48]+cadena01[-27]) #concatena la palabra SI
print(msg24+" "+msg25+" "+msg26+" "+msg27) #imprima la palabra concatenada ES VIVIR COMO SI


#EJERCICIO NRO 11
#                     10         20         30          40      50
#         012345678901234567890123456789012345678901234567890123456789
cadena02="JUAN HUBIERA INGRESADO A LA UNIVERSIDAD SI HUBIERA ESTUDIADO"
#         098765432109876543210987654321098765432109876543210987654321
#           -50         -40        -30         -20    -10
#CONCATENAR
#NO HUBIERA NINGUNO
msg28=(cadena02[14]+cadena02[21]) #concatena la palabra NO
msg29=(cadena02[5]+cadena02[6]+cadena02[7]+cadena02[8]+cadena02[9]+cadena02[10]+cadena02[11]) #concatena la palabra HUBIERA
msg30=(cadena02[14]+cadena02[13]+cadena02[-46]+cadena02[-45]+cadena02[28]+cadena02[29]+cadena02[59]) #concatena la palabra NINGUNO
print(msg28+" "+msg29+" "+msg30) #imprima la palabra concatenada NO HUBIERA NINGUNO

#EJERCICIO NRO 12
#                     10
#         01234567890123456789
cadena03="JUAN FANNING  GARCIA"
#         09876543210987654321
#       -10
#CONCATENAR
#ANA FANNI JUANA
msg31=(cadena03[2]+cadena03[3]+cadena03[2]) #concatena la palabra ANA
msg32=(cadena03[5]+cadena03[6]+cadena03[7]+cadena03[7]+cadena03[9]) #concatena la palabra FANNI
msg33=(cadena03[0]+cadena03[1]+cadena03[6]+cadena03[-10]+cadena03[2]) #concatena la palabra JUANA
print(msg31+" "+msg32+" "+msg33) #imprima la palabra concatenada ANA FANNI JUANA

#EJERCICIO NRO 13
#                     10       20        30        40      50
#        012345678901234567890123456789012345678901234567890123
cadena4="MARCA DE ZAPATILLAS: ADIDAS, NIKE, REEBOK, PUMAS, CATV"
#        432109876543210987654321098765432109876543210987654321
#        -50     -40       -30      -20       -10
#CONCATENAR
#SE VAN A COMPAR
msg34=(cadena4[18]+cadena4[36]) #concatena la palabra SE
msg35=(cadena4[-1]+cadena4[1]+cadena4[29]) #concatena la palabra VAN
mdg36=(cadena4[17]) #concatena la palabra A
mgs37=(cadena4[3]+cadena4[39]+cadena4[0]+cadena4[43]+cadena4[-53]+cadena4[2]) #concatena la palabra COMPAR
print(msg34+" "+msg35+" "+mdg36+" "+mgs37) #imprima la palabra concatenada SE VAN A COMPAR

#EJERCICIO NRO 14
#                     10       20       30
#        0123456789012345678901234567890123456789
cadena5="ALBERT EINSTEIN FUE UN FISICO ALEMAN P.Z"
#        0987654321098765432109876543210987654321
#      -40     -30      -20       -10
#CONCATENAR
#AL REAL PLAZA
msg38=(cadena5[0]+cadena5[-39]) #concatena la palabra AL
msg39=(cadena5[4]+cadena5[3]+cadena5[30]+cadena5[31]) #concatena la palabra REAL
msg40=(cadena5[37]+cadena5[1]+cadena5[0]+cadena5[-1]+cadena5[-40]) #concatena la palabra PLAZA
print(msg38+" "+msg39+" "+msg40) #imprima la palabra concatenada AL REAL PLAZA


#EJERCICIO NRO 15
#                     10       20
#        01234567890123456789012345
cadena6="ABCDEFGHIJKLMNOPQRSTUWXYZV"
#        65432109876543210987654321
#        -20     -10
#CONCATENAR
#MUCHAS COSAS POR NAVIDAD
mgs41=(cadena6[12]+cadena6[20]+cadena6[2]+cadena6[7]+cadena6[-26]+cadena6[-8]) #concatena la palabra MUCHAS
mgs42=(cadena6[2]+cadena6[14]+cadena6[18]+cadena6[0]+cadena6[-8]) #concatena la palabra COSAS
mgs43=(cadena6[15]+cadena6[14]+cadena6[-9]) #concatena la palabra POR
mgs44=(cadena6[13]+cadena6[0]+cadena6[25]+cadena6[8]+cadena6[3]+cadena6[-26]+cadena6[-23]) #concatena la palabra NAVIDAD
print(mgs41+" "+mgs42+" "+mgs43+" "+mgs44) #imprima la palabra concatenada MUCHAS COSAS POR NAVIDAD
