import mergit.main as main
import sys as sys
import os
#os.environ["PYGAME_FREETYPE"] = ""
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    application = main.Application()
    application.run()

    quit()