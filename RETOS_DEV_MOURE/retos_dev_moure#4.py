"""
#4
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
 """

#como en el ejercicio #1 ya habia hecho una lista similar, en este lo modifico y agrego algunas variaciones


def numeros_primos():
    for numeros in range (0,100):
        if  numeros <= 1:
            print (numeros , ' No es un numero primo')
        elif numeros % 2 == 0 and numeros > 2:
            print (numeros , ' No es un numero primo')
        elif numeros % 3 == 0 and numeros > 3:
            print (numeros , ' No es un numero primo')
        elif numeros % 5 == 0 and numeros > 5:
            print (numeros , ' No es un numero primo')
        elif numeros % 7 == 0 and numeros > 7:
            print (numeros , ' No es un numero primo')
        else:
            print (numeros , ' Es un numero primo')

numeros_primos       #devolvera solo el numero y dira si es primo o no


def num_primos_input():
    for numeros in range ((int(input("Ingresa el principio del rango:\n"))) , (int(input("Ingresa el fin del rango:\n")))):
        if  numeros <= 1:
            print (numeros , ' No es un numero primo')
        elif numeros % 2 == 0 and numeros > 2:
            print (numeros , ' No es un numero primo')
        elif numeros % 3 == 0 and numeros > 3:
            print (numeros , ' No es un numero primo')
        elif numeros % 5 == 0 and numeros > 5:
            print (numeros , ' No es un numero primo')
        elif numeros % 7 == 0 and numeros > 7:
            print (numeros , ' No es un numero primo')
        else:
            print (numeros , ' Es un numero primo')

num_primos_input() #te pedira 2 valores para el rango y dira si es primo o no
            

def num_primos_input_lista():
    lista_num_primos=[]

    for numeros in range ((int(input("Ingresa el principio del rango:\n"))) , (int(input("Ingresa el fin del rango:\n")))):
        if  numeros <= 1:
            print (numeros , ' No es un numero primo')
        elif numeros % 2 == 0 and numeros > 2:
            print (numeros , ' No es un numero primo')
        elif numeros % 3 == 0 and numeros > 3:
            print (numeros , ' No es un numero primo')
        elif numeros % 5 == 0 and numeros > 5:
            print (numeros , ' No es un numero primo')
        elif numeros % 7 == 0 and numeros > 7:
            print (numeros , ' No es un numero primo')
        else:
            print (numeros , ' Es un numero primo')
            lista_num_primos.append(numeros)

    print(lista_num_primos) 


num_primos_input_lista() #pedira valores para el principio y fin del rango, dira si son o no primos y generara una lista con los que lo sean
