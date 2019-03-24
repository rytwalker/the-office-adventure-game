# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []
        self.happiness = 1
        self.moved = True

    def init_player(self):
        print('Welcome to Scranton Business Park!')
        print('Is it your first day at Dunder Mifflin?')
        self.name = input('\nWhat\'s your name? \n> ')
        print(f"\nWe're glad to have you here {self.name}!")

    def print_item_names(self):
        if len(self.items) == 0:
            return 'Your inventory is empty.'
        return [item.name for item in self.items]

    def get_item(self, input):
        for i, item in enumerate(self.current_room.items):
            if item.name.lower() == input:
                new_item = self.current_room.items.pop(i)
                self.items.append(new_item)
                item.on_get(self)
                print(f"\nYou picked up a {new_item}\n")
                print(f"Updated inventory: {self.print_item_names()}\n")

    def drop_item(self, input):
        for i, item in enumerate(self.items):
            if item.name.lower() == input:
                self.current_room.items.append(self.items.pop(i))
                item.on_drop(self)
                print(f"Updated inventory: {self.print_item_names()}")

    def __repr__(self):
        return f"Player is in {self.current_room.name} \n Inventory: {self.print_item_names()}"
