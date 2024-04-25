# starting state
# ending state
# Getting from starting state to ending state
# symbols have relationships to them.
# symbol is abstract and name and real life connotation does not matter
import random as ran
import copy

class SymbolicAi():
    def __init__(self, listOfSymbols, listOfRelationships, startState, endState, maxBoats = 10):
        self.symbols = listOfSymbols
        self.relatationships = listOfRelationships
        self.startState = startState
        self.endState = endState
        self.engram = [] # stores the previous interations
        self.currentState = startState
        self.maxBoats = maxBoats
        self.done = False

    def changeState(self):
        # going to change the symbol in this position
        changing = ran.randrange(0, len(self.currentState))
        self.currentState[changing][1] = ran.randrange(1, self.maxBoats)


    def evaluateState(self):

        score = 0
        evalset = None
        tempCurrentState = copy.deepcopy(self.currentState)

        # change the eval set according to illegal groupings
        for item in self.relatationships:
            evalset = item.constraint(tempCurrentState)
        
        # see how close the set matches
        for index, item in enumerate(evalset):
            if (item[0] == self.endState[index][0]) and (item[1] == self.endState[index][1]):
                score += 1
        
        # save the result as part of its history
        self.engram.append([self.currentState, score])

        # score matches the length, meaning each position is correct
        if score == len(self.endState):
            self.done = True
            print("Solution Found:", self.currentState)

        # get the index of the best scoring state
        max_index, _ = max(enumerate(self.engram), key=lambda x: x[1][1])

        # set the current state to the best state
        self.currentState = self.engram[max_index][0]
            

    def solve(self):
        i = 0
        # run until done or many iterations
        while not self.done and i <= 10000:
            i += 1
            print("solving... \n Tries: ", i, self.currentState)
            self.changeState()
            self.evaluateState()

    

class Relationship():
    def __init__(self, symbolName, whiteList = None, blackList = None):
        self.symbol = symbolName
        self.whiteList = whiteList
        self.blackList = blackList

    def constraint(self, inputState):
        #find the boats
        boats = []
        badBoats = []
        inputSet = copy.copy(inputState)

        # find all boats
        for item in inputSet:
            if item[1] not in boats:
                boats.append(item[1])
        
        # rearrange to get the contents of each boat
        filteredArray = []
        for boat in boats:
            filteredArray = [array for array in inputSet if array[1] == boat]

            for aBoat in filteredArray:
                # if its yourself, dont check if whitelist or blacklist
                if aBoat[0] == self.symbol:
                    continue
                # if the symbol exists in the boat and any accompanying item is not in the whitelist, add it to list of bad boats
                if self.symbol in [array[0] for array in filteredArray] and aBoat[0] not in self.whiteList:
                    # print(self.symbol, [array[0] for array in filteredArray])
                    # print(aBoat[0], self.whiteList)
                    # print(self.symbol in [array[0] for array in filteredArray], aBoat[0] not in self.whiteList)
                    badBoats.append(aBoat[1])

                # if the symbol exists and is with a blacklisted symbol, add to bad boats
                if self.symbol in [array[0] for array in filteredArray] and aBoat[0] in self.blackList:
                    badBoats.append(aBoat[1])

        for index, set in enumerate(inputSet):
            if set[1] in badBoats:
                inputSet[index][0] = None

        return inputSet




