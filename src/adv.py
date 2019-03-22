from room import Room
from player import Player
from item import Item
from data.rooms import rooms
from data.items import items
# from threading import Timer

# Place items in rooms
rooms['fun_run'].items = [items['shirt']]
rooms['lobby'].items = [items['mouse']]
rooms['cafe'].items = [items['map']]
rooms['200'].items = [items['treasure']]


# Main
def try_direction(direction, current_room):
    attribute = direction + '_to'
    # see if inputted direction is one we can move to
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        print('You can\'t go that way. Try a different direction.')
        return current_room

# Make a new player object that is currently in the 'outside' room.


# Init a new player to play the game
player = Player(rooms['outside'])
print('Welcome to Scranton Business Park!')
print('Is it your first day at Dunder Mifflin?')
player.name = input('What\'s your name? \n> ')
print(f"We're glad to have you here {player.name}!")

# game loop
while True:
    # Display current room, desc, items
    print(player.current_room)

    # User enters a command
    user_input = input('What do you want to do?\n> ').lower().split(' ')

    # hanlde user input with two words
    if len(user_input) == 2:
        # pick up an item
        if user_input[0] == 'get' or user_input[0] == 'take':
            player.get_item(user_input[1])
        # drop an item
        elif user_input[0] == 'drop':
            player.drop_item(user_input[1])
        # go to a new room
        elif user_input[0] == 'go':
            player.current_room = try_direction(
                user_input[1][0], player.current_room)

    # hanlde user input with one word
    elif len(user_input) == 1:
        # quit game
        if user_input[0] == 'q':
            print('You left the game, game over!')
            break
        # hanlde view inventory
        if user_input[0] == 'i' or user_input[0] == 'inventory':
            print(f"inventory: {player.print_item_names()}")
            continue
        # else handle as direction
        player.current_room = try_direction(user_input[0], player.current_room)

    if player.happiness <= 0:
        print(
            'Happiness is too low you lost the will to go on. You lose')
        break
