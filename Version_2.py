from PySide6.QtCore import Qt, QFile, QFileInfo, QSettings, QTextStream
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QWidgetAction, QApplication, QFileDialog, QMainWindow,
                               QPlainTextEdit, QFileDialog, QMessageBox)


def __init__(self, parent=None):
    QMainWindow.__init__(self)
    self.textEdit = QPlainTextEdit()
    self.setCentralWidget(self.textEdit)

    self.createActions()
    self.createMenus()
    self.createToolBars()
    self.createStatusBar()

    self.readSettings()

    self.textEdit.document().contentsChanged.connect(self.documentWasModified)

    self.setCurrentFile("")
    self.setUnifiedTitleAndToolBarOnMac(True)
