#!/usr/bin/env python
import os
import shutil

class mp3_converter():
    def __init__(self, path, ext, dirName):
        """Class that takes folder of music files of one file type, 
        converts them to mp3 and creates a new directory and moves them into it
        Input path of files that you would like to convert
        Extension of files you would like to convert i.e. WAV
        Folder name of the new directory you would like to create"""
        self.path = path
        self.ext = ext
        self.dirName = dirName

    def lower_underscore(self):
        """
        Converts all files in path to lowercase
        Replaces all spaces in filename with _
        """
        directory = self.path
        [os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').lower()) for f in os.listdir(directory)]

    def mp3(self):
        """
        Converts all files in path with entered extension to mp3
        """
        directory = self.path

        for f in os.listdir(directory):
            if (f.endswith(self.ext)):
                os.system("ffmpeg -i {} -ar 44100 -ac 2 -b:a 192k {}/{}.mp3".format(
                    os.path.join(directory, f), directory, os.path.splitext(f)[0]))

    def make_dir(self):
        """
        Creates a directory for mp3's and moves all 
        previously created mp3's into it
        """
        mp3_directory = self.path + "/" + self.dirName
        if not os.path.exists(mp3_directory):
            os.makedirs(mp3_directory)
        for filename in os.listdir(self.path):
            if (filename.endswith(".mp3")):
                source = os.path.join(self.path, filename)
                shutil.move(source, mp3_directory)
