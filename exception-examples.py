try:
    num = int(input("Give me a number"))
    print(f"The square of the number is {num**2}")
except:
    print("Invalid input")



name = input("What is your name?")

age1 = input(f"How old are you {name}?")
if name == "Nica":
    print("Your IQ is below 50 bro")
try:
    age = int(age1)
    print(f"{name}, you were born in {2024-age}")

except ValueError:
    print("Invalid response")
else:
    print("Thanks for playing properly")
finally:
    print("THanks for playing")




