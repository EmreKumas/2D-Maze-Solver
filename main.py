from maze import Maze


class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cost = 0
        self.east = None
        self.south = None
        self.west = None
        self.north = None

    def check_equality(self, x, y):
        return x == self.x and y == self.y

    def __str__(self):
        return "x = " + str(self.x) + "\ny = " + str(self.y) + "\n"


def create_node(x, y):
    node = Node()

    # Initializing node's coordinates.
    node.x = x
    node.y = y

    # Adding the node into the nodes list.
    nodes.append(node)

    # Setting the cost 1 if it is not a trap square.
    if maze.traps[node.x][node.y] == 1:
        node.cost = 7
    else:
        node.cost = 1

    # Setting all child nodes.
    if maze.can_pass(node.x, node.y, "east"):
        # Before creating a new node, we should check if that node exists. If yes, we don't need to create it.
        node.east = node_exists(node.x, node.y + 1)
        if node.east is None:
            node.east = create_node(node.x, node.y + 1)

    if maze.can_pass(node.x, node.y, "south"):
        node.south = node_exists(node.x + 1, node.y)
        if node.south is None:
            node.south = create_node(node.x + 1, node.y)

    if maze.can_pass(node.x, node.y, "west"):
        node.west = node_exists(node.x, node.y - 1)
        if node.west is None:
            node.west = create_node(node.x, node.y - 1)

    if maze.can_pass(node.x, node.y, "north"):
        node.north = node_exists(node.x - 1, node.y)
        if node.north is None:
            node.north = create_node(node.x - 1, node.y)

    return node


def node_exists(x, y):
    for node in nodes:
        if node.check_equality(x, y):
            return node
    return None


nodes = []  # Keeping all nodes in a list to prevent duplicate nodes.
maze = Maze()

# Main function
if __name__ == "__main__":
    # Creating the graph.
    root = create_node(maze.start[0], maze.start[1])
