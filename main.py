# arrange the symbols in lists, aka boats, that relationships define as okay
# state has a symbol in a container. Each container has a number. 

# starting state
# ending state
# Getting from starting state to ending state
# symbols have relationships to them.
# symbol is abstract and name and real life connotation does not matter

# eh, good enough for now

import symbolic as sym

listOfSymbols = ["Jeff","Perry","Joe","Manny"]

state = [["Jeff", 1], ["Perry", 1], ["Joe", 1],["Manny",5]]

endState = [["Jeff", 2], ["Perry", 2], ["Joe", 6],["Manny",6]]

listOfRelationships = [sym.Relationship("Jeff", ["Perry"], ["Joe", "Manny"])]


myAi = sym.SymbolicAi( listOfSymbols, listOfRelationships, state, endState)

myAi.solve()