from graph import Graph


def depth_first_search():
    # Firstly, lets add the root element to the frontier.
    frontier.append(graph.root)

    # Variables
    goal_state = None
    solution_cost = 0
    solution = []

    # DFS
    while len(frontier) > 0:
        # First, we need to remove the last node from the frontier and add it to the visited...
        current_node = frontier.pop()
        visited.append(current_node)

        # Stop DFS, if we are in a goal state...
        if is_goal(current_node):
            goal_state = current_node
            break

        # Lets add all child nodes of the current element to the end of the list...
        add_to_frontier(current_node)

    # Check if DFS was successful...
    if goal_state is None:
        print("No goal state found.")
        return

    # We need to calculate the cost of the solution AND get the solution itself...
    current = goal_state
    while current is not None:
        solution_cost += current.cost
        solution.insert(0, current)
        # Get the parent node and continue...
        current = current.parent

    # Print the results...
    print("Depth First Search(DFS):\n")
    print("Cost of the solution:", solution_cost)
    print("The solution path (" + str(len(solution)) + " nodes):", end=" ")
    for node in solution:
        print(node, end=" ")
    print("\nExpanded nodes (" + str(len(visited)) + " nodes):", end=" ")
    for node in visited:
        print(node, end=" ")
    print()


def add_to_frontier(current_node):
    # If the child nodes are not None AND if they are not in visited, we will add them to the frontier.
    # But we'll do it in reverse order because we add each node to the end of the list and EAST should be the last node.
    if current_node.north is not None and not is_in_visited(current_node.north):
        add_this(current_node, current_node.north)
    if current_node.west is not None and not is_in_visited(current_node.west):
        add_this(current_node, current_node.west)
    if current_node.south is not None and not is_in_visited(current_node.south):
        add_this(current_node, current_node.south)
    if current_node.east is not None and not is_in_visited(current_node.east):
        add_this(current_node, current_node.east)


def add_this(parent_node, child_node):
    # We need to set the parent node...
    child_node.parent = parent_node
    frontier.append(child_node)


def is_in_visited(node):
    for n in visited:
        if node.check_equality(n.x, n.y):
            return True
    return False


def is_goal(node):
    if graph.maze.goals[node.x][node.y] == 1:
        return True
    return False


# ############################################## GLOBAL VARIABLES
graph = None
frontier = []
visited = []

if __name__ == "__main__":
    # Initiating the graph.
    graph = Graph()

    # DFS
    depth_first_search()
