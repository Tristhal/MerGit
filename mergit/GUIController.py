import mergit.GUIInterfaces as GUI
import mergit.Project as Project
import pygame as pyg


class GUIController():

    def __init__(self, width, height):
        pyg.font.init()
        self.projectController = Project.ProjectController()
        self._width = width
        self._height = height
        self.width = width
        self.height = height

        self._positions = [[0, 0, width, 26], [300, 26, width - 300, height - 26], [0, 26, 300, height - 26]]
        self.positions = [[0, 0, width, 26], [300, 26, width - 300, height - 26], [0, 26, 300, height - 26]]

        self.interfaceButtons = GUI.InterfaceButtons(0, 0, width, 26, self.projectController)
        self.interfaceSurface = pyg.Surface((width, 26))
        self.conflictDisplay = GUI.ConflictDisplay(0, 0, width - 300, height - 26, self.projectController)
        self.conflictSurface = pyg.Surface((width - 300, height - 26))
        self.projectDisplay = GUI.ProjectDisplay(0, 0, 300, height - 26, self.projectController)
        self.projectSurface = pyg.Surface((300, height - 26))

        self.objects = [self.interfaceButtons, self.conflictDisplay, self.projectDisplay]
        self.surfaces = [self.interfaceSurface, self.conflictSurface, self.projectSurface]
        
    def update(self, mx, my, mb, keys):
        for i in range(len(self.objects)):
            self.objects[i].update(mx-self.positions[i][0], my-self.positions[i][1], mb, keys)

    def draw(self, screen):
        for i in range(len(self.objects)):
            self.objects[i].draw(self.surfaces[i])
            screen.blit(self.surfaces[i], (self.positions[i][0], self.positions[i][1]))

    def resize(self, newWidth, newHeight, scalex, scaley):
        X = 0
        Y = 1
        WIDTH = 2
        HEIGHT = 3

        self.width = newWidth
        self.height = newHeight
        width = self._width
        height = self._height
        scales = []

        # Interface Display
        i = 0
        nscalex = newWidth / self._width  # scale based off screen size
        nscaley = newHeight / self._height
        self.interfaceSurface = pyg.Surface((self._positions[i][WIDTH] * nscalex, self._positions[i][HEIGHT]))
        scales.append([nscalex, nscaley])

        # Conflict Display
        i = 1
        nscalex = newWidth / self._width  # scale base of screen size
        nscaley = (newHeight - self._positions[i][Y]) / (self._positions[i][HEIGHT])  # extend screen from starting point to end of the screen
        self.conflictSurface = pyg.Surface((self._positions[i][WIDTH] * nscalex, self._positions[i][HEIGHT] * nscaley))
        scales.append([nscalex, nscaley])

        # Project Display
        i = 2
        nscalex = newWidth / self._width  # scale base of screen size
        nscaley = (newHeight - self._positions[i][Y]) / (self._positions[i][HEIGHT])  # extend screen from starting point to end of the screen
        self.projectSurface = pyg.Surface((self._positions[i][WIDTH] * nscalex, self._positions[i][HEIGHT] * nscaley))
        scales.append([nscalex, nscaley])

        self.surfaces = [self.interfaceSurface, self.conflictSurface, self.projectSurface]

        # scale x positions of screens
        for i in range(len(self.positions)):
            self.positions[i][0] = self._positions[i][0] * scales[i][X]
            self.objects[i].resize(scales[i][X], scales[i][Y])
