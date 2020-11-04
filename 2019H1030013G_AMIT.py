#!/usr/bin/env python3
import time
import numpy
import heapq
from queue import Queue

class board:
  def __init__(self,puzzle,parent,pos,level,cost):
    self.puzzle = puzzle
    self.parent = parent
    self.children = []  
    self.pos = pos
    self.level = level
    self.cost = cost
   
   
  def move_up(self,goal):
    pos = 0

    for i in range(len(self.puzzle)):
      if self.puzzle[i] == 0:
        pos = i
        break
    parent_puzzle = list(self.puzzle)

    if (pos != 0 and pos != 1 and pos != 2 and pos != 3):
      temp = parent_puzzle[pos]
      parent_puzzle[pos] = parent_puzzle[pos-4]
      parent_puzzle[pos-4] = temp
      pos = pos - 4
      cost = find_cost(parent_puzzle,goal,self.level+1)
      child = board(parent_puzzle,self,pos,self.level+1,cost)
      self.children.append(child)

  def move_down(self,goal):
    pos = 0
    
    for i in range(len(self.puzzle)):
      if self.puzzle[i] == 0:
        pos = i
        break
    parent_puzzle = list(self.puzzle)

    if (pos != 12 and pos != 13 and pos != 14 and pos != 15):
      temp = parent_puzzle[pos]
      parent_puzzle[pos] = parent_puzzle[pos+4]
      parent_puzzle[pos+4] = temp
      pos = pos + 4
      cost = find_cost(parent_puzzle,goal,self.level+1)
      child = board(parent_puzzle,self,pos,self.level+1,cost)
      self.children.append(child)
     
    
    # for e in self.children:
    #   print(e)
  
  

  def move_left(self,goal):
     pos = 0
    
     for i in range(len(self.puzzle)):
       if self.puzzle[i] == 0:
         pos = i
         break
     parent_puzzle = list(self.puzzle)
     
     if (pos != 0 and pos != 4 and pos != 8 and pos != 12):
       temp = parent_puzzle[pos]
       parent_puzzle[pos] = parent_puzzle[pos-1]
       parent_puzzle[pos-1] = temp
       pos = pos - 1
       cost = find_cost(parent_puzzle,goal,self.level+1)
       child = board(parent_puzzle,self,pos,self.level+1,cost)
       self.children.append(child)

  def move_right(self,goal):
    pos = 0
    
    for i in range(len(self.puzzle)):
      if self.puzzle[i] == 0:
        pos = i
        break
    parent_puzzle = list(self.puzzle)

    if (pos != 3 and pos != 7 and pos != 11 and pos != 15):
      temp = parent_puzzle[pos]
      parent_puzzle[pos] = parent_puzzle[pos+1]
      parent_puzzle[pos+1] = temp
      pos = pos + 1
      cost = find_cost(parent_puzzle,goal,self.level+1)
      child = board(parent_puzzle,self,pos,self.level+1,cost) #parent storing here
      self.children.append(child)

  def __lt__(self, other):
        return self.cost < other.cost

def find_cost(child_board,goal,child_level):
    x = sum(abs(board_pos%4 - goal_pos%4) + abs(board_pos//4 - goal_pos//4)
        for board_pos, goal_pos in ((child_board.index(i), goal.index(i)) for i in range(1, 16)))
    return x + child_level
  


def FindMinimumPath(initialState,goalState):
  
  minPath = []
  nodesGenerated = 0
  initial = list(numpy.concatenate(initialState).flat)
  goal = list(numpy.concatenate(goalState).flat)
  for i in range(len(initial)):
        if initial[i] == 'A':
            initial[i] = 10
        if initial[i] == 'B':
            initial[i] = 11
        if initial[i] == 'C':
            initial[i] = 12
        if initial[i] == 'D':
            initial[i] = 13
        if initial[i] == 'E':
            initial[i] = 14
        if initial[i] == 'F':
            initial[i] = 15
        if initial[i] == '0':
            initial[i] = 0
        if initial[i] == '1':
            initial[i] = 1
        if initial[i] == '2':
            initial[i] = 2
        if initial[i] == '3':
            initial[i] = 3
        if initial[i] == '4':
            initial[i] = 4
        if initial[i] == '5':
            initial[i] = 5
        if initial[i] == '6':
            initial[i] = 6
        if initial[i] == '7':
            initial[i] = 7
        if initial[i] == '8':
            initial[i] = 8
        if initial[i] == '9':
            initial[i] = 9 
  for i in range(len(initial)):
        if goal[i] == 'A':
            goal[i] = 10
        if goal[i] == 'B':
            goal[i] = 11
        if goal[i] == 'C':
            goal[i] = 12
        if goal[i] == 'D':
            goal[i] = 13
        if goal[i] == 'E':
            goal[i] = 14
        if goal[i] == 'F':
            goal[i] = 15
        if goal[i] == '0':
            goal[i] = 0
        if goal[i] == '1':
            goal[i] = 1
        if goal[i] == '2':
            goal[i] = 2
        if goal[i] == '3':
            goal[i] = 3
        if goal[i] == '4':
            goal[i] = 4
        if goal[i] == '5':
            goal[i] = 5
        if goal[i] == '6':
            goal[i] = 6
        if goal[i] == '7':
            goal[i] = 7
        if goal[i] == '8':
            goal[i] = 8
        if goal[i] == '9':
            goal[i] = 9
  cost = find_cost(initial,goal,0)
  pos = 0
  for i in range(len(initial)):
    if initial[i] == 0:
      pos = i
      break
# dist = 0
    
# print(dist)
  heap_list = []
  start_board = board(initial,None,pos,0,cost)
  visited = set()

  heapq.heappush(heap_list,(cost,start_board))


  while len(heap_list) != 0:
    obj = heapq.heappop(heap_list)
    temp = obj[1]

    if (temp.puzzle == goal):
    #    print("found")
       tracer = temp
       break
  
    temp.move_up(goal)
    temp.move_down(goal)
    temp.move_right(goal)
    temp.move_left(goal)

    for child  in temp.children:
       if (tuple(child.puzzle) not in visited ):
           visited.add(tuple(child.puzzle))
           heapq.heappush(heap_list,(child.cost,child))

  
  ans_parent = []
  positions = []
  minPath = []

  while tracer.parent != None:
      ans_parent.append(tracer.puzzle)
      positions.append(tracer.pos)
      tracer = tracer.parent

  positions.append(start_board.pos)
  ans_parent.append(start_board.puzzle)
  ans_parent.reverse()
  positions.reverse()


  for i in range (len(positions)-1):
    diff = positions[i] - positions[i+1]
    if (diff == -1):
      minPath.append("right")
    elif (diff == 1):
      minPath.append("left")
    elif (diff == 4):
      minPath.append("up")
    else:
      minPath.append("down")
  nodesGenerated = len(visited)

  return minPath, nodesGenerated

#**************   DO NOT CHANGE ANY CODE BELOW THIS LINE *****************************


def ReadInitialState():
    with open("initial_state1.txt", "r") as file: #IMP: If you change the file name, then there will be an error when
                                                        # evaluators test your program. You will lose 2 marks.
        initialState = [[x for x in line.split()] for i,line in enumerate(file) if i<4]
    return initialState

def ShowState(state,heading=''):
    print(heading)
    for row in state:
        print(*row, sep = " ")

def main():
    initialState = ReadInitialState()
    ShowState(initialState,'Initial state:')
    goalState = [['0','1','2','3'],['4','5','6','7'],['8','9','A','B'],['C','D','E','F']]
    ShowState(goalState,'Goal state:')
    
    start = time.time()

    minimumPath, nodesGenerated = FindMinimumPath(initialState,goalState)
    timeTaken = time.time() - start
    
    if len(minimumPath)==0:
        minimumPath = ['Up','Right','Down','Down','Left']
        print('Example output:')
    else:
        print('Output:')

    print('   Minimum path cost : {0}'.format(len(minimumPath)))
    print('   Actions in minimum path : {0}'.format(minimumPath))
    print('   Nodes generated : {0}'.format(nodesGenerated))
    print('   Time taken : {0} s'.format(round(timeTaken,4)))

if __name__=='__main__':
    main()
