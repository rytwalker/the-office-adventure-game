import os
from termcolor import colored, cprint
from pyfiglet import Figlet
from room import Room
from player import Player
from item import Item
from data.rooms import rooms
from data.items import items
from data.text import text
# from threading import Timer

# Place items in rooms
rooms['fun_run'].items = [items['shirt']]
rooms['lobby'].items = [items['mouse']]
rooms['cafe'].items = [items['map']]
rooms['200'].items = [items['treasure']]


# Main
def try_direction(direction, current_room):
    attribute = direction + '_to'
    directions = {'n': 'North', 's': "South", 'e': "East", 'w': "West"}
    # see if inputted direction is one we can move to
    if hasattr(current_room, attribute):
        cprint(f'Walked {directions[direction]}...', 'blue')
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        cprint('You can\'t go that way. Try a different direction.', 'red')
        return current_room


f = Figlet(font='big')
print(f.renderText('The Office CLI Adventure'))

# Init a new player to play the game
player = Player(rooms['outside'])
player.init_player()

# game loop
while True:
    # Display current room, desc, items
    if player.moved:
        print(player.current_room)

    # User enters a command
    user_input = input('What do you want to do?\n> ').lower().split(' ')

    # hanlde user input with two words
    if len(user_input) == 2:
        # pick up an item
        if user_input[0] == 'get' or user_input[0] == 'take':
            player.moved = False
            player.get_item(user_input[1])
        # drop an item
        elif user_input[0] == 'drop':
            player.moved = False
            player.drop_item(user_input[1])
        # go to a new room
        elif user_input[0] == 'go':
            player.moved = True
            os.system("clear")
            player.current_room = try_direction(
                user_input[1][0], player.current_room)

    # hanlde user input with one word
    elif len(user_input) == 1:
        # quit game
        if user_input[0] == 'q':
            print('Thank you for playing! See you next time!\n')
            break
        # hanlde view inventory
        if user_input[0] == 'i' or user_input[0] == 'inventory':
            player.moved = False
            print(f"inventory: {player.print_item_names()}")
            continue
        # handle help
        if user_input[0] == 'h' or user_input[0] == 'help':
            player.moved = False
            cprint(text['help'], 'yellow')
            continue
        # else handle as direction
        player.moved = True
        os.system("clear")
        player.current_room = try_direction(user_input[0], player.current_room)

    if player.happiness <= 0:
        print(
            'Happiness is too low you lost the will to go on. You lose')
        break
