import sys, pygame

# Inicializando o Pygame
pygame.init()

position = width , height = 500 , 450
speed = [1,1]
# Cor de fundo da tela (preto)
background_color = (0,0,0)
# Configurando a tela (largura e altura)
screen = pygame.display.set_mode(position)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# Definindo um título para a janela
pygame.display.set_caption("Jogo da Bola")


# Loop principal do jogo
running = True
while running:
    # Processando os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
         speed[1] = -speed[1]
    # Preenchendo o fundo com a cor
    screen.fill(background_color)
    screen.blit(ball, ballrect)

    # Atualizando a tela
    pygame.display.flip()

# Encerrando o Pygame

