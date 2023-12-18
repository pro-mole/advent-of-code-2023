#!/usr/local/bin/python3

# Model the pipe maze as a graph with an adjacency hashtable (X,Y) => [(X2,Y2), ...]
# Where the tile at X, Y is connected to the tile at X2,Y2

tile_types = {
    '|': [(0,1), (0,-1)],
    '-': [(1,0), (-1,0)],
    'J': [(-1,0), (0,-1)],
    'L': [(1,0), (0,-1)],
    'F': [(1,0), (0,1)],
    '7': [(-1,0), (0,1)]
}

# == PART 1 ==
maze = {}
start_pos = None

# Add a tile of type T (char) the the graph
# This creates the bilateral adjacency between the tiles as well
def add_tile(maze, tile, position):
    if tile in tile_types:
        if position not in maze:
            maze[position] = set()
    
        for dX, dY in tile_types[tile]:
            maze[position].add((position[0] + dX, position[1] + dY))

# Read input and populate the maze
with open("input", "r") as input_file:
    y = 0
    for line in input_file.readlines():
        x = 0
        for tile in line:
            if tile == 'S':
                start_pos = (x, y) # Deal with Start Position later
            add_tile(maze, tile, (x, y))
            x += 1
        y += 1

# Map distance from starting position
distance = {
    start_pos: 0
}

# Find pipes connected to the start and go on from there
next_tile = []
for pos in maze:
    if start_pos in maze[pos]:
        next_tile.append(pos)

while len(next_tile) > 0:
    next = next_tile.pop(0)
    for neighbor in maze[next]:
        if neighbor in distance:
            distance[next] = distance[neighbor] + 1
        else:
            next_tile.append(neighbor)

print(f"Part 1 Answer: {max(distance.values())}")

# == PART 2 ==

# Read the maze and count tiles inside the pipes
# Basically, sweep the lines of the grid and count how many vertical sections are crossed when reading a .
# (if even, we're outside, if odd, we're inside)
inside_tiles = 0

# We'll use the distance table generated above as a way to identify which tiles are actually part of the maze
# Debug flag
maze_visualizer = False
with open("input", "r") as input_file:
    y = 0
    for line in input_file.readlines():
        x = 0
        vsection = [False, False] # Section crossing for upper pipes and lower pipes
        for tile in line:
            if tile.isspace(): break

            if (x,y) not in distance:
                if vsection != [False, False]:
                    if maze_visualizer: print('#', end='')
                    inside_tiles += 1
                elif maze_visualizer: print('.', end='')
            elif tile in tile_types:
                if maze_visualizer: print(tile, end='')
                for connection in tile_types[tile]:
                    if connection[1] == 1:
                        vsection[0] = not vsection[0]
                    elif connection[1] == -1:
                        vsection[1] = not vsection[1]
            elif tile == 'S':
                # Edge case: the S is actually something else we have to reverse engineer
                for pos in maze:
                    if start_pos in maze[pos]:
                        vconnection = pos[1] - start_pos[1]
                        if vconnection == 1:
                            vsection[0] = not vsection[0]
                        elif vconnection == -1:
                            vsection[1] = not vsection[1]
                if maze_visualizer: print("+", end='')
            x += 1
        if maze_visualizer: print()
        y += 1

print(f"Part 2 Answer: {inside_tiles}")
