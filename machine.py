from mechParts import *

class machine():
  currentState = None
  puzzle = puzzle("dummy") #dummy puzzle
  allStates = {}
  allTransitions = {}
  mechParameters = {}
  def addState(stateName, stateData):
    pass
  def moveTransition(oldOrigin, transIndex, origin = None, destination = None):
    print("Moving transition", oldOrigin, ":", transIndex)
    if type(destination) == "string":
      print(" Assigning DESTINATION", destination)
    elif type(origin) == "string"):
      print("  Assigning ORIGN", origin)

  def 

  def setParamsFromState(self, stateName):
    
    
    
  def takeStep():
    # get current state
