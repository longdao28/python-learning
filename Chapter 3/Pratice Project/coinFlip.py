import random
numberOfStreaks = 0


for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    list = []
    for i in range(100):
        if random.randint(0,1) == 0:
            list.append('H')
        else:
            list.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.

    sixHeadStreaks = 0
    sixOfTailStreaks = 0

    for f in range(len(list)):
        if list[f] == 'H':
            sixHeadStreaks += 1
            sixOfTailStreaks = 0
            if sixHeadStreaks == 6:
                sixHeadStreaks = 0
                numberOfStreaks += 1
        elif list[f] == 'T':
            sixOfTailStreaks += 1
            sixHeadStreaks = 0
            if sixOfTailStreaks == 6:
                sixOfTailStreaks = 0
                numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
