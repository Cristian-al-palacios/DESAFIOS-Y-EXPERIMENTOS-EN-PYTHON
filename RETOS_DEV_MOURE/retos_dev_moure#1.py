#Empece completando un reto y termine experimentando con distintas formulas, solo por probar.
#Y una cosa fue llevando a la otra 

""""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for numeros in range (101):
        if (numeros %3 == 0) and (numeros % 5 == 0):
            print('fizzbuzz')
        elif numeros % 5 == 0:
            print ('buzz')
        elif numeros % 3 == 0:
            print ('fizz')
        else:
            print (numeros)

fizzbuzz()

#una vez cumplida la consigna del reto, me pongo a experimentar un poco.
#utilizo la misma logica para pares e impares

def par_impar():
    for numeros in range (101):
        if numeros %2 == 0:
            print('Par')
        else:
            print('Impar')    

par_impar()

#pero creo que queda mejor si aparece el numero junto con la referencia de par o impar


def num_par_impar():
    for numeros in range (101):
        if numeros %2 == 0:
            print(numeros , 'Par')
        else:
            print(numeros , 'Impar')    

num_par_impar()

#############################################################################
#y ahora con los numeros primos, primero los separe para que junto con cada numero indique si es primo o no
#despues se me ocurrio agregarlos a una lista


def numeros_primos():
    lista_num_primos=[]
    for numeros in range (1,101):
        if 101 % numeros == 0 and numeros == 1:
            print (str(numeros) + ' No es un numero primo')
        elif numeros % 2 == 0 and numeros > 2:
            print (str(numeros) + ' No es un numero primo')
        elif numeros % 3 == 0 and numeros > 3:
            print (str(numeros) + ' No es un numero primo')
        elif numeros % 5 == 0 and numeros > 5:
            print (str(numeros) + ' No es un numero primo')
        elif numeros % 7 == 0 and numeros > 7:
            print (str(numeros) + ' No es un numero primo')
        else:
            print (str(numeros) + ' Es un numero primo')
            lista_num_primos.append(numeros)

    print(lista_num_primos)
        

numeros_primos() 



#termine creando unas listas y separando los numeros primos dentro de ellas

def listas_primos_o_no_primos():
    lista_numeros=(list(range(1,101)))
    lista_numeros_primos =[]
    lista_numeros_no_primos=[]

    for numeros in lista_numeros:
        if numeros == 1:
            lista_numeros_no_primos.append(numeros)    
        elif numeros % 2 == 0 and numeros > 2:
            lista_numeros_no_primos.append(numeros)    
        elif numeros % 3 == 0 and numeros > 3:
            lista_numeros_no_primos.append(numeros)
        elif numeros % 5 == 0 and numeros > 5:
            lista_numeros_no_primos.append(numeros)
        elif numeros % 7 == 0 and numeros > 7:
            lista_numeros_no_primos.append(numeros)
        else:
            lista_numeros_primos.append(numeros)

    print(lista_numeros)
    print(lista_numeros_primos)
    print(lista_numeros_no_primos)

listas_primos_o_no_primos()