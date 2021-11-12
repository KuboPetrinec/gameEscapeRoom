#!/usr/bin/python3
import states
import features
#HRA NA CVIKA

# slovniky budeme vidiet CELY ZIVOT !
# vytvaranie dictionary ktory bude vytvarat miestnosti


# type hinting - aky TYP bude room
# ROBIME TO KVOLI VYVOJOVEMU PROSTREDIU ABY SOM DOSTAL ADEKVATNE METODY K PREMENNEJ
def show_room(room: dict):
    # dokumentacny retazec - dokumenatcia k prikazu
    """
    Show content of the room. (brief description)
    The function shows the name and description of the room. It also prints the information about items, which are in
    the room, if there are any. In the end, it prints list of exits if there are any.
    :param room: the room to print info about. (full description)
    :return: nothing (until we set function to return something)
    """

    # zachytenie vynimky/exception
    # type checking
    if type(room) != dict:
        print('BUBUBU')
        raise TypeError('Room is not of type dictionary')

    print(f"Nachadzas sa v miesnosti {room['name']}")
    print(f"{room['description']}")

    if room['items'] == []:
        print("Nevidíš tu nič zvláštne.")
    else:
        print(f"Vidis tieto veci: {', '.join(room['items'])}")
        # for item in room.get('items'):
        #     print(f"{item}", sep=',', end=' ')

    if room['exits'] == []:
        print("Z tejto miestnosti neexistujú žiadne východy.")
    else:
        print(f"Vidis tieto vychody: {', '.join(room['exits'])}")
        #for exit in room.get('exits'):
        #    print(f"{exit}", sep=',', end=' ')

# na pokracovanie hrania pouzivame premenne nie ich hodnoty
STATE_PLAYING = 'playing'
STATE_QUIT = 'quit'

# vypise zakladne info o hre


def about_game():
    print("Ocitol si sa v hre Indiana Jones vytvorenej Kubom.")
    print('(c)2021 Hra by JAKUB')


commands = ['o hre', 'prikazy', 'koniec', 'rozhliadni sa', 'alliasy']


# vypis vsetkych prikazov
def prikazy():
    print("Zoznam dostupnych prikazov :")
    print(commands)


def rozhliadni_sa():
    print('Nachadzas sa v tmavej zatuchnutej miestnosti bez okien, co dava tusit, ze si niekolko metrov pod zemou. '
          'Zeby kosicky hrad? Aj to je mozne, ti prebleslo hlavou.')


def show_allias():
    print("Alliasy pre prikazy:")
    print("koniec=quit/q/bye, o hre=about/info, prikazy=commands/help/?")

def inventory():
    if backpack == []:
        print('Tvoj batoh je prazdny.')
    else:
        print(f"V batohu mas : {', '.join(backpack)}")

def add_item_to_backpack(line):
    if line.startswith('vezmi'):
        what=line.split('vezmi')[1].strip()
        if not what:
            print("Neviem co chces zobrat.")
        elif what in room.get('items'):
            print("Takuto vec nevidim v miestnosti.")
        else:
            room['items'].remove(what)
            backpack.append(what)
            print(f"Pridal si do batohu {what}")


# varianty prikazu na ukoncenie hry
the_end = ('', 'koniec', 'quit', 'bye', 'q')

if __name__ == '__main__':
    # init game
    name = None
    line = None
    game_state = states.STATE_PLAYING


    backpack = [
        {
            'name': 'figa borova',
            'description': 'Borová figa. Čo viac k tomu dodať.',
            'features': [MOVABLE]
        },
        {
            'name': 'minca',
            'description': 'Zlatá minca.',
            'features': [MOVABLE]
        }
    ]

    room = {
        'name': 'dungeon',
        'description': 'Nachadzas sa v tmavej zatuchnutej miestnosti bez okien, co dava tusit, ze si niekolko metrov'
                       'pod zemou. Zeby kosicky hrad? Aj to je mozne, ti prebleslo hlavou.',
        'items':[
            {
                'name': 'kanister',
                'description': '3l kanister s benzinnom.',
                'features': [MOVABLE, USABLE]
            },
            {
                'name':'zapalky',
                'description': 'safety match zapalky. Zahrkal si krabickou a po jej otvoreni si nasiel len tri.',
                'features': [MOVABLE, USABLE]
            },
            {
                'name': 'hasiaci pristroj',
                'description': 'Cervena nadoba snehoveho hasiaceho pristroja. Plumba dava vediet, ze este nebol pouzity.',
                'features': [MOVABLE, USABLE]
            },
            {
                'name': 'noviny',
                'description': 'Bravicko do kazdej domacnosti.',
                'features': [MOVABLE, USABLE]
            },
        ],
        'exits': ['do zahrady'],
    }

    # end of init game

    print('''
===============================================================================================
                          Vitaj v hre INDIAN JONES :  ESCAPE ROOM.                                    
===============================================================================================
    ''')
    # rendering the dark room (starting room)
    show_room(room)
    # ctrl + q = zobrazenie dokumentacie k funkcii

    # main loop
    line = None

    while game_state == states.STATE_PLAYING:
        # normalizing string
        line = input('> ').lower().strip()

        if line == '':
            continue

        elif line in ('', 'koniec', 'quit', 'bye', 'q'):
            game_state = states.STATE_QUIT

        elif line in ('o hre', 'about', 'info'):
            about_game()

        elif line in ('rozhliadni sa', 'look around'):
            # rozhliadni_sa()
            show_room(room)

        elif line == 'alias':
            show_allias()

        elif line in ('inventory','inv','i'):
            inventory()

        #elif line in ('vezmi papier','add'):
        elif line.startswith('vezmi'):
            name = line.split('vezmi')[1].strip()
            if name == '':
                print("Neviem co chces zobrat.")
            elif name not in room.get('items'):
                print("Takuto vec nevidim v miestnosti.")
            else:
                room['items'].remove(name)
                backpack.append(name)
                print(f"Pridal si do batohu {name}")

        elif line in ('prikazy', 'commands', 'help', '?'):
            # prikazy()
            print("Zoznam prikazov v hre:")
            print("* koniec - ukonci rozohratu hru")
            print("* o hre - vypise informacie o hre")
            print("# prikazy - vypise vsetky dostupne prikazy")
            print("* rozhliadni sa - vypise popis miestnosti")
            print("* alliasy : koniec=quit/q/bye, o hre=about/info, prikazy=commands/help/?, rozhliadni sa=look around")
        else:
            print("Taky prikaz nepoznam")