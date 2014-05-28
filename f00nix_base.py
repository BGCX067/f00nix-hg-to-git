#!/usr/bin/env python

import os
import sys
import wx
import wx.media


class MainWinFrame(wx.Frame):
    def __init__(self, parent, inpTitle, inpStyle, inpSize): # the inpSize should be a tuple
        super(MainWinFrame, self).__init__(parent, title = inpTitle, style = inpStyle, size = inpSize)
        self.disp_media_frame()   # main function to display the UI

    def disp_media_frame(self):
        # menuBar = wx.MenuBar()
        # fileMenu = wx.Menu()
        # helpMenu = wx.Menu()
        #
        # exitItem = fileMenu.Append(wx.ID_EXIT, "Quit f00nix", "Quit f00nix")
        # aboutItem = helpMenu.Append(wx.ID_ANY, "About f00nix authors", "f00nix author")
        #
        # menuBar.Append(fileMenu, "&File")
        # menuBar.Append(helpMenu, "&Help")
        #
        # self.Bind(wx.EVT_MENU, self.onExit, exitItem)
        # self.Bind(wx.EVT_MENU, self.onAbout, aboutItem)
        # self.SetMenuBar(menuBar)

        # after the work with the menuBar is over, time to check the buttons for the player
        # currently sticking to plain buttons
        # also have to remember to add publishing portion like rhythmbox client -- that should help in remotely controlling the player
        # just like we used to do in Windows platform

        # now the panel which will be used for almost everything
        self.panel = wx.Panel(self, -1)

        # create the player and other such controls
        self.player = wx.media.MediaCtrl(self.panel)

        # Buttons for the player
        self.load = wx.Button(self.panel, wx.ID_ANY, "Load the music file") # this will be moved away later - auto load will be added, load will be
        # added to the fileMenu
        self.load.Bind(wx.EVT_BUTTON, self.loadFile)
        self.play = wx.Button(self.panel, wx.ID_ANY, "Play")
        self.play.Bind(wx.EVT_BUTTON, self.onPlay)
        self.pause = wx.Button(self.panel, wx.ID_ANY, "Pause")
        self.pause.Bind(wx.EVT_BUTTON, self.onPause)
        self.stop = wx.Button(self.panel, wx.ID_ANY, "Stop")
        self.stop.Bind(wx.EVT_BUTTON, self.onStop)

        # the slider showing how much has been played
        self.slider = wx.Slider(self.panel, wx.ID_ANY, size = (300, -1))
        self.slider.Bind(wx.EVT_SLIDER, self.seekFile)

        # slider update :: wx.Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onTimer)
        self.timer.Start(100)

        # the labels that will be required
        self.totDuration = wx.StaticText(self.panel, wx.ID_ANY, "0 seconds") # remember to convert the seconds to minutes:seconds and then display the same
        self.playedDuration = wx.StaticText(self.panel, wx.ID_ANY, "0 seconds") # similar conversion to that of totDuration

        # remember to add the volume portion

        self.CreateStatusBar()
        self.SetStatusText("f00nix developer version - buggy")

        # the sizers
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        infoCtrlSizer = wx.BoxSizer(wx.HORIZONTAL)
        sliderSizer = wx.BoxSizer(wx.HORIZONTAL)
        totSizer = wx.BoxSizer(wx.HORIZONTAL)
        playedSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(self.load, 0, wx.CENTER, 5)
        btnSizer.Add(self.play, 1, wx.CENTER, 5)
        btnSizer.Add(self.pause, 2, wx.CENTER, 5)
        btnSizer.Add(self.stop, 3, wx.CENTER, 3)
        playedSizer.Add(self.playedDuration, 0, wx.CENTER, 5)
        sliderSizer.Add(self.slider, 0, wx.CENTER, 5)
        totSizer.Add(self.totDuration, 0, wx.CENTER, 5)
        infoCtrlSizer.Add(playedSizer, 0, wx.CENTER, 5)
        infoCtrlSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        infoCtrlSizer.Add(sliderSizer, 1, wx.CENTER, 5)
        infoCtrlSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        infoCtrlSizer.Add(totSizer, 2, wx.CENTER, 5)

        self.mainSizer.Add(infoCtrlSizer, 0, wx.ALL|wx.CENTER, 5)
        self.mainSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)
        self.panel.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.Show()

        # self.panel.SetInitialSize()
        # self.SetInitialSize()


    def onTimer(self, event):
        current = self.player.Tell()
        if int(current) / 100 < 0:
            pass
        else:
            self.playedDuration.SetLabel("%i seconds" % (int(current) / 100))
        self.slider.SetValue(current)

        self.panel.SetInitialSize()
        self.SetInitialSize()

    def loadFile(self, event):
        msg = wx.FileDialog(self, message = "Open desired media file", style = wx.OPEN, wildcard = "Media Files|*.wav;*.mp3;*.mp4") # current for only two formats
        if msg.ShowModal() == wx.ID_OK:
            self.path = msg.GetPath()

            if not self.player.Load(self.path):
                wx.MessageBox("Media file could not be loaded")
            else:
                self.player.Play()
        self.totDuration.SetLabel("%d seconds" % (self.player.Length() / 100))
        self.SetStatusText("Now Playing : %s" % (os.path.split(self.path)[1]))
        self.slider.SetRange(0, self.player.Length())

        self.panel.SetInitialSize()
        self.SetInitialSize()

    def onPlay(self, event):
        self.player.Play()
        self.slider.SetRange(0, self.player.Length())
        self.totDuration.SetLabel("%d seconds" % (self.player.Length() / 100))
        self.SetStatusText("Now Playing : %s" % (os.path.split(self.path)[1]))
        self.panel.SetInitialSize()
        self.SetInitialSize()   # might have to remove this line and the one above it

    def onPause(self, event):
        self.player.Pause()

    def onStop(self, event):
        self.player.Stop()
        self.slider.SetValue(0) # reset to the starting position
        self.SetStatusText("Last Played : %s" % (os.path.split(self.path)[1]))
        self.totDuration.SetLabel("0 seconds")

    def seekFile(self, event):
        self.player.Seek(self.slider.GetValue())

    def onExit(self, event):
        self.Close()
        sys.exit(0)

    def onAbout(self, event):
        wx.MessageBox("Author : war10ck", "f00nix Author info", wx.OK | wx.ICON_INFORMATION)