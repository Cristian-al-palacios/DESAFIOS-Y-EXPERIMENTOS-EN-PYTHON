"""
*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""
#Este ejercicio me tuvo horas pensando, creando y sumando variables.
#cuando relaje la cabeza pienso la manera de hacerlo diferente.

def fibonacci():
    
    num_a = 0   
    print(num_a) 
    num_b = 1
    print(num_b)

    for numeros in range (48):
        
        num_a, num_b = num_b, num_a + num_b
        print(num_b)

fibonacci()

  
