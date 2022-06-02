import sys
import time
from algoritmos import BFS, iterative_DFS, Dijkstra, Greedy, A_Star
from uteis import get_int_list, get_string
from heuristicas import wrong_pieces, distance_manhattan_sum

##### Main  ################################################################################

if len(sys.argv) not in (11,12):
    print("OPS - Invalid Input")
    exit()

alg = sys.argv[1]
puzzle = get_string([sys.argv[i] for i in range(2,11)])

print_console = False
if len(sys.argv) == 12:
    print_console = True if sys.argv[11] == "PRINT" else False

print(alg) # for log
print(puzzle) # for log
start_time = time.time() # for log

if alg == "B":
    print()
    BFS(start=puzzle, print_console=print_console) 
if alg == "I":
    print()
    iterative_DFS(start=puzzle, print_console=print_console)
if alg == "U":
    print()
    Dijkstra(start=puzzle, print_console=print_console)
if alg == "A":
    print("wrong_pieces")
    A_Star(start=puzzle, print_console=print_console, heuristic=wrong_pieces)
    print("%s" % (time.time() - start_time)) # for log
    print(alg) # for log
    print(puzzle) # for log
    print("distance_manhattan_sum")
    start_time = time.time() # for log
    A_Star(start=puzzle, print_console=print_console, heuristic=distance_manhattan_sum)
if alg == "G":
    print("wrong_pieces")
    Greedy(start=puzzle, print_console=print_console, heuristic=wrong_pieces)
    print("%s" % (time.time() - start_time)) # for log
    print(alg) # for log
    print(puzzle) # for log
    print("distance_manhattan_sum")
    start_time = time.time() # for log
    Greedy(start=puzzle, print_console=print_console, heuristic=distance_manhattan_sum)
if alg == "H":
    #HillClimbing(start=get_string(puzzle), print_console=print_console)
    pass

print("%s" % (time.time() - start_time)) # for log

#python TP1.py B 1 2 3 4 0 5 7 8 6 PRINT
#python TP1.py B 1 2 3 4 0 5 7 8 6

############################################################################################