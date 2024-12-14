# Temperature Converter: Converts between Celsius and Fahrenheit

print("Welcome to the Temperature Converter!")
print("You can now convert temperatures between Celsius and Fahrenheit. ")

while True: # This while loop replaces a potential error message
    try:
        temp = float(input("How many degrees is it outside: "))
        break
    except ValueError:
        print("Sorry, please input a number (degrees). ")
        continue

unit = input("Celsius or Fahrenheit (F or C)?: ")

# Temperature conversion
if unit.lower() == "c": #
    temp = (temp * 9 / 5) + 32
    print(f" It is currently {temp:.2f} degrees Fahrenheit. ") #Blocking the temp at .2 decimals
elif unit.lower() == "f":
    temp = (temp - 32) * 5 / 9
    print(f"It is currently {temp:.2f} degrees Celsius. ")
else:
    print("Sorry, that isn't a valid input. Please restart and choose C or F! ")
