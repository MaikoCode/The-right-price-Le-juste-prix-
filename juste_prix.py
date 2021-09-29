import random
import colorama
from colorama import Fore




def entry():

            try:
                print("Your number: ",end='')
                user_num = int(input(Fore.BLUE))
                if user_num <= 0 or user_num > 100:
                    raise Exception()
            except KeyboardInterrupt:
                exit()
            except:
                return entry()
            else:
                return user_num

def main(main_game):

    colorama.init(autoreset=True)

    while main_game:

            score = 10
            random_num = random.randint(1, 100)
            game_continue = True

            user_input = entry()

            while game_continue and score > 0:
                

                if user_input == random_num:
                    print(Fore.GREEN + "Congratulations, your score is " + str(score))
                    game_continue = False
                elif user_input > random_num and score > 1:
                    score -= 1
                    print(Fore.MAGENTA + "The mystery number is smaller, you have {} points left ".format(score))
                    user_input = entry()
                elif user_input < random_num and score > 1:
                    score -= 1
                    print(Fore.MAGENTA + "The mystery number is bigger, you have {} points left".format(score))
                    user_input = entry()
                else:
                    score -= 1
                    print(Fore.RED + "Sorry you lost, you have {} points left".format(score))

            print('*****************************************', end='\n')
            replay_input = input(Fore.YELLOW + "Do you want to replay !!: ")

            if replay_input == 'y':
                main_game = True
            else:
                main_game = False

if __name__ == '__main__':
    colorama.init(autoreset=True)
    print(Fore.BLUE + """___________.__                          .__               .__                .__       .__     __   
\__    ___/|  |__   ____   _____________|__| ____  ____   |__| ______ _______|__| ____ |  |___/  |_ 
  |    |   |  |  \_/ __ \  \____ \_  __ \  |/ ___\/ __ \  |  |/  ___/ \_  __ \  |/ ___\|  |  \   __\
  |    |   |   Y  \  ___/  |  |_> >  | \/  \  \__\  ___/  |  |\___ \   |  | \/  / /_/  >   Y  \  |  
  |____|   |___|  /\___  > |   __/|__|  |__|\___  >___  > |__/____  >  |__|  |__\___  /|___|  /__|  
                \/     \/  |__|                 \/    \/          \/           /_____/      \/       """)
    print("Choose a number between 1 and 100:")
    print("You have 10 points")
    main(True)
        



## By MaikoCode 




