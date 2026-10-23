import random
from tracing_attributes import (
    edge_tracing, edge_tracing_parity, corner_tracing,
    final_order, final_parity_order
)

# Standard 3x3 Speffz letter scheme

corner_speffz = {
    "A": (0,"UBL"),
    "B": (1,"UBR"),
    "C": (2,"UFR"),
    "D": (3,"UFL"),
    "E": (4,"LBU"),
    "F": (5,"LFU"),
    "G": (6,"LFD"),
    "H": (7,"LBD"),
    "I": (8,"FLU"),
    "J": (9,"FRU"),
    "K": (10,"FRD"),
    "L": (11,"FLD"),
    "M": (12,"RFU"),
    "N": (13,"RBU"),
    "O": (14,"RBD"),
    "P": (15,"RFD"),
    "Q": (16,"BRU"),
    "R": (17,"BLU"),
    "S": (18,"BLD"),
    "T": (19,"BRD"),
    "U": (20,"DFL"),
    "V": (21,"DFR"),
    "W": (22,"DBL"),
    "X": (23,"DBR"),
}

edge_speffz_parity = {
    "A": (0,"UB"),
    "C": (1,"UR"),
    "B": (2,"UF"),
    "D": (3,"UL"),
    "E": (4,"LU"),
    "F": (5,"LF"),
    "G": (6,"LD"),
    "H": (7,"LB"),
    "M": (8,"RU"),
    "J": (9,"FR"),
    "K": (10,"FD"),
    "L": (11,"FL"),
    "I": (12,"FU"),
    "N": (13,"RB"),
    "O": (14,"RD"),
    "P": (15,"RF"),
    "Q": (16,"BU"),
    "R": (17,"BL"),
    "S": (18,"BD"),
    "T": (19,"BR"),
    "U": (20,"DF"),
    "V": (21,"DR"),
    "W": (22,"DB"),
    "X": (23,"DL"),
}

edge_speffz = {
    "A": (0,"UB"),
    "B": (1,"UR"),
    "C": (2,"UF"),
    "D": (3,"UL"),
    "E": (4,"LU"),
    "F": (5,"LF"),
    "G": (6,"LD"),
    "H": (7,"LB"),
    "I": (8,"FU"),
    "J": (9,"FR"),
    "K": (10,"FD"),
    "L": (11,"FL"),
    "M": (12,"RU"),
    "N": (13,"RB"),
    "O": (14,"RD"),
    "P": (15,"RF"),
    "Q": (16,"BU"),
    "R": (17,"BL"),
    "S": (18,"BD"),
    "T": (19,"BR"),
    "U": (20,"DF"),
    "V": (21,"DR"),
    "W": (22,"DB"),
    "X": (23,"DL"),
}


def getLetterScheme(edges, corners):
    letterScheme = [edges, corners]
    return letterScheme


def getLetterArrays(letterScheme):
    letters = ([], [])
    for letter in letterScheme[0].keys():
        letters[0].append(letter)
    for letter in letterScheme[1].keys():
        letters[1].append(letter)
    return letters


# Defines how the cube turns, including the face (X, Y, or Z), the face allocation (R, L, D, U, F, B), and the rotation (90 degrees clockwise, anti-clockwise, or 180 degrees)
moves = [
    ['X', 'R', 'R'],
    ['X', 'R', "R'"],
    ['X', 'R', 'R2'],
    ['X', 'L', 'L'],
    ['X', 'L', "L'"],
    ['X', 'L', 'L2'],
    ['Y', 'D', 'D'],
    ['Y', 'D', "D'"],
    ['Y', 'D', 'D2'],
    ['Y', 'U', 'U'],
    ['Y', 'U', "U'"],
    ['Y', 'U', 'U2'],
    ['Z', 'F', 'F'],
    ['Z', 'F', "F'"],
    ['Z', 'F', 'F2'],
    ['Z', 'B', 'B'],
    ['Z', 'B', "B'"],
    ['Z', 'B', 'B2']
]

scrambleLength = 20


def generateScramble(scrambleLength, moves):
    moveSequence = []
    successfulChosenIndexes = []
    while len(moveSequence) < scrambleLength:
        randMoveIndex = random.randint(0, len(moves)-1)
        if len(moveSequence) == 0:
            moveSequence.append(moves[randMoveIndex][2])
            successfulChosenIndexes.append(randMoveIndex)
            continue
        if len(moveSequence) == 1:
            if moves[successfulChosenIndexes[0]][1] != moves[randMoveIndex][1]:
                moveSequence.append(moves[randMoveIndex][2])
                successfulChosenIndexes.append(randMoveIndex)
                continue
        if moves[successfulChosenIndexes[len(moveSequence)-1]][1] == moves[randMoveIndex][1]:
            continue
        if moves[successfulChosenIndexes[len(moveSequence)-2]][0] == moves[successfulChosenIndexes[len(moveSequence)-1]][0]:
            if moves[successfulChosenIndexes[len(moveSequence)-1]][0] == moves[randMoveIndex][0]:
                continue
        moveSequence.append(moves[randMoveIndex][2])
        successfulChosenIndexes.append(randMoveIndex)
        continue
    return moveSequence


def makeRMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[0]
    newEdgeLetterState[1] = currentEdgeLetterState[19]
    newEdgeLetterState[2] = currentEdgeLetterState[2]
    newEdgeLetterState[3] = currentEdgeLetterState[3]
    newEdgeLetterState[4] = currentEdgeLetterState[4]
    newEdgeLetterState[5] = currentEdgeLetterState[5]
    newEdgeLetterState[6] = currentEdgeLetterState[6]
    newEdgeLetterState[7] = currentEdgeLetterState[7]
    newEdgeLetterState[8] = currentEdgeLetterState[8]
    newEdgeLetterState[9] = currentEdgeLetterState[1]
    newEdgeLetterState[10] = currentEdgeLetterState[10]
    newEdgeLetterState[11] = currentEdgeLetterState[11]
    newEdgeLetterState[12] = currentEdgeLetterState[13]
    newEdgeLetterState[13] = currentEdgeLetterState[14]
    newEdgeLetterState[14] = currentEdgeLetterState[15]
    newEdgeLetterState[15] = currentEdgeLetterState[12]
    newEdgeLetterState[16] = currentEdgeLetterState[16]
    newEdgeLetterState[17] = currentEdgeLetterState[17]
    newEdgeLetterState[18] = currentEdgeLetterState[18]
    newEdgeLetterState[19] = currentEdgeLetterState[21]
    newEdgeLetterState[20] = currentEdgeLetterState[20]
    newEdgeLetterState[21] = currentEdgeLetterState[9]
    newEdgeLetterState[22] = currentEdgeLetterState[22]
    newEdgeLetterState[23] = currentEdgeLetterState[23]

    newCornerLetterState[0] = currentCornerLetterState[0]
    newCornerLetterState[1] = currentCornerLetterState[19]
    newCornerLetterState[2] = currentCornerLetterState[16]
    newCornerLetterState[3] = currentCornerLetterState[3]
    newCornerLetterState[4] = currentCornerLetterState[4]
    newCornerLetterState[5] = currentCornerLetterState[5]
    newCornerLetterState[6] = currentCornerLetterState[6]
    newCornerLetterState[7] = currentCornerLetterState[7]
    newCornerLetterState[8] = currentCornerLetterState[8]
    newCornerLetterState[9] = currentCornerLetterState[1]
    newCornerLetterState[10] = currentCornerLetterState[2]
    newCornerLetterState[11] = currentCornerLetterState[11]
    newCornerLetterState[12] = currentCornerLetterState[13]
    newCornerLetterState[13] = currentCornerLetterState[14]
    newCornerLetterState[14] = currentCornerLetterState[15]
    newCornerLetterState[15] = currentCornerLetterState[12]
    newCornerLetterState[16] = currentCornerLetterState[22]
    newCornerLetterState[17] = currentCornerLetterState[17]
    newCornerLetterState[18] = currentCornerLetterState[18]
    newCornerLetterState[19] = currentCornerLetterState[21]
    newCornerLetterState[20] = currentCornerLetterState[20]
    newCornerLetterState[21] = currentCornerLetterState[9]
    newCornerLetterState[22] = currentCornerLetterState[10]
    newCornerLetterState[23] = currentCornerLetterState[23]

    return newEdgeLetterState, newCornerLetterState

def makeUMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[1]
    newEdgeLetterState[1] = currentEdgeLetterState[2]
    newEdgeLetterState[2] = currentEdgeLetterState[3]
    newEdgeLetterState[3] = currentEdgeLetterState[0]
    newEdgeLetterState[4] = currentEdgeLetterState[16]
    newEdgeLetterState[5] = currentEdgeLetterState[5]
    newEdgeLetterState[6] = currentEdgeLetterState[6]
    newEdgeLetterState[7] = currentEdgeLetterState[7]
    newEdgeLetterState[8] = currentEdgeLetterState[4]
    newEdgeLetterState[9] = currentEdgeLetterState[9]
    newEdgeLetterState[10] = currentEdgeLetterState[10]
    newEdgeLetterState[11] = currentEdgeLetterState[11]
    newEdgeLetterState[12] = currentEdgeLetterState[8]
    newEdgeLetterState[13] = currentEdgeLetterState[13]
    newEdgeLetterState[14] = currentEdgeLetterState[14]
    newEdgeLetterState[15] = currentEdgeLetterState[15]
    newEdgeLetterState[16] = currentEdgeLetterState[12]
    newEdgeLetterState[17] = currentEdgeLetterState[17]
    newEdgeLetterState[18] = currentEdgeLetterState[18]
    newEdgeLetterState[19] = currentEdgeLetterState[19]
    newEdgeLetterState[20] = currentEdgeLetterState[20]
    newEdgeLetterState[21] = currentEdgeLetterState[21]
    newEdgeLetterState[22] = currentEdgeLetterState[22]
    newEdgeLetterState[23] = currentEdgeLetterState[23]

    newCornerLetterState[0] = currentCornerLetterState[1]
    newCornerLetterState[1] = currentCornerLetterState[2]
    newCornerLetterState[2] = currentCornerLetterState[3]
    newCornerLetterState[3] = currentCornerLetterState[0]
    newCornerLetterState[4] = currentCornerLetterState[16]
    newCornerLetterState[5] = currentCornerLetterState[17]
    newCornerLetterState[6] = currentCornerLetterState[6]
    newCornerLetterState[7] = currentCornerLetterState[7]
    newCornerLetterState[8] = currentCornerLetterState[4]
    newCornerLetterState[9] = currentCornerLetterState[5]
    newCornerLetterState[10] = currentCornerLetterState[10]
    newCornerLetterState[11] = currentCornerLetterState[11]
    newCornerLetterState[12] = currentCornerLetterState[8]
    newCornerLetterState[13] = currentCornerLetterState[9]
    newCornerLetterState[14] = currentCornerLetterState[14]
    newCornerLetterState[15] = currentCornerLetterState[15]
    newCornerLetterState[16] = currentCornerLetterState[12]
    newCornerLetterState[17] = currentCornerLetterState[13]
    newCornerLetterState[18] = currentCornerLetterState[18]
    newCornerLetterState[19] = currentCornerLetterState[19]
    newCornerLetterState[20] = currentCornerLetterState[20]
    newCornerLetterState[21] = currentCornerLetterState[21]
    newCornerLetterState[22] = currentCornerLetterState[22]
    newCornerLetterState[23] = currentCornerLetterState[23]

    return newEdgeLetterState, newCornerLetterState

def makeFMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[0]
    newEdgeLetterState[1] = currentEdgeLetterState[1]
    newEdgeLetterState[2] = currentEdgeLetterState[15]
    newEdgeLetterState[3] = currentEdgeLetterState[3]
    newEdgeLetterState[4] = currentEdgeLetterState[4]
    newEdgeLetterState[5] = currentEdgeLetterState[2]
    newEdgeLetterState[6] = currentEdgeLetterState[6]
    newEdgeLetterState[7] = currentEdgeLetterState[7]
    newEdgeLetterState[8] = currentEdgeLetterState[9]
    newEdgeLetterState[9] = currentEdgeLetterState[10]
    newEdgeLetterState[10] = currentEdgeLetterState[11]
    newEdgeLetterState[11] = currentEdgeLetterState[8]
    newEdgeLetterState[12] = currentEdgeLetterState[12]
    newEdgeLetterState[13] = currentEdgeLetterState[13]
    newEdgeLetterState[14] = currentEdgeLetterState[14]
    newEdgeLetterState[15] = currentEdgeLetterState[20]
    newEdgeLetterState[16] = currentEdgeLetterState[16]
    newEdgeLetterState[17] = currentEdgeLetterState[17]
    newEdgeLetterState[18] = currentEdgeLetterState[18]
    newEdgeLetterState[19] = currentEdgeLetterState[19]
    newEdgeLetterState[20] = currentEdgeLetterState[5]
    newEdgeLetterState[21] = currentEdgeLetterState[21]
    newEdgeLetterState[22] = currentEdgeLetterState[22]
    newEdgeLetterState[23] = currentEdgeLetterState[23]

    newCornerLetterState[0] = currentCornerLetterState[0]
    newCornerLetterState[1] = currentCornerLetterState[1]
    newCornerLetterState[2] = currentCornerLetterState[15]
    newCornerLetterState[3] = currentCornerLetterState[12]
    newCornerLetterState[4] = currentCornerLetterState[4]
    newCornerLetterState[5] = currentCornerLetterState[2]
    newCornerLetterState[6] = currentCornerLetterState[3]
    newCornerLetterState[7] = currentCornerLetterState[7]
    newCornerLetterState[8] = currentCornerLetterState[9]
    newCornerLetterState[9] = currentCornerLetterState[10]
    newCornerLetterState[10] = currentCornerLetterState[11]
    newCornerLetterState[11] = currentCornerLetterState[8]
    newCornerLetterState[12] = currentCornerLetterState[21]
    newCornerLetterState[13] = currentCornerLetterState[13]
    newCornerLetterState[14] = currentCornerLetterState[14]
    newCornerLetterState[15] = currentCornerLetterState[20]
    newCornerLetterState[16] = currentCornerLetterState[16]
    newCornerLetterState[17] = currentCornerLetterState[17]
    newCornerLetterState[18] = currentCornerLetterState[18]
    newCornerLetterState[19] = currentCornerLetterState[19]
    newCornerLetterState[20] = currentCornerLetterState[5]
    newCornerLetterState[21] = currentCornerLetterState[6]
    newCornerLetterState[22] = currentCornerLetterState[22]
    newCornerLetterState[23] = currentCornerLetterState[23]

    return newEdgeLetterState, newCornerLetterState

def makeLMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[0]
    newEdgeLetterState[1] = currentEdgeLetterState[1]
    newEdgeLetterState[2] = currentEdgeLetterState[2]
    newEdgeLetterState[3] = currentEdgeLetterState[11]
    newEdgeLetterState[4] = currentEdgeLetterState[5]
    newEdgeLetterState[5] = currentEdgeLetterState[6]
    newEdgeLetterState[6] = currentEdgeLetterState[7]
    newEdgeLetterState[7] = currentEdgeLetterState[4]
    newEdgeLetterState[8] = currentEdgeLetterState[8]
    newEdgeLetterState[9] = currentEdgeLetterState[9]
    newEdgeLetterState[10] = currentEdgeLetterState[10]
    newEdgeLetterState[11] = currentEdgeLetterState[23]
    newEdgeLetterState[12] = currentEdgeLetterState[12]
    newEdgeLetterState[13] = currentEdgeLetterState[13]
    newEdgeLetterState[14] = currentEdgeLetterState[14]
    newEdgeLetterState[15] = currentEdgeLetterState[15]
    newEdgeLetterState[16] = currentEdgeLetterState[16]
    newEdgeLetterState[17] = currentEdgeLetterState[3]
    newEdgeLetterState[18] = currentEdgeLetterState[18]
    newEdgeLetterState[19] = currentEdgeLetterState[19]
    newEdgeLetterState[20] = currentEdgeLetterState[20]
    newEdgeLetterState[21] = currentEdgeLetterState[21]
    newEdgeLetterState[22] = currentEdgeLetterState[22]
    newEdgeLetterState[23] = currentEdgeLetterState[17]

    newCornerLetterState[0] = currentCornerLetterState[8]
    newCornerLetterState[1] = currentCornerLetterState[1]
    newCornerLetterState[2] = currentCornerLetterState[2]
    newCornerLetterState[3] = currentCornerLetterState[11]
    newCornerLetterState[4] = currentCornerLetterState[5]
    newCornerLetterState[5] = currentCornerLetterState[6]
    newCornerLetterState[6] = currentCornerLetterState[7]
    newCornerLetterState[7] = currentCornerLetterState[4]
    newCornerLetterState[8] = currentCornerLetterState[20]
    newCornerLetterState[9] = currentCornerLetterState[9]
    newCornerLetterState[10] = currentCornerLetterState[10]
    newCornerLetterState[11] = currentCornerLetterState[23]
    newCornerLetterState[12] = currentCornerLetterState[12]
    newCornerLetterState[13] = currentCornerLetterState[13]
    newCornerLetterState[14] = currentCornerLetterState[14]
    newCornerLetterState[15] = currentCornerLetterState[15]
    newCornerLetterState[16] = currentCornerLetterState[16]
    newCornerLetterState[17] = currentCornerLetterState[3]
    newCornerLetterState[18] = currentCornerLetterState[0]
    newCornerLetterState[19] = currentCornerLetterState[19]
    newCornerLetterState[20] = currentCornerLetterState[18]
    newCornerLetterState[21] = currentCornerLetterState[21]
    newCornerLetterState[22] = currentCornerLetterState[22]
    newCornerLetterState[23] = currentCornerLetterState[17]

    return newEdgeLetterState, newCornerLetterState

def makeDMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[0]
    newEdgeLetterState[1] = currentEdgeLetterState[1]
    newEdgeLetterState[2] = currentEdgeLetterState[2]
    newEdgeLetterState[3] = currentEdgeLetterState[3]
    newEdgeLetterState[4] = currentEdgeLetterState[4]
    newEdgeLetterState[5] = currentEdgeLetterState[5]
    newEdgeLetterState[6] = currentEdgeLetterState[10]
    newEdgeLetterState[7] = currentEdgeLetterState[7]
    newEdgeLetterState[8] = currentEdgeLetterState[8]
    newEdgeLetterState[9] = currentEdgeLetterState[9]
    newEdgeLetterState[10] = currentEdgeLetterState[14]
    newEdgeLetterState[11] = currentEdgeLetterState[11]
    newEdgeLetterState[12] = currentEdgeLetterState[12]
    newEdgeLetterState[13] = currentEdgeLetterState[13]
    newEdgeLetterState[14] = currentEdgeLetterState[18]
    newEdgeLetterState[15] = currentEdgeLetterState[15]
    newEdgeLetterState[16] = currentEdgeLetterState[16]
    newEdgeLetterState[17] = currentEdgeLetterState[17]
    newEdgeLetterState[18] = currentEdgeLetterState[6]
    newEdgeLetterState[19] = currentEdgeLetterState[19]
    newEdgeLetterState[20] = currentEdgeLetterState[21]
    newEdgeLetterState[21] = currentEdgeLetterState[22]
    newEdgeLetterState[22] = currentEdgeLetterState[23]
    newEdgeLetterState[23] = currentEdgeLetterState[20]

    newCornerLetterState[0] = currentCornerLetterState[0]
    newCornerLetterState[1] = currentCornerLetterState[1]
    newCornerLetterState[2] = currentCornerLetterState[2]
    newCornerLetterState[3] = currentCornerLetterState[3]
    newCornerLetterState[4] = currentCornerLetterState[4]
    newCornerLetterState[5] = currentCornerLetterState[5]
    newCornerLetterState[6] = currentCornerLetterState[10]
    newCornerLetterState[7] = currentCornerLetterState[11]
    newCornerLetterState[8] = currentCornerLetterState[8]
    newCornerLetterState[9] = currentCornerLetterState[9]
    newCornerLetterState[10] = currentCornerLetterState[14]
    newCornerLetterState[11] = currentCornerLetterState[15]
    newCornerLetterState[12] = currentCornerLetterState[12]
    newCornerLetterState[13] = currentCornerLetterState[13]
    newCornerLetterState[14] = currentCornerLetterState[18]
    newCornerLetterState[15] = currentCornerLetterState[19]
    newCornerLetterState[16] = currentCornerLetterState[16]
    newCornerLetterState[17] = currentCornerLetterState[17]
    newCornerLetterState[18] = currentCornerLetterState[6]
    newCornerLetterState[19] = currentCornerLetterState[7]
    newCornerLetterState[20] = currentCornerLetterState[21]
    newCornerLetterState[21] = currentCornerLetterState[22]
    newCornerLetterState[22] = currentCornerLetterState[23]
    newCornerLetterState[23] = currentCornerLetterState[20]

    return newEdgeLetterState, newCornerLetterState

def makeBMove(currentEdgeLetterState, currentCornerLetterState):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24

    newEdgeLetterState[0] = currentEdgeLetterState[7]
    newEdgeLetterState[1] = currentEdgeLetterState[1]
    newEdgeLetterState[2] = currentEdgeLetterState[2]
    newEdgeLetterState[3] = currentEdgeLetterState[3]
    newEdgeLetterState[4] = currentEdgeLetterState[4]
    newEdgeLetterState[5] = currentEdgeLetterState[5]
    newEdgeLetterState[6] = currentEdgeLetterState[6]
    newEdgeLetterState[7] = currentEdgeLetterState[22]
    newEdgeLetterState[8] = currentEdgeLetterState[8]
    newEdgeLetterState[9] = currentEdgeLetterState[9]
    newEdgeLetterState[10] = currentEdgeLetterState[10]
    newEdgeLetterState[11] = currentEdgeLetterState[11]
    newEdgeLetterState[12] = currentEdgeLetterState[12]
    newEdgeLetterState[13] = currentEdgeLetterState[0]
    newEdgeLetterState[14] = currentEdgeLetterState[14]
    newEdgeLetterState[15] = currentEdgeLetterState[15]
    newEdgeLetterState[16] = currentEdgeLetterState[17]
    newEdgeLetterState[17] = currentEdgeLetterState[18]
    newEdgeLetterState[18] = currentEdgeLetterState[19]
    newEdgeLetterState[19] = currentEdgeLetterState[16]
    newEdgeLetterState[20] = currentEdgeLetterState[20]
    newEdgeLetterState[21] = currentEdgeLetterState[21]
    newEdgeLetterState[22] = currentEdgeLetterState[13]
    newEdgeLetterState[23] = currentEdgeLetterState[23]

    newCornerLetterState[0] = currentCornerLetterState[7]
    newCornerLetterState[1] = currentCornerLetterState[4]
    newCornerLetterState[2] = currentCornerLetterState[2]
    newCornerLetterState[3] = currentCornerLetterState[3]
    newCornerLetterState[4] = currentCornerLetterState[23]
    newCornerLetterState[5] = currentCornerLetterState[5]
    newCornerLetterState[6] = currentCornerLetterState[6]
    newCornerLetterState[7] = currentCornerLetterState[22]
    newCornerLetterState[8] = currentCornerLetterState[8]
    newCornerLetterState[9] = currentCornerLetterState[9]
    newCornerLetterState[10] = currentCornerLetterState[10]
    newCornerLetterState[11] = currentCornerLetterState[11]
    newCornerLetterState[12] = currentCornerLetterState[12]
    newCornerLetterState[13] = currentCornerLetterState[0]
    newCornerLetterState[14] = currentCornerLetterState[1]
    newCornerLetterState[15] = currentCornerLetterState[15]
    newCornerLetterState[16] = currentCornerLetterState[17]
    newCornerLetterState[17] = currentCornerLetterState[18]
    newCornerLetterState[18] = currentCornerLetterState[19]
    newCornerLetterState[19] = currentCornerLetterState[16]
    newCornerLetterState[20] = currentCornerLetterState[20]
    newCornerLetterState[21] = currentCornerLetterState[21]
    newCornerLetterState[22] = currentCornerLetterState[13]
    newCornerLetterState[23] = currentCornerLetterState[14]

    return newEdgeLetterState, newCornerLetterState

def moveImpact(currentEdgeLetterState, currentCornerLetterState, move):
    newEdgeLetterState = [None]*24
    newCornerLetterState = [None]*24
    if (move == 'R'):
        newEdgeLetterState, newCornerLetterState = makeRMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeRMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeRMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'R2'):
        newEdgeLetterState, newCornerLetterState = makeRMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeRMove(newEdgeLetterState, newCornerLetterState)
    if (move == "R'"):
        newEdgeLetterState, newCornerLetterState = makeRMove(currentEdgeLetterState, currentCornerLetterState)
    if (move == 'U'):
        newEdgeLetterState, newCornerLetterState = makeUMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeUMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeUMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'U2'):
        newEdgeLetterState, newCornerLetterState = makeUMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeUMove(newEdgeLetterState, newCornerLetterState)
    if (move == "U'"):
        newEdgeLetterState, newCornerLetterState = makeUMove(currentEdgeLetterState, currentCornerLetterState)
    if (move == 'F'):
        newEdgeLetterState, newCornerLetterState = makeFMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeFMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeFMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'F2'):
        newEdgeLetterState, newCornerLetterState = makeFMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeFMove(newEdgeLetterState, newCornerLetterState)
    if (move == "F'"):
        newEdgeLetterState, newCornerLetterState = makeFMove(currentEdgeLetterState, currentCornerLetterState)
    if (move == 'L'):
        newEdgeLetterState, newCornerLetterState = makeLMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeLMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeLMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'L2'):
        newEdgeLetterState, newCornerLetterState = makeLMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeLMove(newEdgeLetterState, newCornerLetterState)
    if (move == "L'"):
        newEdgeLetterState, newCornerLetterState = makeLMove(currentEdgeLetterState, currentCornerLetterState)
    if (move == 'D'):
        newEdgeLetterState, newCornerLetterState = makeDMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeDMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeDMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'D2'):
        newEdgeLetterState, newCornerLetterState = makeDMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeDMove(newEdgeLetterState, newCornerLetterState)
    if (move == "D'"):
        newEdgeLetterState, newCornerLetterState = makeDMove(currentEdgeLetterState, currentCornerLetterState)
    if (move == 'B'):
        newEdgeLetterState, newCornerLetterState = makeBMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeBMove(newEdgeLetterState, newCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeBMove(newEdgeLetterState, newCornerLetterState)
    if (move == 'B2'):
        newEdgeLetterState, newCornerLetterState = makeBMove(currentEdgeLetterState, currentCornerLetterState)
        newEdgeLetterState, newCornerLetterState = makeBMove(newEdgeLetterState, newCornerLetterState)
    if (move == "B'"):
        newEdgeLetterState, newCornerLetterState = makeBMove(currentEdgeLetterState, currentCornerLetterState)
    return newEdgeLetterState, newCornerLetterState

def getScrambledLetterPositions(letters, scramble):
    edges = letters[0]
    corners = letters[1]
    for move in scramble:
        edges, corners = moveImpact(edges, corners, move)
    return edges, corners

def getSolvedEdges(edges, scrambledEdges):
    solvedEdges = []
    for i in range(len(scrambledEdges)):
        if edges[i] == scrambledEdges[i]:
            solvedEdges.append(scrambledEdges[i])
    return solvedEdges

def getSolvedCorners(corners, scrambledCorners):
    solvedCorners = []
    for i in range(len(scrambledCorners)):
        if corners[i] == scrambledCorners[i]:
            solvedCorners.append(scrambledCorners[i])
    return solvedCorners

def getSolvedPieces(pieces, scrambledPieces):
    solvedEdges = getSolvedEdges(pieces[0], scrambledPieces[0])
    solvedCorners = getSolvedCorners(pieces[1], scrambledPieces[1])
    return solvedEdges, solvedCorners

edgePieceLocations = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 4,
    'G': 5,
    'H': 6,
    'I': 2,
    'J': 7,
    'K': 8,
    'L': 4,
    'M': 1,
    'N': 9,
    'O': 10,
    'P': 7,
    'Q': 0,
    'R': 6,
    'S': 11,
    'T': 9,
    'U': 8,
    'V': 10,
    'W': 11,
    'X': 5
}

edgePieceLocationsParity = {
    'A': 0,
    'C': 1,
    'B': 2,
    'D': 3,
    'E': 3,
    'F': 4,
    'G': 5,
    'H': 6,
    'M': 2,
    'J': 7,
    'K': 8,
    'L': 4,
    'I': 1,
    'N': 9,
    'O': 10,
    'P': 7,
    'Q': 0,
    'R': 6,
    'S': 11,
    'T': 9,
    'U': 8,
    'V': 10,
    'W': 11,
    'X': 5
}

cornerPieceLocations = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 0,
    'F': 3,
    'G': 4,
    'H': 5,
    'I': 3,
    'J': 2,
    'K': 6,
    'L': 4,
    'M': 2,
    'N': 1,
    'O': 7,
    'P': 6,
    'Q': 1,
    'R': 0,
    'S': 5,
    'T': 7,
    'U': 4,
    'V': 6,
    'W': 7,
    'X': 5
}

def createMemo1(scrambledPieces):
    #First solve corners to check for parity
    cornerMemo = []
    solvedCornerPieces = set()
    finalEdgeTracing = edge_tracing
    final_edge_speffz = edge_speffz
    correctEdgeOrder = final_order
    correctCornerOrder = final_order
    finalEdgeLocations = edgePieceLocations
    finalCornerLocations = cornerPieceLocations
    solvedCorners = getSolvedCorners(correctCornerOrder, scrambledPieces[1])
    if solvedCorners:
        for solvedCorner in solvedCorners:
            solvedCornerPieces.add(finalCornerLocations[solvedCorner])
    for corner in corner_tracing:
        cornerBuffer = scrambledPieces[1][corner[2]]
        if corner[1] not in solvedCornerPieces:
            cornerMemo.append(corner[0])
            for letter in ['C', 'J', 'M']:
                if letter in cornerMemo:
                    cornerMemo.remove(letter)
        while corner[1] not in solvedCornerPieces:
            cornerMemo.append(cornerBuffer)
            solvedCornerPieces.add(finalCornerLocations[cornerBuffer])
            cornerBuffer = scrambledPieces[1][corner_speffz[cornerBuffer][0]]
    for letter in ['C', 'J', 'M']:
        if letter in cornerMemo:
            cornerMemo.remove(letter)
    parity = haveParity(cornerMemo)
    if parity:
        cornerMemo.append('B')
        correctEdgeOrder = final_parity_order
        finalEdgeLocations = edgePieceLocationsParity
        finalEdgeTracing = edge_tracing_parity
        final_edge_speffz = edge_speffz_parity
    # Now solve for edges (based on corner parity)
    edgeMemo = []
    solvedEdgePieces = set()
    solvedEdges = getSolvedEdges(correctEdgeOrder, scrambledPieces[0])
    if solvedEdges:
        for solvedEdge in solvedEdges:
            solvedEdgePieces.add(finalEdgeLocations[solvedEdge])
    for edge in finalEdgeTracing:
        edgeBuffer = scrambledPieces[0][edge[2]]
        if edge[1] not in solvedEdgePieces:
            edgeMemo.append(edge[0])
            for letter in ['K', 'U']:
                if letter in edgeMemo:
                    edgeMemo.remove(letter)
        while edge[1] not in solvedEdgePieces:
            edgeMemo.append(edgeBuffer)
            solvedEdgePieces.add(finalEdgeLocations[edgeBuffer])
            edgeBuffer = scrambledPieces[0][final_edge_speffz[edgeBuffer][0]]
    for letter in ['K', 'U']:
        if letter in edgeMemo:
            edgeMemo.remove(letter)
    if parity:
        edgeMemo = edgeMemoLetterSwaps(edgeMemo)
    if cornerMemo[-2:] == ['B', 'B']:
        cornerMemo = cornerMemo[:-2]
    return parity, edgeMemo, cornerMemo


def haveParity(cornerMemo):
    return len(cornerMemo)%2 == 1



def edgeMemoLetterSwaps(edgeMemo):
    return ['C' if letter == 'B' else 'B' if letter == 'C' else 'M' if letter == 'I' else 'I' if letter == 'M' else letter for letter in edgeMemo]
