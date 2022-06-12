# Author: Executive Levon
# https://execlevon.wixsite.com/malcomstien
import sys
import time
a = 2
b = 0.2
c = 0.08
d = 1

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
time.sleep(a)
print("Play, or not to play, that is the question.")
print()
time.sleep(d)
startGame = input("Start Game (x) Exit (z) ")
if startGame == 'z' or startGame == 'Z':
    print("Suit yourself.")
    exit()
elif startGame == 'x' or startGame == 'X':
    print()
    print()
    print("Great!")
    time.sleep(a)
    print("But before you start... it's important to know your family.")
    print()
    time.sleep(a)
    print()
    print("HECTOR (YOU): TEENAGER, BROTHER NORMAN. (BARD)")
    time.sleep(d)
    print("NORMAN (BROTHER): FARMER/GARDENER, HUSBAND OF EDMUND. (DRUID)")
    time.sleep(d)
    print("EDMUND (GUARDIAN): HOUSEKEEPER, HUSBAND OF NORMAN. (SOURCERER)")
    time.sleep(d)
    print("MYNOR (HOUSEMATE): HELPS AROUND, HAS MANY MAIDENS. (ROUGE)")
    time.sleep(d)
    print("EUSTACE: ???. (?????)")
    time.sleep(d)
    print()
    print()
    Continue = input("Press (x) to continue ")
    if Continue.lower().strip() == 'x':
        print()
        time.sleep(a)
        print("Your name is HECTOR MALCOMSTIEN, and you are 260 years old.")
        time.sleep(a)
        print("Today is Sunday, and your brother always takes you to the fair on Sundays.")
        time.sleep(a)
        print("But in order to go, you must wake up.")
        print()
        time.sleep(a)
        wakeup = input("Wake up(y) / Sleep in(n) ")
        if wakeup.lower().strip() == 'y':
            print()
            time.sleep(a)
            print("You arise from your comfortable bed.")
            time.sleep(a)
            print("You go to the bathroom to brush your teeth and comb your hair. ")
            time.sleep(a)
            print("Feeling fresh and clean on this chilly autumn day, it’s time  to pick out an appropriate outfit.")
            time.sleep(a)
            print("You have two outfits available.")
            time.sleep(a)
            print()
            print("Outfit [1] is a pair of brown overalls with a forest green striped shirt.")
            time.sleep(d)
            print("Outfit [2] a pair of blue jeans and a brown sweater.")
            time.sleep(a)
            print()
            outfit = input("What outfit do you wear? (1 / 2)")
            if outfit.lower().strip() == '1':
                print()
                time.sleep(a)
                print("Very stylish of you!")
                time.sleep(a)
                print("Wearing your favorite outfit makes you feel like you’re ready to concur the day.")
                time.sleep(a)
                print("You can’t do that on an empty stomach, though. Head down to the kitchen to get your breakfast.")
                time.sleep(d)
                print()
                kit = input("Press (k) to enter the kitchen.")
                if kit.lower().strip() == 'k':
                    print()
                    print()
                    time.sleep(a)
                    print("You sit down at the table, and EDMUND sets down your pancakes, along with a cup of orange juice.")
                    time.sleep(a)
                    print(" You submerge the breakfast pastry in honey, topping it with a handful of blueberries.")
                    print()
                    time.sleep(a)
                    s = '“Thank you for making my favorite!” '
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    time.sleep(a)
                    s = '“You’re awfully welcome.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("EDMUND chimes as he prepares his own morning meal.")
                    time.sleep(a)
                    print()
                    s = '“Say, where is brother?” '
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    s = '“NORMAN is outside setting up the carriage to leave. When you’re done eating, you might want to help him.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    s = '“Alrighty.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("You manage to say with a face full of food.")
                    print()
                    print()
                    print('Once you’re done eating, you slip on your shoes before going outside. You run into MYNOR on your way out.')
                    time.sleep(a)
                    print()
                    s = '“Oh hey, are you coming too?”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("He shakes his head in response.")
                    time.sleep(a)
                    print("He usually comes on Sundays, but he must have a date.")
                    time.sleep(a)
                    print("Looks like NORMAN will be selling his crops alone today. You can always help out, of course.")
                else:
                    print("I bet you feel so cool right now.")


            elif outfit.lower().strip() == '2':
                print()
                time.sleep(a)
                print("Very practical of you!")
                time.sleep(a)
                print("Wearing your outside clothes makes you feel like you’re ready to concur the day.")
                time.sleep(a)
                print("You can’t do that on an empty stomach, though. Head down to the kitchen to get your breakfast.")
                print()
                time.sleep(d)
                kit = input("Press (k) to enter the kitchen.")
                if kit.lower().strip() == 'k':
                    print()
                    print()
                    time.sleep(a)
                    print("You sit down at the table, and EDMUND sets down your pancakes, along with a cup of orange juice.")
                    time.sleep(a)
                    print(" You submerge the breakfast pastry in honey, topping it with a handful of blueberries.")
                    print()
                    time.sleep(a)
                    s = '“Thank you for making my favorite!” '
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    time.sleep(a)
                    s = '“You’re awfully welcome.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("EDMUND chimes as he prepares his own morning meal.")
                    time.sleep(a)
                    print()
                    s = '“Say, where is brother?” '
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    s = '“NORMAN is outside setting up the carriage to leave. When you’re done eating, you might want to help him.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print()
                    s = '“Alrighty.”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("You manage to say with a face full of food.")
                    print()
                    print()
                    print('Once you’re done eating, you slip on your shoes before going outside. You run into MYNOR on your way out.')
                    time.sleep(a)
                    print()
                    s = '“Oh hey, are you coming too?”'
                    for character in s:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(b)
                    print()
                    print("He shakes his head in response.")
                    time.sleep(a)
                    print("He usually comes on Sundays, but he must have a date.")
                    time.sleep(a)
                    print("Looks like NORMAN will be selling his crops alone today. You can always help out, of course.")
                else:
                    print("Oh, come on. Follow the damn rules like everyone else.")


        elif wakeup.lower().strip() == 'n':
            print()
            time.sleep(a)
            print("You succumb to your pillow and comforter for just a few more minutes.")
            time.sleep(a)
            print("...")
            print("NORMAN knocks on your door, tempting you with a delicious pancake breakfast that EDMUND is cooking.")
            time.sleep(a)
            print("Now convinced to get up, you sprint to the bathroom to brush your teeth and comb your hair.")
            time.sleep(a)
            print("Not having enough time to pick out an outfit, you grab the one that NORMAN had picked out last night.")
            time.sleep(a)
            print("A pair of blue jeans accompanied with a brown sweater.")
            time.sleep(a)
            print("Hungry, with no time to spare, you rsh your way down to the kitchen for your breakfast. ")
            print()
            time.sleep(d)
            kit = input("Press (k) to enter the kitchen.")
            if kit.lower().strip() == 'k':
                print()
                print()
                time.sleep(a)
                print(
                    "You sit down at the table, and EDMUND sets down your pancakes, along with a cup of orange juice.")
                time.sleep(a)
                print(" You submerge the breakfast pastry in honey, topping it with a handful of blueberries.")
                print()
                time.sleep(a)
                s = '“Thank you for making my favorite!” '
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print()
                time.sleep(a)
                s = '“You’re awfully welcome.”'
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print("EDMUND chimes as he prepares his own morning meal.")
                time.sleep(a)
                print()
                s = '“Say, where is brother?” '
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print()
                s = '“NORMAN is outside setting up the carriage to leave. When you’re done eating, you might want to help him.”'
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print()
                s = '“Alrighty.”'
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print("You manage to say with a face full of food.")
                print()
                print()
                print(
                    'Once you’re done eating, you slip on your shoes before going outside. You run into MYNOR on your way out.')
                time.sleep(a)
                print()
                s = '“Oh hey, are you coming too?”'
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                print("He shakes his head in response.")
                time.sleep(a)
                print("He usually comes on Sundays, but he must have a date.")
                time.sleep(a)
                print("Looks like NORMAN will be selling his crops alone today. You can always help out, of course.")
            else:
                print("Fine, Be a prick.")

    else:
        print("If you're not going to follow the rules, you don't deserve to play. ")
        exit()
