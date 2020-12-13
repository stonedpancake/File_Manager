from PySide6.QtCore import Qt, QFile, QFileInfo, QSettings, QTextStream
from PySide6.QtGui import QIcon
from PySide6.Widgets import (QAction, QApplication, QFileDialog, QMainWindow,
                             QPlainTextEdit, QFileDialog, QMessageBox)

def __init__(self, parent=None):
    QMainWindow.__init__(self)            self.textEdit =  QPlainTextEdit()
    self.setCentralWidget(textEdit)

    self.createActions()
    self.createMenus()
    self.createToolBars()
    self.createStatusBar()

    self.readSettings()

    self.textEdit.document().contentsChanged.connect(self.documentWasModified)

    self.setCurrentFile("")
    self.setUnifiedTitleAndToolBarOnMac(True)