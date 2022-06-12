# Author: Executive Levon
# https://execlevon.wixsite.com/malcomstien


print()
print()
print("     o-o-o-o-o-o-o-o-o-o-o-o-o-o")
print("     0                         0")
print("     0       MALCOMSTIEN:      0")
print("     0         ECLIPSE         0")
print("     0                         0")
print("     o-o-o-o-o-o-o-o-o-o-o-o-o-o")
print()
print()
print("Play, or not to play, that is the question.")
print()
startGame = input("Start Game (x) Exit (z) ")
if startGame.lower().strip() == 'z':
    print("Suit yourself.")
    exit()
elif startGame.lower().strip() == 'x':
    print()
    print()
    print("Great!")
    print("But before you start... it's important to know your family.")
    print()
    print()
    print("HECTOR (YOU): TEENAGER, BROTHER NORMAN. (BARD)")
    print("NORMAN (BROTHER): FARMER/GARDENER, HUSBAND OF EDMUND. (DRUID)")
    print("EDMUND (GUARDIAN): HOUSEKEEPER, HUSBAND OF NORMAN. (SOURCERER)")
    print("MYNOR (HOUSEMATE): HELPS AROUND, HAS MANY MAIDENS. (ROUGE)")
    print("EUSTACE: ???. (?????)")
    print()
    print()
    Continue = input("Press (x) to continue")
    if Continue.lower().strip() == 'x':
        print()
        print("Your name is HECTOR MALCOMSTIEN, and you are 260 years old.")
        print("Today is Sunday, and your brother always takes you to the fair on Sundays.")
        print("But in order to go, you must wake up.")
    else:
        print("If you're not going to follow the rules, you don't deserve to play.")
        exit()
