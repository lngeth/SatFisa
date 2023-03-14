import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class GraphSAT:
  """Represent a Graph in code

  Attributes:
    __graph_tab: List of each integer entered by the user (i.e. 2 1 1 2 => [2,1,1,2])
    __nb_node: Number of nodes of the graph
    __nb_edge: Number of edges of the graph
    __list_edge: List of edges of the graph. List of tuples (i.e. [(1,2), (2,3), ...])
  """

  def __init__(self, graph_s):
    """Init the Graph object with String format Graph given by user"""
    self.__graph_tab = [int(s) for s in graph_s.strip().split(" ")]
    self.string_to_graph()

  def string_to_graph(self):
    """Convert the string graph given by the user into Graph object"""
    graph_tab = self.__graph_tab
    if (len(graph_tab) < 2):
      raise Exception("Le format du graphe donné est incorrect...")
    elif ((graph_tab[1] * 2) != (len(graph_tab) - 2)):
      raise Exception("Des arètes n'ont pas été définies...")
    
    # graph is correct: add to Graph properties
    self.__nb_node = graph_tab[0]
    self.__nb_edge = graph_tab[1]
    list_edge = []
    for i in range(2, len(graph_tab)-1, 2):
      list_edge.append((graph_tab[i], graph_tab[i+1]))
    self.__list_edge = list_edge
  
  def get_dimacs_clauses(self, export_to=""):
    """Convert the Graph object into Dimacs format
    export_to correspond to the path of the output file
    """
    nb_node = self.__nb_node
    list_variable = np.arange(1, (nb_node*3)+1)

    list_clause = []
    list_clause.append("2 0") # first node is RED
    
    for i in range(0, len(list_variable), 3):
      # at least a color
      s = "{0} {1} {2} 0".format(list_variable[i], list_variable[i+1], list_variable[i+2])
      list_clause.append(s)

      # at most one color
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[i+1])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[i+2])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+1], list_variable[i+2])
      list_clause.append(s)
    
    # not same color of neighbor
    for edge in self.__list_edge:
      i = (edge[0]-1)*3
      j = (edge[1]-1)*3
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[j])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+1], list_variable[j+1])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+2], list_variable[j+2])
      list_clause.append(s)

    head = "p cnf {} {}".format(nb_node*3, len(list_clause))

    # export to output file
    if (export_to != ""):
      # erase everything first
      f = open(export_to, mode="w")
      f.write(head + "\n")
      f.close()

      # write the current SAT problem
      f = open(export_to, mode="a")
      for c in list_clause:
        f.write(c + "\n")
      f.close()

    return (head, list_clause)

  def draw_graph_sat(self):
    """Draw the Graph with Networkx"""
    G = nx.Graph()
    G.add_nodes_from(np.arange(1, self.__nb_node + 1))
    G.add_edges_from(self.__list_edge)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000)
    plt.show()
