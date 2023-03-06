import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphSAT:

  def __init__(self, graph_s):
    self.__graph_s = graph_s.replace(" ", "")
    self.string_to_graph()

  def string_to_graph(self):
    s = self.__graph_s
    if (len(s) < 2):
      raise Exception("Le format du graphe donné est incorrect...")
    if ((int(s[1]) * 2) != (len(s) - 2)):
      raise Exception("Des arètes n'ont pas été définies...")
    
    # graph is correct: add to Graph properties
    self.__nb_node = int(s[0])
    self.__nb_edge = int(s[1])
    list_edge = []
    for i in range (2, len(s)-1):
      list_edge.append((int(s[i]), int(s[i+1])))
    self.__list_edge = list_edge

  def draw_graph_sat(self):
    G = nx.Graph()
    G.add_nodes_from(np.arange(1, self.__nb_node + 1))
    G.add_edges_from(self.__list_edge)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000)
    plt.show()
