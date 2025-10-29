from main_functions import launcher
from game import main

running = True

while running:
    launch = launcher()

    if launch:
        print('Starting game...')
        # opening scroll
        main()
    else:
        print('Goodbye!')
        running = False