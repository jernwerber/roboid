# on initialize, look for a usb device that has a folder called sounds
# or we can give it a path... for the rpi it'll probably be /dev/sda or something like that

# specify valid file formats, based on file extensions (easiest way?)
playable_formats = ['mp3','ogg','wav']

import os


with os.scandir("C:\Temp") as dirs:
    for d in dirs:
        print(d.name[-3:])
