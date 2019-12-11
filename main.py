import search
from graph import Graph


if __name__ == "__main__":
    # Setting graph we initiated to search class...
    graph = Graph()
    search.graph = graph

    search.depth_first_search()
    search.breath_first_search()
    search.iterative_deepening_search()
    search.uniform_cost_search()
