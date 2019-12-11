from collections import OrderedDict


# ############################################## GLOBAL VARIABLES
graph = None
frontier = []
visited = OrderedDict()  # To prevent duplicates, we use OrderedDict


def depth_first_search():
    dfs_bfs_ids_ucs("Depth First Search(DFS):")


def breath_first_search():
    dfs_bfs_ids_ucs("Breath First Search(BFS):")


def iterative_deepening_search():
    dfs_bfs_ids_ucs("Iterative Deepening Search(IDS):")


def uniform_cost_search():
    dfs_bfs_ids_ucs("Uniform Cost Search(UCS):")


def greedy_best_first_search():

    # Variables
    goal_state = None
    solution_cost = 0
    solution = []

    # Lets clear frontier and visited, then add root element to the frontier.
    frontier.clear()
    visited.clear()
    frontier.append(graph.root)

    while len(frontier) > 0:

        # Firstly, we need to sort the frontier according to heuristic...
        sort_frontier(return_heuristic)

        # We need to remove the correct node from the frontier and add it to the visited.
        current_node = frontier.pop(0)
        visited[current_node] = None

        # Stop GBFS, if we are in a goal state...
        if is_goal(current_node):
            goal_state = current_node
            break

        # Add to frontier as in BFS.
        add_to_frontier(current_node, "BFS")

    # Check if GBFS was successful...
    if goal_state is not None:

        # We need to calculate the cost of the solution AND get the solution itself...
        current = goal_state
        while current is not None:
            solution_cost += current.cost
            solution.insert(0, current)
            # Get the parent node and continue...
            current = current.parent

        # Print the results...
        print_results("Greedy Best First Search(GBFS):", solution_cost, solution, visited)
    else:
        print("No goal state found.")


def dfs_bfs_ids_ucs(algorithm):

    # Variables
    pop_index = 0
    goal_state = None
    solution_cost = 0
    solution = []
    expanded_nodes = []
    iteration = -1

    # DFS_BFS_IDS
    while goal_state is None and iteration <= graph.maximum_depth:

        # For each iteration, we will increase iteration by one and clear frontier and visited. Also append root node.
        iteration += 1
        frontier.clear()
        visited.clear()
        frontier.append(graph.root)

        # If IDS, we will add iteration number...
        if "IDS" in algorithm:
            expanded_nodes.append("Iteration " + str(iteration) + ":")

        while len(frontier) > 0:

            # If DFS or IDS, we will remove last node from the frontier.
            # IF BFS, we will remove the first node from the frontier.
            if "DFS" in algorithm or "IDS" in algorithm:
                pop_index = len(frontier) - 1

            # IF UCS, we need to sort the frontier according to cost...
            if "UCS" in algorithm:
                sort_frontier(return_cost)

            # We need to remove the correct node from the frontier according to the algorithm and add it to the visited.
            current_node = frontier.pop(pop_index)
            visited[current_node] = None

            # Stop DFS_BFS_IDS, if we are in a goal state...
            if is_goal(current_node):
                goal_state = current_node
                break

            # Lets add all child nodes of the current element to the end of the list...
            # If IDS, we need to add child nodes according to the iteration number.
            if "IDS" in algorithm:
                parent = current_node
                for i in range(iteration):
                    # If parent is not none, iterate to upper parent.
                    parent = parent if parent is None else parent.parent

                if parent is None:
                    add_to_frontier(current_node, "DFS")
            # Else, we add all child nodes.
            else:
                add_to_frontier(current_node, algorithm)

        # Add all visited nodes to expanded nodes, before clearing it.
        for node in visited:
            expanded_nodes.append(node)

        # We will continue only if this is an IDS search...
        if "IDS" not in algorithm:
            break

    # Check if DFS_BFS_IDS was successful...
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
    print_results(algorithm, solution_cost, solution, expanded_nodes)


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
    for goal in graph.maze.goals:
        if goal[0] == node.x and goal[1] == node.y:
            return True
    return False


def print_results(algorithm, solution_cost, solution, expanded_nodes):
    print(algorithm)
    print("Cost of the solution:", solution_cost)
    print("The solution path (" + str(len(solution)) + " nodes):", end=" ")
    for node in solution:
        print(node, end=" ")
    print("\nExpanded nodes (" + str(len(expanded_nodes)) + " nodes):", end=" ")
    if "IDS" in algorithm:
        print()
        for i in range(len(expanded_nodes) - 1):
            if type(expanded_nodes[i+1]) == str:
                print(expanded_nodes[i])
            else:
                print(expanded_nodes[i], end=" ")
    else:
        for node in expanded_nodes:
            print(node, end=" ")
    print("\n")


def return_cost(node):
    return node.cost


def return_heuristic(node):
    return node.heuristic


def sort_frontier(sort_by):
    frontier.sort(key=sort_by)
