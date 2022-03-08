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
    for i in range(95):
        if list[i] == 'H' and list[i + 1] == 'H' and list[i + 2] == 'H' and list[i + 3] == 'H' and list[i + 4] == 'H' and list[i + 5] == 'H':
            numberOfStreaks += 1
        elif list[i] == 'T' and list[i + 1] == 'T' and list[i + 2] == 'T' and list[i + 3] == 'T' and list[i + 4] == 'T' and list[i + 5] == 'T':
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 10000))
