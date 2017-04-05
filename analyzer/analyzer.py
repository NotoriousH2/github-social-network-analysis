import settings
import networkx as nx
    

def read_graph():
    path = settings.GEXF_PATH
    graph = nx.read_gexf(path)
    return graph
    

if __name__ == "__main__":
    graph = read_graph()