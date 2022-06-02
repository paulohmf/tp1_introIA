from uteis import get_int_list, get_string, print_path, get_adjacency_list, get_weighted_adjacency_list
from heuristicas import wrong_pieces, distance_manhattan_sum

##### Algoritmos  ###########################################################################################################

####### BFS  
def BFS(start, print_console, goal="123456780"):

    visited = []
    #depth_visited = []
    father_visited = []

    queue = []
    queue.append((start, 0, -1)) # node, depth and parent's position

    while len(queue) > 0:
        node = queue.pop(0)

        visited.append(node[0])
        #depth_visited.append(node[1])
        father_visited.append(node[2])

        if node[0] == goal:
            print(node[1]) # print depth
            print(len(visited)) # for log
            if print_console:
                print_path(visited, father_visited)
            return

        for neighbor in get_adjacency_list(node[0]):
            if neighbor not in visited and neighbor not in [n[0] for n in queue]:
                queue.append((neighbor, node[1]+1, visited.index(node[0]))) 
                # add neighbor, depth and parent's position
 
    print("Essa instância não possui solução.")
    print(len(visited)) # for log
    return

#######
####### Iterative DFS  
def limited_DFS(limit, start, print_console, goal="123456780"):
    
    visited = []
    #depth_visited = []
    father_visited = []

    stack = []
    stack.append((start, 0, -1))  # node, depth and parent's position

    while len(stack) > 0:
        node = stack.pop()

        visited.append(node[0])
        #depth_visited.append(node[1])
        father_visited.append(node[2])

        if node[0] == goal:
            print(node[1]) # print depth
            if print_console:
                print_path(visited, father_visited)
                #return True
            return True, len(visited) # for log

        if node[1] < limit:
            for neighbor in get_adjacency_list(node[0]):
                if neighbor not in visited and neighbor not in [n[0] for n in stack]:
                    stack.append((neighbor, node[1]+1, visited.index(node[0])))
                    # add neighbor, depth and parent's position

    #return False
    return False, len(visited) # for log

def iterative_DFS(start, print_console, goal="123456780"):
    steps = 0

    stop = False
    limit = 0
    while(not stop): 
        #stop = limited_DFS(limit, start, print_console, goal)
        stop, step = limited_DFS(limit, start, print_console, goal) # for log
        steps += step # for log
        limit+=1
        if limit >= 36:
            print("Essa instância não possui solução.")
            break
    print(steps) #for log
#######
####### Dijkstra     

def Dijkstra(start, print_console, goal="123456780"):

    visited = []
    #depth_visited = []
    father_visited = []

    frontier = []
    frontier.append((start, 0, -1, 1))  # node, depth, parent's position and cost

    while len(frontier) > 0:
        frontier = sorted(frontier, key=lambda x: x[3]) #sort by cost
        node = frontier.pop(0)

        visited.append(node[0])
        #depth_visited.append(node[1])
        father_visited.append(node[2])

        if node[0] == goal:
            print(node[1]) # print depth
            print(len(visited)) # for log
            if print_console:
                print_path(visited, father_visited)
            return

        for neighbor in get_adjacency_list(node[0]):
            if neighbor not in visited:
                puzzles_frontier = [n[0] for n in frontier]
                if neighbor not in puzzles_frontier:
                    frontier.append((neighbor, node[1]+1, visited.index(node[0]), 1+node[3]))
                    # add neighbor, depth, parent's position and cost
                else:
                    puzzles_frontier_weights = [n[3] for n in frontier]
                    pos = puzzles_frontier.index(neighbor)
                    weight = puzzles_frontier_weights[pos]

                    if 1+node[3] <= weight:
                        frontier.pop(pos)
                        frontier.append((neighbor, node[1]+1, visited.index(node[0]), 1+node[3]))
                        # update neighbor, depth, parent's position and cost
 
    print("Essa instância não possui solução.")
    print(len(visited)) # for log
    return

#######
####### Greedy 

def Greedy(start, print_console, heuristic, goal="123456780"):

    visited = []
    #depth_visited = []
    father_visited = []

    frontier = []
    frontier.append((start, 0, -1, heuristic(start))) # node, depth, parent's position and cost:(heuristic)

    while len(frontier) > 0:
        frontier = sorted(frontier, key=lambda x: x[3]) #sort by cost
        node = frontier.pop(0)

        visited.append(node[0])
        #depth_visited.append(node[1])
        father_visited.append(node[2])

        if node[0] == goal:
            print(node[1]) # print depth
            print(len(visited)) # for log
            if print_console:
                print_path(visited, father_visited)
            return

        for neighbor, neighbor_heuristic_weight  in get_weighted_adjacency_list(node[0], heuristic):
            if neighbor not in visited:
                puzzles_frontier = [n[0] for n in frontier]
                if neighbor not in puzzles_frontier:
                    frontier.append((neighbor, node[1]+1, visited.index(node[0]), 1++neighbor_heuristic_weight))
                    # add neighbor, depth, parent's position and cost:(heuristic)
                else:
                    puzzles_frontier_weights = [n[3] for n in frontier]
                    pos = puzzles_frontier.index(neighbor)
                    weight = puzzles_frontier_weights[pos]

                    if neighbor_heuristic_weight <= weight:
                        frontier.pop(pos)
                        frontier.append((neighbor, node[1]+1, visited.index(node[0]), neighbor_heuristic_weight))
                        # update neighbor, depth, parent's position and cost:(heuristic)
 
    print("Essa instância não possui solução.")
    print(len(visited)) # for log
    return

#######
####### A_Star 

def A_Star(start, print_console, heuristic, goal="123456780"):

    visited = []
    #depth_visited = []
    father_visited = []

    frontier = []
    frontier.append((start, 0, -1, heuristic(start))) # node, depth, parent's position and cost:(real + heuristic)

    while len(frontier) > 0:
        frontier = sorted(frontier, key=lambda x: x[3]) #sort by cost
        node = frontier.pop(0)

        visited.append(node[0])
        #depth_visited.append(node[1])
        father_visited.append(node[2])

        if node[0] == goal:
            print(node[1]) # print depth
            print(len(visited)) # for log
            if print_console:
                print_path(visited, father_visited)
            return

        for neighbor, neighbor_heuristic_weight  in get_weighted_adjacency_list(node[0], heuristic):
            if neighbor not in visited:
                puzzles_frontier = [n[0] for n in frontier]

                if neighbor not in puzzles_frontier:
                    frontier.append((neighbor, node[1]+1, visited.index(node[0]), 1+node[3]+neighbor_heuristic_weight))
                    # add neighbor, depth, parent's position and cost:(1+old_cost+heuristic)
                else:
                    puzzles_frontier_weights = [n[3] for n in frontier]
                    pos = puzzles_frontier.index(neighbor)
                    weight = puzzles_frontier_weights[pos]

                    if 1+node[3]+neighbor_heuristic_weight <= weight:
                        frontier.pop(pos)
                        frontier.append((neighbor, node[1]+1, visited.index(node[0]), 1+node[3]+neighbor_heuristic_weight))
                        # update neighbor, depth, parent's position and cost:(1+old_cost+heuristic)
 
    print("Essa instância não possui solução.")
    print(len(visited)) # for log
    return
#######
####### HillClimbing 
    #TODO
#######

#############################################################################################################################