# import statements.
from send_message import send_message
from read_message import read_message
from add_status import add_status
from add_friend import add_friend
from  read_chat import read_chat
from termcolor import colored
import colorama
# start_chat() function definition
def start_chat(name, age, rating):

    colorama.init()
    welcome_message = "Authentication complete. Welcome\n" \
                          "Name : " + name + "\n" \
                          "Age: " + str(age) + "\n" \
                          "Rating: " + str(rating) + "\n"
    print colored(welcome_message,'green')
        # displaying menu for user.

    show_menu = True
    while show_menu:
        menu_choices = "What do you want to do ? \n" \
                       "1.Add status \n" \
                       "2.Add a friend \n" \
                       "3.Send a secret message \n" \
                       "4.Read a secret message \n" \
                       "5.Read chats \n" \
                       "6.Close Application \n"

        result = int(raw_input(menu_choices))

        # validating users input
        if result == 1:
            # action
            current_status_message = add_status()
            print colored("Your Current status is: "+current_status_message,'green')
        elif result == 2:
            # action
            no_of_friends = add_friend()
            print colored("You have %d friends " % (no_of_friends),'green')
        elif(result ==3):
            send_message()
        elif(result ==4):
            read_message()
        elif result==5:
            read_chat()
        elif result == 6:
            # close application
            show_menu = False
        else:
            print colored("Wrong choice. Try again.",'red')