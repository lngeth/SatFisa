# Import libraries
import numpy as np
import networkx as nx
import re

# Import tools class
from interface.logs import *
from draw.graph import *

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
      bash_command = "glucose -model data/SAT_in.txt"
      process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
      output, error = process.communicate()
      output = output.decode("utf-8")
      # extract the result only
      res = re.search(r's\s[A-Z]{0,3}SATISFIABLE', output)
      output = output[res.start():]
      print(output.strip())

      # g.draw_graph_sat()
    except Exception as e:
       print("Erreur :", e)
       print("(Format voulu : nb_noeuds nb_aretes n1 n2 ...)")
       print("Veuillez réessayer : ")
    else:
      break

endProgram()