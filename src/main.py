# Import libraries
import numpy as np
import networkx as nx
import re

# Import tools class
from interface.logs import *
from draw.graph import *
from glucose import *

import subprocess # to run bash command

startProgram()

line = ""
while(True):
    # get line
    line = input()
    print("Graph : {}\n".format(line))
    if (line == "exit"):
        break
    
    # format line to graph
    try:
      g = GraphSAT(line)

      # write Dimacs format into txt files
      head, clauses = g.get_dimacs_clauses(export_to="data/SAT_in.txt")
      print_dimacs(head, clauses)

      # run glucose
      glucose = Glucose("data/SAT_in.txt")
      res = glucose.run()
      print(res)

      print("Afficher le graph avec Networkx ? (y/n)")
      line = input()
      if (line == "y"):
        g.draw_graph_sat()
    except Exception as e:
       print("Erreur :", e)
       print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
       print("Veuillez réessayer : ")
    else:
      break

endProgram()