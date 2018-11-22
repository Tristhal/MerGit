from PyQt5 import QtWidgets


class GetFile(QtWidgets.QWidget):
    def __init__(self):
        super(GetFile, self).__init__()
        
    def getFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        try:
            return name
        except:
            return None

    def getFolder(self):
        name = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Project")
        print(name)
        try:
            return name
        except:
            return None
