import tkinter as tk
#from util import *

class board():
  root = None
  #superframe = tk.LabelFrame()
  #canvas = tk.Canvas()
  def __init__(self, root):
    self.root = root
    self.superframe = tk.LabelFrame(root, text = "Board")
    self.canvas = tk.Canvas(self.superframe)
    self.canvas.pack()
    print("Board object initialised!")
  def clear(self):
    pass


class timeline():
  root = None
  #superframe = tk.LabelFrame()
  #scrollbar = None
  def __init__(self, root):
    self.root = root
    superframe = tk.LabelFrame(root, text = "Timeline")
    self.superframe = superframe
    self.controls = tk.Frame(superframe)
    self.bars = tk.Frame(superframe)
    self.visualFrame = tk.LabelFrame(superframe, text = "Visualiser")
    self.visual = tk.Canvas(self.visualFrame)
    self.visual.pack(fill = "both", pady = 3)
    self.controls.grid(row = 0, column = 0, sticky = "w")
    self.bars.grid(row = 0, column = 1)
    self.visualFrame.grid(row = 0, column = 2, sticky = "e")
    superframe.columnconfigure(0, weight=1, minsize=150)
    superframe.columnconfigure(1, weight=99, minsize=150)
    superframe.columnconfigure(2, weight=1, minsize=150)
    superframe.rowconfigure(0, weight=1, minsize=60)
    #self.scrollbar = tk.Scrollbar(self.superframe)
    #self.scrollbar.pack()
    print("Timeline object initialised!")
  ## populate timeline based on lists o inputs and outputs
  def populate(self, range, inbox, outbox, pins = list()):
    pass
  def clear(self):
    pass

class adjuster():
  root = None
  #superframe = rk.LabelFrame()
  def __init__(self, root):
    self.root = root
    self.superframe = tk.LabelFrame(root, text="Configure")
    self.topicFrame = tk.LabelFrame(self.superframe, text="Selection")
    self.topicFrame.grid(row = 0, column = 0)
    self.topic = tk.Canvas(self.topicFrame)
    self.topic.pack(fill = "x", pady = 3)
    self.modeLabel = tk.Label(self.superframe, text="Click a state or transition to edit!")
    self.modeLabel.grid(row = 1, column = 0)
    self.superframe.rowconfigure(0, weight=2, minsize=50)
    self.superframe.rowconfigure(1, weight=1, minsize=15)
    print("Adjuster object initialised!")
