import numpy as np
from uteis import get_int_list, get_string

##### Heuristicas  ###########################################################################

def wrong_pieces(puzzle):
  goal="123456780"
  return 9 - np.sum(np.array(get_int_list(puzzle)) == np.array(get_int_list(goal)))

def distance_manhattan_sum(puzzle):
    np_array = np.array(get_int_list(puzzle))
    matrix = np_array.reshape((3,3))
    
    goal = {1:[0,0], 2:[0,1], 3:[0,2], 
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 0:[2,2]}
            
    n, m = matrix.shape
    
    sum = 0
    for i in range(n):
        for j in range(m):
            num = matrix[i,j]
            sum += abs(i - goal[num][0]) + abs(j - goal[num][1]) # manhattan distance
            #distance = abs(x2 - x1) + abs(y2 - y1)
    
    return sum

##############################################################################################