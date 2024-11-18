def choose_practicum():
    name = input("What is your name ")
    practicum = input("chooes a practicum ")
    if practicum == "Costumes" or practicum == "Scenery" or practicum == "Lighting" or practicum == "Sound":
        correct = input(f"Your name is {name} and you have chosen {practicum}. Is this correct ")
        if correct == "Yes":
            print(f"ok {name} you have comfirmed your selection of {practicum} ")
        else:
            print(f"ok lets try this again then")
            return choose_practicum()
    else:
        print(f"{practicum} is not a valid choice please choose from the following, Costumes, Scenery, Lighting, Sound")
        return choose_practicum()


choose_practicum()