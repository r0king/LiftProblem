# from typing import List

class Lift:
  def __init__(self,M):
    self.current_floor = -1 
    self.starting_floor = 0
    self.destination_floor = 0
    self.state = "CLOSE"
    self.T = -1
    self.end_time = 0
    self.direction = "NONE" # ["UP","DOWN","NONE"]
    self.pending = []
  
  
  def print(self):
    print(f'-->  {self.current_floor}  ({self.state})\tT: {self.T+1} ')
    
  def add_destination(self, start,end):
    
    # start is where i am rn and end is where i vanna go
    # current floor is where the lift is rn 
    diff = end - start    
    # if +ive => I needs to go up
    # else I needs to go down
    # if the lift is going up and I needs to go up and lift is currently below me
    if (diff > 0) and (self.direction == "UP") and (start > self.current_floor):
      # new i am between the other guys starting_floor and destination 
      # if he needs to go from 2->7 starting_floor,destination_floor
      # i needs to go from 3-5 start,end
      # lift is currently at the starting_floor ie 2
      # lift has to go to shortest floor between me ,destination_floor or my end to next shortest
      targets = [start,self.destination_floor,end]
      targets.sort()
      # add 2 new routs to pending which the lift has to go
      self.pending.append((targets[1],targets[2]))
      self.pending.append((targets[0],targets[1]))

    elif (diff <0 ) and (self.direction == "DOWN") and (start < self.current_floor):      
      targets = [start,self.destination_floor,end]
      targets.sort()
      self.pending.append((targets[1],targets[0]))
      self.pending.append((targets[2],targets[1]))

    # set the starting floor and ending floor 
    self.starting_floor = start
    self.destination_floor = end
    
  def set_direction(self):  
    # set the direction of lift as if its goin up down or not
    if self.current_floor != self.starting_floor:
      if self.current_floor > self.starting_floor:
        self.direction = "DOWN"
      else :
        self.direction =  "UP"
    else:
      self.direction = "NONE"
    
  def move(self):      
    
    #close door if open
    if self.state == "OPEN":
      self.state = "CLOSE"
      self.T +=1
      # set the time in which the lift is idle
      self.end_time = self.T
      self.print()
      # if there is pending routes the lift has to go to
      if self.pending:
        (start,end) = self.pending.pop(-1)
        # create a new path for the lift
        self.add_destination(start,end)
      #set new starting_floor as destination floor
      if self.current_floor != self.destination_floor:
        self.starting_floor = self.destination_floor
      return 

    #decide to move lift up or down
    self.set_direction()
    #move the lift up or down
    if self.direction == "DOWN":
      self.current_floor += -1  
      #open door if starting_floor is reached
      if self.current_floor == self.starting_floor:
        self.state = "OPEN"
      self.T +=1
    elif self.direction ==  "UP":
      self.current_floor += 1
      self.T +=1      
      #open door if starting_floor is reached
      if self.current_floor == self.starting_floor:
        self.state = "OPEN"
    self.print()
    
    
def init(M):  
  lift =  Lift(M)
  return lift