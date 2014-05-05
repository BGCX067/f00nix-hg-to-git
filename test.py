#!/usr/bin/env python

import os
import sys
import fnmatch
from pyglet.gl import *
import pyglet
from pyglet.window import key

def main():
    musExists = False
    if os.path.exists(os.environ['HOME'] + '/Music') and os.path.isdir(os.environ['HOME'] + '/Music'):
        print("Is a directory") # read all the music files from this directory
        musExists = True
    else:
        print('Music directory not found')
        sys.exit(1)

    musList = []
    for root, dirnames, filenames in os.walk(os.environ['HOME'] + '/Music'):
        for fname in fnmatch.filter(filenames, '*.mp3'):
            musList.append(os.path.join(root, fname))

    for index in range(0, len(musList)):
        print musList[index]

    # TODO: Create the function to read the music library

class playerWindow(pyglet.window.Window):
    GUI_WIDTH = 400
    GUI_HEIGHT = 300
    GUI_PADDING = 4
    GUI_BUTTON_HEIGHT = 16

    def __init__(self, player):
        super(playerWindow, self).__init__(caption='f00nix v0 Dev', visible = False, resizable = False)

        self.player = player
        self.player.push_handlers(self)
        self.player.eos_action = self.player.EOS_PAUSE

        self.playPauseBtn = TextButton(self)
        self.playPauseBtn.x = self.GUI_PADDING
        self.playPauseBtn.y = self.GUI_PADDING
        self.playPauseBtn.height = self.GUI_BUTTON_HEIGHT
        self.playPauseBtn.width = 45
        self.playPauseBtn.on_press = self.on_playPause

        win = self

if __name__ == '__main__':
    main()