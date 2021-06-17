import time,os,sys
from colorama import Fore, Back, Style

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def clearScreen():
  os.system("clear")

while True: 
    answer = input('Would you like to play a game? (yes/no) \n ')
    if answer.lower().strip() == "yes":
        print('Pickup your axe, bravewarrior! \n')

        answer = input('Which route do you prefer choosing? (left/right) ').lower().strip()
        if answer == "left":
            print(Fore.LIGHTBLUE_EX + 'Omg you have reached the river and chosen a longer route \n')
            print(Style.RESET_ALL)
            print('Make a boat from the wood lying around \n')
            time.sleep(5)
            print('Boat has been constructed')
            print('Get into the boat and sail it \n')
            time.sleep()
            answer = input('Type s for sailing the boat \n').lower().strip()
            if answer == 's':
                time.sleep(4)
                print('Boat has reached the shore \n')
            else:
                print(Fore.BLUE + 'Boat has been drowned and you are dead' + 'U+2620')
                time.sleep(1)  
                typingPrint("Good bye!\n")
                typingPrint("This screen will clear itself in 3..")
                time.sleep(1)
                typingPrint("2..")
                time.sleep(1)
                typingPrint("1..")
                time.sleep(1)
                clearScreen()
            
        elif answer == "right":
            print('Kill the monster'+'\n')
            time.sleep(2)
            print(Fore.RED + 'Monster has been annihilated')
            print(Style.RESET_ALL)
            print(Fore.GREEN + 'The monster was a normal human being that was turned into a demon by a curse')
            print(Style.RESET_ALL)
            
    else:
        print('That\'s bad, lets play some other day')
        break