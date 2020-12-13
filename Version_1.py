import os

import pygame
from pygame import *

not_available_files = []


def info(directory, filename, status, delete_status, error_status):
    if not error_status:
        if not delete_status:
            print()
            print(f'File: {filename}')
            print(f"Path: {directory + '/' + filename}")
            print(f"Size: {image.load(directory + '/' + filename).get_size()[0]}, "
                  f"{image.load(directory + '/' + filename).get_size()[1]}")
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


def test(directory, filename):
    status = False
    error_status = False
    delete_status = False

    try:
        if image.load(directory + '/' + filename).get_size() >= (1920, 1080):
            status = True
    except pygame.error:
        error_status = True
        delete_file(directory, filename, status, error_status)

    if not error_status:
        info(directory, filename, status, delete_status, error_status)


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


def main(directory):
    for filename in os.listdir(directory):
        test(directory, filename)
    delete_not_available_files(directory, not_available_files)


if __name__ == '__main__':
    directory = 'C:/Programming/Projects/Python/Sweet House/SWEET HOUSE/Materials/Bg Pictures/Scary Room'
    main(directory)
