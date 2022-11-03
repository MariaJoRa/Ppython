huespedes={101:'Juan Valdes', 105:'Paquita la del Barrio', 202: 'Mariana Pajon'} #Define los elementos del diccionario (par:clave-valor)



print (huespedes) #Se imprimen los elementos del diccionario
print (huespedes.items()) #Se imprime el par clave-valor en paréntesis

print (huespedes.keys()) #Se imprimen solo las claves que identifican cada valor o elemento
for key in huespedes:
    print (key) #Se imprimen las claves  de forma individual mediante un ciclo for

print (huespedes.values()) #Se imprimen solo los valores del diccionario
for key in huespedes:
    print (huespedes[key]) #Se imprime cada valor del diccionario mediante un ciclo for
print()

for habitacion in huespedes:
    print (habitacion,':',huespedes[habitacion]) #Se imprime la clave (habitación) con dos puntos para indicar el valor(huesped) que hay en cada una mediante un ciclo for
print()
for habitacion,huesped in huespedes.items():
    print (habitacion,':',huespedes[key]) #Se imprime la clave(habitación) y el valor correspondiente a la llave mediante un ciclo for
for indice, key in enumerate(huespedes):
    print (indice+1,key,huespedes[key]) #Se imprime el índice de cada elemento(par clave-valor) del arreglo sumando a este 1. Además se imprime la clave y el elemento mediante un ciclo for
print()

print (huespedes[105]) #Se imprime el valor con la clave 105
print (huespedes.get(105)) #Se "obtiene" el valor con la clave 105

print ('====================================') #Se imprime un separador

huespedes[102]='Fanny Lu' #Se añade un nuevo elemento con clave: 102 y valor: Fanny Lu
huespedes[107]='Don Omar' #Se añade un nuevo elemento con clave: 107 y valor: Don Omar
huespedes.setdefault('109','Luis Miguel') #Se crea el elemento con clave: 109 y valor: Luis Miguel

for huesped in huespedes.items():
    print (habitacion,':',huesped) #Se imprimen todos los elementos( iniciales y nuevos) del diccionario mediante un ciclo for
print()

registroshoy={201:'Vicente Fernandez',301:'Pepe Guardiola'} #Se definen dos nuevos elementos (clave-valor)
huespedes.update(registroshoy)#Se agregan los nuevos elementos al diccionario "huespedes"
for habitacion, huesped in huespedes.items():
    print (habitacion,':',huesped) # Se imprime el diccionario con los elementos actualizados mediante un ciclo for
print()

print ('====================================') #Se imprime un separador

huespedes[107]='Ricky Martin' #Ahora el huesped 107 es Ricky Martin (La clave 107 tiene ahora como valor: Ricky Martin
print (huespedes) #Se imprimen los elementos actualizados del diccionario

print ('====================================') #Se imprime un separador


del huespedes[102] #Se elimina el elemento con clave: 102 del diccionario
huespedes.pop(202) #Se elimina el elemento con índice/clave 102
print(huespedes)# Se imprime el diccionario sin los elementos eliminados

print ('====================================')#Se imprime un separador

copia1=huespedes.copy() #Crea una copia del diccionario
print ('copia1: ',copia1) #Se imprime la copia del diccionario
copia2={} #Se define copia2
copia2.update(huespedes)  #Se añaden los valores del diccionario a copia2
print ("copia2: ",copia2) #Se imprime copia2

print ('====================================') #Se imprime un separador

lista=[2,5,7,1] #Se crea una lista
diccio=dict.fromkeys(lista,"xxx") #Se crea un diccionario a partir de los elementos de la lista con estos como clave con valor "xxx"
print(diccio)#Se imrpime el diccionario creado

print ('====================================') #Se imprime un separador
inventario={"plata": (500,2500), 'cartera' : ["Cedula","Monedas","Boletas"],'mecato':'Detodito','dias':1}#Se crea un diccionario
print (inventario) #Se imprime el diccionario
inventario["cartera"].sort() #Se organizan los valores correspondientes a la clave "Cartera" en orden alfabético
print(inventario) #Se imprime el diccionario con el nuevo orden de los valores  correspondientes a "Cartera"
inventario["cartera"].remove("Monedas") #Se elimina el valor "Monedas" correspondiente a la clave "Cartera"
print(inventario) #Se imprime el inventario sin el valor "Monedas" correspondiente a la clave "Cartera"
print(inventario.get("plata")[0]) #Se obtiene e imprime el valor con índice 0 correspondiente a la clave "plata"