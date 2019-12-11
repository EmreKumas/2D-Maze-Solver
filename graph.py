import sys
from maze import Maze


class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cost = 0
        self.parent = None
        self.east = None
        self.south = None
        self.west = None
        self.north = None
        self.heuristic = 0

    def check_equality(self, x, y):
        return x == self.x and y == self.y

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"


class Graph:

    nodes = []  # Keeping all nodes in a list to prevent duplicate nodes.
    maze = None

    def __init__(self):
        # Creating the graph.
        self.maze = Maze()
        self.root = self.create_node(self.maze.start[0], self.maze.start[1])

        # Finding maximum depth.
        self.maximum_depth = self.find_maximum_depth() - 1

        # Creating heuristic...
        self.create_heuristic()

        # We will make the cost of root node 0, because that's where we start.
        self.root.cost = 0

    def create_node(self, x, y):
        node = Node()

        # Initializing node's coordinates.
        node.x = x
        node.y = y

        # Adding the node into the nodes list.
        self.nodes.append(node)

        # Setting the cost 1 if it is not a trap square.
        if self.maze.traps[node.x][node.y] == 1:
            node.cost = 7
        else:
            node.cost = 1

        # Setting all child nodes.
        if self.maze.can_pass(node.x, node.y, "east"):
            # Before creating a new node, we should check if that node exists. If yes, we don't need to create it.
            node.east = self.node_exists(node.x, node.y + 1)
            if node.east is None:
                node.east = self.create_node(node.x, node.y + 1)
                node.east.parent = node

        if self.maze.can_pass(node.x, node.y, "south"):
            node.south = self.node_exists(node.x + 1, node.y)
            if node.south is None:
                node.south = self.create_node(node.x + 1, node.y)
                node.south.parent = node

        if self.maze.can_pass(node.x, node.y, "west"):
            node.west = self.node_exists(node.x, node.y - 1)
            if node.west is None:
                node.west = self.create_node(node.x, node.y - 1)
                node.west.parent = node

        if self.maze.can_pass(node.x, node.y, "north"):
            node.north = self.node_exists(node.x - 1, node.y)
            if node.north is None:
                node.north = self.create_node(node.x - 1, node.y)
                node.north.parent = node

        return node

    def node_exists(self, x, y):
        for node in self.nodes:
            if node.check_equality(x, y):
                return node
        return None

    def find_maximum_depth(self):
        maximum_depth = 0

        for node in self.nodes:
            current_node = node
            local_depth = 0
            while current_node is not None:
                current_node = current_node.parent
                local_depth += 1

            # If local_depth is greater, we will set it as maximum_depth.
            maximum_depth = max(maximum_depth, local_depth)

        return maximum_depth

    def get_node_cost(self, x, y):
        for node in self.nodes:
            if node.check_equality(x, y):
                return node.cost
        return 0

    def clear_parents(self):
        for node in self.nodes:
            node.parent = None

    def create_heuristic(self):
        # Create a heuristic for each node...
        for node in self.nodes:
            # Select minimum distance to a closest goal...
            total_cost = sys.maxsize
            for goal in self.maze.goals:
                cost = 0
                vertical_distance = goal[1] - node.y
                horizontal_distance = goal[0] - node.x

                # Then we will add each node's cost until to the goal state...
                x = 0
                y = 0
                while vertical_distance > 0:
                    y += 1
                    cost += self.get_node_cost(node.x, node.y + y)
                    vertical_distance -= 1
                while horizontal_distance > 0:
                    x += 1
                    cost += self.get_node_cost(node.x + x, node.y + y)
                    horizontal_distance -= 1
                while vertical_distance < 0:
                    y -= 1
                    cost += self.get_node_cost(node.x + x, node.y + y)
                    vertical_distance += 1
                while horizontal_distance < 0:
                    x -= 1
                    cost += self.get_node_cost(node.x + x, node.y + y)
                    horizontal_distance += 1

                # Select the minimum heuristic...
                total_cost = min(total_cost, cost)

            # After calculating the total cost, we assign it into node's heuristic...
            node.heuristic = total_cost
