choices = {1:"Rock",
           2:"Paper",
           3:"Scissors"}
import random
Cchoice = random.choice(list(choices.keys()))
print(" Wellcome in this mini game,You will play against computer (Rock,Paper,Scissors)")
print("Note:just choose the number you dont need to write the whole word =)\n")
def error() :
  print("You didnt chose a number !!")
  print("Try again..")
def error2 () :
  print("you didnt chouse a number in [1.2.3]")
  print("just enter one of this numbers !")
def rest() :
  Uchoice = input("Chose a Number : \n[1]Rock\n[2]Paper\n[3]Scissors\n==>")
  return Uchoice
while True :
  Uchoice = rest()
  try :
    Uchoice = float(Uchoice)
  except ValueError : 
    error()
    continue
  if Uchoice not in [1,2,3] :
    error2()
    continue
  else :
    break
if Cchoice == Uchoice :
  print("You Chouse ==> " + choices[Uchoice])
  print ("The PC chose ==> " + choices[Cchoice])
  print('It is draw !!')
elif Uchoice == Cchoice + 1 :
  print("You chose ==> " + choices[Uchoice])
  print("The PC chose ==> " + choices[Cchoice])
  print(" You Won !! ")
else:
  print("You chose ==> " + choices[Uchoice])
  print("The PC chose ==> " + choices[Cchoice])
  print("You Lose !!")





