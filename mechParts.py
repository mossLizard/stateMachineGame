import tkinter as tk
#from util import *


class solution():
  name = ""
  puzzlePath = ""
  solutionSubPath = ""
  def __init__(self, path = "", subPath = ""):
    pass

class puzzle():
  name = ""
  path = ""
  def __init__(self, path = "", isDummy = False, isResponsive = False):
    self.isDummy = isDummy
    if isDummy:
      self.name = "dummy"
      self.path = None
      self.isResponsive = isResponsive
  def genTestCase(self, index, ofset, delay):
    return {"NYI"}

class mechTrans():
  origin = "" # state name
  destination = ""
  trigger = ""
  output = ""
  isVital = False
  isLocked = False
  conditionType = "None"
  conditionVar = "A"

class mechState():
  name = "STATE"
  symbol = "salt"
  isVital = False # cannot be removed, can be edited.
  isLocked = False
  isAccepting = False
  paraSet = {}
  def __init__(self, name):
    print("Creating new machine state", name)
    self.name = name
    isEssential = False
    isLocked = False
    paraSet = {}
  def addParameterOverride(self, paraname, value):
    paraSet[paraname] = value
  def removeParameterOverride(Self, paraname):
    paraSet.pop(paraname)
