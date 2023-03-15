# Import libraries
import numpy as np
import re

# Import tools class
from SAT_solver.graph import *
from SAT_solver.glucose import *

import subprocess # to run bash command

print("Bonjour ! DM SAT logique\nVeuillez entrer le graph souhaité :")
print("('exit' pour sortir)\n")

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

      glucose = Glucose("data/SAT_in.txt")
      res = []

      while True:
        # write Dimacs format into txt files
        head, clauses = g.get_dimacs_clauses(export_to="data/SAT_in.txt")
        
        # print the Dimacs format
        print("To Dimacs format :")
        print(head)
        for c in clauses:
          print(c)

        # run glucose
        res = glucose.fit()

        # if UNSAT, try with 1 more color (4 color max: Theorem 4-color)
        if (res[0] == False):
          print("UNSATISFIABLE pour {} couleurs...\n".format(g.nb_color))
          g.nb_color += 1
        else:
          break

      print("SATISFIABLE avec {} couleurs !\n{}".format(g.nb_color, res[1]))

      # print the n-coloriable graph
      print("\nExercice {0} : {0} couleurs nécessaires !".format(g.nb_color))
      colored_ngraph = g.get_Ncolor_graph(res[1])
      for i in range(len(colored_ngraph)):
        print("Noeud {} : {}".format(i+1, colored_ngraph[i]))

    except Exception as e:
      print("Erreur :", e)
      print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
      print("Veuillez réessayer : ")
    else:
      break

print("\nFin du programme...")