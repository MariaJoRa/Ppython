t = (23,'a',(2.5,3.7,'x'),["perrito","gatito"],'Pepe') #Se definen los elementos de la tupla t
print (t) #Se imprimen los elementos de la tupla t
print (len(t)) #Se imprime el número de elementos de la tupla


print ('=====================================') #Se imprime un separador
print (t[0]) #Se imprime el elemento de la tupla con índice 0
print (t[3]) #Se imprime el elemento de la tupla con índice 3
print (t[1:3]) #Se imprimen los elementos con índices del 1 y 2
print (t[3][1]) #Se imprime el valor con índice 1 del elemento con índice 3 de la tupla


print ('====================================')#Se imprime un separador
print (t[3]) #Se imrpime el elemento de la tupla con índice 3
t[3].append('lorito') #Se agrega el valor "lorito" al final del elemento con índice 3
print (t) #Se imprime la tupla con los valores actualizados

print ('====================================') #Se imprime un separador
for elemento in t:
    print (elemento) #Se imprime cada elemento de la tupla mediante un ciclo for

print ('====================================') #Se imprime un separador
for index in range(0,len(t)):
    print (t[index]) #Se cada elemento de la tupla (desde el elemento con indice cero, hasta el elemento con índice igual a la longitud de la tupla) mediante un ciclo for

print ('====================================')#Se imprime un separador
if 'a' in t:
    print ("El elemento 'a' esta en la tupla") #Si el elemento "a" se encuentra en la tupla, imprimir "El elemto "a" está en la tupla" (mediante un condicional)

print ('====================================')#Se imprime un separador
lista=list(t) #Se crea una lista a partir de los elementos de la tupla t
lista[1]='A' #Se cambia el elemento con índice 1 por el elemento "A" en la lista creada
print (lista) #Se imprime la lista con los elementos actualizados

tupla=tuple(lista) #Se crea una tupla a partir de la lista
print (tupla) #Se imprime la nueva tupla
print ('====================================')#Se imprime un separador
l = [(1,1), (2,4), (3,9), (4,16), (5,25)] #Se crea una lista con valores (x, y)
for x, y in l:
    print (x, ':', y) #Se imrpime cada elemento de la lista (par x,y) mediante un ciclo for