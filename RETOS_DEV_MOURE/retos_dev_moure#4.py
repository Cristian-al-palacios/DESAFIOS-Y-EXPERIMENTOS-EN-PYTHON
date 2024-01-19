"""
#4
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
 """

#En honor a la verdad, este ya lo habia hecho sin darme cuando probaba cosas en el ejercicio #1

def numeros_primos():
    lista_num_primos=[f"Lista de numeros primos:"]
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