from collections import OrderedDict
import os
import mergit.FileStructure as fs
'''
1. ProjectController
2. Project
3. ConflictManager
4. Conflict
'''
# ##########################################################################################################################################
# ##########################################################################################################################################


class ProjectController():

    def __init__(self, warning_handler):
        self.projects = OrderedDict()
        self.conflictManager = ConflictManager()
        self.activeProject = None
        self.numProjects = 0
        self.warningHandler = warning_handler
        self.activeFile = None
        self.activeConflict = None

        # Flags
        self.changedConflict = False

    def addProject(self, filepath):
        '''
        Returns number of files
        '''
        if not self.isGitRepo(filepath):
            self.warningHandler("Not Git Repository")
        # Reset variables
        self.activeFile = None
        self.activeConflict = None

        self.activeProject = Project(filepath.split("/")[-1], filepath)

        for path in self.activeProject.filePaths:
            file = self.activeProject.fs.getFile(path)
            file = file.open()  # Get lines
            file = file.split("\n")
            # Add file and associated conflicts to the project
            self.activeProject.conflicts.append(self.conflictManager.find_conflicts(file, path.split("/")[-1]))
            self.activeProject.files.append(file)

        if len(self.activeProject.filePaths) > 0:
            self.activeFile = 0
            self.changedConflict = True
            if len(self.activeProject.conflicts[0]) > 0:
                self.activeConflict = 0
            else:
                self.activeConflict = None

        self.numProjects += 1
        return len(self.activeProject.filePaths)

    def nextConflict(self):
        self.changedConflict = True
        numConflicts = len(self.getConflicts())
        if self.activeConflict is None or numConflicts == 0 or self.activeConflict >= numConflicts:
            self.nextFile()
        else:
            self.activeConflict = (self.activeConflict + 1)
            if self.activeConflict >= len(self.activeProject.conflicts[self.activeFile]):
                self.nextFile()
            
    def nextFile(self):
        print("Debug: Going to next file")
        self.activeConflict = None
        if len(self.activeProject.files) == 0:
            print("Debug: No Files in Project")
            self.activeFile = None
        else:
            # Cycle to next file
            self.activeFile = (self.activeFile + 1) % len(self.activeProject.filePaths)
            # Select the first conflict if available
            if len(self.activeProject.conflicts[self.activeFile]) > 0:
                self.activeConflict = 0
            else:
                self.activeConflict = None

    def getConflicts(self):
        return self.activeProject.conflicts[self.activeFile]

    def getConflict(self):
        if self.activeConflict is None:
            print("Error: No active conflict")
        else:
            return self.getConflict[self.activeFile][self.activeConflict]

    def getFile(self):
        return self.activeProject.files[self.activeFile]

    def getActiveFilename(self, id):
        return self.activeProject.filePaths[id]

    def isGitRepo(self, file_path):
        for name in os.listdir(file_path):
            if os.path.isdir(name) and name == ".git":
                return True
        return False

    def getProject(self, id):
        return self.projects[id]

    def update(self):
        self.changedConflict = False


class Project():

    def __init__(self, name, path):
        self.fs = fs.FileStructure(path)

        # Data
        self.filePaths = self.fs.getStructureContents(["txt", "py"], True)
        self.files = []
        self.lineStates = []
        self.conflicts = []

        # Identifiers
        self.name = name
        self.path = path

        # Status
        self.activeConflict = None

# ##########################################################################################################################################
# ##########################################################################################################################################


class ConflictManager():
    
    def __init__(self):
        pass

    def find_conflicts(self, lines, filename):
        conflicts = []
        # lines = file_string.split("\n")
        line_index = 0
        while (line_index < len(lines)):
            if "<<<<" in lines[line_index]:
                conflict = Conflict(filename)
                conflict.start_index = line_index + 1
                while(line_index < len(lines)):
                    if ">>>>" in lines[line_index]:
                        conflict.end_index = line_index + 1
                        conflict.lines = lines[conflict.start_index - 1:conflict.end_index]
                        conflicts.append(conflict)
                        break
                    line_index += 1
            line_index += 1
        return conflicts


class Conflict():

    def __init__(self, filename):
        self.lines = []
        self.start_index = None
        self.end_index = None
        self.file_name = filename
        self.resolved = False
