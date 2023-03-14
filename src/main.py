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
      res = glucose.fit()
      if (res[0]):
        print("SATISFIABLE 3 couleurs ! \n{}".format(res[1]))

        # print the 3-coloriable graph
        print("\nExercice 3 : 3-coloriable")
        colored_3graph = g.get_Ncolor_graph(res[1])
        for i in range(len(colored_3graph)):
           print("Noeud {} : {}".format(i+1, colored_3graph[i]))
      else:
        print("UNSATISFIABLE 3 couleurs !")

        # print the 4-coloriable graph
        print("\nContinue sur 4 couleurs (exercice 4) ? ([y]/n)")
        line = input()
        if (line == "y" or line == ""):
          g.nb_color = 4
          head, clauses = g.get_dimacs_clauses(export_to="data/SAT_in.txt")
          print_dimacs(head, clauses)

          res = glucose.fit()
          if (res[0]):
            print("SATISFIABLE 4 couleurs ! \n{}".format(res[1]))

            colored_4graph = g.get_Ncolor_graph(res[1])
            for i in range(len(colored_4graph)):
              print("Noeud {} : {}".format(i+1, colored_4graph[i]))

      print("\nAfficher le graph avec Networkx ? ([y]/n)")
      line = input()
      if (line == "y" or line == ""):
        g.draw_graph_sat()

    except Exception as e:
       print("Erreur :", e)
       print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
       print("Veuillez réessayer : ")
    else:
      break

endProgram()