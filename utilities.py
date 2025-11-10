from typing import List

from items.KeyItems import KeyItem


def get_yes_no(prompt):
    while True:
        choice = input(f'{prompt} (Y/N): ').strip().lower()
        if choice in ['y', 'n']:
            return choice
        print("Please enter Y or N.")

def check_key_items_unlock(key_items: List[KeyItem], block_value: str):
    match = any(d['value'] == block_value for d in key_items)

    if match is True:
        return True
    else:
        return False
    