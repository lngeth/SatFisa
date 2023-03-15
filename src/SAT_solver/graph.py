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
    self.COLORS = ["green", "red", "blue", "yellow"]
    self.__graph_tab = [int(s) for s in graph_s.strip().split(" ")]
    self.__nb_node = 0
    self.__nb_edge = 0
    self.__list_edge = []
    self.nb_color = 3
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

    nb_color = self.nb_color

    nb_node = self.__nb_node
    list_variable = np.arange(1, (nb_node*nb_color)+1)

    list_clause = []
    list_clause.append("2 0") # first node is RED

    
    
    for i in range(0, len(list_variable), nb_color):
      # at least a color
      s = ""
      for v in range(nb_color):
        s += str(list_variable[i+v]) + " "
      s += "0"
      list_clause.append(s)

      # at most one color
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[i+1])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[i+2])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+1], list_variable[i+2])
      list_clause.append(s)
      if (nb_color == 4):
        s = "-{0} -{1} 0".format(list_variable[i], list_variable[i+3])
        list_clause.append(s)
        s = "-{0} -{1} 0".format(list_variable[i+1], list_variable[i+3])
        list_clause.append(s)
        s = "-{0} -{1} 0".format(list_variable[i+2], list_variable[i+3])
        list_clause.append(s)
    
    # not same color of neighbor
    for edge in self.__list_edge:
      i = (edge[0]-1)*nb_color
      j = (edge[1]-1)*nb_color

      for v in range(nb_color):
        s = "-{0} -{1} 0".format(list_variable[i+v], list_variable[j+v])
        list_clause.append(s)

      """
      s = "-{0} -{1} 0".format(list_variable[i], list_variable[j])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+1], list_variable[j+1])
      list_clause.append(s)
      s = "-{0} -{1} 0".format(list_variable[i+2], list_variable[j+2])
      list_clause.append(s)
      if (nb_color == 4):
        s = "-{0} -{1} 0".format(list_variable[i+3], list_variable[j+3])
        list_clause.append(s)
      """

    head = "p cnf {} {}".format(nb_node*nb_color, len(list_clause))

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
  
  def get_Ncolor_graph(self, sat_res):
    tab_sat = sat_res.split(" ")
    tab_sat.pop() # remove the 0
    tab_sat = [int(s) for s in tab_sat] # convert to int
    colored_graph = []
    for v in range(0, len(tab_sat), self.nb_color): # each variable --> v
      for v_c in range(self.nb_color): # each color of variable --> v_c
        index_var = v + v_c
        if (tab_sat[index_var] > 0):
          colored_graph.append(self.COLORS[v_c])
          break
    return colored_graph
