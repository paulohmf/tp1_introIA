##### Uteis  ##################################################################

RULES = {0: [1, 3],
         1: [0, 2, 4],
         2: [1, 5],
         3: [0, 4, 6],
         4: [1, 3, 5, 7],
         5: [2, 4, 8],
         6: [3, 7],
         7: [4, 6 ,8],
         8: [5, 7]}

def get_int_list(str_puzzle):
    return [int(p) for p in str_puzzle]

def get_string(puzzle):
    return ''.join([str(p) for p in puzzle])

def print_puzzle(puzzle):
    print()
    print(' '.join([str(p) if p != 0 else " " for p in puzzle[0:3]]).strip())
    print(' '.join([str(p) if p != 0 else " " for p in puzzle[3:6]]).strip())
    print(' '.join([str(p) if p != 0 else " " for p in puzzle[6:9]]).strip())

def print_path(visited, father_visited):
    to_print = []
    to_print.append(visited[-1])

    control = father_visited[-1]
    while control != -1:
        to_print.append(visited[control])
        control = father_visited[control]

    for puzzle in reversed(to_print):
        print_puzzle(get_int_list(puzzle))

def get_adjacency_list(puzzle):
    if type(puzzle) == type("abc"):
        copy_puzzle = get_int_list(puzzle)
    else:
      copy_puzzle = puzzle.copy()

    index = copy_puzzle.index(0)

    adjacency_list = []
    for rule in RULES[index]:
        move = copy_puzzle.copy()

        move[index] =  copy_puzzle[rule]
        move[rule] = 0

        adjacency_list.append(get_string(move))
    return adjacency_list



def get_weighted_adjacency_list(puzzle, heuristic):
    if type(puzzle) == type("abc"):
        copy_puzzle = get_int_list(puzzle)
    else:
      copy_puzzle = puzzle.copy()

    index = copy_puzzle.index(0)

    adjacency_list = []
    for rule in RULES[index]:
        move = copy_puzzle.copy()

        move[index] =  copy_puzzle[rule]
        move[rule] = 0

        move = get_string(move)
        adjacency_list.append((move, heuristic(move)))
    return adjacency_list

################################################################################