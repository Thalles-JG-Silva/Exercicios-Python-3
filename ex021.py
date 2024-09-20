#Faça um programa em python que abra e reproduza o áudo de um arquivo MP3

import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load("seu_arquivo.mp3")

# Inicia a reprodução do áudio
pygame.mixer.music.play()

# Mantém o programa rodando enquanto o áudio é reproduzido
while pygame.mixer.music.get_busy():  # Verifica se a música ainda está tocando
    pygame.time.Clock().tick(10)
