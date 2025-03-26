# TODO: Faça um programa em Pythom que abra e reproduza um áudio em MP3.

"""import pygame
pygame.init()
pygame.mixer.music.load('reproduzirMp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()
""" """
O programa não tocou o mp3
"""

import pygame
import time

# Inicializa o pygame
pygame.init()

# Carrega o arquivo de música
pygame.mixer.music.load("AlgoritmoComPython-/Exercicios/reproduzirMp3.mp3")

# Reproduz a música
pygame.mixer.music.play()

# Espera a música terminar
while pygame.mixer.music.get_busy():
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente

    """
    Foi necessário ==> 
    1. Instalar o 'pip3 install pygamae'
    2. E depois fazer 'python.exe -m pip install --upgrade pip'
    """
