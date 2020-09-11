import random
import sys  # sys to exit the game
import pygame
from pygame.locals import *

# Global variables for game
FPS = 32
Screen_Width = 578
Screen_Height = 511
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
Ground_Y = Screen_Height*0.8
Game_Sprites = {}
Game_Sounds = {}
PLAYER = 'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\bird.png'
BACKGROUND = 'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\background.png'
Pipe = 'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\pipe.png'


def welcomeScreen():
    '''
    shows welcome screen
    '''
    playerx = int(Screen_Width/5)
    playery = int((Screen_Height - Game_Sprites['Player'].get_height())/2)
    messagex = int((Screen_Width - Game_Sprites['message'].get_width())/2)
    messagey = int(Screen_Height*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross close game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # if user clicks space or upkey start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return

            else:
                Screen.blit(Game_Sprites['Background'], (0, 0))
                Screen.blit(Game_Sprites['Player'], (playerx, playery))
                Screen.blit(Game_Sprites['message'], (messagex, messagey))
                Screen.blit(Game_Sprites['ground'], (basex, Ground_Y))
                pygame.display.update()
                FPSClock.tick(FPS)


def mainGame():
    score = 0
    playerx = int(Screen_Width/5)
    playery = int(Screen_Width/2)
    basex = 0

    # creating pipes
    newpipe1 = getRandompipe()
    newpipe2 = getRandompipe()

    # my list of upper pipes
    upperPipes = [{'x': Screen_Width+200, 'y': newpipe1[0]['y']},
                  {'x': Screen_Width+200+(Screen_Width/2), 'y': newpipe2[0]['y']}, ]
    # my list of lower pipes
    lowerPipes = [
        {'x': Screen_Width + 200, 'y': newpipe1[1]['y']},
        {'x': Screen_Width + 200 + (Screen_Width / 2), 'y': newpipe2[1]['y'], }
    ]
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccV = -8  # vel while flapping

    playerFlapped = False  # true only when bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccV
                    playerFlapped = True
                    Game_Sounds['wing'].play()

        # this function will return true if crashed
        crashtest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashtest:
            return

        # check for score
        playerMidPros = playerx+Game_Sprites['Player'].get_width() / 2
        for pipe in upperPipes:
            pipeMidPros = pipe['x'] + Game_Sprites['pipe'][0].get_width()/2
            if pipeMidPros <= playerMidPros < pipeMidPros+4:
                score += 1
                print(f"Your score is {score}")
                Game_Sounds['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = Game_Sprites['Player'].get_height()
        playery = playery + min(playerVelY, Ground_Y-playery-playerHeight)

        # move pipes to left:
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

            # Add a new pipe when first is going left:
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandompipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

            # if pipe out of screen remove it
        if upperPipes[0]['x'] < -Game_Sprites['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

            # lets blit our sprites
        Screen.blit(Game_Sprites['Background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            Screen.blit(Game_Sprites['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            Screen.blit(Game_Sprites['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        Screen.blit(Game_Sprites['ground'], (basex, Ground_Y))
        Screen.blit(Game_Sprites['Player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]

        width = 0

        for digit in myDigits:
            width += Game_Sprites['numbers'][digit].get_width()
        Xoffset = (Screen_Width-width)/2

        for digit in myDigits:
            Screen.blit(Game_Sprites['numbers'][digit],
                        (Xoffset, Screen_Height*0.12))
            Xoffset += Game_Sprites['numbers'][digit].get_width()
        pygame.display.update()
        FPSClock.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > Ground_Y-25 or playery < 0:
        Game_Sounds['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = Game_Sprites['pipe'][0].get_height()
        if (playery < pipeHeight+pipe['y'] and abs(playerx-pipe['x']) < Game_Sprites['pipe'][0].get_width()):
            Game_Sounds['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + Game_Sprites['Player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < Game_Sprites['pipe'][0].get_width():
            Game_Sounds['hit'].play()
            return True
    return False


def getRandompipe():
    '''
    generate position of two pipes for bliting
    '''
    pipe_Height = Game_Sprites['pipe'][0].get_height()
    offset = Screen_Height/3
    y2 = offset+random.randrange(0, int(Screen_Height -
                                        Game_Sprites['ground'].get_height()-1.2*offset))

    pipeX = Screen_Width+100
    y1 = pipe_Height - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper pipe
        {'x': pipeX, 'y': y2}  # lower pipe
    ]
    return pipe


if __name__ == '__main__':
    pygame.init()  # pygame module initialize
    FPSClock = pygame.time.Clock()
    pygame.display.set_caption("Flappy Bird By Ansh Dholakia")
    Game_Sprites['numbers'] = (
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number0.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number1.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number2.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number3.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number4.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number5.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number6.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number7.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number8.png').convert_alpha(),
        pygame.image.load(
            'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\number9.png').convert_alpha()
    )
    Game_Sprites['message'] = pygame.image.load(
        'C:\\Users\\Ansh\\PycharmProjects\\First Project File\\Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\message.png').convert_alpha()
    Game_Sprites['ground'] = pygame.image.load(
        'Flappy_Bird_Gallery\\SPRITES_FLAPPY_BIRD\\ground.png').convert_alpha()
    Game_Sprites['pipe'] = (pygame.transform.rotate(pygame.image.load(
        Pipe).convert_alpha(), 180), pygame.image.load(Pipe).convert_alpha())

    # Game Sounds:
    Game_Sounds['die'] = pygame.mixer.Sound(
        'Flappy_Bird_Gallery/MUSIC_FLAPPY_BIRD/death.wav')
    Game_Sounds['wing'] = pygame.mixer.Sound(
        'Flappy_Bird_Gallery\\MUSIC_FLAPPY_BIRD\\flap.wav')

    Game_Sounds['hit'] = pygame.mixer.Sound(
        'Flappy_Bird_Gallery\\MUSIC_FLAPPY_BIRD\\hit.wav')
    Game_Sounds['swoosh'] = pygame.mixer.Sound(
        'Flappy_Bird_Gallery\\MUSIC_FLAPPY_BIRD\\Slurp.wav')
    Game_Sounds['point'] = pygame.mixer.Sound(
        'Flappy_Bird_Gallery\\MUSIC_FLAPPY_BIRD\\point.wav')

    Game_Sprites['Background'] = pygame.image.load(BACKGROUND).convert()
    Game_Sprites['Player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen()  # Welcome screen to user until button pressed
        mainGame()
