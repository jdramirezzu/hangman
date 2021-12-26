"""
Este es un código donde se realiza un juego de ahorcado clásico, 
en el juego de ahorcado el objetivo es adivinar la palabra conociendo en un inicio 
solo el número total de letras que tienen. Las letras se pueden ir adivinando de a una
y cuando se acierta en una letra, se llenan los espacios que las ocupan. 
"""
import random
import os 

def welcome(): 
    """Esta función le da la bienvenida al usuario"""
    name = input("Please enter your play name: ")

    if name.isalpha() ==True:
        print("Bienvenido al juego",name, "vas a tener la oportunidad de adivinar hasta que nuestro muñeco se ahorqué, ¡Elige sabiamente!")
    else: 
        print("Solo puedes usar letras para definir tu nombre")
        name = input("Por favor introduce tu nickname: ")


def play_again():
    """ Esta función le pregunta al usuario si quiere tener una nueva partida"""
    decision = input("Escribe S si quieres volver a jugar y N si no quieres volver a jugar: ")

    if decision == 'S':
        main()
    elif decision == 'N':
        print("Esperamos que el juego haya sido de tu agrado")
    else:
        print("Por favor introduce una de las opciones solicitadas")




def obtener_palabra():
    with open ('data.txt', 'r', encoding='utf-8') as f:
        palabras = [line.strip() for line in f]
            
         
    palabra_juego = random.choice(palabras)  

       
    return palabra_juego



def main():
    #Variable booleana para cuando acierta o no, default false
    acierto = False 
    
    #Bienvenida al usuario 
    welcome()

    #Lista con el abecedario
    abecedario = ['abcdefghijklmnñopqrstuvwxyz']

    #La palabra a adivinar
    palabra = obtener_palabra()

    #Variable con el número de intentos 
    intentos = 7 

    print(palabra)
    
    

    while acierto == False and intentos > 0:
        #En esta parte se enuncia el número de intentos, el número de letras que tiene la palabra a adivinar
        #y se empieza a solicitar al usuario que adivine
        print("Tienes ", str(intentos), ' intentos')
        print("La palabra contiene", len(palabra)-1, "letras.")
        opciones = (len(palabra)-1)*'_'
        print(opciones)
        
        guess = input("Adivina una letra de la palabra o la palabra completa: ").lower()
        

        #Lista vacia para las letras adivinadas 
        letras_advinadas = []

        
        if guess not in palabra:
            intentos -= 1
            print(f"Te quedan {intentos}")
            
        
        if len(guess) == 1 and guess in palabra:
            menor_index = palabra.find(guess)
            mayor_index = palabra.rfind(guess)
            
            if (menor_index != -1 and mayor_index != -1) and menor_index != mayor_index :
                string_list = list(opciones)
                string_list[menor_index] = guess
                string_list[mayor_index] = guess
                opciones = "".join(string_list)           
                print(opciones)

                
            
            elif menor_index != -1:
                string_list = list(opciones)
                string_list[menor_index] = guess
                opciones = "".join(string_list)
                print(opciones)

        if len(guess) == len(palabra):
            if guess == palabra:
                opciones = guess
                print(opciones)
                print("Felicitaciones,¡ganaste!")
                acierto = True
                
        

        


if __name__=='__main__':
    os.system("cls")
    main()