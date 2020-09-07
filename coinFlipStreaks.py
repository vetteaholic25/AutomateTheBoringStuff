import random
numberOfStreaks = 0
streakLength=6
nExperiment=10000
for experimentNumber in range(nExperiment):
    results=[]
    # Code that creates a list of 100 'heads' or 'tails' values.
    for flips in range(100):
        coinFlip=random.randint(0,1)
        if coinFlip==0:
            results.append('H')
        else:
            results.append('T')


    # Code that checks if there is a streak of 6 heads or tails in a row.
    lastFlip=None
    currentStreak=1
    for coinFlip in results:
        if coinFlip==lastFlip:
            currentStreak+=1
            if currentStreak==streakLength:
                numberOfStreaks+=1
                break
        else:
            currentStreak=1
        lastFlip=coinFlip
print('Chance of streak: %s%%' % (numberOfStreaks*100 / 10000)
