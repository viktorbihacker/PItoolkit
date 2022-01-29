import random


def generator():
    default_password_length = 12
    maximum_password_length = 32
    character_repository = {'special': [[33, 41], [43, 47], [58, 64], [91, 96], [123, 126]],
                            'number': [48, 57], 'upper': [65, 90], 'lower': [97, 122]}
    character_keys = ['special', 'number', 'upper', 'lower']
    generated = ''
    try:
        character_number = int(input(f'Enter password length({default_password_length}-{maximum_password_length}): '))
    except ValueError:
        print(f'Password length set to {default_password_length}.')
        character_number = default_password_length
    if character_number < default_password_length:
        print(f'Password length set to {default_password_length}.')
        character_number = default_password_length
    if character_number > maximum_password_length:
        print(f'Password length set to {maximum_password_length}.')
        character_number = maximum_password_length
    while character_number > 0:
        current_pick = character_keys[(character_number % 4) - 1]
        if current_pick == 'special':
            current_special = random.randint(0, 3)
            range_start = character_repository.get(current_pick)[current_special][0]
            range_end = character_repository.get(current_pick)[current_special][1]
        else:
            range_start = character_repository.get(current_pick)[0]
            range_end = character_repository.get(current_pick)[1]
        generated += chr(random.randint(range_start, range_end))
        character_number -= 1
    password = ''.join(random.sample(generated, len(generated)))
    print(f'Password: {password}')