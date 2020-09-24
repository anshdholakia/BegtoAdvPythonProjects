import pyautogui as pg
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pg.keyDown(key)

def isCollide(data):

    for i in range(270,271):
        for j in range(564, 690):
            if data[i, j] < 100:
                hit("up")
                return

    for i in range(270,271):
        for j in range(400, 564):
            if data[i,j] < 120:
                hit("down")
                return


    return



# def draw():
#     pass



if __name__ == '__main__':
    print("Dino Game Initializing and Starting in 3 seconds")
    time.sleep(3)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data=image.load()
        isCollide(data)
    # print(asarray(image))

    # rectangle for cactus
    # for i in range(260,300):
    #         for j in range(564,690):
    #             data[i,j]=120
    #
    # # rectangle for bird
    # for i in range(260,300):
    #         for j in range(400,564):
    #             data[i,j]=0


    # image.show()

