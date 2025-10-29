def get_yes_no(prompt):
    while True:
        choice = input(f'{prompt} (Y/N): ').strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Please enter Y or N.")