# Jared Harms - IT-140 

def main():  # contains game logic and when called, begins game

    rooms = {
        'Dimrill Gate': {'West': 'First Hall'},
        'First Hall': {'South': 'Great Hall', 'East': 'Dimrill Gate', 'item': 'Axe'},
        'Great Hall': {'North': 'First Hall', 'South': 'Chamber of Mithril',
                       'West': 'Second Hall', 'East': 'Bridge of Khazadum', 'item': 'Narsil'},
        'Second Hall': {'North': 'Throne Room', 'East': 'Great Hall', 'item': 'Sword'},
        'Throne Room': {'South': 'Second Hall', 'item': 'Glamdring'},
        'Bridge of Khazadum': {'North': 'Chamber of Mazarbul', 'West': 'Great Hall', 'item': 'Staff'},
        'Chamber of Mazarbul': {'South': 'Bridge of Khazadum', 'item': 'Bow'},
        'Chamber of Mithril': {'North': 'Great Hall', 'East': 'Dungeon', 'item': 'Sting'},
        'Dungeon': {}
    }  # Define dict 'rooms' to contain available items and directions in each room

    an_words = {'Axe'}  # Create word lists to determine leading word when printing
    a_words = {'Bow', 'Sword', 'Staff'}
    none_words = {'Narsil', 'Glamdring', 'Sting'}

    current_room = 'Dimrill Gate'  # Initialize starting room, save as current_room

    inventory = []  # Initialize inventory as empty list

    act = ''  # Initialize action, save as empty string

    noun = ''  # Initialize noun, save as empty string

    commands = ['go', 'get']  # Define acceptable action words

    def show_instructions():  # when called, Prints game instructions to player

        print("Lord of the Rings: Adventure Game")

        print("Collect all 7 items to win the game or encounter the Balrog and lose")

    def show_moves():  # when called, Prints list of available commands to player

        print("Directional movements: go South, go North, go East, go West")

        print("Add to inventory movement: get 'item name'")

    def show_status():  # when called, Prints player status with current room, inventory, and what is seen in room

        print(f"\nYou are at the {current_room}")

        print(f"Inventory: {inventory}")

        if 'item' in rooms[current_room] and \
                rooms[current_room]['item'] not in inventory:  # Checks if room contains an item that
            # has not yet been picked up - if item has not been picked up

            if rooms[current_room]['item'] in an_words:  # Checks an_word list to determine leading word

                print(f"You see an {rooms[current_room]['item']}")

            elif rooms[current_room]['item'] in none_words:  # Checks none_word list to determine leading word

                print(f"You see {rooms[current_room]['item']}")

            elif rooms[current_room]['item'] in a_words:  # Checks a_word list to determine leading word

                print(f"You see a {rooms[current_room]['item']}")

        print("--------------")

    def add_to_inventory():  # when called, adds a picked up item to the players inventory

        if noun in rooms[current_room]['item']:  # checks to see if selected item in room

            for key, value in rooms[current_room].items():  # evaluates key value pairs in current room

                if noun in value:  # checks to see if noun is a value in current room

                    inventory.append(value)  # adds value 'item' to inventory list

        print(f"{value} added to inventory")

    def reject_move():  # when called, forces player to re-enter input command

        print("Command requires two words\n")

        show_moves()

    show_instructions()  # prints instructions

    show_moves()  # prints list of available commands

    while current_room != 'Dungeon' and len(inventory) < 7:  # repeats while player not in dungeon and doesn't have
        # all items

        show_status()  # prints current status to player

        move = input("Enter your move:\n")  # receives input move from player

        move = move.split()  # splits move into a list of two words

        if len(move) == 2:  # checks to ensure input contains an action and a noun

            act = move[0]  # initializes action as first word in list move

            noun = move[1].title()  # initializes noun as second word in list move

            if act == 'go':  # Checks to determine if player is 'going somewhere'

                if noun.title() in rooms[current_room]:  # checks if cardinal direction movement possible from room

                    print(f"Moving {noun.title()}\n")

                    for key, value in rooms[current_room].items():  # evaluates list of key value pairs in room

                        if noun in key:  # updates value of current_room if cardinal direction is key in room

                            current_room = value

                elif noun.title() not in rooms[current_room]:  # Redirects player if movement direction not available

                    print('The way is shut.... it was made by those who are dead.... and the dead keep it.')

            if act == 'get':  # Checks to see if we are 'getting' an item

                if current_room == 'Dimrill Gate':  # Redirects player if no item in current room

                    print('There are no items in this room')

                elif current_room != 'Dimrill Gate':  # checks that we're in a room with an item in it

                    if noun in rooms[current_room].values() and noun in inventory:  # checks if we already have item

                        print("We've already grabbed that item")

                    elif noun in rooms[current_room].values():  # checks whether selected item in room

                        add_to_inventory()  # adds selected item to inventory

                    elif noun not in rooms[current_room].values():  # redirects player if selected item not in room

                        print("We won't find that item here")

            if act not in commands:  # rejects command if action word is not 'go' or 'get'

                print("Please review the available movements:\n")

                show_moves()  # prints a list of available commands to the user

        if len(move) != 2:  # rejects input if command does not contain an action AND a noun

            reject_move()

        if current_room == 'Dungeon':  # checks current room to lose game if in Dungeon

            print("\nA Balrog of Morgoth approaches... Fly you fools.\nGame over. Thanks for playing.")

        if len(inventory) > 6:  # Checks inventory length to win game if all items collected

            print("\nVictory is yours! You've collected all of the items.\n"
                  "The Orcs won't stand a chance. Thanks for playing.")


main()  # starts game
