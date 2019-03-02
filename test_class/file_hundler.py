"""
This class handel only file. Reading, writing or something.
DON't let this have other funcitons.
"""
import os
import sys


# TODO think: How to intergrate 'Strategy Pattern' with this class?? Just adding in method?
# Or ... Attribution, Constructor maybe

class FileHandler:
    # TODO consider which is better ENUM for filetype or not
    filetypes = ['.txt', '.csv', '.pgm']

    def __init__(self):
        self = self

    def get_filetype(self, filepath):
        # TODO Jundge the filetype with regular match
        # Retrieve the extension index  like ".txt"

        filetype = ""
        # Check the argument filepath in filetypes list with for * in

        return filetype


    def read_file(self, fileptype):
        # Caution
        # Let the extended class do this method like "CsvFileHandler"
        return

    def write_file(self):
        # TODO decide the second argument...  path? str? other?
        return


class CsvFileHandler(FileHandler):
    def __init__(self):
        super().__init__()
