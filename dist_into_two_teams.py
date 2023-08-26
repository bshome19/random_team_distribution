import random


players = input("Enter players name: ").split()
# players = ["Rahul", "Sachin", "Sourav", "Virat", "Yuvraj", "DeVillers"]

n = len(players)
team1 = []

for _ in range(n//2):
    idx = random.randint(0, len(players)-1)
    team1.append(players[idx])
    players.remove(players[idx])
    
team2 = players
print("Team1:", team1)
print("Team2:", team2)
