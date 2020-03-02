print("random team selection".center(80))
from random import choice
player1=input("Enter first player name")
player2=input("Enter second player name")
player3=input("Enter third player name")
player4=input("Enter fourth player name")
player5=input("Enter fifth player name")
player6=input("Enter sixth player name")
player7=input("Enter seventh player name")
player8=input("Enter eight player name")
player9=input("Enter ninth player name")
player10=input("Enter tenth player name")
player11=input("Enter eleventh player name")
player12=input("Enter twelth player name")
players=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11,player12]
teamA=[]
teamB=[]
while len(players)>0:
 playersA=choice(players)
 teamA.append(playersA)
 players.remove(playersA)
 
 playersB=choice(players)
 teamB.append(playersB)
 players.remove(playersB)

print("TeamA is :", teamA)
print("TeamB is :", teamB)