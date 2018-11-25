import mergit.UI as UI
import mergit.Widgets as Widgets
from mergit.settings import *

'''
1. InterfaceButtons
2. ConflictDisplay
3. ProjectDisplay
'''

# ##########################################################################################################################################
# ##########################################################################################################################################


class InterfaceButtons():
    def __init__(self, x, y, pannelWidth, pannelHeight, projectController):
        self.pannelWidth = pannelWidth
        self.pannelHeight = pannelHeight
        self.x = x
        self.y = y
        self.projectController = projectController
        self.fileGetter = Widgets.GetFile()
        self.dialogueBox = Widgets.DisplayMessage()
        self.createMenu()

    def createMenu(self):
        # Undo Button
        # NextConflict
        self.menu = UI.Pannel(self.x, self.y, width=self.pannelWidth, height=self.pannelHeight)
        box = self.menu.box
        box.changeSettings(background_color=BACKGROUND_LIGHT_1)
        buffersize = 3
        # Menu Bar
        box = UI.Box(0, 0, self.menu, self.pannelWidth, self.pannelHeight, background_color=BACKGROUND_DARK_1, border=True, scaling="xw")
    
        self.menu.add("Menu Bar", box)

        # LoadProject Button
        button = UI.Button(buffersize, buffersize, self.menu, width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, functions_triggered=[self.loadProject], background_color=BUTTON_COLOR, scaling="xw")
        button.box_base.changeSettings(background_color=BUTTON_COLOR)
        button.box_hover.changeSettings(background_color=BUTTON_HOVER)
        self.menu.add("Load Project Button", button)

        # Load Project Label
        text = UI.TextLine(buffersize, buffersize, self.menu, "Load", width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, background_color=(0, 0, 0, 0), text_color=TEXT_LIGHT, font_size=16,
                           scaling="xw", border=False, alignment="center center")

        self.menu.add("Load Project Label", text)

        offset = buffersize + self.pannelHeight * 2 - 2 * buffersize
        # SaveProject Button
        button = UI.Button(offset + buffersize, buffersize, self.menu, width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, functions_triggered=[self.saveProject], background_color=BUTTON_COLOR, scaling="xw")
        button.box_base.changeSettings(background_color=BUTTON_COLOR)
        button.box_hover.changeSettings(background_color=BUTTON_HOVER)
        self.menu.add("Save Project Button", button)

        # Save Project Label 
        text = UI.TextLine(offset + buffersize, buffersize, self.menu, "Save", width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, background_color=(0, 0, 0, 0), text_color=TEXT_LIGHT, font_size=16,
                           scaling="xw", border=False, alignment="center center")

        self.menu.add("Save Project Label", text)
        offset += buffersize + self.pannelHeight * 2 - 2 * buffersize

        # Last Conflict Button
        button = UI.Button(offset + buffersize, buffersize, self.menu, width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, functions_triggered=[self.lastConflict], background_color=BUTTON_COLOR, scaling="xw")
        button.box_base.changeSettings(background_color=BUTTON_COLOR)
        button.box_hover.changeSettings(background_color=BUTTON_HOVER)
        self.menu.add("Last Project Button", button)

        # Last Conflict Label 
        text = UI.TextLine(offset + buffersize, buffersize, self.menu, "Last", width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, background_color=(0, 0, 0, 0), text_color=TEXT_LIGHT, font_size=16,
                           scaling="xw", border=False, alignment="center center")

        self.menu.add("Last Conflict Label", text)
        offset += buffersize + self.pannelHeight * 2 - 2 * buffersize

        # NextConflict Button
        button = UI.Button(offset + buffersize, buffersize, self.menu, width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, functions_triggered=[self.nextConflict], background_color=BUTTON_COLOR, scaling="xw")
        button.box_base.changeSettings(background_color=BUTTON_COLOR)
        button.box_hover.changeSettings(background_color=BUTTON_HOVER)
        self.menu.add("Last Conflict Button", button)

        # Save Project Label 
        text = UI.TextLine(offset + buffersize, buffersize, self.menu, "Next", width=self.pannelHeight * 2 - 2 * buffersize,
                           height=self.pannelHeight - 2 * buffersize, background_color=(0, 0, 0, 0), text_color=TEXT_LIGHT, font_size=16,
                           scaling="xw", border=False, alignment="center center")

        self.menu.add("Next Conflict Label", text)
        offset += buffersize + self.pannelHeight * 2 - 2 * buffersize

    def loadProject(self, button):
        self.folder = self.fileGetter.getFolder()
        if self.folder == "":
            print("Projet Load Cancelled")
        elif not(self.folder is None):
            self.projectController.addProject(self.folder)
            print("Load Project", self.folder)

    def saveProject(self, button):
        if self.projectController.activeProject is None:
            self.dialogueBox.sendWarning("No Project Selected!")
        elif self.dialogueBox.askConfirmation("Save Project?", "Do you want to save?"):
            print("Save Project")
        else:
            # DO STUFF
            pass

    # Consider moving to ConflictDisplay or ProjectDisplay
    def nextConflict(self, button):
        print("Go to next conflict")

    def lastConflict(self, button):
        print("Go to last conflict")

    def undoButton(self, button):
        print("Undo")

    def redoButton(self, button):
        print("Redo")

    def update(self, mx, my, mb, keys):
        self.menu.update(mx, my, mb, keys)

    def draw(self, screen):
        self.menu.draw(screen)

    def resize(self, width, height):
        self.menu.resize(width, height)

# ##########################################################################################################################################
# ##########################################################################################################################################


class ConflictDisplay():
    def __init__(self, x, y, pannelWidth, pannelHeight, projectController):
        self.pannelWidth = pannelWidth
        self.pannelHeight = pannelHeight
        self.x = x
        self.y = y
        self.projectController = projectController
        self.createMenu()

    def createMenu(self):
        # LoadProject Button
        # Save Button
        # Undo Button
        # NextConflict
        self.menu = UI.Pannel(self.x, self.y, width=self.pannelWidth, height=self.pannelHeight)
        # Title
        '''text = UI.TextLine(0, 0, self.menu, "Conflict Display", width=PANNEL_WIDTH-1, height=28,
                           background_color=BACKGROUND_DARK_1, text_color=TEXT_LIGHT, alignment="top left", font_size=22)
        text.background.changeSettings(border=False)
        self.menu.add("Title", text)
        '''
        # Text Box
        textBox = UI.TextBox(0, 0, self.menu, lines=["dog€", "cat", "doggo", "/tbye", "jjjjjjjj", "\thello", "TTTTT", "/tbye", "jjjjjjjj", "\thello", "TTTTT", "/tbye", "jjjjjjjj","\thello", "TTTTT"] * 100, width=self.pannelWidth,
                             height=self.pannelHeight, number_color=TEXT_LIGHT, text_color=TEXT_LIGHT, background_color=BACKGROUND_DARK_2,
                             line_states=3, line_colors=[BACKGROUND_DARK_2, LINE_DELETE, LINE_KEEP])
        textBox.scrollBar.box_bar.changeSettings(background_color=BACKGROUND_DARK_1)
        textBox.scrollBar.box_scroll_bar.changeSettings(border_color=OUTLINE_DARK, background_color=BACKGROUND_DARK_3)
        self.menu.add("File View", textBox)

    def update(self, mx, my, mb, keys):
        self.menu.update(mx, my, mb, keys)

        if (self.projectController.changedConflict):
            self.menu.get("File View").setText(self.projectController.getFile(self.projectController.activeFile))

    def draw(self, screen):
        self.menu.draw(screen)

    def resize(self, width, height):
        self.menu.resize(width, height)

# ##########################################################################################################################################
# ##########################################################################################################################################


class ProjectDisplay():
    def __init__(self, x, y, pannelWidth, pannelHeight, projectController):
        self.pannelWidth = pannelWidth
        self.pannelHeight = pannelHeight
        self.x = x
        self.y = y
        self.projectController = projectController
        self.createMenu()

    def createMenu(self):
        # LoadProject Button
        # Save Button
        # Undo Button
        # NextConflict
        # the 20 is arbitrary atm should be changed so it can be easily configured
        self.menu = UI.Pannel(self.x, self.y, width=self.pannelWidth, height=self.pannelHeight)
        box = self.menu.box
        box.changeSettings(background_color=BACKGROUND_DARK_3, border_color=BACKGROUND_DARK_1, border=True)

        # TestLabel
        text = UI.TextLine(0, 0, self.menu, "Active Project", width=self.pannelWidth, height=28,
                           background_color=BACKGROUND_DARK_1, text_color=TEXT_LIGHT, alignment="top left", font_size=22,
                           border=True, scaling="xw")
        self.menu.add("Title", text)
        offset = 28

        # Current Project
        if not (self.projectController.activeProject is None):
            text = UI.TextLine(0, offset, self.menu, self.projectController.activeProject.name, width=self.pannelWidth, height=18,
                               background_color=BACKGROUND_DARK_1, text_color=TEXT_LIGHT, alignment="center left", font_size=14, scaling="w", border=True)
        else:
            text = UI.TextLine(0, offset, self.menu, "Load a Project", width=self.pannelWidth, height=18,
                               background_color=BACKGROUND_DARK_1, text_color=TEXT_LIGHT, alignment="center left", font_size=14, scaling="w", border=True)
        self.menu.add("Active Project", text)

    def update(self, mx, my, mb, keys):
        self.menu.update(mx, my, mb, keys)

        # Update Active Project Name
        if not (self.projectController.activeProject is None):
            self.menu.get("Active Project").setText(self.projectController.activeProject.name)
            self.menu.get("Active Project").setBold(True)

    def draw(self, screen):
        self.menu.draw(screen)

    def resize(self, width, height):
        self.menu.resize(width, height)
