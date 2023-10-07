#Define the player class
class Player:
 def play(self):
   print("The player is playing cricket.") 
#Define the Batsman class,derived from player
class Batsman(Player): 
 def play(self):
   print("The batsman is batting.") #Define the bowler class,derived from player
class Bowler(Player):
 def play(self):
   print("The bowler is bowling.")
#create object of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()
#Call the play()method for each object
batsman.play()
bowler.play()