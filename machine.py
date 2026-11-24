from mechParts import *

class machine():
  currentState = None
  puzzle = puzzle(isDummy = True) #dummy puzzle
  allStates = {}
  allTransitions = {}
  mechParameters = {}
  def addState(stateName, stateData):
    pass
  def moveTransition(oldOrigin, transIndex, origin = None, destination = None):
    print("Moving transition", oldOrigin, ":", transIndex)
    if type(destination) == "string":
      print(" Assigning DESTINATION", destination)
    elif type(origin) == "string":
      print("  Assigning ORIGN", origin)
      
  def setParamsFromState(self, stateName):
    pass
    
    
  def takeStep():
    pass
    # get current state
