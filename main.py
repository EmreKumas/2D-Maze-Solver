import re


def read_maze():
    file = open("maze.txt", "r")
    line = file.readline().rstrip("\n\r")
    empty_line = 0

    while empty_line < 2:
        # To be able to construct more beautiful input file, we let a blank line to be readable.
        if not line:
            empty_line += 1
        else:
            empty_line = 0

        # Now, we will check headings...
        if line == "Size":
            first_size = file.readline().rstrip("\n\r")
            second_size = file.readline().rstrip("\n\r")
            set_size(first_size, second_size)
        elif line == "Walls":
            walls = []
            line = file.readline().rstrip("\n\r")
            # We are going to read every line until Traps section...
            while line:
                walls.append(line)
                line = file.readline().rstrip("\n\r")
            set_walls(walls)
        elif line == "Traps":
            traps = []
            line = file.readline().rstrip("\n\r")
            # We are going to read every line until Start section...
            while line:
                traps.append(line)
                line = file.readline().rstrip("\n\r")
            set_traps(traps)
        elif line == "Start":
            start = file.readline().rstrip("\n\r")
            set_start(start)

        line = file.readline().rstrip("\n\r")

    file.close()


# noinspection PyUnusedLocal
def set_size(x, y):
    global maze_size
    # First setting the row count
    if "rows" in x:
        maze_size.append(int(re.sub("[^0-9]", "", x)))
    elif "rows" in y:
        maze_size.append(int(re.sub("[^0-9]", "", y)))

    # Then setting the column count
    if "columns" in x:
        maze_size.append(int(re.sub("[^0-9]", "", x)))
    elif "columns" in y:
        maze_size.append(int(re.sub("[^0-9]", "", y)))

    # Lastly we will fill wall and trap arrays with zero.
    global maze_walls_vertical
    global maze_walls_horizontal
    global maze_traps
    maze_walls_vertical = [[0 for i in range(maze_size[1] - 1)] for i in range(maze_size[0])]
    maze_walls_horizontal = [[0 for i in range(maze_size[1])] for i in range(maze_size[0] - 1)]
    maze_traps = [[0 for i in range(maze_size[1])] for i in range(maze_size[0])]


def set_walls(walls):
    global maze_walls_vertical
    global maze_walls_horizontal
    walls_length = len(walls)

    for i in range(walls_length):
        # First case is row...
        if "row" in walls[i]:
            row_index = int(re.sub("[^0-9]", "", walls[i]))
            column_indexes = walls[i+1].split()
            for index in column_indexes:
                maze_walls_vertical[row_index - 1][int(index) - 1] = 1
        # Second case is column...
        elif "column" in walls[i]:
            column_index = int(re.sub("[^0-9]", "", walls[i]))
            row_indexes = walls[i + 1].split()
            for index in row_indexes:
                maze_walls_horizontal[int(index) - 1][column_index - 1] = 1


def set_traps(traps):
    global maze_traps
    for trap in traps:
        indexes = list(map(int, trap.split()))
        maze_traps[indexes[0] - 1][indexes[1] - 1] = 1


def set_start(start):
    global maze_start
    indexes = list(map(int, start.split()))
    maze_start.append(indexes[0] - 1)
    maze_start.append(indexes[1] - 1)


def can_pass(row, column, direction):
    global maze_walls_vertical
    global maze_walls_horizontal
    global maze_size

    # Check if the player can pass
    if direction == "east":
        if column == (maze_size[1] - 1):
            return False
        return not (maze_walls_vertical[row][column] == 1)
    elif direction == "south":
        if row == (maze_size[0] - 1):
            return False
        return not (maze_walls_horizontal[row][column] == 1)
    elif direction == "west":
        if column == 0:
            return False
        return not (maze_walls_vertical[row][column - 1] == 1)
    elif direction == "north":
        if row == 0:
            return False
        return not (maze_walls_horizontal[row - 1][column] == 1)


# Global variables
maze_size = []
maze_walls_vertical = [[]]
maze_walls_horizontal = [[]]
maze_traps = [[]]
maze_start = []

# Main function
if __name__ == "__main__":
    read_maze()
