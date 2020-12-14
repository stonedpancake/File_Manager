import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice


app = QApplication(sys.argv)
ui_file_name = "file_manager_design_1.ui"
ui_file = QFile(ui_file_name)
loader = QUiLoader()
window = loader.load(ui_file)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        print(window)

        window.btn_load.clicked.connect(self.check())
        window.btn_file.clicked.connect(self.check())

        window.box_filters.setItemText(0, 'box_filters works')

    def setup(self):
        pass

    def check(self):
        print('btn_load works')
        print('btn_file works')



if __name__ == "__main__":

    Window()

    window.show()

    sys.exit(app.exec_())