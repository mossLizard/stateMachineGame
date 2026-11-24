#PLEASE

import tkinter as tk
import tkinter.ttk as ttk
from util import * # reusing a vec2 thing I made for a previous project

from mechParts import *
from uiParts import *


if __name__ == "__main__"  :
  root = tk.Tk()
  root.configure()
  root.geometry('720x540')
  root.minsize(600,400)
  root.title("PLEease")
  monospaceFont = ("Courier", 10, "normal")

  o_machine = None
  o_board = board(root)
  o_timeline = timeline(root)
  o_adjust = adjuster(root)
  o_board.superframe.grid(row = 0, column = 0)
  o_adjust.superframe.grid(row = 0, column = 1)
  o_timeline.superframe.grid(row = 1, column = 0, columnspan = 2)
  root.columnconfigure(0, weight=1)
  root.columnconfigure(1, weight=10)
  root.rowconfigure(0, weight=1)
  root.rowconfigure(1, weight=10)
    
  print("READY")
  # MAIN
  root.mainloop()
