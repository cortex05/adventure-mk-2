def launcher():
    print('Welcome! What would you like to do?')
    print('1 - Start Game')
    print('2 - Exit')
    choice = input('')

    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        input('Invalid choice. Please try again. Press Enter.')
        return launcher()
