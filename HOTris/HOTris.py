# PYTRIS™ Copyright (c) 2017 Jason Kim All Rights Reserved.

import pygame
from mino import *
from random import *
from pygame.locals import *

# Define
block_size = 17 # Height, width of single block
width = 10 # Board width
height = 20 # Board height
framerate = 30 # Bigger -> Slower
Music_playing = True
Skin_Changed = False

pygame.init()

clock = pygame.time.Clock() # 초단위로 움직이는 메소드
screen = pygame.display.set_mode((600, 600)) # 디스플레이 사이즈
pygame.mixer.music.load("./assets/musics/BaseMusic.wav")
pygame.mixer.music.play(loops=-1 , start=0.0)
pygame.time.set_timer(pygame.USEREVENT , framerate * 10) # refresh
pygame.display.set_caption("HOTris")

class ui_variables:
    # Fonts
    font_path = "./assets/fonts/HoonWhitecatR.ttf"
    h1 = pygame.font.Font(font_path, 50)
    h2 = pygame.font.Font(font_path, 30)
    h4 = pygame.font.Font(font_path, 20)
    h5 = pygame.font.Font(font_path, 13)
    h6 = pygame.font.Font(font_path, 10)
    h7 = pygame.font.Font(font_path, 20)
    h8 = pygame.font.Font(font_path, 20)
    h9 = pygame.font.Font(font_path, 20)
    h10 = pygame.font.Font(font_path, 20)

    # Sounds (wav , ogg available)
    click_sound = pygame.mixer.Sound("./assets/sounds/Intro.wav")
    move_sound = pygame.mixer.Sound("./assets/sounds/Wook_Block.wav")
    drop_sound = pygame.mixer.Sound("./assets/sounds/whip.wav")
    single_sound = pygame.mixer.Sound("./assets/sounds/Sexy_Single.wav")
    double_sound = pygame.mixer.Sound("./assets/sounds/Sexy_Double.wav")
    triple_sound = pygame.mixer.Sound("./assets/sounds/Sexy_Triple.wav")
    tetris_sound = pygame.mixer.Sound("./assets/sounds/Sexy_Quad.wav")
    S_UP_sound = pygame.mixer.Sound("./assets/sounds/SpeedUp.wav")
    S_DOWN_sound = pygame.mixer.Sound("./assets/sounds/SpeedDown.wav")

    # Background colors
    black = (10, 10, 10) #rgb(10, 10, 10)
    white = (255, 255, 255) #rgb(255, 255, 255)
    grey_1 = (26, 26, 26) #rgb(26, 26, 26)
    grey_2 = (35, 35, 35) #rgb(35, 35, 35)

    # Tetrimino colors
    cyan = (240, 206, 155) #rgb(69, 206, 204) # I
    blue = (242, 13, 13) #rgb(64, 111, 249) # J
    orange = (220, 109, 247) #rgb(253, 189, 53) # L
    yellow = (235, 244, 235) #rgb(246, 227, 90) # O
    green = (240, 206, 155) #rgb(98, 190, 68) # S
    pink = (220, 109, 247) #rgb(242, 64, 235) # T
    red = (242, 13, 13) #rgb(225, 13, 27) # Z
    board_out = (153, 255, 102) #blue

    doll_head = (255, 204, 153)
    doll_arm_leg = (255, 153, 255)
    doll_eye = (102, 255, 255)
    doll_body = (204, 51, 255)


    t_color = [grey_2, cyan, blue, orange, yellow, green, pink, red]
def draw_Button () :
    #  speed up
    pygame.draw.rect(
        screen,
        ui_variables.red,
        Rect(50, 400, 50, 50)

    )
    text_SpeedUp = ui_variables.h7.render("S_Up", 1, ui_variables.black)
    screen.blit(text_SpeedUp, (50,415))
    #  speed down
    pygame.draw.rect(

        screen,
        ui_variables.doll_eye,
        Rect(50, 470, 50, 50)

    )

    text_SpeedDown = ui_variables.h8.render("S_Down", 1, ui_variables.black)
    screen.blit(text_SpeedDown , (50, 485))

    pygame.draw.rect(

        screen,
        (255, 204, 153),
        Rect(450, 400, 100, 50)

    )

    text_SpeedDown = ui_variables.h9.render("Music ON/OFF", 1, ui_variables.black)
    screen.blit(text_SpeedDown, (450, 415))

    pygame.draw.rect(

        screen,
        (255, 204, 153),
        Rect(450, 500, 100, 50)

    )

    text_SpeedDown = ui_variables.h10.render("New Theme", 1, ui_variables.black)
    screen.blit(text_SpeedDown, (450, 515))

def draw_doll() :

        pygame.draw.rect(
            screen,
            ui_variables.doll_head,
            Rect(300, 400, 40, 50)
        )
        pygame.draw.circle(screen, ui_variables.doll_eye, (310, 420), 5, 5)
        pygame.draw.circle(screen, ui_variables.doll_eye, (330, 420), 5, 5)
        pygame.draw.rect(
            screen,
            ui_variables.doll_body,
            Rect(290, 450, 60, 100)
        )
        # arm
        pygame.draw.rect(
            screen,
            ui_variables.doll_arm_leg,
            Rect(260, 480, 30, 10)
        )
        pygame.draw.rect(
            screen,
            ui_variables.doll_arm_leg,
            Rect(350, 450, 30, 10)
        )
        # remove pre arm
        pygame.draw.rect(
            screen,
            ui_variables.board_out,
            Rect(260, 450, 30, 10)
        )
        pygame.draw.rect(
            screen,
            ui_variables.board_out,
            Rect(350, 480, 30, 10)
        )
        # leg
        pygame.draw.rect(
            screen,
            ui_variables.doll_arm_leg,
            Rect(290, 550, 10, 30)
        )
        pygame.draw.rect(
            screen,
            ui_variables.doll_arm_leg,
            Rect(340, 550, 10, 30)
        )




def draw_doll_2() :
    pygame.draw.rect(
        screen,
        ui_variables.doll_head,
        Rect(300, 400, 40, 50)
    )
    pygame.draw.circle(screen, ui_variables.doll_eye, (310, 420), 5, 5)
    pygame.draw.circle(screen, ui_variables.doll_eye, (330, 420), 5, 5)
    pygame.draw.rect(
        screen,
        ui_variables.doll_body,
        Rect(290, 450, 60, 100)
    )
    # arm
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(260, 450, 30, 10)
    )
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(350, 480, 30, 10)
    )
    # remove pre arm
    pygame.draw.rect(
        screen,
        ui_variables.board_out,
        Rect(260, 480, 30, 10)
    )
    pygame.draw.rect(
        screen,
        ui_variables.board_out,
        Rect(350, 450, 30, 10)
    )
    # leg
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(290, 550, 10, 30)
    )
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(340, 550, 10, 30)
    )




def draw_Hot_Images(level) :

    Hot_image_1 = pygame.image.load("./assets/images/HIMG/LEVEL_1.png")
    Hot_image_2 = pygame.image.load("./assets/images/HIMG/LEVEL_2.png")
    Hot_image_3 = pygame.image.load("./assets/images/HIMG/LEVEL_3.png")
    Hot_image_4 = pygame.image.load("./assets/images/HIMG/LEVEL_4.png")

    if level == 1 :
        screen.blit(Hot_image_1, (301, 1))
    elif level == 2 :
        screen.blit(Hot_image_2, (301, 1))
    elif level == 3 :
        screen.blit(Hot_image_3, (301, 1))
    elif level == 4 :
        screen.blit(Hot_image_4, (301, 1))


# Draw single block
def draw_block(x, y, color):
    pygame.draw.rect(
        screen,
        color,
        Rect(x, y, block_size, block_size)
    )
    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(x, y, block_size, block_size),
        1
    )

# Draw game screen
def draw_board(next, hold, score, level, goal):
    screen.fill(ui_variables.board_out)

    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(204, 0, 96, 374)
    )

    pygame.draw.rect(
        screen,
        ui_variables.doll_head,
        Rect(300, 400, 40, 50)
    )
    pygame.draw.circle(screen, ui_variables.doll_eye, (310, 420), 5, 5)
    pygame.draw.circle(screen, ui_variables.doll_eye, (330, 420), 5, 5)
    pygame.draw.rect(
        screen,
        ui_variables.doll_body,
        Rect(290, 450, 60, 100)
    )
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(290, 550, 10, 30)
    )
    pygame.draw.rect(
        screen,
        ui_variables.doll_arm_leg,
        Rect(340, 550, 10, 30)
    )

    draw_Hot_Images(level)
    draw_Button()
    # Draw next mino
    grid_n = tetrimino.mino_map[next - 1][0]

    for i in range(4):
        for j in range(4):
            dx = 220 + block_size * j
            dy = 150 + block_size * i
            if grid_n[i][j] != 0:
                pygame.draw.rect(
                    screen,
                    ui_variables.t_color[grid_n[i][j]],
                    Rect(dx, dy, block_size, block_size)
                )

    # Draw hold mino
    grid_h = tetrimino.mino_map[hold - 1][0]

    if hold_mino != -1:
        for i in range(4):
            for j in range(4):
                dx = 220 + block_size * j
                dy = 50 + block_size * i
                if grid_h[i][j] != 0:
                    pygame.draw.rect(
                        screen,
                        ui_variables.t_color[grid_h[i][j]],
                        Rect(dx, dy, block_size, block_size)
                    )

    # Set max score
    if score > 999999:
        score = 999999

    # Draw texts
    text_hold = ui_variables.h5.render("HOLD", 1, ui_variables.black)
    text_next = ui_variables.h5.render("NEXT", 1, ui_variables.black)
    text_score = ui_variables.h5.render("SCORE", 1, ui_variables.black)
    score_value = ui_variables.h4.render(str(score), 1, ui_variables.black)
    text_level = ui_variables.h5.render("LEVEL", 1, ui_variables.black)
    level_value = ui_variables.h4.render(str(level), 1, ui_variables.black)
    text_goal = ui_variables.h5.render("GOAL", 1, ui_variables.black)
    goal_value = ui_variables.h4.render(str(goal), 1, ui_variables.black)


    # Place texts
    screen.blit(text_hold, (215, 14))
    screen.blit(text_next, (215, 114))
    screen.blit(text_score, (215, 214))
    screen.blit(score_value, (220, 230))
    screen.blit(text_level, (215, 264))
    screen.blit(level_value, (220, 280))
    screen.blit(text_goal, (215, 314))
    screen.blit(goal_value, (220, 330))

    #Draw Board Rect
    for x in range(width):
        for y in range(height):
            dx = 17 + block_size * x
            dy = 17 + block_size * y
            draw_block(dx, dy, ui_variables.t_color[matrix[x][y]])

# Draw a tetrimino
def draw_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix[x + j][y + i] = grid[i][j]

# Erase a tetrimino
def erase_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix[x + j][y + i] = 0

def is_bottom(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (y + i + 1) > 19:
                    return True
                elif matrix[x + j][y + i + 1] != 0:
                    return True

    return False

def is_leftedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j - 1) < 0:
                    return True
                elif matrix[x + j - 1][y + i] != 0:
                    return True

    return False

def is_rightedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j + 1) > 9:
                    return True
                elif matrix[x + j + 1][y + i] != 0:
                    return True

    return False

def is_turnable(x, y, mino, r):
    if r != 3:
        grid = tetrimino.mino_map[mino - 1][r + 1]
    else:
        grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 19:
                    return False
                elif matrix[x + j][y + i] != 0:
                    return False

    return True

def is_stackable(mino):
    grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            #print(grid[i][j], matrix[3 + j][i])
            if grid[i][j] != 0 and matrix[3 + j][i] != 0:
                return False

    return True

# Initial values

what_K = 0
blink = True
start = False
done = False
game_over = False

score = 0
level = 1
goal = level * 5

dx, dy = 3, 0
rotation = 0

mino = randint(1, 7)
next_mino = randint(1, 7)

hold = False
hold_mino = -1

matrix = [[0 for y in range(height)] for x in range(width)]




###########################################################
# Loop Start
###########################################################


while not done:

    # Game screen
    if start:

        for event in pygame.event.get():

            if event.type == QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN :
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] >= 50 and pygame.mouse.get_pos()[1] >= 400:
                    if pygame.mouse.get_pos()[0] <= 100 and pygame.mouse.get_pos()[1] <= 450 :
                        framerate = int(framerate * 0.85)
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 10)
                        ui_variables.S_UP_sound.play()

                if mouse_pos[0] >= 50 and pygame.mouse.get_pos()[1] >= 470:
                    if pygame.mouse.get_pos()[0] <= 100 and pygame.mouse.get_pos()[1] <= 520 :
                        framerate = int(framerate * 1.15)
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 10)
                        ui_variables.S_DOWN_sound.play()

                if mouse_pos[0] >= 450 and pygame.mouse.get_pos()[1] >= 400:
                    if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 450 :
                        if Music_playing:
                            pygame.mixer.music.pause()
                            Music_playing = False
                        else:
                            pygame.mixer.music.unpause()
                            Music_playing = True

                if mouse_pos[0] >= 450 and pygame.mouse.get_pos()[1] >= 500:
                    if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 550 :
                        if Skin_Changed == False:
                            Skin_1 = (84, 169, 146)
                            Skin_2 = (143, 181, 156)
                            Skin_3 = (237, 219, 195)
                            Skin_4 = (232, 197, 113)
                            Skin_5 = (217, 76, 58)
                            Skin_6 = (129, 58, 38)
                            Skin_7 = (99,130,112)
                            Skin_8 = (43,67,79)
                            ui_variables.t_color = [Skin_1 , Skin_2 , Skin_3 , Skin_4 , Skin_5 , Skin_6 , Skin_7 , Skin_8]
                            Skin_Changed = True
                            pygame.display.update()
                        else:
                            Skin_9 =  (35,35,35)
                            Skin_10 = (43,67,79)
                            Skin_11 = (12,227,255)
                            Skin_12 = (81,240,232)
                            Skin_13 = (149,254,208)
                            Skin_14 = (240,193,127)
                            Skin_15 = (255,163,145)
                            Skin_16 = (231,129,102)
                            ui_variables.t_color = [Skin_9, Skin_10, Skin_11, Skin_12, Skin_13, Skin_14, Skin_15, Skin_16]
                            Skin_Changed = False
                            pygame.display.update()


            elif event.type == USEREVENT:

                # Draw a mino
                draw_mino(dx, dy, mino, rotation)
                draw_board(next_mino, hold_mino, score, level, goal)
                if blink :
                    draw_doll()
                    blink = False
                else :
                    draw_doll_2()
                    blink = True
                # Erase a mino
                erase_mino(dx, dy, mino, rotation)

                # Move mino down
                if not is_bottom(dx, dy, mino, rotation):
                    dy += 1

                # Create new mino
                else:
                    score += 10 * level
                    draw_mino(dx, dy, mino, rotation)
                    draw_board(next_mino, hold_mino, score, level, goal)
                    if is_stackable(next_mino):
                        mino = next_mino
                        next_mino = randint(1, 7)
                        dx, dy = 3, 0
                        rotation = 0
                        hold = False
                    else:
                        start = False
                        game_over = True

                # Erase line
                erase_count = 0
                for j in range(20):
                    is_full = True
                    for i in range(10):
                        if matrix[i][j] == 0:
                            is_full = False
                    if is_full:
                        erase_count += 1
                        k = j
                        while k > 0:
                            for i in range(10):
                                matrix[i][k] = matrix[i][k - 1]
                            k -= 1
                if erase_count == 1:
                    ui_variables.single_sound.play()
                    score += 50 * level
                elif erase_count == 2:
                    ui_variables.double_sound.play()
                    score += 150 * level
                elif erase_count == 3:
                    ui_variables.triple_sound.play()
                    score += 350 * level
                elif erase_count == 4:
                    ui_variables.tetris_sound.play()
                    score += 1000 * level

                # Increase level give rewards
                goal -= erase_count
                if goal < 1 and level < 15:
                    level += 1
                    goal += level * 5
                    framerate = int(framerate * 0.8)
                    pygame.time.set_timer(pygame.USEREVENT , framerate * 10)




            elif event.type == KEYDOWN:
                erase_mino(dx, dy, mino, rotation)
                if event.key == K_SPACE:
                    ui_variables.drop_sound.play()
                    while not is_bottom(dx, dy, mino, rotation):
                        dy += 1
                elif event.key == K_LSHIFT:
                    if hold == False:
                        ui_variables.move_sound.play()
                        if hold_mino == -1:
                            hold_mino = mino
                            mino = next_mino
                            next_mino = randint(1, 7)
                        else:
                            hold_mino, mino = mino, hold_mino
                            dx, dy = 3, 0
                            rotation = 0
                        hold = True
                elif event.key == K_UP:
                    if is_turnable(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        rotation += 1
                    if rotation == 4:
                        rotation = 0
                elif event.key == K_DOWN:
                    if not is_bottom(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dy += 1
                elif event.key == K_LEFT:

                    if not is_leftedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                elif event.key == K_RIGHT:

                    if not is_rightedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                draw_mino(dx, dy, mino, rotation)
                draw_board(next_mino, hold_mino, score, level, goal)

        pygame.display.update()

    # Game over screen
    elif game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    ui_variables.click_sound.play()
                    game_over = False
                    hold = False
                    dx, dy = 3, 0
                    rotation = 0
                    mino = randint(1, 7)
                    next_mino = randint(1, 7)
                    hold_mino = -1
                    score = 0
                    matrix = [[0 for y in range(height)] for x in range(width)]

        over_text = ui_variables.h2.render("GAME OVER", 1, ui_variables.white)
        over_start = ui_variables.h5.render("Press space to RE HOT", 1, ui_variables.white)

        if game_over == True:
            draw_board(next_mino, hold_mino, score, level, goal)
            screen.blit(over_text, (20, 100))

            if blink:
                screen.blit(over_start, (32, 160))
                draw_doll()
                blink = False
            else:
                draw_doll_2()
                blink = True

            pygame.display.update()
            clock.tick(3)

    # Start screen
    else:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    ui_variables.click_sound.play()
                    start = True

        screen.fill(ui_variables.red)
        pygame.draw.rect(
            screen,
            ui_variables.red,
            Rect(0, 187, 300, 187)
        )

        title = ui_variables.h1.render("HOTris", 1, ui_variables.grey_1)
        title_start = ui_variables.h5.render("Press space to be HOT", 1, ui_variables.white)
        title_info = ui_variables.h6.render("Made by HSJPRIME. Forked From INJE", 1, ui_variables.white)


        screen.blit(title_start, (250, 280))
        screen.blit(title, (250, 200))
        screen.blit(title_info, (250, 335))

        if not start:
            pygame.display.update()
            clock.tick(3)


pygame.quit()
