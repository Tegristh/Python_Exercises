print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bienvenue sur l'île au trésor.")
print("Vous devez trouver le trésor.") 

choice1 = input('Après avoir marché quelques pas, vous arrivez à un croisement.\n voulez vous suivre le chemin de "gauche"? ou celui de "droite"?\n').lower()
if choice1 != "gauche":
  print("Vos pas vous ont mené dans une clairière ou vous avez rencontré une colonie de chats sauvagements mignons et quelqu'un d'autre à trouvé le trésor pendant que vous succombiez à leurs ronrons")
else:
  choice2 = input("Vous avez emprunté la voie de gauche et avez suivi le chemin jusqu'a arriver en bordure d'un fleuve.\n Allez vous 'attendre' l'arrivée potentielle d'un bateau, ou 'nager' tel un athlète jusqu'a la rive opposée?\n").lower()
  if choice2 != "attendre":
    print("Arrivé au milieux de la traversée, vous avez décidé de vous reposer en prenant appui sur ce qui vous semblait etre un tron d'arbre. En réalité c'etait un crocodile qui vous obligera à faire demi tour, abandonnant au passage vos rèves de richesse")
  else:
    choice3 = input("Vous arrivez devant une sorte de manoir, apparemment vous allez devoir choisir entre 3 portes, une 'rouge', une 'jaune' et une 'bleue'\n").lower()
    if choice3 != "jaune":
      print("un bruit métallique se fait entendre lorsque vous tournez la poignée, probablement un mécanisme vérouillant les autres portes. Vous forcez de tout votre poid contre la porte qui souvre péniblement sur une pièce entièrement vide")
    else:
      print("Vos efforts ont payé, vous voici devant le légendaire trésor de l'île au trésor.")