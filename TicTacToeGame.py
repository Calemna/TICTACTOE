import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 700))

#THE CAPTION TITLE
pygame.display.set_caption("TIC TAC TOE")
#THE TITLE IN THE BACKGROUND
font = pygame.font.Font('pixel-operator-mono-bold.ttf', 130)
showing_font = font.render('TIC TAC TOE', False, (0, 0, 0))
#THE FONT TITLE IS GAME MENU SCENE
font2 = pygame.font.Font('pixel-operator-mono-bold.ttf', 100)
showing_font2 = font2.render('MODE SELECTION', False, (255,0,0))
#Caption Image
icon_image = pygame.image.load('captionimage.png')
pygame.display.set_icon(icon_image)

#BACKGROUND IMAGE
background = pygame.image.load('backgroundimage.png')
background = pygame.transform.scale(background, (800, 700))


#THE BUTTON YUNG IMAGE NILA AT SIZE
#BUTTONS FOR THE MENU SCENE
button_clicked = pygame.image.load('Playclicked.png')
button_unclicked = pygame.image.load('Playunclick.png')
button_clicked = pygame.transform.scale(button_clicked, (200, 100))
button_unclicked = pygame.transform.scale(button_unclicked, (200, 100))
button_rect = button_unclicked.get_rect(center=(400, 400))
#BUTTONS FOR THE GAME SCENE
button_playervsplayer = pygame.image.load('Player vs player button.png')
button_playervsplayer = pygame.transform.scale(button_playervsplayer, (200, 100))
button_playervsai = pygame.image.load('Player vs AI button.png')
button_playervsai = pygame.transform.scale(button_playervsai, (200, 100))
button_playervsplayer_rect = button_playervsplayer.get_rect(center=(400, 300))
button_playervsai_rect = button_playervsai.get_rect(center=(400,450))

#THE CLICK PUWEDE GAMITIN SA BUTTON SA STATEMENT
clicked = False

#SCENE CONTROL
scene = "menu"

#ALL OF THE FUNCTIONS TO STORE
#GRID FOR 3 x 3 TIC TAC TOE
def drawing_grid():
    grid = (71, 58, 18)
    cell_size = 200
    grid_width = cell_size * 3
    grid_height = cell_size * 3
    #TO CENTER THE GRID
    start_x = (800 - grid_width) // 2
    start_y = (700 - grid_height) // 2
    x_offset = 5
    for x in range(1, 3):
    # HORIZONTAL LINES   
        pygame.draw.line(screen, grid, (start_x, start_y + x * cell_size), (start_x + grid_width, start_y + x * cell_size), 5)
    # VERTICAL LINES
        pygame.draw.line(screen, grid, (start_x + x * cell_size + x_offset, start_y), (start_x + x * cell_size + x_offset, start_y + grid_height), 5)
#PLAYER VS PLAYER SCENE LOOP
def playervsplayer_scene():
    while scene == "playervsplayer":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#THE SCREEN BLIT FOR PLAYER VS PLAYER SCENE       
        screen.blit(background, (0, 0))
        drawing_grid()
        pygame.display.update()
#PLAYER VS AI SCENE LOOP
def playervsai_scene():
    while scene == "playervsai":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#THE SCREEN BLIT FOR PLAYER VS AI SCENE        
        screen.blit(background, (0, 0))
        pygame.display.update()
#GAME SCENE LOOP
def game_scene():
    global scene
    while scene == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_playervsplayer_rect.collidepoint(event.pos):
                    clicked = True  
                    print("Click")
                    scene = "playervsplayer"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_playervsai_rect.collidepoint(event.pos):
                    clicked = True
                    scene = "playervsai"
#THE GAME SCENE SCREEN BLIT
        screen.blit(background, (0, 0))
        screen.blit(button_playervsplayer,button_playervsplayer_rect)
        screen.blit(button_playervsai,button_playervsai_rect)
        button_playervsplayer_rect         
        screen.blit(showing_font2,(50, 70))
        pygame.display.update()

#MENU SCENE LOOP
def menu_scene():
    global scene
while scene == "menu":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                clicked = True
                scene = "game"
        elif event.type == pygame.MOUSEBUTTONUP:
            if button_rect.collidepoint(event.pos) and clicked:
                clicked = False               
#SCREEN BLIT FOR MENU SCENE
    screen.blit(background, (0, 0))
    screen.blit(showing_font,(40, 70))
    screen.blit(button_clicked if clicked else button_unclicked, button_rect)
    pygame.time.delay(30)
    pygame.display.update()




#THE SCENE MAIN LOOP
while True:
    if scene == "menu":
        menu_scene()
    elif scene == "game":
        game_scene()
    elif scene == "playervsplayer":
        playervsplayer_scene()
    elif scene == "playervsai":
        playervsai_scene()