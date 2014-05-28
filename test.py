#!/usr/bin/env python

import wx
import wx.media
import f00nix_base

# Author : war10ck
# Platform : Linux
# Copyright : None, use as much as you want - inspired from foobar in windows platform


def main():
    print('Working')
    appInst = wx.App(redirect=False)
    f00nix_base.MainWinFrame(None, inpTitle="f00nix Dev Version - Buggy", inpStyle=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, inpSize = (800, 800))
    appInst.MainLoop()

if __name__ == '__main__':
    main()