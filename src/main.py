# Import libraries
import numpy as np
import networkx as nx

# Import tools class
from interface.logs import *
from draw.graph import *

startProgram()

line = ""
while(True):
    # get line
    line = input()
    print("Graph :", line)
    if (line == "exit"):
        break
    
    # format line to graph
    try:
      g = GraphSAT(line)

      # draw Graph
      g.draw_graph_sat()
    except Exception as e:
       print("Erreur :", e)
       print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
       print("Veuillez réessayer : ")
    else:
      break

endProgram()