#!/usr/bin/env python
import os
import shutil

class mp3_converter():
    def __init__(self, path, ext, dirName):
        """Class that takes folder of one music files of one file type, creates
        a new directory, and converts them to mp3
        Input path, ext of """
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

# TODO: Create mp3 object
# conv = mp3_converter("/Users/justinwilliams/Music/Music/judas_knife/wetransfer-844020",
#             ".wav", "mp3")

# TODO: Apply lower_underscore method to mp3 object
# conv.lower_underscore()

# TODO: Apply mp3 method to convert mp3 object
# conv.mp3()

# TODO: 
# conv.make_dir()