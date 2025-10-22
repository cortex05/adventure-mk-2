
running = True

while running:
    print('Welcome! What would you like to do?')
    print('1 - Start Game')
    print('2 - Exit')
    choice = input('')

    if choice == '1':
        print('Starting game...')
    elif choice == '2':
        print('Goodbye!')
        running = False
    else:
        input('Invalid choice. Please try again. Press Enter.')