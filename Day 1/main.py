#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

print('Welcome to the band name generator\n')

city_name = input("Please enter the name of the city you grew up in : ")

pet_name = input("Please enter the name of your pet : ")

print("Your Band name could be {city} {pet}".format(city=city_name,pet=pet_name))
