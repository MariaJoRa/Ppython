rios={ "Nilo": 'Egipto', "Amazonas": 'Brasil', "Danubio": 'Austria', "Meno":'Alemania', "Thames":'Ingleterra'}

for rio in rios:
    print("El río "+ rio + " corre en "+ rios[rio])

print("Se imprimen los nombres de los ríos incluidos en el diccionario:")
for key in rios:
    print (key)

print("Se imprimen los nombres de cada país incluido en el diccionario:")
for key in rios:
    print (rios[key])

print("Punto 2_____________________________")
glosario={"Método": "Es un bloque de código que contiene instrucciones que pueden ser usadas varias veces en el código",
          "Variable global": "Es una variable que se puede invocar en cualquier parte del código",
          "Variable local": "Es una variable que puede ser usada sólo en una parte del código",
          "Palabras reservadas": "Son palabras que tienen una función específica en el código, cada lenguaje de programación tiene sus propias palabras reservadas",
          "Arreglo": "Es un conjunto ordenado de datos que permite almacenar varios valores en una sóla variable"}

for palabra in glosario:
    print (palabra,':',glosario[palabra])

