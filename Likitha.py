from itertools import combinations
dict = {75:250,45:280,35:120,30:200,15:100,60:300,90:350,20:110,10:90}
dict2 = {'PacMan': 250,'speed racer':280,'pump it up':120,'space invaders':200,'mortal kombat':100,'Atari Breakout':300,'Super tetris':350,'Star wars':110,'Street fighter II':90}
numbers = (dict.keys())

result = [seq for i in range(len(numbers), 0, -1) for seq in combinations(numbers, i) if sum(seq) <= 120]
result2 = []
for i in result:
    temp = []
    for j in list(i):
        temp.append(dict[j])
    result2.append(temp)


maximumSumList = (max(result2,key=sum))
def get_key(val):
    for key, value in dict2.items():
         if val == value:
             return key
for i in maximumSumList:
    print(get_key(i))