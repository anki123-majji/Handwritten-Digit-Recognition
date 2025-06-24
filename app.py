import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2

# Window settings
WINDOWSIZEX = 640
WINDOWSIZEY = 480

BOUNDRYINC = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IMAGESAVE = False

MODEL = load_model("D:/Deep learning/bestmodel.keras")
LABELS = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}

pygame.init()
FONT = pygame.font.Font("freesansbold.ttf", 18)
DISPLAYSURF = pygame.display.set_mode((WINDOWSIZEX, WINDOWSIZEY))
pygame.display.set_caption("Digit Recognition Board")

iswriting = False
Number_xcord = []
Number_ycord = []
img_cnt = 1
PREDICT = True

DISPLAYSURF.fill(BLACK)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEMOTION and iswriting:
            xcord, ycord = event.pos
            pygame.draw.circle(DISPLAYSURF, WHITE, (xcord, ycord), 4, 0)
            Number_xcord.append(xcord)
            Number_ycord.append(ycord)

        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == MOUSEBUTTONUP:
            iswriting = False

            if Number_xcord and Number_ycord:
                rect_min_x = max(min(Number_xcord) - BOUNDRYINC, 0)
                rect_max_x = min(max(Number_xcord) + BOUNDRYINC, WINDOWSIZEX)
                rect_min_y = max(min(Number_ycord) - BOUNDRYINC, 0)
                rect_max_y = min(max(Number_ycord) + BOUNDRYINC, WINDOWSIZEY)

                Number_xcord = []
                Number_ycord = []

                # Get RGB array and crop it
                img_array = pygame.surfarray.array3d(DISPLAYSURF)
                cropped_img = img_array[rect_min_x:rect_max_x, rect_min_y:rect_max_y]
                cropped_img = np.transpose(cropped_img, (1, 0, 2))  # for OpenCV format

                if cropped_img.size != 0:
                    gray = cv2.cvtColor(cropped_img, cv2.COLOR_RGB2GRAY)
                    resized = cv2.resize(gray, (28, 28))
                    padded = np.pad(resized, ((10, 10), (10, 10)), 'constant', constant_values=0)
                    final_img = cv2.resize(padded, (28, 28)) / 255.0
                    final_img = np.expand_dims(final_img, axis=-1)

                    if IMAGESAVE:
                        cv2.imwrite(f"image_{img_cnt}.png", padded)
                        img_cnt += 1

                    prediction = MODEL.predict(final_img.reshape(1, 28, 28, 1))
                    label = str(LABELS[np.argmax(prediction)])

                    textsurface = FONT.render(label, True, RED, WHITE)
                    textRectObj = textsurface.get_rect()
                    textRectObj.left, textRectObj.bottom = rect_min_x, rect_max_y
                    DISPLAYSURF.blit(textsurface, textRectObj)

        # Press 'n' to clear screen
        if event.type == KEYDOWN:
            if event.unicode == "n":
                DISPLAYSURF.fill(BLACK)

    pygame.display.update()
