import networkx as nx

class Graph:

    def __init__(self):
        self.G = None

    def parse_data2graph(self, file_name):
        self.G = nx.read_edgelist(file_name, create_using=nx.DiGraph())

    def add_connection(self, conn):
        if not self.G:
            return {"Error":  "set graph before"}
        self.G.add_edge(*conn)
        return {"Graph":  nx.adjacency_data(self.G)}

    def get_info(self):
        if not self.G:
            return {"Error":  "set graph before"}
        stat_max = max([len(self.G[i]) for i in self.G.adj])
        stat_min = min([len(self.G[i]) for i in self.G.adj])
        stat_medium = self.G.number_of_edges()/self.G.number_of_nodes()
        return {"Graph": nx.adjacency_data(self.G), "max": stat_max, "min": stat_min, "medium": stat_medium}