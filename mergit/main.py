import mergit.UI as UI
import mergit.GUIController as GUIController
import pygame as pyg
import random as random
import os as os
import sys as sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))

    return os.path.join(base_path, relative_path)


class Application():
    # File Testing
    def __init__(self):
        '''pyg.mixer.init()
        self.music = random.choice([pyg.mixer.Sound(resource_path("./resources/Music.wav")),
                                   pyg.mixer.Sound(resource_path("./resources/Music2.wav"))])
        self.music.play(10)
        self.music.set_volume(1)
        '''
        # Global Variables
        self.START_WIDTH = 16*60
        self.START_HEIGHT = 9*60
        self.screenWidth = self.START_WIDTH
        self.screenHeight = self.START_HEIGHT
        self.screen = pyg.display.set_mode((self.screenWidth, self.screenHeight), pyg.RESIZABLE)
        pyg.display.set_caption("MerGit")
        try:
            gameIcon = pyg.image.load(resource_path('./resources/Icon.png'))
            pyg.display.set_icon(gameIcon)
        except FileNotFoundError:
            print("Windo icon file not found")

    def run(self):
        # Menu
        gui = GUIController.GUIController(self.screenWidth, self.screenHeight)
        clock = pyg.time.Clock()
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            
            # FPS limiter
            clock.tick(60)
            mousebuttonup = False
            scroll = (0, 0)
            for evnt in pyg.event.get():
                if evnt.type == pyg.QUIT:
                    running = False
                if evnt.type == pyg.MOUSEBUTTONUP:
                    mousebuttonup = True
                if evnt.type == pyg.VIDEORESIZE:
                    self.screenWidth = max(self.START_WIDTH, evnt.w - int(evnt.w) % 2)
                    self.screenHeight = max(self.START_HEIGHT, evnt.h)
                    self.screen = pyg.display.set_mode((self.screenWidth, self.screenHeight), pyg.RESIZABLE)
                    gui.resize(self.screenWidth, self.screenHeight, self.screenWidth/self.START_WIDTH, self.screenHeight/self.START_HEIGHT)
                if evnt.type == pyg.MOUSEBUTTONDOWN:
                    if evnt.button == 4:
                        scroll = (1, 0)
                    elif evnt.button == 5:
                        scroll = (0, 1)

            events = pyg.event.get()
            mx, my = pyg.mouse.get_pos()
            mb = pyg.mouse.get_pressed() + scroll
            keys = pyg.key.get_pressed()
            # print(mx, my)
            # print(pyg.display.get_surface().get_size())
            gui.update(mx, my, mb, keys)
            gui.draw(self.screen)
            if False:
                for i in range(0, self.screenWidth, 100 * self.screenWidth // (16*60)):
                    pyg.draw.line(self.screen, (0, 0, 0), (i, 0), (i, self.screenHeight))
                for i in range(0, self.screenHeight, 100 * self.screenHeight // (9*60)):
                    pyg.draw.line(self.screen, (0, 0, 0), (0, i), (self.screenWidth, i))

            pyg.display.flip()

