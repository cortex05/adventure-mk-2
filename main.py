from main_functions import launcher

running = True

while running:
    launch = launcher()

    if launch:
        print('Starting game...')
        # opening scroll
    else:
        print('Goodbye!')
        running = False