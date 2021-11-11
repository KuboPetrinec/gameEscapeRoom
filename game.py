#!/usr/bin/python3
import states

# na pokracovanie hrania pouzivame premenne nie ich hodnoty
STATE_PLAYING = 'playing'
STATE_QUIT = 'quit'

# vypise zakladne info o hre
def about_game():
    print("Ocitol si sa v hre Indiana Jones vytvorenej Kubom.")
    print('(c)2021 Hra by JAKUB')


commands = ['o hre', 'prikazy', 'koniec']


# vypis vsetkych prikazov
def prikazy():
    print("Zoznam dostupnych prikazov :")
    print(commands)


# varianty prikazu na ukoncenie hry
the_end = ('', 'koniec', 'quit', 'bye', 'q')


if __name__ == '__main__':

    print('''
===============================================================================================
                          Vitaj v hre INDIAN JONES :  ESCAPE ROOM.                                    
Nachadzas sa v tmavej miestnosti. Nic momentalne nevidis. Musis sa odtialto dostat lebo umries!
===============================================================================================
    ''')
    #rendering the dark room (starting room)
    print('Nachadzas sa v tmavej zatuchnutej miestnosti bez okien, co dava tusit, ze si niekolko metrov pod zemou. Zeby kosicky hrad? Aj to je mozne, ti prebleslo hlavou.')

    # main loop
    game_state = states.STATE_PLAYING
    line = None

    while game_state == states.STATE_PLAYING:
        #normalizing string
        line = input('> ').lower().strip()

        if line == '':
            continue

        elif line in ('', 'koniec', 'quit', 'bye', 'q'):
            game_state = states.STATE_QUIT

        elif line in ('o hre', 'about', 'info'):
            about_game()

        elif line in ('prikazy', 'commands', 'help', '?'):
            # prikazy()
            print("Zoznam prikazov v hre:")
            print("* koniec - ukonci rozohratu hru")
            print("* o hre - vypise informacie o hre")
            print("# prikazy - vypise vsetky dostupne prikazy")
            print("* alliasy : koniec=quit/q/bye, o hre=about/info, prikazy=commands/help/?")
        else:
            print("Taky prikaz nepoznam")
