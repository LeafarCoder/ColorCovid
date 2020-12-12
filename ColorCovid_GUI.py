#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
import tkinter as tk
import tkinter.ttk as ttk
import ColorCovid_support
import Toplevel1 as tl

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, vc
    root = tk.Tk()
    root.state('zoomed')
    root.iconbitmap('resources/virus.ico')
    top = tl.Toplevel1 (root)
    ColorCovid_support.init(root, top)
    root.mainloop()


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

if __name__ == '__main__':
    vp_start_gui()

