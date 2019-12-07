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
            while line != "Traps" and line:
                walls.append(line)
                line = file.readline().rstrip("\n\r")
            set_walls(walls)

        line = file.readline().rstrip("\n\r")

    file.close()


def set_size(x, y):
    pass


def set_walls(walls):
    pass


# Global variables
maze_size = []
maze_walls_vertical = [[]]
maze_walls_horizontal = [[]]

# Main function
if __name__ == "__main__":
    read_maze()
