# Virtual Bartender


from random import choice
drink = ["Whiskey", "Rum", "Tequila", "gin", "Schnaps", "Wine", "Champagne", "Cognac"]
mixers = ["Fanta", "Cola", "Red Bull", "Tonic"]

print(f"{choice(drink)}{choice(mixers)}")

print("I am the virtual bartender, welcome to the bar")
name = input("How should I call you?")


try:
    age = input("How old are you?")
    age = int(age) # This is where we could have problems in case the input can not be converted into an integer
    legal = None
    country = input("Where are you from")
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else:
        legal = True


    if legal:
        print(f"Here is a {choice(drink)} {choice(mixers)}")
    else:
        print(f"I can only serve you {choice(mixers)}")





except ValueError:
    print("I do not have time for your games")