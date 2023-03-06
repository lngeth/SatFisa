import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphSAT:

  def __init__(self, graph_s):
    self.__graph_tab = [int(s) for s in graph_s.strip().split(" ")]
    self.string_to_graph()

  def string_to_graph(self):
    graph_tab = self.__graph_tab
    print(graph_tab)
    if (len(graph_tab) < 2):
      raise Exception("Le format du graphe donné est incorrect...")
    elif ((graph_tab[1] * 2) != (len(graph_tab) - 2)):
      raise Exception("Des arètes n'ont pas été définies...")
    
    # graph is correct: add to Graph properties
    self.__nb_node = graph_tab[0]
    list_edge = []
    for i in range(2, len(graph_tab)-1, 2):
      list_edge.append((graph_tab[i], graph_tab[i+1]))
    self.__list_edge = list_edge

  def draw_graph_sat(self):
    G = nx.Graph()
    G.add_nodes_from(np.arange(1, self.__nb_node + 1))
    G.add_edges_from(self.__list_edge)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000)
    plt.show()
