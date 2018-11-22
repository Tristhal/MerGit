from collections import OrderedDict
import os
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
        self.activeProject = None
        self.numProjects = 0
        self.warningHandler = warning_handler

    def addProject(self, filepath):
        '''
        Returns project ID str
        '''
        if not self.isGitRepo(filepath):
            self.warningHandler("Not Git Repository")
        self.activeProject = Project(filepath.split("/")[-1], filepath)
        self.numProjects += 1
        return filepath

    def isGitRepo(self, file_path):
        for name in os.listdir(file_path):
            if os.path.isdir(name) and name == ".git":
                return True
        return False

    def getProject(self, id):
        return self.projects[id]


class Project():

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.conflicts = None
        self.activeConflict = None

# ##########################################################################################################################################
# ##########################################################################################################################################


class ConflictManager():

    def find_conflicts(file_string):
        conflicts = []
        lines = file_string.split("\n")
        line_index = 0
        while (line_index < len(lines)):
            if "<<<<" in lines[line_index]:
                conflict = Conflict()
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

    def __init__(self):
        self.lines = []
        self.start_index = None
        self.end_index = None
        self.file_name = None
        self.resolved = False
