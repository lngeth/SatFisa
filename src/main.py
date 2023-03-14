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

      # draw Graph
      print("To Dimacs format :")

      # write Dimacs format into txt files
      head, clauses = g.get_dimacs_clauses()
      f = open("data/SAT_in.txt", mode="w")
      f.write(head + "\n")
      f.close()
      f = open("data/SAT_in.txt", mode="a")
      for c in clauses:
        f.write(c + "\n")
      f.close()
      
      f = open("data/SAT_in.txt", mode="r")
      print(f.read())
      f.close()

      # run glucose
      glucose = Glucose("data/SAT_in.txt")
      res = glucose.run()
      print(res)

      # g.draw_graph_sat()
    except Exception as e:
       print("Erreur :", e)
       print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
       print("Veuillez réessayer : ")
    else:
      break

endProgram()