from itertools import combinations
completionTime = [75,45,30,35,30,15,60,90,20,10]
payOutRate = [250,280,150,120,200,100,300,350,110,90]
game = ['PacMan','Speed Racer','Pump It Up','Space Invaders','Mario Bros','Mortal Kombat','Atari Breakout','Super Tetris','Star Wars','Street Fighter II']
targetTime = 120
def timeCombinations(completionTime,targetTime):
    result = [seq for i in range(len(completionTime), 0, -1) for seq in combinations(completionTime, i) if sum(seq) <= targetTime]
    payOutCombinations(result,payOutRate)

def payOutCombinations(result,payOutRate):
    

timeCombinations(completionTime,targetTime)