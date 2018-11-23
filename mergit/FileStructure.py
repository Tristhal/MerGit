'''
###############################################################################################

        File:       fileSystem.py
        Author:     Raman Seviaryn
        Purpose:    This is the file system module for the Git merger

###############################################################################################
'''

import os

class File:

    def __init__(self, filepath):
        self.filepath = filepath
        self.file_extentions = filepath.split(".")[-1]
        self.name = filepath.split("/")[-1]
        self.contents = ""
        self.contents_pulled = False

    def open(self, force=False):
        if not self.contents_pulled or force:
            with open(self.filepath, "r") as f:
                self.contents = f.read().strip()
        return self.contents

    def writeOut(self, message=False):
        with open(self.filepath, "w") as f:
            if message:
                f.write(message)
            else:
                f.write(self.contents)
        self.contents = ""
        self.contents_pulled = False

    def close(self):
        self.contents = ""
        self.contents_pulled = False

    def dprint(self):
        print("File: "+self.filepath)

class Folder:

    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1]
        self.contents = []
        self.populate()

    def populate(self):
        ldir = os.listdir(self.path)
        for i in ldir:
            if len(i.split(".")) > 1:
                self.contents.append(File(self.path+"/"+i))
            else:
                self.contents.append(Folder(self.path+"/"+i))

        #self.contents.sort()  // finish this in later implementation
        #done

    def dprint(self):
        print(" --- Folder --- ")
        print("Folder: "+self.path)
        for i in self.contents:
            i.dprint()
        print(" --- End Folder --- ")

    def getContents(self, whitelist=[], only_files=True):
        contents = []
        if not only_files:
            contents.append(self.path)
        for i in self.contents:
            if type(i) is File:
                if len(whitelist) == 0 or i.filepath.split(".")[-1] in whitelist:
                    contents.append(i.filepath)
            elif type(i) is Folder:
                contents += i.getContents(whitelist, only_files)
            else:
                print("Unknown object in file Structure")
        return contents

    def getFile(self, file_path):
        local_path = file_path[(len(self.path)+1):]
        next_jump = local_path.split("/")[0]
        for i in self.contents:
            if i.name == next_jump:
                if type(i) is Folder:
                    return i.getFile(file_path)
                elif type(i) is File:
                    return i
                else:
                    print("Unknown object in file Structure")
        return None

class FileStructure:

    def __init__(self, path):
        self.root = Folder(path)

    def dprint(self):
        self.root.dprint()

    def getStructureContents(self, whitelist=[], only_files=True):
        return self.root.getContents(whitelist, only_files)

    def getFile(self, filepath):
        return self.root.getFile(filepath)


'''
fs = FileStructure(os.getcwd())
for i in fs.getStructureContents(["txt"], True):
    print(i)

print("--------------------------------")

for i in fs.getStructureContents([], False):
    print(i)
'''
