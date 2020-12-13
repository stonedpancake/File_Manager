from PySide6.QtCore import Qt, QFile, QFileInfo, QSettings, QTextStream
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidgetAction, QApplication, QFileDialog, QMainWindow, \
    QPlainTextEdit, QFileDialog, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textEdit = QPlainTextEdit()
        self.curFile = ""
        # ...

    def loadFile(self, fileName):
        pass

    def closeEvent(self, event):
        pass

    def newFile(self):
        pass

    def open(self):
        pass

    def save(self):
        pass

    def saveAs(self):
        pass

    def about(self):
        pass

    def documentWasModified(self):
        pass
    # Enable this only if QT_NO_SESSIONMANAGER is not defined
    # def commitData(self):
    #   pass

    def createActions(self):
        pass

    def createStatusBar(self):
        pass

    def readSettings(self):
        pass

    def writeSettings(self):
        pass

    def maybeSave(self):
        pass

    def saveFile(self, fileName):
        pass

    def setCurrentFile(self, fileName):
        pass

    def strippedName(self, fullFileName):
        pass