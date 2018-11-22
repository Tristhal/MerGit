from pygame import gfxdraw
import pygame as pyg
from collections import OrderedDict
'''
1. Pannel(self, x, y, width=10, height=10)
2. GenericFrame()
3. Box(self, x, y, parent, width=10, height=10,
    hollow=False, border=False, background_color=(255, 255, 255),
    border_color=(0, 0, 0))

4. Button(self, x, y, parent, width=10, height=10, functions_triggered=[], functions_pressed=[])
5. CheckBox
6. ScrollBar
7. fontLoad
8. TextLine
9. TextBox
10. Line
'''
from mergit.settings import *

# ##########################################################################################################################################
# ##########################################################################################################################################


class Pannel():
    """
    Parameters
    ----------
    x : double
    y : double
    width : double
    height : double

    Attributes
    ----------
    x : double
    y : double
    width : double
    height : double
    objects : dictionary of objects
        objects in pannel {name : object}
    """
    def __init__(self, x, y, width=10, height=10, scaling="xywh"):
            self._x = x
            self._y = y
            self.scaling = scaling + "p"
            self.width = width
            self.height = height
            self.scaley = 1
            self.scalex = 1
            # Visual Traits
            self.box = Box(0, 0, self, width=width, height=height, scaling=scaling)

            self.objects = OrderedDict()
            self._id_pos = 0

    def draw(self, screen):
        self.box.draw(screen)
        for key in self.objects.keys():
            self.objects[key].draw(screen)

    def update(self, mx, my, mb, keys):
        for key in self.objects.keys():
            self.objects[key].update(mx, my, mb, keys)

    def get(self, name):
        # Error Handled Here #
        try:
            return self.objects[name]
        except KeyError:
            return None
            print("Error: Invalid Key / Object not in pannel")

    def add(self, name, obj):
        # Error Handled Here #
        if name is None:
            # Use next available id
            while (self.idStr(self.id) in self.objects):
                self.id += 1
            self.objects[self.idStr(self.id)] = obj
        else:
            if (name in self.objects):
                print("Error: Object with key \"" + name + "\" already exists")
            else:
                self.objects[name] = obj

    def idStr(self, number):
        return "Key:" + str(self.id)

    def setBox(self, box):
        self.box = box

    def getBox(self):
        return self.box

    # Override
    def getX(self, debug=False):
        if "x" in self.scaling:
            if not("w" in self.scaling) and "p" in self.scaling:
                return self._x * self.scalex + self._width * (self.scalex - 1)
            else:
                return self._x * self.scalex
        else:
            return self._x

    # Override
    def getY(self):
        if "y" in self.scaling:
            if not("h" in self.scaling) and "p" in self.scaling:
                return self._y * self.scaley + self._height * (self.scalex - 1)
            else:
                return self._y * self.scaley
        else:
            return self._y

    def getScaleX(self):
        return self.scalex

    def getScaleY(self):
        return self.scaley

    # Override
    def resize(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley
        self.box.scale(scalex, scaley)
        # resize objects
        for key in self.objects.keys():
            self.objects[key].scale(self.getScaleX(), self.getScaleY())
# ##########################################################################################################################################
# ##########################################################################################################################################


class GenericFrame():
    def __init__(self, x, y, parent, width=10, height=10, scaling="xywh"):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.scalex = 1
        self.scaley = 1
        self.parent = parent
        self.scaling = scaling

    def draw(self, screen):
        pass

    def update(self, mx, my, mb, keys):
        pass

    def getX(self, debug=False):
        if "x" in self.scaling:
            if not("w" in self.scaling) and "p" in self.scaling:
                return self._x * self.scalex + self.parent.getX() + self._width * (self.scalex - 1)
            else:
                return self._x * self.scalex + self.parent.getX()
        else:
            return self._x + self.parent.getX()

    def getY(self):
        if "y" in self.scaling:
            if not("h" in self.scaling) and "p" in self.scaling:
                return self._y * self.scaley + self.parent.getY() + self._height * (self.scalex - 1)
            else:
                return self._y * self.scaley + self.parent.getY()
        else:
            return self._y + self.parent.getY()

    def getWidth(self):
        if "w" in self.scaling:
            if "x" not in self.scaling:
                return self._width * self.scalex + self._x * (self.scalex - 1)
            else:
                return self._width * self.scalex
        else:
            return self._width

    def getHeight(self):
        if "h" in self.scaling:
            if "y" not in self.scaling:
                return self._height * self.scaley + self._y * (self.scaley)
            else:
                return self._height * self.scaley
        else:
            return self._height

    def setNewY(self, y):
        self._y = y / self.scaley

    def scale(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley

# ##########################################################################################################################################
# ##########################################################################################################################################


class Box(GenericFrame):
    '''
    Parameters
    ----------
    x : double
        relative position to parent
    y : double
        relative position to parent
    parent : object
        - Object to which the box is anchored
        - Must contain public getX and getY methods

    Optional Parameters
    -------------------
    width : double
    height : double
    border : boolean
    hollow : boolean
    background_color : RGB or RGBA
    border_color : RGB or RGBA

    Atributes
    ---------
    x : double
        relative x position to parent
    y : double
        relative y position to parent
    parent : object
        - Object to which the box is anchored
        - Must contain public x and y variables
    border : boolean
    hollow : boolean
    background_color : RGB or RGBA
    border_color : RGB or RGBA
    image : blitable image

    Methods
    -------
    draw(pygame surface)
    changeSettings(self, x=None, y=None, parent=None, width=None, height=None,
                       hollow=None, border=None, background_color=None,
                       border_color=None)
    setImage(pygame image)
    update(mx, my, mb, keys)
    getX()
    getY()
    getWidth()
    getHeight()
    scale(scalex, scaley)

    '''
    def __init__(self, x, y, parent, width=10, height=10,
                 hollow=False, border=False, background_color=(255, 255, 255),
                 border_color=(0, 0, 0), scaling="xywh"):
        '''
        Constructor
        '''
        GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling)
        # Visual Traits
        self.border = border
        self.hollow = hollow
        self.background_color = background_color
        self.border_color = border_color
        self.image = None
        self.obj = None

    def draw(self, screen):
        """
        """
        if not (self.hollow):
            gfxdraw.box(screen, (int(self.getX()), self.getY(), self.getWidth(), self.getHeight()),
                        self.background_color)
        if (self.border):
            gfxdraw.rectangle(screen, (int(self.getX()), self.getY(), self.getWidth(), self.getHeight()),
                              self.border_color)
        if (self.image is not None):
            screen.blit(self.image)
        elif (self.obj is not None):
            self.obj.draw(screen)

    def changeSettings(self, x=None, y=None, parent=None, width=None, height=None,
                       hollow=None, border=None, background_color=None,
                       border_color=None):
        """
        self, x=None, y=None, parent=None, width=None, height=None,
                       hollow=None, border=None, background_color=None,
                       border_color=None
        """
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if parent is not None:
            self.parent = parent
        if width is not None:
            self._width = width
        if height is not None:
            self._height = height
        if hollow is not None:
            self.hollow = hollow
        if border is not None:
            self.border = border
        if background_color is not None:
            self.background_color = background_color
        if border_color is not None:
            self.border_color = border_color

    def setImage(self, image):
        self.image = image

    def setObj(self, obj):
        '''
        object with .draw(screen) function to draw
        '''
    # ######################################################################################## Change set to change scale back change

    def getRect(self):
        return pyg.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight())

# ##########################################################################################################################################
# ##########################################################################################################################################


class Button(GenericFrame):
    '''
    Parameters
    ----------
    x : double
        relative x postiion to parent
    y : double
        relative y position to parent
    parent : object
        - Object to which the box is anchored
        - Must contain getX and getY functions

    Optional Parameters
    -------------------
    width : double
    height : double
    border : boolean
    hollow : boolean
    background_color : RGB or RGBA
    border_color : RGB or RGBA

    Atributes
    ---------
    width : double
    height : double
    parent : object
        - Object to which the box is anchored
        - Must contain getX and getY functions
    box_base : GenericFrame object to draw
    box_triggered : GenericFrame object to draw
    box_pressed : GenericFrame object to draw
    box_hover : GenericFrame object to draw
    functions_triggered : when triggered (mouse up) call these functions with self as an argument
    functions_pressed : when pressed call these functions with self as an argument

    '''
    def __init__(self, x, y, parent, width=10, height=10, functions_triggered=[],
                 functions_pressed=[], border=False, background_color=(255, 0, 255), scaling="xywh"):

            GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling)
            # visual traits
            self.box_base = Box(0, 0, self, width=width, height=height, border=border, background_color=background_color, scaling=scaling)
            self.box_triggered = Box(0, 0, self, width=width, height=height, border=border, background_color=background_color, scaling=scaling)
            self.box_pressed = Box(0, 0, self, width=width, height=height, border=border, background_color=background_color, scaling=scaling)
            self.box_hover = Box(0, 0, self, width=width, height=height, border=border, background_color=background_color, scaling=scaling)
            # button state
            self.triggered = False
            self.pressed = False
            self.hover = False
            # trigger functions
            self.functions_triggered = functions_triggered
            self.functions_pressed = functions_pressed

    # Override
    def draw(self, screen):
        if self.triggered:
            self.box_triggered.draw(screen)
        elif self.pressed:
            self.box_pressed.draw(screen)
        elif self.hover:
            self.box_hover.draw(screen)
        else:
            self.box_base.draw(screen)

    # Override
    def update(self, mx, my, mb, keys):
        click = False
        if self.pressed and (mb[0] == 0):
            click = True
        # reset state variables
        self.hover = False
        self.triggered = False
        self.pressed = False
        # check collide and set new state
        if pyg.Rect(self.getX(), self.getY(), self.getWidth(), self.getHeight()).collidepoint(mx, my):
            self.hover = True
            if mb[0]:
                self.pressed = True
                self.hover = False
            elif click:
                self.triggered = True
                self.hover = False
        # handle the updates
        if self.triggered:
            self.triggerHandle()
        elif self.pressed:
            self.pressedHandle()

    def triggerHandle(self):
        for i in self.functions_triggered:
            i(self)

    def pressedHandle(self):
        for i in self.functions_pressed:
            i(self)

    # Override
    def scale(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley
        self.box_base.scale(scalex, scaley)
        self.box_triggered.scale(scalex, scaley)
        self.box_hover.scale(scalex, scaley)
        self.box_pressed.scale(scalex, scaley)

# ##########################################################################################################################################
# ##########################################################################################################################################


# scaling untested
class checkBox(GenericFrame):

    def __init__(self, x, y, parent, width=10, height=10, functions_toggled=[], background_color=(0, 0, 0),
                 scaling="xywh"):
        GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling)
        self.button = Button(x, y, self, width=width, height=height, border=True, functions_triggered=[self.toggleButton], scaling=scaling)
        self.box_toggled = Box(x + 2, y + 2, self, width=width - 4, height=height - 4, background_color=(0, 0, 0), scaling=scaling)

        # Box value
        self.value = False

    def draw(self, screen):
        self.button.draw(screen)
        if self.value:
            self.box_toggled.draw(screen)

    def update(self, mx, my, mb, keys):
        self.button.update(mx, my, mb, keys)

    def toggleButton(self, button):
        self.value = not self.value

    def toggleHandle(self):
        for i in self.functions_toggled:
            i(self)

    def getValue(self):
        return self.value

    # override
    def scale(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley
        self.button.scale(scalex, scaley)
        self.box_toggled.scale(scalex, scaley)
# ##########################################################################################################################################
# ##########################################################################################################################################


class ScrollBar(GenericFrame):

    def __init__(self, x, y, parent, width=10, height=100, bar_size=10, functions_moved=[], scaling="xywh", color=(50, 50, 55)):
        GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling + "p")  # p for parent
        # traits
        self.mouseScroll = True
        # visual traits
        self.bar_size = bar_size
        self.box_scroll_bar = Box(0, 0, self, width=width, height=height, border=True, scaling=scaling.replace("x", ""))
        self.box_bar = Box(1, 0, self, width=width - 2, height=bar_size, background_color=color, scaling=scaling.replace("x", ""))
        # scroll state
        self.scrollPosition = 0.01
        self.scrollPercentage = 0.01
        # trigger functions
        self.functions_moved = functions_moved
        # mouse state variables
        self.was_pressed = 0

    def draw(self, screen):
        self.box_scroll_bar.draw(screen)
        self.box_bar.draw(screen)

    def update(self, mx, my, mb, keys):
        edge_buffer = 1

        newpos = 0
        if mb[0] == 1:
            if self.box_bar.getRect().collidepoint(mx, my) or self.was_pressed == 1:
                self.was_pressed = 1
                newpos = my
        else:
            self.was_pressed = 0

        if self.mouseScroll and self.box_scroll_bar.getRect().collidepoint(mx, my) and mb[3]:
            newpos = self.box_bar.getY() - 1
        elif self.mouseScroll and self.box_scroll_bar.getRect().collidepoint(mx, my) and mb[4]:
            newpos = self.box_bar.getY() + 1

        if newpos:
            self.scrollPosition = (max(min(newpos, self.getY() + self.getHeight() - int(self.box_bar.getHeight()) - edge_buffer), self.getY()) - self.getY())  # Percentage Height
            print("DEBUG", self.scrollPosition)
            self.scrollPosition /= self.getHeight()
            self.scrollPercentage = self.scrollPosition / ((self.getHeight() - int(self.box_bar.getHeight()) - edge_buffer) / self.getHeight())
            self.movedHandle()
        # Fix the box position manually
        self.box_bar.setNewY(self.scrollPosition * self.getHeight())

    def movedHandle(self):
        for i in self.functions_moved:
            i(self)

    def getValue(self):
        return self.scrollPercentage

    # Override
    def scale(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley
        self.box_scroll_bar.scale(scalex, scaley)
        self.box_bar.scale(scalex, scaley)
# ##########################################################################################################################################
# ##########################################################################################################################################


def loadFont(font, font_size):
    temp = None
    try:
        temp = pyg.font.Font(font, font_size)
    except OSError:
        try:
            temp = pyg.font.SysFont(font, font_size)
        except FileNotFoundError:
            pass
    
    if temp is None:
        print("Error: Font file not found")
        return pyg.font.SysFont(None, font_size)
    else:
        return temp


class TextLine(GenericFrame):

    def __init__(self, x, y, parent, text="", width=10, height=10, background_color=(255, 255, 255),
                 text_color=(0, 0, 0), font=DEFAULT_TEXT, font_size=16, alignment="top left", scaling="xywh", border=True):
        GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling + "p")

        self.background = Box(0, 0, self, width=width, height=height, border=border, background_color=background_color, scaling=scaling)
        self.alignment = alignment
        self.font = loadFont(font, font_size)
        self._text = text
        self.textColor = text_color
        self.label = self.font.render(text, True, text_color)

    def setBold(self, bool):
        self.font.set_bold(bool)

    def setFont(self, font, font_size):
        self.font = loadFont(font, font_size)

    def draw(self, screen):
        alignment = self.alignment.split()
        # Checking for Valid alignment
        if(len(alignment) != 2):
            print("Invalid Alignment")
            return

        if alignment[0] == "center":
            buffery = (self.getHeight() - self.label.get_height()) / 2 + 2
        elif alignment[0] == "top":
            buffery = 2
        elif alignment[0] == "bottom":
            buffery = (self.getHeight() - self.label.get_height())

        if alignment[1] == "center":
            bufferx = (self.getWidth() - self.label.get_width()) / 2
        elif alignment[1] == "left":
            bufferx = 2
        elif alignment[1] == "right":
            bufferx = (self.getWidth() - self.label.get_width())-2

        if(bufferx is None or buffery is None):
            print("Invalid Alignment")
            return

        self.background.draw(screen)
        screen.blit(self.label, (int(self.getX() + bufferx), int(self.getY() + buffery)))

    def setText(self, text):
        self._text = text
        self.label = self.font.render(text, True, self.textColor)

    def scale(self, scalex, scaley):
        self.scalex = scalex
        self.scaley = scaley
        self.background.scale(scalex, scaley)
# ##########################################################################################################################################
# ##########################################################################################################################################


class TextBox(GenericFrame):

    def __init__(self, x, y, parent, width=10, height=10, lines=[], font=DEFAULT_TEXT, font_size=16, scaling="xywh", text_color=(0, 0, 0), number_color=(0, 0, 0), background_color=(255,255,255), line_states=1, line_colors=[(255,255,255)]):
        '''
        Constructor
        '''
        GenericFrame.__init__(self, x, y, parent, width=width, height=height, scaling=scaling + "p")

        # Graphical Settings
        # Text
        self.setFont(font, font_size, text_color=text_color)  # assign all font variables

        self.numberColor = number_color
        self.backgroundColor = background_color
        self.lineStates = line_states
        self.lineColors = line_colors
        # Components
        self.box = Box(0, 0, self, width=width, height=height, scaling=scaling, background_color=background_color)
        self.scrollBar = ScrollBar(self.getWidth() - 20, 0, self, 20, self.getHeight(), functions_moved=[self.scrollHandle], bar_size=20, scaling=scaling.replace("w", ""))
        # Data
        self.lines = lines
        self.listOfLines = []
        self.populate(lines)
        self.firstLine = 0
        self.numberWidth = self.fontSpacing * len(str(len(self.listOfLines)))
        # Component
        self.createButtons()

    def setFont(self, font_name, font_size, text_color=None):
        self.font_size = font_size
        self.fontType = font_name
        self.font = loadFont(font_name, font_size)
        self.lineHeight = int(1.15 * self.font.get_height())
        if text_color is not None:
            self.textColor = text_color
        self.fontSpacing = 1 * self.font_size

    def draw(self, screen):
        self.box.draw(screen)  # Draw Background
        self.numberWidth = self.fontSpacing * len(str(len(self.listOfLines)))
        counter = 0
        textBuffer = 15
        for x in range(self.firstLine, min(self.firstLine + int(self.getHeight()//self.lineHeight), len(self.listOfLines)), 1):
            # Graphical Settings
            textLinePosition = (self.getX() + self.numberWidth + textBuffer, self.getY() + (self.lineHeight * counter))
            textLineGBRect = (self.getX(), round(int(self.getY()) + (self.lineHeight * counter)), self.getWidth(), self.lineHeight)
            # Drawing
            gfxdraw.box(screen, textLineGBRect, self.listOfLines[x].getColor())
            self.buttons[counter].draw(screen)
            # Draw Line of Text
            label = TextLine(textLinePosition[0], textLinePosition[1], self, alignment="center left", height=self.lineHeight,
                             width=self.getWidth(), background_color=(0, 0, 0, 0), border=False)
            label.label = self.listOfLines[x].label
            label.draw(screen)
            # draw line number
            label = TextLine(self.getX(), self.getY() + (self.lineHeight * counter), self, str(x), width=self.numberWidth,
                             height=self.lineHeight, font=self.fontType, alignment="center right",
                             text_color=self.numberColor, background_color=(0, 0, 0, 0), border=False)
            label.draw(screen)
            # Update
            counter += 1
        self.scrollBar.draw(screen)

    def update(self, mx, my, mb, keys):
        self.scrollBar.update(mx, my, mb, keys)
        for i in range(len(self.buttons)):
            self.buttons[i].update(mx, my, mb, keys)
            if(self.buttons[i].triggered):
                self.listOfLines[self.firstLine + i].nextState()

    def populate(self, lines):
        # lines = array of text lines
        for x in self.lines:
            self.listOfLines.append(Line(x, self.lineStates, self.textColor, self.font, self.lineColors))

    def createButtons(self):
        self.buttons = []
        for i in range(int(min(self.getHeight()//self.lineHeight, len(self.lines) - self.firstLine))):
            buttonYPosition = self.getY() + (self.lineHeight * i)

            button = Button(self.getX(), buttonYPosition, self, self.numberWidth, self.lineHeight, background_color=BUTTON_COLOR, border=False)
            button.box_base.changeSettings(background_color=BUTTON_COLOR)
            button.box_hover.changeSettings(background_color=BUTTON_HOVER)
            self.buttons.append(button)

    def remove(self, index):
        del self.listOfLines[index]

    def add(self, index, line):
        self.listOfLines.inset(index, [self.font.render(line, True, self.textColor, (255, 255, 255))])

    def clear(self):
        self.listOfLines.clear()

    def scrollHandle(self, scrollBar):
        print("DEBUG", self.scrollBar.getValue())
        self.firstLine = int(scrollBar.getValue() * len(self.listOfLines))
        self.createButtons()

    # Override
    def scale(self, scalex, scaley):
        GenericFrame.scale(self, scalex, scaley)
        self.box.scale(scalex, scaley)
        self.scrollBar.scale(scalex, scaley)
        self.createButtons()


class Line:

        def __init__(self, text, states, text_color, font, colors=[(255, 255, 255)], state=0):
            self.label = font.render(text.replace("\t"," " * TABSPACES), True, text_color)
            self.state = state
            self.colors = colors
            self.textColor = text_color
            self.states = states
            self.text = text
            self.font = font

        def getColor(self):
            return self.colors[self.state]

        def nextState(self):
            self.state = (self.state + 1) % self.states
