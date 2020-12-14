import sys
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QPushButton
from PySide6.QtGui import QCloseEvent

run_ = True


def run():
    app = QApplication(sys.argv)
    ex = Example()
    app.exec_()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):
        btn_quit = QPushButton('Quit', self)
        btn_quit.clicked.connect(QApplication.instance().quit)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.move(100, 100)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('PySide6 Example')

        self.show()

    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to quit?',
                                     QMessageBox.No | QMessageBox.No)

        if reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    run()
