def extract():
    try:
        with open("./messageid.input", "r") as file:
            text = file.readlines()
    except FileNotFoundError:
        quit("Please place an input file (messageid.input) in the root directory with the text...")
