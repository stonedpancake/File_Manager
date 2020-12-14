import os
import sys

from PySide6.QtUiTools import QUiLoader
import pygame
import PyQt5
from pygame import *
from PySide6.QtWidgets import (QPushButton, QApplication,
                               QFileDialog, QMainWindow)

not_available_files = []


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(50, 50, 200, 200)
        self.setWindowTitle('Awesome File Manager')
        QUiLoader.load(self, 'file_manager_design_1.ui')

        self.box_filters.setItemText(0, 'first filter')

        files = QFileDialog.getOpenFileNames(self)
        btn_file = QPushButton('Open', self)
        for file in files[0]:
            btn_file.clicked.connect(main(file))


def info(file, filename, status, delete_status, error_status):
    if not error_status:
        if not delete_status:
            print()
            print(f'File: {filename}')
            print(f"Path: {file}")
            print(f"Size: {image.load(file).get_size()[0]}, "
                  f"{image.load(file).get_size()[1]}")
            if status:
                print('Status: available')
            else:
                print('Status: not available')
                not_available_files.append(filename)
    if error_status:
        print(f'File: {filename}\nStatus: undefined')
        if delete_status:
            print(f'File: {filename}\nStatus: deleted')


def delete_not_available_files(directory, filenames_list):
    print("\nDelete not available files:?")
    for filename in filenames_list:
        print('\t' + filename)
    answer = input()
    if answer.lower() == 'yes':
        for filename in filenames_list:
            os.remove(directory + '/' + filename)


def test(file, filename):
    status = False
    error_status = False
    delete_status = False

    try:
        if image.load(file).get_size() >= (1920, 1080):
            status = True
    except pygame.error:
        error_status = True
        delete_file(file, filename, status, error_status)

    if not error_status:
        info(file, filename, status, delete_status, error_status)


def delete_file(directory, filename, status, error_status):
    if error_status:
        print(f"\nUndefined file: {filename}\nDelete file?")
        answer = input()
        delete = False
        if answer.lower() == 'yes':
            delete = True
        if delete:
            os.remove(directory + '/' + filename)
            return True
        else:
            info(directory, filename, status, delete, error_status)
            return False
    else:
        return False


def main(file):
    filename = file.split('/')[-1]
    print(filename)
    test(file, filename)
    delete_not_available_files(file, not_available_files)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Window()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
