def startProgram():
    print("Bonjour ! DM SAT logique\nVeuillez entrer le graph souhaité :"
        )
    print("('exit' pour sortir)\n")

def endProgram():
    print("\nFin du programme...")

def print_dimacs(head, clauses):
    print("To Dimacs format :")
    print(head)
    for c in clauses:
        print(c)