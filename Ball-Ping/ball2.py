import pygame

# Inicializando o Pygame
pygame.init()

# Definindo a largura e a altura da tela
width, height = 700, 500

# Configurando a tela
screen = pygame.display.set_mode((width, height))

# Definindo um título para a janela
pygame.display.set_caption("Jogo da Bola")

# Cor de fundo da tela (preto)
background_color = (255, 255, 255)

# Carregando uma imagem da bola (substitua pelo caminho correto da imagem)
ball = pygame.image.load("pokeball.png")
ballrect = ball.get_rect()

#Definindo a velocidade da bola
speed = [2, 2]
# Loop principal do jogo
running = True
while running:
    # Processando os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movendo a bola
    ballrect = ballrect.move(speed)

    # Verificando as colisões com as bordas da tela
    if ballrect.left < 0 or ballrect.right > width:
         speed[0] = -speed[0]  # Inverter a velocidade horizontal (pingar)
    if ballrect.top < 0 or ballrect.bottom > height:
         speed[1] = -speed[1]  # Inverter a velocidade vertical (pingar)

    # Preenchendo o fundo com a cor
    screen.fill(background_color)

    # Desenhando a bola na tela
    screen.blit(ball, ballrect)

    # Atualizando a tela
    pygame.display.flip()

# Encerrando o Pygame
pygame.quit()
