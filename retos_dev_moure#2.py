"""
 Escribe una función que reciba dos palabras (String) y retorne
 verdadero o falso (Bool) según sean o no anagramas.
 - Un Anagrama consiste en formar una palabra reordenando TODAS
 las letras de otra palabra inicial.
 - NO hace falta comprobar que ambas palabras existan.
 - Dos palabras exactamente iguales no son anagrama.
 """

#en un primer momento pense hacerlo con listas

def func_anagrama():
    lista_palabra_1=[]
    lista_palabra_2=[]

    palabra1=(input('Ingresa palabra1:'))
    lista_palabra_1.append(palabra1)

    palabra2=(input('Ingresa palabra2:'))
    lista_palabra_2.append(palabra2)

    if palabra1 == palabra2:
        print(False)
    elif sorted(str(lista_palabra_1)) == sorted(str(lista_palabra_2)):
        print(True)
    else:
        print(False)


func_anagrama()

#cuando entendi el metodo, busque la forma de simplificarlo.
#Y solucione la deteccion de mayusculas y minusculas


def funci_anagrama():

    palabra1=(input('Ingresa palabra1:'))
    
    palabra2=(input('Ingresa palabra2:'))
    
    if palabra1.lower() == palabra2.lower():
        print(False)
    elif sorted(palabra1.lower()) == sorted(palabra2.lower()):
        print(True)
    else:
        print(False)

funci_anagrama()

    
#un poquito de estetica

def funcion_anagrama():

    pal1=(input('Ingresa 1er palabra:\n'))
    
    pal2=(input('Ingresa 2da palabra:\n'))
    
    if pal1.lower() == pal2.lower():
        print ('No son Anagramas')
    elif sorted(pal1.lower()) == sorted(pal2.lower()):
        print ('Son Anagramas')
    else:
        print('No son Anagramas')

funcion_anagrama()