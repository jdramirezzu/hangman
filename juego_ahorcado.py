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
        print("Bienvenido al juego, vas a tener la oportunidad de adivinar hasta que nuestro muñeco se ahorqué, ¡Elige sabiamente!")
    else: 
        print("Solo puedes usar letras para definir tu nombre")
        name = input("Por favor introduce tu nickname: ")


def play_again():
    """ Esta función le pregunta al usuario si quiere tener una nueva partida"""
    




def read_data():
    with open ('data.txt', 'r', encoding='utf-8') as f:
        palabras = [line for line in f]
            
         
    palabra_juego = random.choice(palabras)     
    return palabra_juego



def main():
    pass


if __name__=='__main__':
    os.system("cls")
    main()