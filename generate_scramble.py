import os
from cube_attributes import (
    edge_speffz, edge_speffz_parity, corner_speffz,
    moves, scrambleLength, getScrambledLetterPositions,
    generateScramble, getLetterArrays, getLetterScheme, createMemo1,
)


letters = getLetterArrays(getLetterScheme(edge_speffz, corner_speffz))
parityLetters = getLetterArrays(getLetterScheme(edge_speffz_parity, corner_speffz))

newScramble = generateScramble(scrambleLength, moves)
simpleScramble = getScrambledLetterPositions(letters, ['U2'])
scrambledPieces = getScrambledLetterPositions(letters, newScramble)

os.system('cls')
edgeMemo1, cornerMemo1 = createMemo1(scrambledPieces)



def pair_join(chars):
    return [''.join(chars[i:i+2]) for i in range(0, len(chars), 2)]


print('----------------------------------------------------------------------------------------------------------------------------------------------')
print('The Following Scramble is: ' + str(newScramble))
print("\nThe edge memo is: " + str(pair_join(edgeMemo1)))
print("\nThe corner memo is: " + str(pair_join(cornerMemo1)))
print('----------------------------------------------------------------------------------------------------------------------------------------------')
