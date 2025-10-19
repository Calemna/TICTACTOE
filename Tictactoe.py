import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("TIC TAC TOE")

# fonts
font_big = pygame.font.Font('PixelOperatorMono-Bold.ttf', 130)
font_mid = pygame.font.Font('PixelOperatorMono-Bold.ttf', 80)
font_small = pygame.font.Font('PixelOperatorMono-Bold.ttf', 40)

# icon
icon_image = pygame.image.load('captionimage.png')
pygame.display.set_icon(icon_image)

# bg
background = pygame.image.load('Backgroundimage.png')
background = pygame.transform.scale(background, (800, 700))

# button pics
def load_button_images(normal, hover, size):
    normal_img = pygame.image.load(normal)
    hover_img = pygame.image.load(hover)
    normal_img = pygame.transform.scale(normal_img, size)
    hover_img = pygame.transform.scale(hover_img, size)
    return normal_img, hover_img

# menu button
play_btn, play_btn_hover = load_button_images('Playunclick.png', 'Playclicked.png', (200, 100))
play_btn_rect = play_btn.get_rect(center=(400, 400))

# modes button
pvp_btn, pvp_btn_hover = load_button_images('Player vs player button.png', 'pVSpHover.jpg', (200, 100))
ai_btn, ai_btn_hover = load_button_images('Player vs AI button.png', 'playerVSaiHover.jpg', (200, 100))
pvp_btn_rect = pvp_btn.get_rect(center=(400, 300))
ai_btn_rect = ai_btn.get_rect(center=(400, 450))

# return button
return_btn, return_btn_hover = load_button_images('return-button.jpg', 'return_hover.jpg', (150, 70))
return_btn_rect = return_btn.get_rect(center=(100, 60))

# symbols
x_img = pygame.image.load('X_symbol.png')
o_img = pygame.image.load('O_symbol.png')
x_img = pygame.transform.scale(x_img, (180, 180))
o_img = pygame.transform.scale(o_img, (180, 180))

# cells
scene = "menu"
clicked = False
grid = [["" for _ in range(3)] for _ in range(3)]
cell_size = 200
start_x = (800 - cell_size * 3) // 2
start_y = (700 - cell_size * 3) // 2
current_player = "X"
winner = None
game_over = False

# game function
def draw_grid():
    grid_color = (71, 58, 18)
    for x in range(1, 3):
        pygame.draw.line(screen, grid_color, (start_x, start_y + x * cell_size), (start_x + 600, start_y + x * cell_size), 5)
        pygame.draw.line(screen, grid_color, (start_x + x * cell_size, start_y), (start_x + x * cell_size, start_y + 600), 5)

def draw_marks():
    for row in range(3):
        for col in range(3):
            if grid[row][col] == "X":
                screen.blit(x_img, (start_x + col * cell_size + 10, start_y + row * cell_size + 10))
            elif grid[row][col] == "O":
                screen.blit(o_img, (start_x + col * cell_size + 10, start_y + row * cell_size + 10))

def check_winner():
    global winner, game_over
    lines = grid + [list(col) for col in zip(*grid)] + [[grid[i][i] for i in range(3)], [grid[i][2 - i] for i in range(3)]]
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != "":
            winner = line[0]
            game_over = True
            return
    if all(cell != "" for row in grid for cell in row):
        winner = "Draw"
        game_over = True

def reset_game():
    global grid, current_player, winner, game_over
    grid = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    winner = None
    game_over = False

def ai_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if grid[r][c] == ""]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = "O"

# scenes
def menu_scene():
    global scene
    while scene == "menu":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn_rect.collidepoint(mouse_pos):
                    scene = "game"

        # draw
        screen.blit(background, (0, 0))
        screen.blit(font_big.render("TIC TAC TOE", True, (0, 0, 0)), (40, 70))
        screen.blit(play_btn_hover if play_btn_rect.collidepoint(mouse_pos) else play_btn, play_btn_rect)
        pygame.display.update()

def game_scene():
    global scene
    while scene == "game":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_btn_rect.collidepoint(mouse_pos):
                    reset_game()
                    scene = "playervsplayer"
                elif ai_btn_rect.collidepoint(mouse_pos):
                    reset_game()
                    scene = "playervsai"
                elif return_btn_rect.collidepoint(mouse_pos):
                    scene = "menu"

        # draw
        screen.blit(background, (0, 0))
        screen.blit(font_mid.render("MODE SELECTION", True, (255, 0, 0)), (100, 70))
        screen.blit(pvp_btn_hover if pvp_btn_rect.collidepoint(mouse_pos) else pvp_btn, pvp_btn_rect)
        screen.blit(ai_btn_hover if ai_btn_rect.collidepoint(mouse_pos) else ai_btn, ai_btn_rect)
        screen.blit(return_btn_hover if return_btn_rect.collidepoint(mouse_pos) else return_btn, return_btn_rect)
        pygame.display.update()

def playervsplayer_scene():
    global scene, current_player
    while scene == "playervsplayer":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                for row in range(3):
                    for col in range(3):
                        rect = pygame.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
                        if rect.collidepoint(event.pos) and grid[row][col] == "":
                            grid[row][col] = current_player
                            check_winner()
                            current_player = "O" if current_player == "X" else "X"
            elif event.type == pygame.MOUSEBUTTONDOWN and return_btn_rect.collidepoint(mouse_pos):
                reset_game()
                scene = "game"

        # draw
        screen.blit(background, (0, 0))
        draw_grid()
        draw_marks()
        if game_over:
            msg = "DRAW!" if winner == "Draw" else f"{winner} WINS!"
            screen.blit(font_mid.render(msg, True, (255, 255, 255)), (250, 30))
        screen.blit(return_btn_hover if return_btn_rect.collidepoint(mouse_pos) else return_btn, return_btn_rect)
        pygame.display.update()

def playervsai_scene():
    global scene, current_player
    while scene == "playervsai":
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over and current_player == "X" and event.type == pygame.MOUSEBUTTONDOWN:
                for row in range(3):
                    for col in range(3):
                        rect = pygame.Rect(start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size)
                        if rect.collidepoint(event.pos) and grid[row][col] == "":
                            grid[row][col] = "X"
                            check_winner()
                            current_player = "O"
            elif event.type == pygame.MOUSEBUTTONDOWN and return_btn_rect.collidepoint(mouse_pos):
                reset_game()
                scene = "game"

        # AI turn
        if not game_over and current_player == "O":
            ai_move()
            check_winner()
            current_player = "X"

        # draw
        screen.blit(background, (0, 0))
        draw_grid()
        draw_marks()
        if game_over:
            msg = "DRAW!" if winner == "Draw" else f"{winner} WINS!"
            screen.blit(font_mid.render(msg, True, (255, 255, 255)), (250, 30))
        screen.blit(return_btn_hover if return_btn_rect.collidepoint(mouse_pos) else return_btn, return_btn_rect)
        pygame.display.update()

# main loop
while True:
    if scene == "menu":
        menu_scene()
    elif scene == "game":
        game_scene()
    elif scene == "playervsplayer":
        playervsplayer_scene()
    elif scene == "playervsai":
        playervsai_scene()
