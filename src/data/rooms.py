from room import Room
rooms = {
    'outside':  Room("Outside Scranton Business Park",
                     '''1725 Slouh Ave. Scranton, PA 45342. North of you, is the main enterance'''),
    'fun_run':  Room("""Michael Scott's Dunder Mifflin Scranton Meredith Palmer Memorial Celebrity Rabies Awareness Pro-Am Fun Run Race For The Cure""",
                     "A race to cure rabbies."),

    'lobby':    Room("Lobby", """To the west is Hank's cafe. To the north is a
    hallway that leads to the 100 level suite buildings.
    To the east is the stairs that lead to
    The Second Floor Hallway."""),

    'cafe': Room("Hank's Cafe", """A steep cliff appears before you, falling
    into the darkness. Back to the east is the lobby"""),

    'hallway_one':   Room("First Floor Hallway", """To the west is Suite 100,
    To the east is Suite 110, to the north is Suite 120,
    and the lobby is to the south"""),

    'hallway_two':   Room("Second Floor Hallway", """To the west is Suite 200,
    To the east is Suite 210,
    To the north is the stairway to Hallway Three
    and the stairs to the First Floor Hallway to the south"""),

    'hallway_three':   Room("Third Floor Hallway", """To the west is Suite 300,
    To the east is Suite 302, the hallway continues to the north,
    and the stairs to the Second Floor Hallway lie to the south"""),

    'hallway_three_cont':   Room("Third Floor Hallway Continued", """To the west is Suite 320,
    To the east is Suite 344, to the norht is Suite 345,
    and the beginning of the hallway lies to the south"""),

    '100':   Room("Suite 100 - Ruben's Elec. Cont.", """There's not much
    going on here."""),

    '110':   Room("Suite 110 - W.B. Jones Heating & Air", """There's not much
    going on here."""),

    '120':   Room("Suite 120 - Available 1400", """This room is deserted"""),

    '200':   Room("Suite 200 - Dunder Mifflin Paper", """There's not much
    going on here."""),

    '210':   Room("Suite 210 - Vance Refrigeration", """There's not much
    going on here."""),

    '300':   Room("Suite 300 - Woods & Grammercy", """There's not much
    going on here."""),

    '302':   Room("Suite 302 - Cress Tool & Die", """There's not much
    going on here."""),

    '320':   Room("Suite 320 - E.G. Phylloxy", """There's not much
    going on here."""),

    '344':   Room("Suite 344 - Kavala Data Filters", """There's not much
    going on here."""),

    '345':   Room("Suite 345 - Dwight Schrute", """There's not much
    going on here.""")
}


# Link rooms together
rooms['outside'].n_to = rooms['lobby']
rooms['outside'].s_to = rooms['fun_run']
rooms['fun_run'].n_to = rooms['outside']
rooms['lobby'].n_to = rooms['hallway_one']
rooms['lobby'].w_to = rooms['cafe']
rooms['lobby'].s_to = rooms['outside']
rooms['lobby'].e_to = rooms['hallway_two']
rooms['cafe'].e_to = rooms['lobby']
rooms['hallway_one'].n_to = rooms['120']
rooms['120'].s_to = rooms['hallway_one']
rooms['hallway_one'].w_to = rooms['100']
rooms['100'].e_to = rooms['hallway_one']
rooms['hallway_one'].s_to = rooms['lobby']
rooms['hallway_one'].e_to = rooms['110']
rooms['110'].w_to = rooms['hallway_one']
rooms['hallway_two'].n_to = rooms['hallway_three']
rooms['hallway_two'].w_to = rooms['200']
rooms['200'].e_to = rooms['hallway_two']
rooms['hallway_two'].s_to = rooms['lobby']
rooms['hallway_two'].e_to = rooms['210']
rooms['210'].w_to = rooms['hallway_two']
rooms['hallway_three'].n_to = rooms['hallway_three_cont']
rooms['hallway_three'].w_to = rooms['300']
rooms['300'].e_to = rooms['hallway_three']
rooms['hallway_three'].s_to = rooms['hallway_two']
rooms['hallway_three'].e_to = rooms['302']
rooms['302'].w_to = rooms['hallway_three']
rooms['hallway_three_cont'].n_to = rooms['345']
rooms['345'].s_to = rooms['hallway_three_cont']
rooms['hallway_three_cont'].w_to = rooms['320']
rooms['320'].e_to = rooms['hallway_three_cont']
rooms['hallway_three_cont'].s_to = rooms['hallway_three']
rooms['hallway_three_cont'].e_to = rooms['344']
rooms['344'].w_to = rooms['hallway_three_cont']
