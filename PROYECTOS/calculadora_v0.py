#primer intento de crear una calculadora, extremadamente precaria 
#aun no sale como pretendo, pero funciona para operaciones basicas


def calculadora_v0():
    numero1=int(input('Ingresa el primer numero\n'))
    operacion=(input('ingresa la operacion matematica (+ - * /)\n'))
    numero2=int(input('ingresa el segundo numero\n'))

    if operacion == '+':
        print('El resultado es:\n',(numero1 + numero2))
    elif operacion == '-':
        print( 'El resultado es:\n' ,(numero1 - numero2))
    elif operacion == '*':
        print( 'El resultado es:\n' ,(numero1 * numero2))
    elif operacion == '/':
        print( 'El resultado es:\n' ,(numero1 / numero2))
    else:
        print('No selecciono un operador valido.') 


calculadora_v0()
#no es mucho, pero es trabajo honesto (?)

#voy editando un poco el codigo
        

def calculadora_v01():
    numero1 = int(input('Ingresa el primer numero\n'))
    operacion = (input('ingresa la operacion matematica (+ - * /)\n'))
    numero2 = int(input('ingresa el segundo numero\n'))
    resultado = 'Incorrecto debido a que no selecciono un operador valido'
    #tambien puedo asignar un valor None para no dejar la variable vacia

    if operacion == '+':
        resultado = (numero1 + numero2)
    elif operacion == '-':
        resultado = (numero1 - numero2)
    elif operacion == '*':
        resultado = (numero1 * numero2)
    elif operacion == '/':
        resultado = (numero1 / numero2)
    else:
        print('No selecciono un operador valido.') 

    print(f'El resultado de {numero1} {operacion} {numero2} es: \n{resultado}')


calculadora_v01()


