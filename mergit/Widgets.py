from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

'''
1. DisplayMessage
2. GetFile
'''

# ##########################################################################################################################################
# ##########################################################################################################################################


class DisplayMessage(QWidget):

    def __init__(self):
        super().__init__()

    def sendWarning(self, message):
        QMessageBox.warning(self, 'Warning', message, QMessageBox.Ok)

    def askConfirmation(self, title, message):
        buttonReply = QMessageBox.question(self, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        else:
            return False

# ##########################################################################################################################################
# ##########################################################################################################################################


class GetFile(QWidget):
    def __init__(self):
        super(GetFile, self).__init__()
        
    def getFile(self):
        name = QFileDialog.getOpenFileName(self, 'Open File')
        return name

    def getFolder(self):
        name = QFileDialog.getExistingDirectory(self, "Open Project")
        return name
