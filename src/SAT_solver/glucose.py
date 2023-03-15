import re
import subprocess # to run bash command

class Glucose:
  """Represent the object that is use to execute Glucose command

  Attributes:
    __file: the relative path to the txt file containing the SAT problem in DIMACS format
  """
  def __init__(self, file):
    self.__file = file
  
  def fit(self):
    """Execute the Glucose command with the corresponding txt file
    """
    # run glucose
    bash_command = "glucose -model " + self.__file
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")

    # extract the result only
    res = re.search(r'[A-Z]{0,3}SATISFIABLE', output)
    output = output[res.start():]
    solution = [s.strip() for s in output.strip().split("v")]

    # return the result
    tab = []
    if (len(solution) == 2):
      tab.append(True)
      tab.append(solution[1])
    else:
      tab.append(False)
      tab.append([])

    return tab