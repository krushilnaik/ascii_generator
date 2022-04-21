def openFile(path: str):
    """
    We're only ever using UTF-8 files in this project,
    so set it in here and just use this everywhere.
    Args:
        path (str): the file path to open
    """
    return open(path, encoding="utf-8")


def fetchAlphabet():
    """
    Go through `alphabet.txt` (in this directory)
    and populate the dictionary up top
    to be used as a database for the site
    """

    ALPHABET = {}

    with open("alphabet.txt", encoding="utf-8") as alphabetFile:
        letter = ""

        for line in alphabetFile:
            if line[0].isdigit():
                # gets the second half of the line, without the quotes
                # e.g. 33 '!' -> !
                letter = line.split(" ", 1)[-1].strip()[1:-1]

                # Add the fetched character to the database
                # mapped to list populated in future iterations
                ALPHABET[letter] = []
                continue

            ALPHABET[letter].append(line.strip())

    return ALPHABET
