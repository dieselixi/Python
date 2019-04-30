# OgreAttack.py
# Colin kee
# 2018-09-27

import random ,time

done = False
ogreHealth = 10
playerHealth = 6

while not done:
    print("Current health: Ogre ({0}), You ({1})".format(ogreHealth,playerHealth))
    playerAttack = random.randint(1,2)
    if playerAttack == 2:
        playerHit = random.randint(1,2)
        print("You hit the ogre and did {0} point(s) of damage".format(playerHit))
        ogreHealth -= playerHit
    else:
        print("Your attack missed the ogre.")

    if ogreHealth > 0:
        ogreAttack = random.randint(1,3)
        if ogreAttack == 3:
            ogreHit = random.randint(1,3)
            print("The ogre hit you and did {0} point(s) of damage".format(ogreHit))
            playerHealth -= ogreHit
        else:
            print("You have evaded the ogre's attack.")
    if ogreHealth <= 0:
        print("You have slain the ogre and live to fight another day.")
        done = True
    elif playerHealth <= 0:
        print("You have been slain")
        done = True
    else:
        print()
        time.sleep(2)
