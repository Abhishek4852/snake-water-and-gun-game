import random

l=[[0,1,-1],[-1,0,1],[1,-1,0]]

comchoice = [1,2,3]
user = int(input("enter 1 for snake , 2  for water and 3 for gun "))

com = random.choice(comchoice)
if com == 1:
  print("computer choose snake")

elif com == 2:
  print("computer choose water")

else:
  print("computer choose gun")

result = l[user-1][com-1]

if result == 1:
  print("you win")

elif result == -1:
  print("you lose")

else :
  print("draw")
