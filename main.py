from graph import Graph


def depth_first_search():
    # Firstly, lets add the root element to the frontier.
    frontier.append(graph.root)

    # DFS
    while len(frontier) > 0:
        # First, we need to remove the first node from the frontier and add it to the visited...
        current_node = frontier.pop(0)
        visited.append(current_node)

        # Stop DFS, if we are in a goal state...
        if is_goal(current_node):
            break

        # Lets add all child nodes of the current element to the beginning of the list...
        add_to_frontier(current_node)


def add_to_frontier(current_node):
    # If the child nodes are not None AND if they are not in visited, we will add them to the frontier.
    # But we will do this in reverse order because we add each node to the front of the list.
    if current_node.north is not None and not is_in_visited(current_node.north):
        frontier.insert(0, current_node.north)
    if current_node.west is not None and not is_in_visited(current_node.west):
        frontier.insert(0, current_node.west)
    if current_node.south is not None and not is_in_visited(current_node.south):
        frontier.insert(0, current_node.south)
    if current_node.east is not None and not is_in_visited(current_node.east):
        frontier.insert(0, current_node.east)


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
