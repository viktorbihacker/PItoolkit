def extract():
    try:
        with open("./messageid.input", "r") as file:
            text = file.readlines()
    except FileNotFoundError:
        quit("Please place an input file (messageid.input) in the root directory with the text...")

    ids = []
    duplicate_removed = []
    for line in text:
        for word in line.replace("\n", "").split(" "):
            hyphen_number = 0
            for letter in word:
                if letter == "-":
                    hyphen_number += 1
            if hyphen_number == 4:
                ids.append(word)
    output = ""

    for id in ids:
        if id not in duplicate_removed:
            duplicate_removed.append(id)
    for item in duplicate_removed:
        output += item + "\n"
