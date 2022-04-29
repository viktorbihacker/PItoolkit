def character_duplicate_remover():
    input_string = input(str("String: "))
    no_duplicates = []
    [no_duplicates.append(i) for i in input_string if i not in no_duplicates]
    [print(i, end="") for i in no_duplicates]
