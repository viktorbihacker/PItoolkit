import sys


def password_generator():
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


def main():
    menu_items = ["Password generator", "Second function", "Third function"]
    while True:
        application_name = "PItoolkit"
        application_name_placeholder = len(application_name) * "-"
        menu_title_placeholder = int(max([len(item) for item in menu_items]) / 2) * "-"
        menu_header = f'{menu_title_placeholder}{application_name}{menu_title_placeholder}'
        menu_footer = f"{menu_title_placeholder}{application_name_placeholder}{menu_title_placeholder}"
        for menu_item_index, menu_item in enumerate(menu_items):
            if menu_item_index == 0:
                print(menu_header)
            print(f'{menu_item_index + 1}. {menu_item}')
            if menu_item_index == len(menu_items) - 1:
                print(menu_footer)
        selection = input("Enter selection: ")
        try:
            if 0 < int(selection) < len(menu_items) + 1:
                try:
                    getattr(sys.modules[__name__], "%s" % menu_items[int(selection) - 1].lower().replace(" ", "_"))()
                except AttributeError:
                    quit("Function is not implemented")
        except ValueError:
            quit()
        else:
            quit()


if __name__ == '__main__':
    main()
