from collections import OrderedDict


# ############################################## GLOBAL VARIABLES
graph = None
frontier = []
visited = OrderedDict()  # To prevent duplicates, we use OrderedDict


def depth_first_search():
    dfs_bfs("Depth First Search(DFS):")


def breath_first_search():
    dfs_bfs("Breath First Search(BFS):")


def iterative_deepening_search():
    ids()


def dfs_bfs(algorithm):
    # Firstly, empty frontier and visited.
    frontier.clear()
    visited.clear()

    # Lets add the root element to the frontier.
    frontier.append(graph.root)

    # Variables
    pop_index = 0
    goal_state = None
    solution_cost = 0
    solution = []

    # DFS_BFS
    while len(frontier) > 0:

        # If DFS, we will remove last node from the frontier. If BFS, we will remove the first node from the frontier.
        if "DFS" in algorithm:
            pop_index = len(frontier) - 1

        # We need to remove the correct node from the frontier according to the algorithm and add it to the visited...
        current_node = frontier.pop(pop_index)
        visited[current_node] = None

        # Stop DFS_BFS, if we are in a goal state...
        if is_goal(current_node):
            goal_state = current_node
            break

        # Lets add all child nodes of the current element to the end of the list...
        add_to_frontier(current_node, algorithm)

    # Check if DFS_BFS was successful...
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
    print_results(algorithm, solution_cost, solution)


def ids():
    # Firstly, empty frontier and visited.
    frontier.clear()
    visited.clear()

    # Lets add the root element to the frontier.
    frontier.append(graph.root)

    # Variables
    goal_state = None
    solution_cost = 0
    solution = []
    iteration = 0

    # IDS
    while goal_state is None and iteration <= graph.maximum_depth:
        while len(frontier) > 0:

            # We need to remove the correct node from the frontier according to the algorithm and add it to the visited.
            current_node = frontier.pop(len(frontier) - 1)
            visited[current_node] = None

            # Stop DFS_BFS, if we are in a goal state...
            if is_goal(current_node):
                goal_state = current_node
                break

            # Lets add all child nodes of the current element to the end of the list...
            # If the iteration number is sufficient.
            parent = current_node
            for i in range(iteration):
                parent = parent if parent is None else parent.parent  # If parent is not none, iterate to upper parent.

            if parent is None:
                add_to_frontier(current_node, "DFS")

            print(current_node)

        # After frontier gets empty, we will increase iteration by one and clear frontier and visited.
        iteration += 1
        frontier.clear()
        visited.clear()
        frontier.append(graph.root)


def add_to_frontier(current_node, algorithm):
    # If the child nodes are not None AND if they are not in visited, we will add them to the frontier.
    nodes_to_add = []
    if current_node.east is not None and not is_in_visited(current_node.east):
        nodes_to_add.append(set_parent(current_node, current_node.east))
    if current_node.south is not None and not is_in_visited(current_node.south):
        nodes_to_add.append(set_parent(current_node, current_node.south))
    if current_node.west is not None and not is_in_visited(current_node.west):
        nodes_to_add.append(set_parent(current_node, current_node.west))
    if current_node.north is not None and not is_in_visited(current_node.north):
        nodes_to_add.append(set_parent(current_node, current_node.north))

    # For DFS we'll do it in reverse order because we add each node to the end and EAST should be the last node.
    # For BFS we'll do it in correct order.
    if "DFS" in algorithm:
        nodes_to_add.reverse()

    # Then add each node to the frontier.
    for node in nodes_to_add:
        frontier.append(node)


def set_parent(parent_node, child_node):
    # We need to set the parent node...
    child_node.parent = parent_node
    return child_node


def is_in_visited(node):
    if node in visited:
        return True
    return False


def is_goal(node):
    if graph.maze.goals[node.x][node.y] == 1:
        return True
    return False


def print_results(algorithm, solution_cost, solution):
    print(algorithm)
    print("Cost of the solution:", solution_cost)
    print("The solution path (" + str(len(solution)) + " nodes):", end=" ")
    for node in solution:
        print(node, end=" ")
    print("\nExpanded nodes (" + str(len(visited)) + " nodes):", end=" ")
    for node in visited:
        print(node, end=" ")
    print("\n")
