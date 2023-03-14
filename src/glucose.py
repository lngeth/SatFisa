import re
import subprocess # to run bash command

class Glucose:
  def __init__(self, file):
    self.__file = file
  
  def run(self):
    # run glucose
    bash_command = "glucose -model " + self.__file
    process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode("utf-8")
    # extract the result only
    res = re.search(r's\s[A-Z]{0,3}SATISFIABLE', output)
    output = output[res.start():]
    return output.strip()