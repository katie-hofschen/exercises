def two_fer(name = "you"):
    try:
        val = str(name)
        return "One for " + val + ", one for me."
    except ValueError:
        print("That's not your name?!")


