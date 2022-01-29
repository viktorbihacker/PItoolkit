import sys


def first_function():
    print("First function triggers here")


def main():
    menu_items = ["First function", "Second function", "Third function"]
    while True:
        menu_placeholder = int(max([len(item) for item in menu_items]) / 2) * "-"
        menu_header = f'{menu_placeholder}PItoolkit{menu_placeholder}'
        menu_footer = f"{menu_placeholder}---------{menu_placeholder}"
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
